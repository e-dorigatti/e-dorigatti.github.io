---
layout: post
title:  "The expectation maximization algorithm without the agonizing pain"
date:   2021-03-15 12:00:00 +0200
---

My first introduction to the expectation maximization (EM) algorithm was a bit
traumatic: rarely have I been left so clueless by a lecture. Even after reading
the relevant chapter in Bishop's venerable Machine Learning book a couple of
times things were not so clear. After some more struggles it finally clicked,
and it is really simple!

<!-- more -->

Note: I am going to assume you are comfortable with basic probability facts,
maximum likelihood estimation and latent variable models.

## Motivation
Imagine you are trying to build a generative model of a set of observations:
your model would return the probability of a particular observation
$p(x|\theta)$ based on some unknown parameters $\theta$. To find the most
appropriate description of the data by this model you would then use maximum
likelihood to compute the best values of $\theta$, i.e.

$$
\theta^* = \arg\min_\theta \ln p(x|\theta)
$$

In some cases, it might be much easier to describe the data generating process
using some intermediate _latent_ variable $z$ from which the value of $x$ is
derived:

$$
p(x,z|\theta)=p(x|z,\theta)\cdot p(z|\theta)
$$

If we somehow observed the value of $z$, our maximum likelihood problem would
simply become:

$$
\theta^* = \arg\min_\theta \ln p(x,z\vert\theta)
$$

And could be solved directly. However, $z$ is by its nature unknown to us, which
means that this approach will not work. We might be tempted to marginalize over
$z$ and maximize a likelihood that looks like this:

$$
\theta^* = \arg\min_\theta \ln p(x\vert\theta)
= \arg\min_\theta \ln \left[\sum_z p(x,z\vert\theta)\right]
$$

Doing this can be actually quite hard though because the sum is inside the
logarithm, so it cannot be reduced to a simpler form that is easy to work with.

So it seems that our problem only got harder. Time to be creative!

## Intuition

In our generative model $z$ is computed from $\theta$ and $x$ from $z$. Imagine
then that we fix a value of $\theta$. What we could to is to use our
observations $x$ to compute the value of $z$ that most likely generated the
observed $x$ from the $\theta$ we chose. Even better, we could compute an entire
distribution $p(z\vert x,\theta)$ saying how much we believe in a certain value
of $z$:

$$
p(z\vert x,\theta)=\frac{
p(x\vert z,\theta)p(z\vert\theta)
}{
p(x\vert\theta)
}
$$


This looks very arbitrary because we have no idea what $\theta$ is, but
bear with me.

We can now use this fictional distribution of $z$ to compute the expected
likelihood for the observation $x$. In other words, we compute the likelihood
for all possible values of $z$ and take an average weighted by how confident we
are about that value of $z$:

$$
\mathbb{E}_{z\sim p(z|x,\theta)}\left[\ln p(x,z|\theta)\right]
=\sum_z p(z|x,\theta)\cdot\ln p(x,z|\theta)
$$

(with sums replaced by integrals where appropriate). And this is our best guess
for the likelihood, based on a completely made-up value of $\theta$. To recap,
we chose a value of $\theta$, used that and $x$ to compute a best guess for $z$,
and used that guess to compute a best guess for the likelihood.

Well, now that we have a clue about the likelihood, can we just maximize it? It
seems like a stupid idea because we are still living in a fantasy with an
arbitrary value of $\theta$.

But it actually works! The simple idea behind the EM algorithm is that you can
just start from any value of $\theta$ to compute an updated distribution for
$z$, then use this guess for $z$ to improve the value of $\theta$, and so on,
iteratively refining our guesses for $\theta$ and $z$.

## The EM algorithm

In a nutshell, the steps we saw above are:

 1. Pick an initial value for $\theta$
 2. E step: compute $p(z\vert x,\theta)$
 3. M step: Find a $\theta^\prime$ that maximizes
$$
Q(\theta,\theta^\prime)=\sum_z p(z|x,\theta)\cdot\ln p(x,z|\theta^\prime)
$$
 4. Go back to step 2 until likelihood converges

Note that the posterior distribution of $z$ in the M step always uses the old,
fixed $\theta$ that we estimated in the E step, while the $\theta^\prime$ that
we are maximizing over only acts on the likelihood.

Every pair of E-M steps is guaranteed to increase the likelihood $p(x|\theta)$,
so convergence is guaranteed. In case of non-convex likelihoods, just repeat the
EM algorithm a few times with different random starting values for $\theta$ and
simply pick the best.

Of course the EM algorithm is not a silver bullet, but it is particularly handy when:

 1. Your generative model can be naturally described using latent variables, and
 2. Computation of $p(z\vert x,\theta)$ and $p(x\vert z,\theta)$ is feasible.

