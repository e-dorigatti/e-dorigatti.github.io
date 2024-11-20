---
date: 2023-12-05 12:00:00 +0200
title: "How to use Visual Studio Code to run and debug code on SLURM compute nodes"
layout: post
categories: Development
---

If you're a developer or data scientist using SLURM to handle your compute workloads, you have surely encountered issues in debugging your code on compute nodes. In this blog post, I share a simple solution for that, allowing you to develop and debug code running directly with the compute resources you need. Although the focus is on Visual Studio Code, the same approach can be applied to other IDEs that support remote development via SSH.

<!-- more -->

## The problem with software development on SLURM
SLURM is a cluster manager that allows users to submit jobs to be executed on compute nodes with the appropriate resources.
In principle, one should develop their program on a local machine, then upload it to the cluster, and submit jobs to execute it and obtain results.
In practice, this is cumbersome and error-prone, as there are often compatibility issues between the local machine and the compute nodes on the cluster due to the different execution environments, such as operating systems, library versions, etc.
It is therefore common for SLURM users to do their development on the cluster login node, and either (1) perform small test runs on the login node itself, or (2) test their code by submitting jobs.
Both alternatives are not optimal: in the first case, the resources on the login node are different than those on the compute node and may not suffice to support many users developing concurrently, while in the second case it is impossible to debug the code from the integrated development environment (IDE), seriously hampering development.

In this post, I present a simple solution that solves both problems, allowing one to use the full power of IDE debugging directly on compute nodes.
I will focus on Visual Studio Code, but the same trick should be applicable to other IDEs that support remote development via SSH (including, for example, PyCharm).

## SSH access to compute nodes

An innocent solution would be to directly SSH to a compute node, but this is not a good idea because you would be able to "steal" all the resources on that node, defeating the very purpose of SLURM (which is to share resources among users).
It is for this reason that some SLURM clusters do not even allow users to SSH into compute nodes.
And if your SLURM clusters allows it, you should still be polite and not do it to get compute resources.

Actually, there is a way to achieve the same result while still respecting resource allocation: run a SSH server in a SLURM job!
For this, we can use [Dropbear][dbr], a lightweight SSH server that can be started by normal users.

## Step 1: Set up dropbear

We will only install dropbear for our user on the login node, simply cloning the repository and compiling the binary.
You can find the full instructions [in the repository][dbi], but a basic installation will be like this:

```
> # we are executing this on the login node
> git clone https://github.com/mkj/dropbear
> cd dropbear
> # compile the server
> ./configure
> make PROGRAMS="dropbear dbclient dropbearkey dropbearconvert scp"
> # install binaries in a local folder
> mkdir install
> make install DESTDIR=install
```

If you do not have a compiler available, you can use a package manager such as [Minoconda](https://docs.conda.io/projects/miniconda/en/latest/) or [Micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) to install the [compiler tools package](https://docs.conda.io/projects/conda-build/en/latest/resources/compiler-tools.html) for your user only.

After this, the dropbear binary will be in `~/dropbear/install/usr/local/sbin/dropbear`.
We keep everything in our home folder to avoid messing up with the login node and angering the sysadmins :)

The last step to prepare the server is to generate a key file:

```
> ~/dropbear/install/usr/local/bin/dropbearkey \
    -t ecdsa -s 521 -f ~/dropbear/install/server-key
```

## Step 2: Start the SSH server in a SLURM job

Next, we submit a SLURM job that will run the SSH server.
Note that sessions connecting to this SSH server will *not* inherit the environment variables of the SLURM job, missing essential variables such as `CUDA_VISIBLE_DEVICES` (indicating which GPUs can be used by VSCode and all our scripts), `SLURM_CPUS_PER_TASK` (telling the processes we launch how many CPUs they can use) and so on.
Therefore, before starting the SSH server we are going to save all these useful environment variables into a file, which you should source before running any process that needs to respect the resource allocation from SLURM.

This can be done by using the following script:

```
> cat run-vscode-server-gpu.sh
#!/bin/bash

#SBATCH --time 12:00:00
#SBATCH --job-name vscode-gpu
#SBATCH --cpus-per-task 8
#SBATCH --mem 32G
#SBATCH --partition gpu
#SBATCH --gres gpu:1
#SBATCH --output ~/vscode-gpu.log

DROPBEAR=~/dropbear/install

### store relevant environment variables to a file in the home folder
env | awk -F= '$1~/^(SLURM|CUDA|NVIDIA_)/{print "export "$0}' > ~/.slurm-envvar.bash

# here we make sure to remove this file when this SLURM job terminates
cleanup() {
    echo "Caught signal - removing SLURM env file"
    rm -f ~/.slurm-envvar.bash
}
trap 'cleanup' SIGTERM

### start the SSH server
# dropbear arguments:
#  -r    Server key
#  -F    Don't fork into background
#  -E    Log to stderr rather than syslog
#  -w    Disallow root logins
#  -s    Disable password logins
#  -p    Port where to listen for connections
#  -P    Create pid file PidFile
$DROPBEAR/usr/local/sbin/dropbear \
    -r $DROPBEAR/server-key -F -E -w -s -p 64321 \
    -P $DROPBEAR/var/run/dropbear.pid
> # submit the job
> sbatch run-vscode-server-gpu.sh
```

Dropbear will use the authorized keys in `~/.ssh/authorized_keys` to determine who can connect and who cannot, meaning that you do not have to worry about other users connecting to this SSH server.

Now, simply submit this job before your morning coffee and wait for it to start:

```
> squeue -u `whoami`
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          43029233       gpu vscode-g      edo  R       2:55      1 supergpu03
```

Remember the node where the server is running (`supergpu03`) as we need it later!

In case of troubles the log file should contain more information, but in case of success the server will patiently wait for connections:

```
> cat ~/vscode-cpu.log
[33449] Dec 05 09:52:03 Not backgrounding
```

## Step 3: Configure the Shell and Visual Studio Code

Before doing this, set up Visual Studio Code for remote development via SSH following the [official guide][vsr], including [SSH key-based authentication][sshk].
Next, open the SSH config file by searching for "Remote-SSH: Open SSH Configuration File..." from the command palette (invoked via `Ctrl+Shift+P`), and add the following configuration:

```
# Login node - adapt to your cluster
Host hpc-login
  HostName login.cluster.com
  User edo

# Compute node where the dropbear is running. Note:
#  - The HostName must correspond to the one you saw in `squeue`
#  - ProxyJump instructs VS Code to connect to the compute node via the login node;
#    it is not necessary if you are able to directly connect to the compute node.
#  - The Port is the same we used in `run-vscode-server-gpu.sh`
Host hpc-compute
  HostName supergpu03
  ProxyJump hpc-login
  User edo
  Port 64321
```

Every time you start a new SSH server in this way you should make sure that the `HostName` of the `hpc-compute` host matches what is listed in `squeue`.
Or you could try to run the server always on the same node via `#SBATCH --nodelist supergpu03` in the server submit script, but you may have to wait for resources to free before your server can start.

Next, to make sure that Visual Sudio Code correctly uses the resources reserved by SLURM, and no more, we need to load in our shell the environment variables that we saved earlier when submitting the job. According to the [official solution](https://github.com/microsoft/vscode-remote-release/issues/1722#issuecomment-1938924435) This can be done by sourcing the file from your `/.bashrc`:

```
# source slurm environment if we're connecting through code-tunnel
[ -f ~/.code-tunnel-env.bash ] && source ~/.code-tunnel-env.bash
```

With this solution, you do not need to remember to source that environment file, and all programs will automatically respect the resource allocations.

## Step 4: Connect to the compute node

Finally, connect to the server running on the compute node as you would usually do, i.e., by selecting "Remote-SSH: Connect to Host..." from the command palette and choosing `hpc-compute` as the target.

## Conclusion

Now you can use all the power of Visual Studio Code with compute resources such as GPUs while respecting your resource allocation.

Happy debugging!

 [dbr]: https://github.com/mkj/dropbear
 [dbi]: https://github.com/mkj/dropbear/blob/master/INSTALL.md
 [vsr]: https://code.visualstudio.com/docs/remote/ssh
 [sshk]: https://code.visualstudio.com/docs/remote/troubleshooting#_configuring-key-based-authentication
