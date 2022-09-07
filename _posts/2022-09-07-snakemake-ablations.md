---
date: 2022-06-14 18:00:00 +0200
title: "Running multiple experiments via Snakemake"
layout: post
categories:
  - Research
  - Deep Learning
  - Python
---

After proposing a new method you have to evaluate it in a range of scenarios in
order to understand its strengths and weaknesses. This usually means trying
several variations of the method, on different datasets, multiple times, and
analyzing the results. The total number of runs you have to do quickly explodes,
and automation becomes essential to manage all these experiments.

<!-- more -->

## Basic Setup

I always follow the same basic rules in all my projects:

 1. There must be a single script, or *entry point* to run experiments;
 1. The entry point must take a configuration file as input;
 1. Everything that can be changed in the experiment can be changed (1) from the
    configuration file and (2) via command line arguments to the entry point,
    with the latter taking priority over the former;
 1. The entry point produces the end result and an intermediate log file in a
    configurable location;
 1. Log files are in text format and there is a script to parse them and output
    metrics of interest.

These rules ensure that the method and its evaluation via experiments are
entirely segregated and independent. Moreover, by connecting the entry point to
a command line interface via arguments, configurations, output and log files, we
gain tremendous power to define, run and analyze experiments. The basic
philosophy is adapted from Unix's: everything is a (text) file. But doing this
at scale requires a plan.

## First solution: bash scripts

The obvious solution is to create one or more bash scripts to define the
experiments. Most commonly you need to iterate on grids of parameters:

```bash
for dset in mnist cifar10; do
    for rep in 1..10; do
      python src/method/train.py configs/base.yaml \
          --dataset $dset \
          --seed $((RANDOM)) \
          --logfile outputs/base-$dset-r$rep.out
    done

    python src/method/parse-log.py outputs/base-$dset-r$rep.out \
        > metrics/base-$dset-r$rep.txt
done
```

While you can get quite far with this setup, it has a serious drawback: it is an
all-or-nothing solution. To run only a part of the experiments, perhaps the ones
that failed or new additions, you have to modify the script, commenting lines,
adding safeguards, and generally patch things up. And if you are in a cluster
environment, other users may not appreciate you scheduling hundreds of jobs at
the snap of a finger. That said, given its simplicity, this method can already
get you most of the way.

## Better solution: Snakemake

Snakemake[^sn] is a tool to write workflows, i.e., a sequence of connected steps
(or *rules*) each of which may take as input one or more files and produce
another file as output. These steps are defined into a Snakefile, and Snakemake
takes care of figuring out dependencies and running the jobs that are necessary
to produce the final output files.

Snakemake allows you to write extremely complicated workflows. You could argue
that it is overkill to run grid searches and ablation experiments with it, and I
may be inclined to agree actually. The reason I use it is that it allows me to
define hundreds of jobs and only run only a few at the same time, so that my
colleagues don't hate me for clogging the cluster.

I will introduce the basics of Snakemake by walking you through a Snakefile we
can use to run ablation experiments. Snakemake executes by default the first
rule in the Snakefile, and it is customary to list here all the output files you
want produced at the end of the workflow:

```
rule all:
    input:
        [
            f"outputs/{d}-{d}-r{i}.log"
            for s in ["small", "large"]
            for d in ["cifar10", "mnist"]
            for i in range(5)
        ]
```

The syntax in a Snakefile is a weird mix of yaml and Python. The list
comprehension is used to list all the files we want the workflow to produce. In
this case, we want as output `small-mnist-r5.out`, `large-cifar10-r2.out`, and
so on.

For each of these files, Snakemake will scan all rules in the Snakefile and find
a rule that can produce this file as output. Rules use an `output` directive to
indicate the name of the files they are capable to produce. Most importantly,
the `output` directive can match more than a single file! For example, this rule

```
rule small_dataset:
    output:
        "outputs/small-{dset}-r{i}.out"
    shell: """
        python src/method/train.py \
            --dataset {wildcards.dset} \
            --training-size 500 \
            --logfile {output}"
        """"
```

will match all output files that start with "small-". In this rule, `{dset}` and
`{i}` are two *wildcards* that Snakemake can use to match a file name, so that
this rule will match files such as `small-cifar10-r4.out`, `small-mnist-r1.out`
and so on. Snakemake will execute the shell script in `shell` for each matched
file (separately). Note that in the shell we can access the wildcards that were
matched, such as the dataset `dset` in the file name, as well as the input (in
this case none) and output of the rule and other parameters (see documentation).

The pattern in `output` will also match an infinite amount of garbage such as
`small-asd-rrrr.out`, `small-r-.out` and so on, but Snakemake will ignore these
because these files because they are not defined in the `all` rule. This was the
origin of a fundamental misunderstanding I had about Snakemake so let me
highlight the basic mindset you need to have when writing a Snakefile:

> Define every final output file in the "all" rule, then create rules that match
> one or more of these files in their "output" directive.

We also have to create another similar rule for the large datasets, otherwise
Snakemake will point out that there are some files in the `all` rule that are
not produced by any rule.

```
rule large_dataset:
    output:
        "outputs/large-{dset}-r{i}.out"
    shell: """
        python src/method/train.py \
            --dataset {wildcards.dset} \
            --training-size 50000 \
            --logfile {output}"
        """"
```

And that's basically it! Snakemake simply matches rules to output files and
executes them. If a rules requires input files, Snakemake would search for other
rules that could produce these files and execute them first. Thanks to wildcards,
you can easily define lots of different experiments and configurations.

### Running in a cluster environment

