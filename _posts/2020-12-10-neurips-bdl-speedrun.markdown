---
title: "Speedrunning the NeurIPS Bayesian Deep Learning Poster Session"
layour: post
date: 2020-12-11 09:00:00 +0200
markdown: kramdown
---

Thanks to the virtual platform [Gather.town][gt], I could swiftly zip from
poster to poster in the [NeurIPS Bayesian Deep Learning meetups][bdl] and write
a short summary of all 71 posters in only 2:15 hours!

<!-- more -->

## Gather Town
Gather.town is a virtual platform that looks like a video game, where you move
from place to place and see virtual avatars of other people. Posters were in
different locations and could be viewed by moving there and pressing a key. You
are automatically connected and disconnected to voice and video chat rooms with
nearby participants as you move around, and which makes it very easy to join
discussions around posters.

This was the first time I tried this platform and I am surprised at how easy it
was to visit posters and feel connected to the conference itself. I liked it
much more than a previous online conference that had traditional rooms, one for
each poster. Viewing a poster meant following a link to its room, which was
quite cumbersome. Eliminating this barrier of moving to different rooms by
following links is Gather.town's killer feature.

## The Speedrun
Initially I was just walking from poster to poster, simply looking at what
people were doing. After a while I started taking notes to avoid forgetting
everything by the next day, and moving systematically from a poster to the next.
Only at the end of the first session I realized I had visited half of the
poster, and formally decided to visit the other half during the next session and
write a short summary of each work, reproduced below. That amounts to 71 posters
in 2 hours and 15 minutes, or slightly less than two minutes per poster.

## What makes a bad poster?
Trying to get the essence of a poster in two minutes was not easy, especially
since Bayesian Deep Learning is not my primary area of research (although I am
quite interested in it and loosely follow what happens there). Clearly, the
poster itself can greatly help or hinder this process, and it is easy to
understand if a poster was made purposefully or just by stitching content from
the paper.

Here are three recurring issues I noticed:

 1. **The poster cannot be understood without your explanations.** Some posters
    only contained figures and formulas, with little explanations of what was
    going on. We all get told that *figurez good text baddd*, but it is
    definitely possible to overdo it.
 1. **The poster contains multiple and/or long paragraphs of text,** probably
    coming from the paper. We are all in a hurry, I will read the paper later
    *iff the poster makes me want to do so.* Condensing each paragraph into a
    bullet point would definitely help, but this would probably mean that ...
 1. **The poster is structured like a paper,** containing abstract,
    introduction, background, methods, results, discussion, and references. This
    is a lot of space wasted on details that are not important for a poster, and
    makes it difficult to quickly understand your contribution. Some of that
    information must certainly be included, but such a format makes it hard to
    distill the essence of your work.

The best posters I have seen contained a couple of very carefully crafted and
well visible sentences telling me what is the problem and what is the solution,
together with a sort of graphical abstract. The very best poster, in my opinion,
was *Expressive yet Tractable Bayesian Deep Learning via Subnetwork Inference*,
by Erik Daxberger et al. At the top, it says:

> We propose a Bayesian deep learning method that does expressive inference over
> a carefully chosen subnetwork within a neural network, and show that this
> works better than doing crude inference over the full network.

Short, clear, and to the point. Below, the four steps of the methods, with large
and eloquent figures and a couple of descriptive sentences for each of them. At
the bottom some charts with results. It was crystal clear. The poster did lack
details, and I would argue that *this is exactly why it was a great poster*.

**A bad poster emphasizes the details and leaves out the big picture.** Exactly
the opposite of what it is supposed to do.

Many posters were like this.

(Short anecdote: several years ago I got a bad grade for an assignment
because the poster I made did not mention p-values. I still hold a grudge.)

## What makes a good poster?
Based on the discussion above, a good poster has relatively little content that
is laser-focused:

 1. **Why?** What is the problem you are solving.
 1. **What?** What is your method doing?
 1. **How?** An intuition for how you solve the problem.

A few bullet points for each of the above and one or two images of the concepts
should be enough to convey most works. You cannot just take your paper and trim
content until it fits into a single page. You, the author, need to make the
effort of summarizing your work so that I, the reader, can understand in twenty
or so seconds what, why and how you did what you did.

