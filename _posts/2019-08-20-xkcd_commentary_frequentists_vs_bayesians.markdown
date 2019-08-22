---
layout: post
title:  "xkcd commentary - Frequentists vs. Bayesians"
date:   2019-08-20 11:41:22 +0200
categories: jekyll update
---

I found [this xkcd comic](https://xkcd.com/1132/) hilarious and, at the same
time, brilliant:

![](https://imgs.xkcd.com/comics/frequentists_vs_bayesians.png){: .center-image}

The reason why I like it so much is that it shows what is wrong with frequentist
hypothesis testing very plainly, and why a Bayesian approach might be
preferable. And mind you, this isn't just a philosophical issue, devoid of
real-world value, we statisticians cannot agree on. On the contrary, it has
serious consequences: I am sure you heard of the replication chrisis plaguing
some fields of science. Essentially, people realized that it is not possible to
reach the same conclusions shown in some studies, and one of the culprits is
misunderstanding and wrongful application of hypothesis testing and p-values.

Here, I just want to explain what is going on in that comic. The two scientists
have a hypothesis they want to test (the sun exploded), and do so by gathering
some data (the answer from the machine). A good scientific hypothesis should be
_falsifiable_, it should be possible to show that it is false. If this is not
possible, then that theory is just pseudo-science on the same level as magic,
witches, and dragons. At least this was Popper's reaction to the other
scientific paradigm of the time, namely showing that a theory is true by means
of repeated observations. Things have changed since then, most notably
falsifiability was rejected as a criterion for separating science from
non-science.

The frequentist approach to this task is to assume that the hypothesis is false
(to be precise, that there is "no effect") and compute the probability of the
observations under this assumption; if this probability (the _p-value_) is low
enough, then we can be reasonably sure that the hypothesis must be true,
otherwise _nothing can be said_. Now, people mindlessly use 0.05 as a threshold
to say that something is statistically significant, even though there is no
particular reason to use this value and not another. The true story is that
Fischer, who first developed the theory behind p-values, used this value as a
cut-off to establish that somethig _fishy_ is going on (ha-ha) and worthy of
more investigation. In practice, nowadays, the investigation just stops at that
threshold, as if we found the truth and nothing more needs to be done. (Check
[here](https://xkcd.com/882/) and [here](https://xkcd.com/1478/) for other xkcd
comics pointing out how silly this is).

Going back to the comic, we assume that the sun has _not_ exploded. Since the
machine answered "yes", it must be lying; as the machine only lies when the
outcome of a two-dices roll is a double six, the probability it did lie is
$1/36$. Conversely, the probability it did _not_ lie is $35/36$, so better save
yourselves.

This is obviously ridiculous, but why? Given our understanding of the working of
the sun, it is inconceivable that it will explode anytime soon, and we do not
wish a dice roll to change our opinion on that. There is also another, more
subtle, issue. Sure, the reasoning seems to work. Call the observations (machine
answered "yes") $D$ and the hypothesis (the sun exploded) $H$: $D$ is very
unlikely to happen if $H$ is false, since $D$ happened, then $H$ is true. This
works in mathematical logic, since $\neg H\Rightarrow \neg D$ is equivalent to
$D\Rightarrow H$, but just because of a quirk of the logical implication, namely
that a false premise _does_ imply a false conclusion. Things cannot work like
that in probability though: what if $D$ is _even more_ unlikely to happen if $H$
is true? (if the sun exploded, we would have around 8 minutes to roll the dices
before behing annihilated; it seems reasonable to assume that the scientists in
the comic are performing the experiment at least ten minutes after sunset,
unless they are very anxious individuals).

Essentially, the flaw of the frequentist reasoning is that it does not consider
the probability that $H$ itself is true, or, to be precise, it assumes that the
two outcomes are equally probable. We know this is not true, and we can express
this formally using Bayes' theorem, which states:

$$
p(H\vert D)p(D)=p(D\vert H)p(H)=p(H\cap B)
$$

(this is not the standard form, but I find it more illuminating and easier to
remember), where the vertical bar indicates conditioning: $D\vert H$ means
observing $D$ _after_ we observed (or assumed) $H$. With this notation, the
frequentist reasoning can be summarized as follows: "$p(D\vert\overline{H})$ is
too low, so $H$ is true". Silly right?

Let's now look at the Bayesian approach. We want to know $p(H\vert D)$, which
can be derived from Bayes' theorem:

$$
p(H\vert D)=\frac{p(D\vert H)p(H)}{p(D)}
$$

(this is actually how Bayes' theorem is presented in the first place). $p(D\vert
H)$ is the probability of the detector being honest about our terrible fate,
$p(H)$ our believed probability of the sun exploding _before_ we ask the
detector, and $p(D)$ the probability of the detector saying "yes" (independently
of the state of the sun). Given the working of the machine, we know $p(D\vert
H)=35/36$, and given our knowledge of physics we might say that $p(H)=10^{-6}$
or so. $p(D)$ is in general a bit more complicated to compute, and later I will
show you that it is not necessary to compute it. In this case, however, we can
easily get it using the _law of total probability_:

$$
p(A)=P(A\cap B_1)+\ldots+p(A\cap B_n)
$$

Where $B_1,\ldots,B_n$ is any partition of the sample space. In other words,
they are $n$ different alternatives, such that only one can happen at any given
time; then, the probability of $A$ is the probability that it happens when $B_1$
happens _or_ when $B_2$ happens, _or_ ... _or_ when $B_n$ happens. Since we can
choose anything we want for these sets, we will choose $H$ and $\overline H$,
and we use Bayes' formula once again to get:

$$
\begin{align}
p(D) &= p(D\cap H)+p(D\cap\overline H) \\
&= p(D\vert H)p(H)+p(D\vert\overline H)p(\overline H) \\
&= \frac{35}{36}10^{-6}+\frac{1}{36}\left(1-10^{-6}\right) \\
&\approx \frac{1}{36}
\end{align}
$$

which makes intuitive sense: we really do not expect the sun to explode, so when
the detector says "yes" we would rather believe the dice roll did not went well.
Putting all together we have:

$$
p(H\vert D)\approx\frac{35}{36}10^{-6}\cdot 36=3.5\cdot 10^{-5}
$$

i.e. the detector's answer barely changed the Bayesian's opinion about the state
of the sun. Well, given the answer, now he thinks that the sun is 35 times more
likely to have exploded, but it is still a tiny probability.

In this case, computing $p(D)$ was simple, but it usually is not, because it
requires precise knowledge about the _data generating distribution_, i.e. how
the data is "produced". In this case, we know how the detector works, but in the
general case you cannot write this down. What is the probability of that picture
you took last week with your friends? This is why we usually try our best to get
rid of this term whenever it pops out (i.e. always); usually we just ignore it,
because we are always take the oservations $D$ as fixed, so $p(D)$ is just an
annoying constant. In other cases we can actually remove it. Note that $p(D\vert
H)$ is a lot easier to compute, because it corresponds to our _model_ of the
world, i.e. to how we _assume_ the data is generated. On the other hand, $p(D)$
is the _true_ way in which data is generated, and we cannot afford any
assumption there (or we could use the law of total probability, but that
requires considering all possible data-generating processes, which are
infinite).

Going back to our sun detector, though, we can express the reasoning above using
the _odds_:

$$
O(H\vert D)=\frac{p(H\vert D)}{p(\overline H\vert D)}
=\frac{p(D\vert H)}{p(D\vert overline H)}\cdot\frac{p(H)}{p(\overline H)}
$$

Which is (are?) much simpler to compute:

$$
O(H\vert D)=\frac{35/36}{1/36}\cdot\frac{10^{-6}}{1-10^{-6}}\approx3.5\cdot10^{-5}
$$

note that it is equal to $p(H\vert D)$ _only by chance_. Such a low value means
that we are _extremely_ sure that $H$ is false.

All of this depends on our strong belief of the sun not exploding. If we were
indifferent to it, as our frequentist friend, we would indeed reach the same
conclusion. It can be weird to let our prior belief (or biases) change our
conclusions. Our dream is to only use data to make decisions. After all, math is
unbiased, right? Why not let the data speak for itself? As this comic shows,
this is simply not possible. Sure, priors are subjective, and when they are too
strong, no amound of data can make Bayesians change their mind. On the other
hand, no prior at all can make them very guillible, almost like a child. You
don't believe everything you read on the internet, do you? Then why do you
believe everything your data tells you?

An alternative interpretation of the reasoning conducted by the Bayesian
scientist is that 50\$, or anything else, is a sure bet, for if the sun really
exploded it will not matter that you lost it. This is the real genius behind
this comic.
