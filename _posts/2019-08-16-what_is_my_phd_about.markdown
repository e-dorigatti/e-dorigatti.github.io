---
layout: post
title:  "What is my PhD about?"
date:   2019-08-16 11:41:22 +0200
categories: jekyll update
---

So I have started my PhD last month, after a not-so-good experience in the
consulting industry that prompted me to reflect deeply on my values and goals. I
thought writing a blog would be a good way to improve my communication skills
and further disseminate my research beyond specialized conferences and journals.
Perhaps one day I will write about these reflections in more depth, but for now
it's enough t say that I believe one of my responsibilities as a scientist is to
spread my discoveries to those outside of my field. I still don't have a precise
idea of where this blog is headed, which style to use, etc., I will figure it
out with time. I will try to write at least one article accompanying each paper
I publish, with the idea that this article should make the paper more accessible
to non-researchers.

So let's talk a bit about what my PhD is about; I study in a field called
computational immunology, or immunoinformatics, which is a branch of
computational biology. Immunology is the study of the immune system, i.e. the
part of the body that tries to prevent it from getting sick, and fights diseases
during sickness. My PhD subject is actually statistics, so biology is just an
excuse to do machine learning :) Therefore, I already ask for forgiveness if
some of the things I say about biology are not 100% accurate.

The official title of my PhD is _Uncertainty-aware, Epitope-based Vaccine
Design_, which admittedly can be quite confusing the first few times you read it
(it was for me). Let's break it down, starting from the end: the main topic is
the design of vaccines. A vaccine is a substance that is used to train the
immune system to recognize and fight new diseases. Indeed, the immune system is
able to learn to identify and fight diseases it has never seen, in most cases;
in some cases, though, this process does not go as planned, for a number of
reasons. The fight between the immune system and _pathogens_ (anything that
results in illness) is really a cat-and-mouse game, and some of the most
terrible diseases, such as AIDS and cancer, learned to circumvent or even
disable the immune system. This is where vaccines come into play.

You might have heard that vaccines are just an injection of dead bacteria, and
the first vaccines actually worked like that (consider that the Chinese started
doing this over one thousand years ago). Newer types of vaccines, however, are
designed using computers and can be synthetized in the laboratory, and this is
what I study. I will go in much more depth on this process in later blog posts,
for now it suffices to say that such a vaccine is composed by billions of copies
of the same molecule, or a handful of different molecules, and the building
blocks of these molecules are aminoacids. Designing a vaccine, therefore, means
coming up with a sequence of aminoacids with desirable properties, and then
producing it in a lab. I only study the first step, once I settle on a certain
sequence I pass it to a company that produces the real molecules and tests them.

The vaccines that I design are made from _epitopes_. To understand what they
are, I need to introduce the basic functioning of the immune system. Among the
main actors of the adaptive immune system are T cells, or T lymphocytes (from
lymph, the fluid of the Lymphatic System, and kyto, meaning cell); they float
around the body and inspect other cells to determine wheter they are good or
bad. On their surface they have thousands of receptors, each of which can bind
to a specific sequence of aminoacids, so-called _epitope_. Binding means that
the two molecules, the receptor and the epitope, attract each other and stick
together just like magnets. This step is very selective, because these two
molecules must have matching complementary shapes (think like tetris). As soon
as a receptor on a T cell binds to something, the T cell initiates a response
from the immune system to deal with the issue. Therefore, an epitope is a short
sequence of aminoacids (around 10 or 20) that, when recognized by a T cell,
triggers the immune system.

The vaccines that I design are made by assembling epitopes together, and the
process conceptually consists of two main steps: first, decide which epitopes
should be in the vaccine, and second decide how to best stitch them together so
that the body processes the vaccine as we intend to. What we want is for the
body to recognize that the long molecules in the vaccine are actually made by
shorter epitopes, to separate these epitopes and to present them to T cells. In
order to design a good vaccine, we have to consider all these three steps.

The last part is about uncertainty. Most of the knowledge we have in biology is
rather anecdotical and empirical, in the sense that we often know how things
work by observing the body, but we cannot explain quantitatively why things work
like that. Note that all scientific inquiry is based on observation and
experiments, but only sometimes we are able to distill this experience in a
precise, mathematical way. Up until recently, coming up with a formula to
describe a given process was a work of genius, requiring considerable knowledge
and imagination. Nowadays, we are trying to automate this process and have
computers derive formulas for us, and the field that does that is called machine
learning. Machine learning, together with improved measurement techniques, is
revolutionizing biology, because it is enabling us to accurately describe and
predict several processes that we only understood qualitatively until a few
decades ago. It is having the same effect that civil engineering had on how we
design and construct buildings and bridges: at the beginning, architects knew
what was going to stand up and what was going to crumple just by experience and
personal judgment, while today we are able to run complex simulations to test
how buildings will respond to earthquakes and withstand strong winds even before
they are constructed. This, in turn, allows us to compare hundreds of different
designs and explore the trade-off between accessibility, cost, aesthetics, etc.

So what is uncertainty? Essentially, being uncertain about a quantity means that
we are not sure about its value, we only know a range of likely values. We
cannot know tomorrow's temperature at midday, but we can reasonably say it is
going to be, for example, around 18 degrees Celsius, and most probably between
15 and 20. Why is uncertainty important? One of the reasons is that most of the
formulas we have are simplified description of reality that leave out some
details; even if we don't know how these details affect the result, we can know
to which extent they do, and this tells us if they are safe to ignore. Pluto's
gravitational field did influence the Apollo 11's trajectory to and from the
Moon, but the effect was so small that the additional complications of
considering it in the formulas (very troublesome) was not worth the increase in
accuracy (minuscule). Another reason why uncertainty is important is that the
inputs to the formulas we have often come from measurements, and measurements
are inherently imprecise, even if by a small degree.

Going back to the design of vaccines, I mentioned earlier that we should
consider three steps: whether we can make the body cut the vaccine between the
epitopes, whether these epitopes can be presented to T cells, and whether T
cells can recognize the epitopes. Thanks to machine learning, we can use
measurements and observations about this process to derive a formula that
predicts, given an epitope, whether it will successfully complete the three
required steps. The problem is that we do not really understand the formulas
produced by the computer, and we do not even understand what makes an epitope
successful in this endeavor! Then how can we trust the computer? How can we know
that these formulas give the right result? (usually they don't work in all
cases) If the computer can tell us how certain it is about its predictions, we
can investigate the mistakes it makes, better understand the biological
processes involved, ultimately trust that the computer is going to be correct in
its judgment, and if not, work around the uncertainty by leaving appropriate
safety margins.

So that was quite a lot of information! To sum up, my research focuses on
methods to design synthetic vaccines using computers. These vaccines are made
from epitopes, which are short sequences of aminoacids that trigger a response
from the body, and these methods should be able to tell us how confident they
are that the designed vaccine is safe and effective.