The poster should also contain enough details to sustain a deeper conversation
about your work, but make sure the three points above stand out from the rest,
for example by grouping them at the top left and enclosing them in a colored
box.

## Trends

Some topics that are frequently studied are:

 - How to facilitate the design of better priors,
 - How to perform more efficient inference or predictions,
 - How to increase the flexibility of flows, and
 - How to improve applications of uncertainty, e.g. in out-of-distribution
   detection.
 
## Poster Summaries
Before diving into the short summaries, allow me to apologize to the authors if
my summary does not make justice to their work. Writing a short summary
necessarily means that I have to leave out a lot of information. Considering
that I only looked at each poster for less than two minutes (on average) and
that most of them were out of my area of expertise, in some cases I have
definitely missed the essence or importance of the work. Apologies.

**Uncertainty via Stochastic Gradient Langevin Boosting: Bayesian Gradient
Boosted Decision Trees**, Andrey Malinin, Liudmila Prokhorenkova, Alexei
Ustimenko

Gradient boosted trees are normally trained with stochastic gradient descent.
Langevin dynamics is a gradient descent procedure that eventually results in
samples from the true posterior. Malinin et al. propose to use these samples to
form an ensemble of trees, so that the predictive uncertainty comes from the
variance of the ensemble predictions.

**Know Where to Drop Your Weights: Towards Faster Uncertainty Estimation**,
Akshatha Kamanth, Dwaraknath Ganeshwar, Matias Valdenegro-Toro

Predictive uncertainty via Monte Carlo dropout is expensive to obtain due to the
many forward passes required. Kamanth et al. propose to apply dropout only to
some of the last layers, while re-using the activations of the first few layers
to make inference faster.

**Last Layer Marginal Likelihood for Invariance Learning**, Pola Schwobel,
Martin Jorgensen, Mark van der Wilk

Some invariances can be encoded in the architecture of the network, while others
are usually learned by augmenting the training set. Jorgensen et al. incorporate
arbitrary parametric and differentiable transformations into the network and
learn them by optimizing the likelihood marginalized over sets of augmented
examples, resulting in increased robustness to such transformations.

**One Versus All for Deep Neural Network Incertitude (OVNNI) Quantification**,
Gianni Franchi, Andrei Bursuc, Emanuel Aldea, Severine Dubuisson, Isabelle Bloch

For K-class classification problems, Franchi et al. show that combining the
predictions of an all-versus-all classifier with the predictions of K
one-versus-all classifier gives more reliable estimates of Out-of-Distribution
samples.

**Encoding the Latent Posterior of Bayesian Neural Networks for Uncertainty
Quantification** Gianni Franchi, Andrei Bursuc, Emanuel Aldea, Severine
Dubuisson, Isabelle Bloch

Previous work showed how to compress an ensemble of networks by using a shared
set of weights, modifying them with a different rank-one weight matrix for each
network of the ensemble. Franchi et al. propose instead to sample this
modification from the latent representations of a variational autoencoder.

**Identifying Causal-effect Inference Failure Using Uncertainty-aware Models**
Andrew Jesson, Soren Mindermann, Uri Shalit, Yarin Gal

Jesson et al. show that epistemic uncertainty can be used to understand when
causal inference results are not reliable due to issues with the data, and
propose to abstain from giving recommendations in cases like these.

**End-to-End Semi-Supervised Learning for Differentiable Particle Filters** Hao
Wen, Xiongjie Chen, Georgios Papagiannis, Conghui Hu, Yunpeng Li

Inference for traditional filtering models can be difficult for high dimensional
states or when an appropriate model cannot be formulated

Differentiable filters are able to learn generative models from observations
when not enough knowledge to formulate a model is available. They, however,
require labeled examples of true hidden states. Wen et al. show how to alleviate
this issue and learn parameters of differentiable filters with less data.

**Neural Empricical Bayes: Source Distribution Estimation and its Applications
to Simulation-Based Inference** Maxime Vandegar, Michael Kagan, Antoine
Wehenkel, Gilles Louppe

Given observations from a physical process, the problem is to learn the inputs
to the physical process that resulted in the observed distribution. Vandegar et
al. propose several methods to do so.

**Uncertainty in Structured Prediction: Pushing the Scale Limits of
Uncertainty** Andrey Malinin, Mark Gales