The second point deserves some additional explanation. Usually $p(x\vert
z,\theta)$ is easily computable following the generative model we fixed at the
beginning. The posterior of $z$, however, is not necessarily easy to compute, as
it involves computing the evidence:

$$
p(x\vert\theta)=\sum_z p(x\vert z,\theta)p(z\vert\theta)
$$

This innocent-looking guy can be especially nasty, or indeed intractable for
many interesting models. In such cases, the EM algorithm cannot be applied and
we need to resort to other methods for approximate inference.

## Example

The most popular application of the EM algorithm is, arguably... $K$-means
clustering! In $K$-means clustering, we assume that each observation $x_n$ is
paired with a latent variable $z_n$ that tells which cluster $x_n$ belongs to,
so that $z_n=k$ means that $x_n$ is in the $k$-th cluster. The parameters
$\theta$ contain the $K$ cluster means $\mu_1,\ldots,\mu_K$.

In such a model, the "complete data likelihood" becomes:

$$
p(x,z\vert\theta)
=\prod_{n=1}^N p(x_n,z_n\vert\theta)
=\prod_{n=1}^N p(x_n\vert z_n,\theta)p(z_n\vert\theta)
$$

Where the product follows from the usual assumption that the data points are
independent. Computing the inner terms is easy: conditioning on $z_n$ means
pretending that we know what the value of $z_n$ is, i.e. we know which cluster
$x_n$ belongs to.

$$
p(x_n\vert z_n=k,\theta)p(z_n=\vert\theta)
=\mathcal{N}(x_n\vert\mu_k,\sigma I)\cdot\frac{1}{K}
$$

Where we assume that the clusters contain the same amount of points, hence
$p(z_n)=1/K$, and the points in each cluster are generated by sampling from a
Gaussian distribution with fixed, unknown covariance.

Let's then walk through the EM algorithm. We first need to assume an initial
value of $\theta$, which means that we need to decide the initial cluster
centers; this is usually done by fixing them to $K$ random observations.

### E step
Given these cluster centers, we need to find the distribution of the latent
variables $z$ conditioned on the observations $x$ and the cluster centers. In
other words, we need to find which cluster each observation belongs to. As
before, the distribution of $z$ is factorized:

$$
p(z\vert x,\theta)=\prod_n p(z_n\vert x_n,\theta)
$$

So we can focus on a single example. The inner terms can be computed via Bayes's
formula:

$$
p(z_n=k\vert x_n,\theta)=\frac{
p(x_n\vert z_n=k,\theta)p(z_n=k\vert\theta)
}{
p(x_n\vert\theta)
}
$$

We computed the numerator above, while the denominator can be obtained by the
law of total probability, i.e. "undoing" a marginalization:

$$
p(x_n)
=\sum_{k=1}^K p(x_n,z_n=k)
=\sum_{k=1}^K p(x_n\vert z_n=k,\theta)p(z_n=k\vert\theta)
$$

Which we also computed above. Therefore:

$$
p(z_n=k\vert x_n,\theta)=\frac{
\mathcal{N}(x_n\vert\mu_k,\sigma I)\cdot\frac{1}{K}
}{
\sum_{k^\prime=1}^K\mathcal{N}(x_n\vert\mu_{k^\prime},\sigma I)\cdot\frac{1}{K}
}
$$

This is a "soft" assignment, since each cluster gets a non-zero probability of
having generated $x_n$. We might proceed with this, but in $K$-means we want to
perform a "hard" assignment, i.e. choose only a single cluster. The obvious
choice is to pick the most likely cluster for each point:

$$
p(z_n=k\vert x_n,\theta)=\mathbb{1}\left[
k=\arg\max_{k^\prime}
\mathcal{N}(x_n\vert\mu_{k^\prime},\sigma I)
\right]
$$

Where $\mathbb{1}[P]$ is the indicator function taking value $1$ if $P$ is true,
$0$ otherwise, and the denominator disappeared since it is constant. Since all
clusters are assumed to have the same covariance, the most likely cluster for
$x_n$ is the one with the closest center:

$$
\arg\max_{k^\prime}
\mathcal{N}(x_n\vert\mu_{k^\prime},\sigma I)
=\arg\min_{k^\prime} \vert\vert x_n-\mu_{k^\prime}\vert\vert^2_2
$$


So we reached the familiar first step of $K$-means clustering: assign each point
to the closest cluster center.

**Note:** you might find the leap from soft to hard cluster assignment a bit
hand-wavy, but it can be justified via the limit of a tempered softmax:

$$
p(z_n=k\vert x_n,\theta)=\lim_{\tau\rightarrow 0^+}\frac{
e^{
\tau^{-1}
(x_n-\mu_k)^\intercal(x_n-\mu_k)
}
}{
\sum_{k^\prime=1}^K
e^{
\tau^{-1}
(x_n-\mu_{k^\prime})^\intercal(x_n-\mu_{k^\prime})
}
}
$$

This is still a probability distribution for all positive values of $\tau$, and
in the limit will approach the delta function we used above, putting all the
probability mass on the maximum element.

### M step
At this point we need to compute the new cluster centers based on the points
they are assigned to. In EM jargon, we need to maximize the "expected complete
data likelihood" $Q$:

$$
Q(\theta,\theta^\prime)
=\sum_z p(z|x,\theta)\cdot\ln p(x,z|\theta^\prime)
$$

Given the hard assignment we performed in the E step, the sum above only has a
single term: the one where each point is assigned to the closest cluster. It has
probability one, while all other cluster assignments have probability zero.
Therefore:

$$
Q(\theta,\theta^\prime)
=\ln p(x,z|\theta^\prime)
$$

With the values for $z$ that we found in the E step. We now need to maximize
this with respect to $\theta^\prime$ to find the updated value of $\theta$:

$$
\theta^*
=\arg\max_{\theta^\prime}
\ln\prod_{n=1}^N p(x_n\vert z_n,\theta^\prime)p(z_n\vert\theta^\prime)
=\arg\max_{\theta^\prime}\sum_{n=1}^N\left[
\ln p(x_n\vert z_n,\theta^\prime)+\ln p(z_n\vert\theta^\prime)
\right]
$$

Where the second term inside the sum is constant, so we can forget about it. To
tackle the maximization problem we need to follow the good-old analytical
approach with derivatives. Let's get on with it! We can differentiate with
respect to each cluster center separately:

$$
\nabla_{\mu_k}
Q(\theta,\theta^\prime)
=\sum_{n=1}^N\mathbb{1}\left[z_n=k\right]\nabla_{\mu_k}\ln p(x_n\vert z_n,\mu_k)
$$

Where the indicator makes the sum use only terms that were assigned to cluster
$k$. Since we use normally-distributed clusters, the inner term is:

$$
\nabla_{\mu_k}
\ln p(x_n\vert z_n,\mu_k)
=c+\nabla_{\mu_k}\left(
-\frac{1}{2}
\left(x_n-\mu_k\right)^\intercal
\left(x_n-\mu_k\right)
\right)
=x_n-\mu_k
$$

We now put everything (except for the constants $c$) together and find which
$\mu_k$ makes this equal to zero:

$$
\nabla_{\mu_k}
Q(\theta,\theta^\prime)=
\sum_{n=1}^N\mathbb{1}\left[z_n=k\right]\left(x_n-\mu_k\right)=0
$$

Taking the product, separating the sums, and re-arranging terms gives:

$$
\sum_{n=1}^N\mathbb{1}\left[z_n=k\right]x_n=
\mu_k\sum_{n=1}^N\mathbb{1}\left[z_n=k\right]
$$

Finding $\mu_k$ is now easy:


$$
\mu_k=
\frac{1}{\sum_{n=1}^N\mathbb{1}\left[z_n=k\right]}
\sum_{n=1}^N\mathbb{1}\left[z_n=k\right]x_n
$$

Which is a slightly contrived way of saying that we take the average of all
points assigned to cluster $k$. Exactly what we were expecting!

We might also want to compute the Hessian to make sure this is actually a
minimum of $Q$. Luckily this is easy:

$$
\nabla^2_{\mu_k}
\sum_{n=1}^N\ln p(x_n\vert z_n,\mu_k)
=\sum_{n=1}^N\mathbb{1}\left[z_n=k\right]\nabla_{\mu_k}\left(x_n-\mu_k\right)
=-\sum_{n=1}^N\mathbb{1}\left[z_n=k\right]I
$$

Which is just some negative multiple of the identity matrix. Since all its
eigenvalues are negative and $Q$ is a convex quadratic, we are indeed in the
global minimum.

### Complete algorithm
To sum up, the EM algorithm for $K$-means clustering is:

 1. Initialize the cluster centers $\theta=\mu_1,\ldots,\mu_K$
 2. E step: Compute $p(z\vert x,\theta)$ by assigning each point to the closest cluster
    center.
 3. M step: Maximize $Q(\theta,\theta^\prime)$ by assigning the cluster centers
    to the average of the points assigned to each cluster.
 4. Repeat until the cluster centers are not modified anymore.
