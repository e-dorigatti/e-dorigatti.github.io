---
layout: post
title: "Teaching Variational Autoencoders"
date: 2022-01-13 12:00:00 +0200
categories:
 - Math
 - Deep Learning
 - Teaching
---

Trying to explain the fundamental concepts behind variational autoencoders made
me realize something much deeper about learning and teaching.

<!-- more -->

It took me quite a while to deeply understand variational autoencoders (VAEs). I
feel like many online tutorials only provide a shallow overview of the topic,
get bogged down explaining the (many) details of how they work, and barely, if
at all, touch the topic of what they actually are. It really nothing to do with
autoencoders, really.

Assuming that one knows what an autoencoder (AE) is, the idea of a VAE can be
reached easily by adding a fancy regularization term to the AE loss. The
justification for this regularizer is to force the latent space to be Gaussian
so that we can generate new samples that look like the ones in the training set.

While all of this is true, it is kind of missing the forest for the trees. The
key ideas behind VAEs are *latent variable models* and *amortization*.
Everything else, including variational inference and even autoencoders, is just
noise. So many things in machine learning derive from latent variable models
that studying the derivation of the ELBO early is mostly a waste of time. One
should rather focus on the high level concepts and their connections.

## Is that actually true?

One should rather focus on the high level concepts. Right now I am wondering
whether what I am saying is too reductionist, i.e., while true, maybe it is not
very helpful for those who are still learning the topic. I am reminded of a
(zen?) poem that I cannot find anymore but goes something like:

> A beginner sees a mountain.
>
> An expert sees rocks.
>
> A master sees a mountain.

I really like this poem because it is so true, simple and deep at the same time.
The beginner and the master have the same point of view but for opposite
reasons. The beginner only sees a mountain because according to their
inexperience that's all there is. The master sees a mountain because in their
experience all mountains are just the same. Experts are in that intermediate
stage where every mountain is an unique arrangement of rocks, and every rock has
a different shape than the next, and there are so many possible combinations. An
implication of the poem is that one cannot be a master without seeing all the
rocks first. **Even though mastery ends in the same place where it begins, the
journey makes all the difference.**

This happens in every discipline with a certain depth, including obviously
machine learning. It takes five minutes to understand generative models and
dimensionality reduction on a high level. But try to go under the surface and
you find autoencoders, variational autoencoders, conditional autoencoders,
principal component analysis, probabilistic principal component analysis,
non-linear principal component analysis, Gaussian process latent variable
models, Markov chains, hidden Markov models, normalizing flows, normalizing
flows *with* autoencoders, generative adversarial networks, Bayes nets, Factor
analysis, Markov random fields, ans so on, each of them with tens of variants
and with their own specific inference procedure, whether exact, approximate, and
whatnot. Only after studying all of this one realizes, deep in their heart, that
all of these are pieces of the same puzzle, or rocks of the same mountain.
Initially it's only ignorance, at the end it's knowledge.

That is why I felt this post was useless. Masters know this already. Experts are
too busy looking at rocks and still see the mountain with the perspective of a
beginner. Beginners are not yet aware of the presence of the rocks.

## Back to variational autoencoders

Since I was interrupted halfway through, I may as well finish what I started. So
forget about autoencoders and think at latent variable models. We assume that
every sample $x$ was generated starting from a latent variable $z$. How? No
idea, so let's train a deep neural network figure that out.

Speaking probabilistically, we assume that $x$ is a sample from a fixed
distribution $\mathcal{D}$ (usually Gaussian) with a location parameter given
that the neural network $f$ starting from the latent variable $z$, i.e.,

$$
x\sim\mathcal{D}(f(z))
$$

At this moment, we have no idea what $f$ and $z$ are. There are several
*inference* procedures to make this guess depending on what assumptions one is
willing to make. For example, when $f$ is known and not too complicated, the <a
href="{% post_url 2021-03-15-painless-em %}"> expectation maximization algorithm
</a> could be an option. In this case, however, we opt for variational inference
(VI), a method that allows us to fit an approximate distribution of our choice
to $z$ even with complicated, possibly unknown, $f$. As is common, we assume
that the approximate distribution is a standard normal and we do not care about
the variance, i.e., $z\sim\mathcal{N}(\mu_z, 1)$, where 1 is the identity
matrix.

A direct application of VI would keep $\mu_z$ as a vector of numbers
and adjust their values along with the weights of $f$ to best suit the dataset.
In theory this would work if all one cared about was the latent variables of the
dataset at hand. In practice, this may require lots of training examples to pull
off without overfitting. Hence, the second key idea of VAEs: *amortization*. It
is both simple and crazy at the same time: instead of keeping a separate $\mu$
for each example, let's have another deep neural network predict it! Calling
this network $g$, we have:

$$z\sim\mathcal{N}(g(x), 1)$$

$$x\sim\mathcal{N}(f(z), 1)$$

Note that if you use linear transformations for $f$ and $g$ you get
probabilistic PCA and you can find which matrix to use without using VI at all.
Keeping linearity and using different assumptions on $p(z)$ leads to factor
analysis, categorical PCA, canonical correlation analysis, and independent
component analysis. Variational autoencoders pop up from using deep neural
networks and VI. One could stick a normalizing flow at the end of $g$, perhaps
make it auto-regressive to deal with sequence data. You could have an
intermediate clustering step in the latent space, or, even better, have $g$ do
the clustering by using a mixture distribution for $p(z|x)$. Different rocks,
same mountain.

## Back to teaching

This was the frustration that motivated this post: you do not need to
understand VI to understand VAEs. Explaining VI and VAE together makes things
seem much more complicated than they actually are and hides connections to
related topics.

Separating signal (latent variable models) from noise (variational inference),
or, better, high level from low level concepts, is quite hard to do when one is
getting into a new topic. This is maybe why this post is not so useless after
all: **experts can reach mastery faster if they are explicitly told what to
ignore at first**.