Malinin et al. show how to efficiently create ensembles of autoregressive
models, arguing that one should combine predictions at the token level.

**TyXe: Pyro-Based Bayesian Neural Networks for Pytorch Users in 5 Lines of
Code** Hippolyt Ritter, Theofanis Karaletsos

Ritter et al. present a software framework based on Pyro and Pytorch that makes
it easier to develop Bayesian neural networks.

**Expressive yet Tractable Bayesian Deep Learning via Subnetwork Inference**
Erik Daxberger, Eric Nalisnick, James Urquhart Allingham, Javier Antoran, Jose
Miguel Hernandez-Lobato

Daxberger et al. show how to improve the efficiency of Bayesian deep learning by
only considering uncertainty of the weights of a subset of the network weights.

**Sparse Encoding for More-interpretable feature-selecting representations in
probabilistic (Poisson) matrix factorization** Joshua C. Chang, Patrick
Fletcher, Jungmin Han, Ted L. chang, Shashaank Vattikuti, Bart Desmet, Ayah
Zirikly, Carson C. Chow

Normal sparse coding procedures focus on decoding from the latent codes.
Chang et al. show that focusing on the encoding part results in better
interpretations of the codes.

**Rethinking Function-Space Variational Inference in Bayesian Neural Networks**
Tim G. J. Rudner, Zonghao Chen, Yarin Gal

Variational inference is traditionally performed on weights. Rudner et. al show
how to derive the distribution over functions corresponding to a given
distribution over weights, and argue that working with such a distribution
results in better uncertainties.

**A Probabilistic Perspective on Pathologies in Behavioural Cloning for
Reinforcement Learning** Tim G. J. Rudner, Cong Lu, Michael A. Osborne, Yarin
Gal

Reinforcement learning methods that learn from expert demonstration tend to
collapse to zero-variance predictions for undemonstrated states. Rudner et al.
use a Gaussian Process to enforce a distribution over policies that does not
exhibit this kind of collapse.

**Outcome-Driven Reinforcement Learning via Variational Inference** Tim G. J.
Rudner, Vitchyr H. Pong, Rowan McAllister, Yarin Gal, Sergey Levine

Rudner et al. show how to learn policies that reach a specified outcome without
needing an explicit, user-defined reward signal.

**On Signal-to-noise Ratio Issues in Variational Inference for Deep Gaussian
Processes** Tim G. J. Rudner, Oscar Key, Yarin Gal, Tom Rainforth

One problem with using importance sampling in variational inference is that the
signal-to-noise ratio of the gradient increases as more samples are used. Rudner
et al. introduce a new gradient estimator that does not have this issue.

**Self Normalizing Flows** T. Anderson Keller, Jorn W. T. Peters, Priyank Jaini,
Emiel Hoogeboom, Patrick Forre, Max Welling

Normalizing flows use fixed parametric transformations for which the inverse
must be specified and computed analytically. Hoogeboom et al. propose to learn
a transformation and its inverse as the encoder and decoder of an autoencoder.

**Fixing Asymptotic Uncertainty of BNNs with Infinite ReLU Features** Agustinus
Kristiadi, Mathias Hein, Philipp Hennig

The confidence of BNNs with ReLU activations is low away from the data, but not
the maximum entropy that is expected. Kristiadi et al. propose to remove the
residual certainty by adding a Gaussian Process with a novel kernel to the
predictions of the network.

**Deep Kernel Processes** Lawrence Aitchison, Sebastian Ober, Adam X. Yang

Aitchison et. al propose a generalization of Deep Gaussian Processes in which
the kernel of each layer is constructed through samples from a Wishart
distribution.

**Liberty or Depth: Deep Bayesian Neural Nets Do Not Need Complex Weight
Posterior Approximations** Sebastian Farquhar, Lewis Smith, Yarin Gal

A common worry of mean-field variational inference is that the approximate
posterior is not expressive enough to capture the true posterior. Farquhar et
al. show that this is not true for sufficiently deep networks, and a mean field
approximation can approximate the functional posterior.
     
**Augmented Sliced Wasserstein Distances**, Xiongjie Chen, Yongxin Yang, Yunpeng Li

Despite its usefulness, the Wasserstrein distance is difficult to compute
exactly and must be approximated. Chen et al. introduce a new method to do so.