In a cluster environment you would run Snakemake from the login node and instead
of calling `python` in the shell directive invoke your cluster runner in
blocking mode, for example `srun` or `sbatch --wait` if you are using Slurm.
Invoke Snakemake as follows:

```
> nohup snakemake --jobs 8 --latency-wait 360 --snakefile path/to/Snakefile &
```

This will limit Snakemake to eight concurrent submitted jobs, and with `nohup
... &` you can let it run in the background after you log out. The latency wait
parameter makes Snakemake wait for a while before checking if a rule did or did
not produce the output file, and is necessary in distributed environments to
account for synchronization delays between nodes.

## A more complicated example

Suppose you have several different configurations in a folder, each containing
different variations of a method, and you want to run each configuration on
different datasets multiple times, then analyze these runs to create a final
report.

First, create the `all` rule:

```
rule all:
    input:
        expand("outputs/{config}-{dataset}.out",
               config=os.listdir("./configs/"),
               dataset=["cifar10", "mnist"])
```

The `expand` function is equivalent to the list comprehension we used above. It
will produce all combinations of items in the `config` and `dataset` lists, and
format the string accordingly. Note how we used Python's `os.listdir` to find
all configurations in the `./configs/` folder.

We want each of these output files to contain metrics aggregated over, say, ten
runs of each configuration on each dataset. Therefore, we create a rule that
matches these output files and requires as input the ten repetitions:

```
rule aggregate_results:
    output:
        "outputs/{config}-{dataset}.out"
    input:
        lambda wildcards: expand("logs/{c}-{d}-rep{i}.log",
                                 c=wildcards.config,
                                 d=wildcards.dataset,
                                 i=range(10))

    shell: """
    python src/aggregate-metrics.py {input} > {output}
    """
```

Things look a bit messy here. First, remember that this rule will be executed
separately for each output file it matches. For example, if there is a
configuration `configs/baseline` this rule will match
`outputs/baseline-cifar10.out` among others. In order to produce this output
file, we want this rule to read the inputs `logs/baseline-cifar10-rep0.log` all
the way to `logs/baseline-cifar10-rep9.log`. This list of ten files is the
output of the `lambda` function under the `input` directive. The `wildcards`
argument given to the lambda are those matched in the output file, for example
`baseline` as `config` and `cifar10` as dataset. Remember, the rule is run
*once* for each output file it matches, therefore `{input}` here will contain
all ten input files separated by a space, and the `aggregate-metrics.py` file
will thus be called with ten command line arguments (there are options to quote
this list so it is parsed as a single argument by the shell).

Going one step backward, we now need a rule that defines how to create each of
the log files. Here we want to run training on the right dataset and with the
right configuration:

```
rule run_experiment:
    output:
        "logs/{config}-{dataset}-rep{i}.log"
    shell: """
        python src/method/train.py \
            --config configs/{wildcards.config} \
            --dataset {wildcards.dataset} \
            --logfile {output}"
    """
```

And this should do it! Again, notice how Snakemake simply tries to match the
names of files in the `input` of a rule with the names of files in the `output`
of other rules. It will also make sure that the output files are indeed created
after executing a rule, and terminate with a failure if the file does not exist.
As an exercise, try to think how to expand this Snakefile to first perform some
sort of pretraining on a common dataset, and then run those ten repetitions as a
finetuning step.

## Lab session

To put in practice what you learned so far, here's a Snakefile with the basic
structure of example I just discussed above. It uses stub bash commands instead
of actual training and analysis so that you can see the flow of data.

```
rule all:
    input:
        expand("outputs/{config}-{dataset}.out",
               config=os.listdir("configs"),
               dataset=["cifar10", "mnist"])

rule aggregate_results:
    output:
        "outputs/{config}-{dataset}.out"
    input:
        lambda wildcards: expand("logs/{c}-{d}-rep{i}.log",
                                 c=wildcards.config,
                                 d=wildcards.dataset,
                                 i=range(3))
    shell: """
        set -x
        sleep 1
        cat {input} > {output}
    """


rule run_experiment:
    output:
        "logs/{config}-{dataset}-rep{i}.log"
    shell: """
        set -x
        sleep 1
        echo config {wildcards.config} \
            dataset {wildcards.dataset} \
            repetition {wildcards.i} \
            > {output}
    """
```

Put this in a `Snakefile`, create some fake configurations and output folders,
and run Snakemake in parallel:

```
> mkdir configs logs outputs
> touch configs/conf1 configs/conf2
> snakemake -c 20
```

Note that, despite the sleep commands in there, it will finish pretty quickly as
20 rules are executed in parallel. At the end, the output folder will contain
all files we expect:

```
> ls outputs
conf1-cifar10.out  conf1-mnist.out  conf2-cifar10.out  conf2-mnist.out
> cat outputs/conf2-cifar10.out
config conf2 dataset cifar10 repetition 0
config conf2 dataset cifar10 repetition 1
config conf2 dataset cifar10 repetition 2
```

As an exercise, try to modify this Snakefile to perform a common pretraining
step at the beginning. Maybe even consider different pretraining and finetuning
methods!

## Conclusion
Thanks to its matching capabilities, it is possible to use Snakemake to create
rather complicated experimental workflows succinctly. It took a while for me to
wrap my head around wildcard expansion rules and the mindset needed to write
Snakefiles, but after this barrier lies a world full of possibilities. I hope
this blog post helped you get started running your own experiments. Snakemake is
very powerful and offers many features, so do not hesitate to head over its
documentation.[^sn]

## Links
[^sn]: https://snakemake.readthedocs.io/en/stable/
