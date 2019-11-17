---
title: "The first project of my PhD"
layour: post
date: 2019-11-18 12:00:00 +0200
---

I am in the process of publishing the first paper I wrote in my PhD, and, as
promised, with this post I am making an effort to explain this work to a less
technical audience. I start, however, by quoting the abstract:

> Epitope-based vaccines have revolutionized vaccine research in the last
> decades. Due to their complex nature, bioinformatics plays a pivotal role in
> their development. However, existing algorithms address only specific parts of
> the design process or are unable to provide formal guarantees on the quality
> of the solution. Here we present a unifying formalism of the general epitope
> vaccine design problem that tackles all phases of the design process
> simultaneously and combines all prevalent design principles. We then
> demonstrate how to formulate the developed formalism as an integer linear
> program which guarantees optimality of the designs. This makes it possible to
> explore new regions of the vaccine design space, analyze the trade-offs
> between the design phases, and balance the many requirements of vaccines.


Depending on how much you understood of this, you might prefer to [jump directly
to the paper](https://www.biorxiv.org/content/10.1101/845503v1), or to keep
reading this blog post and, perhaps, read the paper later. Code and data are
available in [this GitHub
repository](https://github.com/SchubertLab/GeneralizedEvDesign).

## Introduction: the biology of epitope vaccines
Proteins are the building blocks of our bodies: in order to function correctly,
cells are continuously producing and using proteins for all sorts of processes.
The DNA is divided in a number of regions, called genes, each of which encodes a
specific protein, and is literally copied whenever that protein is needed. After
being produced, the protein folds into a specific tridimensional structure that
allows the protein to function as it is supposed to.

Unneeded, misfolded, or damaged proteins are broken up into pieces (_peptides_)
by the _proteasome_, [^maupin-furlow_proteasomes_2012] so that their amino acids
can be re-used to produce new proteins. Some of these peptides, however, are
"loaded" onto a structure called MHC (_Major Histocompatibility Complex_) class
I and the resulting block is transported on the surface of the
cell. [^blum_pathways_2013] Peptides presented by the MHC can then be inspected
by cytotoxic T-cells, which are equipped with receptors of varying shapes on
their surface. When a receptor comes into contact with a MHC-peptide complex of
compatible shape, the T-cell knows the inspected cell is malignant, and proceeds
to alert the whole immune system and destroy the other cell through its
"self-destruct button" (_apoptosis_). Peptides that trigger an immune response are
called _epitopes_.

The immune system produces T-cells with a wide variety of different receptors,
so as to increase the chance that there will be a receptor with the right shape
in case of disease. Once a specific receptor is activated, the immune system
will increase the number of cells with that specific receptor, so that the
problem can be identified and dealt with more quickly next time. The key idea
behind this process is that infected cells can be identified by the fact that
they produce new kinds of proteins that the body would not produce.

Vaccines are supposed to trigger this process in our body and train it to
quickly recognize the real pathogen and respond strongly since the beginning
(i.e. they are a _preventive_ measure). For this to work, the vaccine must be as
similar as possible to the pathogen, but without the adverse effects. Epitope
vaccines are a relatively recent innovation that uses synthetic molecules
instead of deactivated pathogens to trigger the immune system, and are believed
to be the solution to cancer, HIV, Malaria, Hepatitis C, Tubercolosis, and so
on. [^pardi_mrna_2018] [^olugbile_malaria_2010] [^zwaveling_established_2002]
The key issue is, then, how to design such molecules.

The starting point is a large number of sequences of the target pathogen; these
sequences are obtained by extracting some sample pathogens from the sick and
reconstructing their DNA. From there, we extract short sequences of nine amino
acids (nine is the most common size of peptides bound to MHC class I). We then
analyze each of these peptides to find the potential epitopes, select which ones
to include in the vaccine and, finally, find what is the best way to assemble
them into a protein. Our innovation is a new method to perform these two last
steps.

Cancer is particularly nasty and difficult to cure because it uses several
mechanisms to remain undetected by the immune system, for example by
down-regulating (decreasing production of) MHC (which is also produced inside
cells) and TAP (the _Transponder associated with Antigen Processing_, a set of
molecules that load peptides on the MHC molecule and transport the resulting
complex on the cell's surface), or by up-regulating (increasing production of)
so-called _checkpoint proteins_, which prevent T-cells to function correctly
around the cancerous region (e.g. by blocking the "self-destruct" button).
Actually, _checkpoint inhibitors_ (drugs that disable checkpoint proteins, so
that T-cells can work as intended) are currently one of the most promising
strategies to cure cancer, [^mellman_cancer_2011] [^alsaab_pd-1_2017] while
vaccines would be used at the early stages, so that the body can fight the
cancer before it gets too bad. [^finn_dawn_2017] [^melief_immunotherapy_2008]
[^hu_towards_2017] [^sahin_personalized_2018]

## Our solution
The novelty in our approach is that we tackle the epitope selection and the
epitope assembly problems at the same time, we are able to find provably optimal
solutions, and we incorporate the three vaccine design principles as special
cases of our formulation. Existing solutions focus only on one of these steps,
either by focusing only on epitope selection[^toussaint_universal_2011] or
epitope assembly, [^schubert_designing_2016] by not being able to guarantee they
found an optimal solution (or how far it is), [^fischer_polyvalent_2007] or
both. [^lundegaard_popcover_2010]

Our solution is based on what is known as the _team orienteering problem_, which
can be though of as the union of the _traveling salesman_ and the _knapsack_
problem. The epitopes are edges in a fully connected, weighted, directed
graph, and are associated with a reward that gives the strength of the immune
response that they elicit. The edges are weighted according to the chosen EV
design type. The problem is, then, to find one or more disjoint tours visiting
at most a given number of vertices that maximize the reward collected, while, at
the same time, keeping the total edge cost below a given threshold. Each tour in
such a graph encodes a protein, because it tells which epitopes to include and
in which order. There can be other optional constraints on the solution, asking,
for example, for a vaccine that covers a high portion of the pathogens or of the
HLA alleles (the genes encoding the MHC; this is a proxy for population
coverage).

If this is still not clear, let me make a simple, real-world example. Imagine
you are the manager of a warehouse with a long list of shipments to perform, and
you want to decide which ones to do today, and which ones to postpone (you get
new orders every day, so you hope that there will be some new deliveries near to
the ones you will not do today, so that you can do them together, hence more
efficiently). The locations of the deliveries stand for the vertices in the
graph, and the payment you receive for successfully delivering a package is the
associated reward. Delivery trucks can travel from any location to any other
location (this is the fully connected and directed part), however locations take
longer to reach from places that are far away (this is the weight of the edge
connecting them). You have at your disposal a certain number of delivery trucks,
and your goal is to find the best route so that you maximize the profit of the
deliveries you make, but keep the time required below a certain threshold.

As mentioned earlier, the epitopes, input to our algorithm, are extracted from
sequences of the target pathogen (its DNA) simply by taking all possible
substrings of 9 amino acids. It is difficult to express the immunogenicity
(reward) of an epitope, because it involves many processes that we cannot
predict with sufficient accuracy as of today. We know, however, that the binding
strength between MHC and the epitope is positively correlated with the strength
of the immune response, so this is what we use as reward. We also have to
account for the high variability of the MHC in humans, and we do this by
averaging the binding strength weighted by the probability of each HLA allele
appearing in the target population, so that epitopes that trigger a moderate
response in most patients are preferred to those that trigger a very strong
response in a small minority. Importantly, this allows us to design different
vaccines for different parts of the world. This is a good thing, it means that
the vaccines can be more effective for the target population.

The weight of the edges determines the type of vaccine. In string-of-beads
vaccines, the epitopes are joined sequentially, so the edge weight is defined as
the difficulty of cutting right in between them; by keeping the total cost below
a given threshold, we are ensuring that the vaccine is not too difficult to chop
up as intended. Mosaic vaccines are composed in such a way that every substring
of 9 amino acids is an epitope found in the pathogen; this makes them look very
similar to the pathogen, and indeed they proved very successful in several
clinical trials. [^kong_expanded_2009] [^santra_breadth_2012]
[^barouch_evaluation_2018] The edge weight for this type of vaccine is inversely
proportional to the overlap between the two epitopes; in this case, keeping the
weight low means designing a shorter vaccine by leveraging highly overlapping
epitopes. Another option is to not assemble the epitopes at all, and deliver
them separately in the vaccine. This, in practice, turns out not to work so
well, because such short proteins are unnatural and end up being processed in a
different way that does not trigger much of an immune response. They can be
designed with our framework, but I won't talk about them because of their
irrelevance.

In practice, we formulate the team orienteering problem as an _integer linear
program_ (ILP) [^vansteenwegen_orienteering_2011] and use an external solver to
find a solution. Briefly, an ILP is an optimization problem where the goal is to
find the values of the unknowns $x_1,\ldots,x_n$ that maximize a linear function
$c_1x_1+\ldots+c_nx_n$, while satisfying linear constraints of the form
$a_{i1}x_1+\ldots+a_{in}x_n\leq b_{i}$. Linear programs can be solved to
optimality, meaning that we are able to find the best values for the unknowns.
The "integer" in ILP simply means that all variables must take integer values,
in our case either zero or one. Interestingly, the introduction of integer
variables makes the problem NP-hard, but, as discussed later, will not be an
issue in our case.

## Results
Through several experiments, we show the new possibilities opened by considering
epitope selection and epitope assembly at the same time. For string-of-beads
vaccines, we are able to explore the trade-off between these two competing
objectives: a high immunogenicity, optimized in the selection phase, and a good
cleavage likelihood, optimized in the assembly phase. This means that our
framework can generate many solutions that all have different immunogenicity and
cleavage, but are optimal in the sense that they cannot be improved in one
quantity without decreasing the other (i.e. they are _Pareto efficient_
solutions).

We have an experiment showing the design of a _polypeptide cocktail_, i.e. a
vaccine that is composed of several shorter proteins; they are designed at the
same time, each of them being a different "team" in the team orienteering
problem. The fact that they are designed together means that the vaccine as a
whole is able to satisfy constraints that the single polypeptides, in isolation,
cannot. In our experiment, we show that the vaccine covers 99% of the pathogen
strains, even though each of the polypeptides has a coverage of about 90%. There
can be several advantages in a vaccine composed of several short proteins
instead of a single long one. They are, for example, easier to manufacture, and
easier to process by the body.

We then have a couple of experiments studying mosaic vaccines; they are superior
to string-of-beads vaccines both on paper and in clinical trials. This is a
consequence of their design, forcing overlaps between the epitopes they contain.
Without going into details on these experiments, the take-away is that mosaic
vaccines can naturally cover a large portion of the pathogens, even when this
was not required, and that they can be further improved by maximizing the
average epitope conservation together with the immunogenicity (in fact, this is
our advice to future users of our framework). In practice, this means that
mosaics tend to target regions of the pathogens that do not mutate frequently,
and this is great news because mutation is one of the main mechanisms that
pathogens employ to escape the immune system.

Finally, by virtue of our definition of immunogenicity, the resulting vaccines
all have a very good population coverage. As mentioned previously, though, the
field still lacks the tools to accurately compute epitope immunogenicity,
therefore, for now, we are limited to simple heuristics that, at least,
correlate with it.

## Limitations and challenges
The main disadvantage of a _general_ framework for vaccine design is that each
disease works in a different way, and thus effective vaccination might need to
leverage different mechanisms. We are still far from having an unified
understanding of the immune system that allows us to create a truly general and
universal vaccine, if such a thing is even possible. You see, pathogens could
just evolve and learn to evade the defenses created with the vaccine. In the
simplest case, we would just have to create a new vaccine that targets the new
mutations, while being based on the same underlying mechanism. The worst case
would be a pathogen evolving so as to fight the mechanism itself. To make things
concrete, consider cancer: as I mentioned previously, it employs a plethora of
strategies to disable the immune system and expand undetected. Vaccines naively
designed with any framework that does not account for this will be ineffective.
Indeed, acquired drug resistance is a real issue for many diseases, from cancer
and malaria to the common cold. Who will capitulate first?

By formulating the epitope vaccine design problem as a team orienteering
problem, we are assuming that each epitope contributes independently to the
immunogenicity of the vaccine. We cannot model possible interactions between
epitopes: in this case, the total immunogenicity would not be a simple sum of
the immunogenicities of the epitopes it is made of. Moreover, the immunogenicity
we compute is an optimistic estimate of the effective immunogenicity. For
string-of-beads vaccines, it does not take cleavage into account: the paper
shows that maximizing immunogenicity results in vaccines with very poor
cleavage. In practice, such vaccines are essentially ineffective, as almost
none of the epitopes we included will be recovered correctly. As for mosaic
vaccines, we sum the immunogenicities of overlapping epitopes, but we still
ignore which of these epitopes will be actually recovered, meaning that the
actual immunogenicity is, again, lower.

Formulating the team orienteering problem as an integer linear program further
limits the things we are able to ask from the vaccine, as we must use linear
objectives and constraints. This was not a problem in this project, but it is
nonetheless a limitation. However, by formulating the problem as an ILP we
gain some flexibility in adding more constraints to the vaccine we are looking
for, as long as they are linear in the unknowns. An example where this is not
possible is for population coverage: it can be computed by knowing which HLA
alleles are covered by the vaccine, but it requires squaring a certain quantity
which cannot be expressed as a linear combination of the variables. One can only
ask for a certain number of HLA alleles to be covered. In this project, we used
27 HLA alleles and can easily cover them all, meaning that only 7% of the world
population will not respond to the vaccine. There is, probably, a geographical
bias in this number, but in principle it can be avoided by carefully choosing
which alleles to include, remembering that population coverage competes with
immunogenicicy and pathogen coverage. It is better to design several highly
effective vaccines targeted at specific countries, rather than a single global
vaccine that works okay-ish for everybody.

Another potential issue of the ILP formulation is that finding a solution might
be extremely time consuming. In most cases, this process is reasonably fast for
this project, taking minutes or hours, even though there are _a lot_ of
variables and constraints (in the order of millions). Pruning the input graph is
an effective strategy to make the process quicker, as most epitopes are lacking
one or more of the qualities that we seek in a good vaccine. Most of the time,
anyways, is spent in optimizing solutions that are only a few percents away from
the optimal one, so the solving process can be safely interrupted early.

In general, vaccine designed and optimized _in silico_ (with the computer) are
achieving the first successes, but there is still a long way to go before they
can be designed reliably and efficiently. The main challenges are that there are
still so many things that we do not know, or that we cannot quantify precisely
enough. As I mentioned previously, for now we can predict the strength of the
immune response only in terms of MHC-epitope binding strength, but there are
many more processes that should be taken into account: proteasomal cleavage, TAP
transport, binding to the T-cell receptor, how the T-cell responds to bound
epitopes, etc. Progress is being made in these areas, but to get reliable
predictions we still need a lot of data or a better understanding at the
molecular level of the chemical processes involved. And there are many more
issues that we cannot even begin to approach, such as the efficacy of the
vaccine after several years and possible adverse effects it may have. For many
of these things, we even lack qualitative understanding, or are, simply,
clueless.

## References
[^maupin-furlow_proteasomes_2012]: Maupin-Furlow J. _Proteasomes and protein conjugation across domains of life._ Nat Rev Microbiol. 2012 Feb;10(2):100–11. 
[^blum_pathways_2013]: Blum JS, Wearsch PA, Cresswell P. _Pathways of antigen processing._ Annu Rev Immunol. 2013;31:443–73. 
[^kong_expanded_2009]:  Kong W-P, Wu L, Wallstrom TC, Fischer W, Yang Z-Y, Ko S-Y, et al. _Expanded Breadth of the T-Cell Response to Mosaic Human Immunodeficiency Virus Type 1 Envelope DNA Vaccination._ Journal of Virology. 2009 Mar 1;83(5):2201–15. 
[^santra_breadth_2012]: Santra S, Muldoon M, Watson S, Buzby A, Balachandran H, Carlson KR, et al. _Breadth of cellular and humoral immune responses elicited in rhesus monkeys by multi-valent mosaic and consensus immunogens._ Virology. 2012 Jul;428(2):121–7. 
[^barouch_evaluation_2018]: Barouch DH, Tomaka FL, Wegmann F, Stieh DJ, Alter G, Robb ML, et al. _Evaluation of a Mosaic HIV-1 Vaccine in a Randomized, Double-Blinded, Placebo-Controlled Phase I/IIa Clinical Trial and in Rhesus Monkeys._ Lancet. 2018 Jul 21;392(10143):232–43. 
[^vansteenwegen_orienteering_2011]: Vansteenwegen P, Souffriau W, Oudheusden DV. _The orienteering problem: A survey._ European Journal of Operational Research. 2011 Feb;209(1):1–10.
[^toussaint_universal_2011]: Toussaint NC, Maman Y, Kohlbacher O, Louzoun Y. _Universal peptide vaccines – Optimal peptide vaccine design based on viral sequence conservation._ Vaccine. 2011 Nov;29(47):8745–53. 
[^fischer_polyvalent_2007]: Fischer W, Perkins S, Theiler J, Bhattacharya T, Yusim K, Funkhouser R, et al. _Polyvalent vaccines for optimal coverage of potential T-cell epitopes in global HIV-1 variants._ Nature Medicine. 2007 Jan;13(1):100–6. 
[^schubert_designing_2016]: Schubert B, Kohlbacher O. _Designing string-of-beads vaccines with optimal spacers._ Genome Medicine 2016 Dec;8(1).
[^lundegaard_popcover_2010]: Lundegaard C, Buggert M, Karlsson A, Lund O, Perez C, Nielsen M. _PopCover: a method for selecting of peptides with optimal population and pathogen coverage._ In: Proceedings of the First ACM International Conference on Bioinformatics and Computational Biology - BCB ’10. Niagara Falls, New York: ACM Press; 2010 p. 658.
[^pardi_mrna_2018]: Pardi N, Hogan MJ, Porter FW, Weissman D. _mRNA vaccines — a new era in vaccinology._ nrd. 2018 Apr;17(4):261–79. 
[^hu_towards_2017]: Hu Z, Ott PA, Wu CJ. _Towards personalized, tumour-specific, therapeutic vaccines for cancer._ Nature Reviews Immunology. 2017 Dec 11;18(3):168–82. 
[^melief_immunotherapy_2008]: Melief CJM, Burg SH van der. _Immunotherapy of established (pre)malignant disease by synthetic long peptide vaccines._ Nat Rev Cancer. 2008 May;8(5):351–60. 
[^sahin_personalized_2018]: Sahin U, Türeci Ö. _Personalized vaccines for cancer immunotherapy._ Science. 2018 Mar 23;359(6382):1355–60. 
[^mellman_cancer_2011]: Mellman I, Coukos G, Dranoff G. _Cancer immunotherapy comes of age._ Nature. 2011 Dec 21;480(7378):480–9. 
[^alsaab_pd-1_2017]: Alsaab HO, Sau S, Alzhrani R, Tatiparti K, Bhise K, Kashaw SK, et al. _PD-1 and PD-L1 Checkpoint Signaling Inhibition for Cancer Immunotherapy: Mechanism, Combinations, and Clinical Outcome._ Front Pharmacol. 2017;8:561. 
[^finn_dawn_2017]: Finn OJ. _The dawn of vaccines for cancer prevention._ Nature Reviews Immunology. 2017 Dec 27;18(3):183–94. 
[^olugbile_malaria_2010]: Olugbile S, Habel C, Servis C, Spertini F, Verdini A, Corradin G. _Malaria vaccines - The long synthetic peptide approach: Technical and conceptual advancements._ Curr Opin Mol Ther. 2010 Feb;12(1):64–76. 
[^zwaveling_established_2002]: Zwaveling S, Ferreira Mota SC, Nouta J, Johnson M, Lipford GB, Offringa R, et al. _Established Human Papillomavirus Type 16-Expressing Tumors Are Effectively Eradicated Following Vaccination with Long Peptides._ The Journal of Immunology. 2002;169(1):350--358. 