**Bayesian Active Learning with Pretrained Language Models** Katerina Margatina,
Loic Barrault, Nikos Aletras

Language models tend to be huge with lots of parameters, requiring a
considerable computational budget to train. Margatina et show how to use
epistemic uncertainty in an active learning setting to fine-tune language
models for a given task.
     
**ThompsonBALD: Bayesian Batch Active Learning for Deep Learning via Thompson
Sampling**, Jaeik Jeon, Brooks Paige

In batch active learning, the labels for multiple examples are required at the
same time. Jeon et al. introduce a method based on Thompson sampling to increase
the diversity of the samples for which labels are required, making the process
more sample efficient.

**Wavelet Flow: Fast Training of High Resolution Normalizing Flows** Jason J.
Yu, Konstantinos G. Derpanis, Marcus A. Brubaker

Normalizing flows can be very expensive to train. Yu et al use Haar wavelets to
downsample and learn from lower resolution images, thus reducing the
computational burden.

**Learning under Model Misspecification: Applications to Variational and
Ensemble Methods** Andres R. Masegosa

Masengosa points out that Bayesian model averaging is not reliable when the
model is misspecified. A theoretical analysis gives a better bound for the
expected generalization error, allowing to train more accurate yet misspecified
models.

**Global Canopy Height Regression from Space-borne LiDAR** Nico Lang, Nikolai
Kalishek, John Armston, Konrad Schindler, Ralph Duaya, Jan Dirk Wegner

Lang et al. show that considering aleatoric and epistemic uncertainty results in
better predictions of tree heights from satellite imaages.

**Sparse Uncertainty Representation in Deep Learning with Inducing Weights**,
Hippolyt Ritter, Martin Kukla, Cheng Zhang, Yingzhen Li

A Bayesian neural network requires more parameters than its deterministic
counterparts, decreasing computational efficiency. Ritter et al. propose to
generate the full set of weights from a smaller set, and perform inference only
on this smaller set.

**Designing Priors for Bayesian Neural Networks**, Tim Pearce, Russell Tsuchida,
Alexandra Brintrup, Mohamed Zaki, Andy Neely and Andrew Y.K. Foong

Despite the connection between neural networks and Gaussian Processes is well
known, it remains difficult to find a neural network architecture that
corresponds to a desired prior distribution. Pearce et al. show how to derive
architectures that correspond to given Gaussian Process kernels, which are much
easier to desing.

**Deep Evidential Regression** Alexander Amini, Wilko Schwarting, Ava Soleimany,
Danela Rus

Amini et al. extend the standard framework for aleatorc uncertainty by using a
hierarchical model, and show that the resulting uncertainty in the aleatoric
mean and variance corresponds to the epistemic uncertainty of the model.

**Evidential Deep Learning for Guided Molecular Property Prediction and
Discovery**, Ava P. Soleimany, alexander amini, Samuel Goldman, Daniela Rus,
Sangeeta N. Bhatia, Connor W. Coley

Using Evidential deep learning, Soleimany et al. show how to better identify
novel antibodies and design improved acquisition functions for active learning.

**Depth Uncertainty in Neural Networks**, Javier Antoran, James Urquhart
Allingham, Jose Miguel Hernandez-Lobato

Depth is an important part of a network's architecture as it corresponds to
wigglier functions. Antoran et al. show how to infer an appropriate depth by
connecting each layer to the output of the network and learning which
connections should be masked out.

**Decentralized Langevin Dynamics for Bayesian Learning** Anjaly Parayil, He
Bai, Jemin George, Prudhvi Gurram

Parayil et al. show how it is possible to train a Bayesian neural network in a
distributed environment via Langevin dynamics.

**i-DenseNets**	Yura Perugachi-Diaz, Jakub M. Tomczak, Sandjai Bhulai

Perugachi-Diaz et al. show how to improve training residual normalizing flows.

**BayesFlow: Scalable Amortized Bayesian Inference with Invertible Networks**
Stefan T. Radev, Ullrich Kothe

Radev et al. show how to learn a Bayesian invertible model to infer the
parameters of a given simulation.

**General Invertible Transformations for Flow-based Generative Models** Jakub M. Tomczak

The transformations used in normalizing flows require the inverse to be
specified. Tomczak shows how to build a general invertible transformation from
arbitrary functions.

**SurVAE Flows: Surjections to Bridge the Gap between VAEs and Flows** Didrik
Nielsen, Priyank Jaini, Emiel Hoogeboom, Ole Winther, Max Welling

The transformation used in normalizing flows should be invertible, hence
injective. This prevents useful transformations such as dimensionality
reduction. Didrik et al. show how to circumvent this issue by using
deterministic, non-injective transformations with stochastic inverse (or
vice-versa**.

**A Bayesian Perspective on Training Speed and Model Selection** Clare Lyle,
Lisa Schut, Binxin Ru, Yarin Gal, Mark van der Wilk

Lyle et al. show that networks that are faster to train also have a larger
marginal likelihood. Based on this insight, the sum of a certain subset of
training losses is proposed as a new estimator of the marginal likelihood.

**The Ridgelet Prior: A Covariance Function Approach to Prior Specification for
Bayesian Neural Networks** Takuo Matsubara, Christ Oates, Francois-Xavier Briol

When viewed as a Gaussian Process, the prior induced by a neural network is
often undesirable. Matsubara et al. propose a new weight initialization scheme
that ensures such a prior distribution corresponds to a chosen prior.

**Bayesian Neural Network Priors Revisited** Vincent Fortuin, Adria
Garriga-Alonso, Florian Wenzel, Gunnar Ratsch, Richard Turner, Mark van der
Wilk, Lawrence Aitchison

Based on the observation that the posterior of a neural network is often
heavy-tailed and non-isotropic, Fortuin et al. propose new priors with these
characteristics and show that they reduce model misspecification.

**Sampling-free Variational Inference for Neural Networks with Multiplicative
Activation Noise** Jannik Schmitt, Stefan Roth

Variational inference can be expensive since it requires Monte Carlo samples
from the weight distribution, as well as twice as many parameters as a
deterministic network. Schmitt et al. propose deterministic weights and noisy
activations and show how to derive the variational posterior in this setting
without the need for samping.

**Clue: A Method for Explaining Uncertainty Estimates** Javier Antoran, Umang
Bhatt, Tameem Adel, Adrian Weller, Jose Miguel Hernandez-Lobato

Antoran et al. propose a method to generate counterfactual examples that have
the same predictions but lower uncertainty, thus highlighting which parts of the
inputs are to blame for the uncertainty.

**Temporal-hierarchical VAE for Heterogenous and Missing Data Handling**
Daniel Barrejon-Moreno, Pablo M. Olmos, Antonio Artes-Rodriguez

By using a hierarchical model and a recurrent neural network on the hidden
states of a variational autoencoder, Barrejon-Moreno et al. show how to pool
information from different samples and improve predictions when data is missing.

**Efficient Low Rank Gaussian Variational Inference for Neural Networks** Marcin
B. Tomczak, Siddharth Swaroop, Richard E. Turner

Traditional variational inference for Bayesian neural networks uses diagonal
covariances mostly for computational reasons. Tomczak et al. show an analytic
form of the ELBO for a low-rank approximation that does not require explicit
computation of the covariance matrix.

**Ensemble Distribution Distillation: Ensemble Uncertainty via a Single Model**
Andrey Malinin, Sergey Chervontsev, Ivan Provilkov, Bruno Mlodozeniec, Mark
Gales

Ensembles are computationally expensive because they require to train and
predict with several models. Malinin et al. show how to eliminate the problem by
deriving a single network that simultaneously predicts mean and variance of the
ensembled predictions via Dirichlet (classification) or Wishart (regression)
distributions.

**Towards a Unified Framework for Bayesian Neural Networks in PyTorch** Audrey
Flower, Beliz Gokkaya, Sahar Karimi, Jessica Ai, Ousmane Dia, Ehsan
Emamjomeh-Zadeh, Ilknur Kaynar Kabul, Erik Meijer, Adly Templeton

Flower et al. propose a new framework based on PyTorch for Bayesian deep
learning.

**Feature Space Singularity for Out-of-Distribution Detection** Haiwen Huang,
Zhihan Li, Lulu Wang, Sishuo Chen, Bin Dong, Xinyu Zhou

Based on the intuition that the learned features of out-of-distribution samples
change slowly during learning, Huang et al. propose a new metric inspired from
the Neural Tangent Kernel to identify such samples.


**Hierarchical Gaussian Processes with Wasserstein-2 Kernels** Sebastian G.
Popescu, David J. Sharp, James H. Cole, and Ben Glocker

Popescu et al. show that the distributional uncertainty portion of the posterior
of a Gaussian Process tends to collapse to zero variance, and propose a new
method to mitigate this issue.

**Sample-efficient Optimization in the Latent Space of Deep Generative Models
via Weighted Retraining** Austin Tripp, Erik Daxberger, Jose Miguel
Hernandez-Lobato

Bayesian optimization can be used on representations learned by a generative
model. Tripp et al. improve the latent representations of promising samples by
periodically retraining the generative model and weighting the samples based on
their usefulness for the Bayesian optimization process.

**A Comparative Evaluation of Methods for Epistemic Uncertainty Estimation**
Lisha Chen, Hanjing Wang, Shiyu Chang, Hui Su, Qiang Ji

Despite the high number of methods proposed to estimate the epistemic
uncertainty of Bayesian neural networks, a systematic comparison of these
methods is lacking. Chen et al. conduct such a comparison and identify reliable
ways to identify the epistemic uncertainty according to the downstream task.

**Estimating Model Uncertainty of Neural Networks in Sparse Information Form**
Jongseok Lee, Matthias Humt, Jianxing Feng, Rudolph Triebel

Lee et al. use a dual representation of a Gaussian distribution to improve the
efficiency of approximate inference.

**Simple & Principled Uncertainty Estimation with Single Deep Model via Distance
Awareness** Jeremiah Liu, Zi Lin, Shreyas Padhy, Dustin Tran, Tania
Bedrax-Weiss, Balaji Lakshminarayanan

Liu et al. argue that good uncertainty can be obtained from a single model by
forcing the learned latent representations to preserve distances in data space,
and propose to do so via a Gaussian process with stationary kernel and spectral
normalization on the latent codes.

**Global Inducing Point Variational Posteriors for Bayesian Neural Networks and
Deep Gaussian Processes** Sebastian W. Ober, Laurence Aitchison

Inference for Gaussian processes can be made more efficient by using a
restricted set of learned pseudo-inputs. Ober et al. propose to use this method
for each layer of a Bayesian neural network for a scalable method that still
allows for correlations between layers.

**Unpacking Information Bottlenecs** Andreas Kirsch, Clare Lyle, Yarin Gal

Kirsch et al. shed light on the correspondence between the information
bottleneck principle and finding the minimal sufficient statistic for the labels
conditioned on the data, showing how such training procedure improves resistance
to adversarial attacks.

**Revisiting the Train Loss: An Efficient Performance Estimator for Neural
Architecture Search** Binxin Ru, Clare Lyle, Lisa Schut, Mark van der Wilk,
Yarin Gal

Estimating the generalization performance of a network during neural
architecture search can be expensive. Ru et al. show that this can be done
reliably using only the training losses, thus improving the efficiency of the process.

**Using hamiltorch to Perform HMC over BNNs with Symmetric Splitting** Adam D.
Cobb, Brian Jalaian

Cobb et al. show that factorizing the Hamiltonian as a sum of separate
components achieves better mixing, thus more efficient sampling for Hamiltonian
Monte Carlo methods.

**Cross-Pollinated Deep Ensembles** Alexander Lyzhov, Daria Voronkova, Dmitry Vetrov

Lyzhov et al. propose a new way of training deep ensembles, fine-tuning the
ensemble by sharing the forward pass across the different networks, i.e., send
each minibatch to the next layer of a different network.

**Bayesian Active Learning for Wearable and Mobile Health** Gautham Krishna
Gudur, Abhijith Ragav, Prahalathan Sundaramoorthy, Venkatesh Umaashankar

Health applications of wearables need to model the human behavior, and the
models employed can be improved using active learning. Krishna et al. use an
acquisition function based on Monte Carlo dropout to bring improvements in the
performance of such models.

**Hierarchical Gaussian Process Priors for Bayesian Neural Networks** Theofnis
Karaletsos, Thang D. Bui

Karaletsos et al. improve out-of-sample uncertainties by using Gaussian
processes to transform layer-specific latent variables into the layer's weights.

**Bayesian Neural Networks for Acoustic Mosquito Detection** Ivan Kiskin, Adam
D. Cobb, Steve Roberts

Kiskin et al. use a Bayesian neural network to detect mosquitoes based on audio
data.

**The Hidden Uncertainty in a Neural Network's Activations** Janis Postels,
Hermann Blum, Cesar Cadena, Roland Siegwart, Luc van Gool, Federico Tombari

The uncertainty in the activations of the hidden layers can be used to detect
out-of-distribution samples. Postels et al. show that it can also be used to
improve the estimation of epistemic and aleatoric uncertainty.

**Mixed-curvature Conditional Prior VAE** Maciej Falkiewicz

Falkiewicz unifies two models introduced previously to allow variational
autoencoders to learn multi-modal latent distributions and handle non-euclidean
latent spaces.

**Bayesian BERT for Trustful Hate Speech Detection** Kristian Miok, Blaz Skrlj,
Daniela Zaharie, Marko Robnik-Sikonja

By using Monte Carlo dropout in the attention layers of a BERT model, Miok et al
improve performance on hate speech detection.


**Bayesian Multi-task Learning: Fully Differentiable Model Discovery** Gert-Jan Booth

Partial differential equations are discovered by optimizing a joint loss
composed of a reconstruction term and a consistency penalty on the underlying
partial differential equation. Booth views this problem in a multi-task setting
and dynamically weighs the two losses based on the uncertainty in each task.

**Towards Principled Prior Assumption in Deep Learning** Lassi Meronen, Martin
Trapp, Arno Solin

Expressing arbitrary prior distributions for Bayesian neural networks is no easy
task. Meronen et al. present a novel activation function corresponding to a
stationary Matern kernel that results in high predictive uncertainty far from
the training data.

**Perfect Density Models Cannot Guarantee Anomaly Detection** Charline Le Lan,
Laurent Dinh

A common assumption in anomaly detection is that anomalies have low likelihood.
Le Lan et al. argue that this is intuition is, in fact, wrong, showing how to
build continuous invertible maps that assign arbitrary density to anomalies
while preserving the overall distribution.

**Semi-supervised Learning of Galaxy Morphology Using Equivariant Transformer
Variational Autoencoders** Mizu Nishikawa-Toomey, Lewis Smith, Yarin Gal

The efficiency of automated classification of visual features of galaxy images
can be improved by relying on the redundancy of the data. Since many images are
just a transformed version of a "canonical** galaxy, Nishikawa-Toomey et al.
propose to undo such transformation by learning its parameters.

**Bayesian Deep Ensembles via the Neural Tangent Kernel** Bobby He, Balaji
Lakshminarayanan, Yee Whye Teh

He et al. explored the connection between deep ensembles, the neural tangent
kernel and deep Gaussian processes.

**Robustness of Bayesian Neural Networks to Gradient-Based Attacks** Ginevro
Carbone, Matthew Wicker, Luca Laurenti, Andrea Patane, Luca Bortolussi, Guido
Sanguinetti

Carbone et al. show that the expected gradient of a Bayesian neural network
under adversarial attacks is zero, thus robustness to this type of attacks can
be achieved simply by taking a large number of samples from the posterior.

**DrugEx2: Drug Molecule De Novo Design by Multi-Objective Reinforcement
Learning for Polypharmacology** X. Liu, K. Ye, H.W.T van Vlijmen, M.T.M.
Emmerich, A.P. IJzerman, G.J.P. van Westen F8

Liu et al. extend and improve upon their previous work to generate novel
molecules by jointly considering three objectives: high affinity, high
diversity, and similar properties to known drugs.

**Why Aren't bootstrapped Neural Networks Better?** Jeremy Nixon, Dustin Tran,
Balaji Lakshminarayanan

Bootstrapping is a widely used technique in statistics, but does not work well
in deep learning. Nixon et al. argue that this is because the reduced amount of
unique training samples is not able to make up for the increased randomness.

**Multi-headed Bayesian U-Net** Moritz Fuchs, Simon Kifhaber, Hendrik Mehrtens,
Faraz Zaidi, Camlia Gonzalez, Arjan Juijper, Anirban Mukhopadhyay

Despite their popularity in segmentation, vanilla U-nets provide poor
out-of-distribution generalization and overconfident predictions. Fuchs et al.
propose a multi-head U-net trained via a variational objective.


[gt]: https://gather.town/
[bdl]: http://bayesiandeeplearning.org
