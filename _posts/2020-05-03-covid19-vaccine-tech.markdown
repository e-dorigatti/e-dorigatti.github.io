---
layout: post
title:  "Technology of vaccines for COVID-19"
date: 2020-05-03 09:00:00 +0200
---

Currently, several vaccines for COVID-19 are undergoing clinical trials. They are
based on a variety of innovative technological platforms, several of which have
never been used in any licensed vaccine. This post analyzes five of them, and
presents a layman explanation of their principles of operation.

<!-- more -->

## Introduction

The purpose of a vaccine is to train the body to quickly recognize and fight
pathogens (troublemakers). In most cases, the immune system is able to take care
of this on its own, but even so several days are necessary before the body is
able to fight off a novel pathogen. Vaccines shorten this timespan and increase
the strength of the response.

Traditional vaccines were made with killed or weakened pathogens. New emerging
platforms alleviate the need of dealing with pathogens when making a vaccine by
synthesizing only the necessary antigens (parts of the pathogen). These
synthetic antigens can be delivered to the relevant parts of the immune system
in a variety of ways. I want to stress this point: different vaccines can be
produced for the exact same antigen by using a different delivery technology.
Three of the five vaccines described below use the same antigen, but a different
method for delivery.

Most vaccines follow a similar path: after injection, they float outside cells
until they are picked up and internalized by professional antigen presenting
cells. These cells will degrade the antigen and present pieces of it on their
surface. At the same time, they migrate in the lymph nodes, the training ground
for (some of) the fighters of the immune system. Once there, naive lymphocytes
will be exposed to the antigen presenting cell. Lymphocytes that recognize
the antigen are activated and leave the lymph node, hunting for anything that
looks like that antigen.

COVID-19 is a disease caused by the novel coronavirus, or SARS-CoV-2. Emerged in
the last months of 2019, by April 2020 it caused lockdowns and curfews all
around the world. Viruses employ several mechanisms to infect cells and hijack
their facilities to produce and release copies of the virus. The novel
coronavirus presents on its surface a spike that recognizes and binds to cells
expressing a particular receptor called ACE2, normally used to control blood
pressure.

Vaccines for COVID-19 aim at activating B cells, a kind of lymphocyte that
produces antibodies when it meets its cognate antigen (the antigen it recognized
on the professional antigen presenting cell). These antibodies look like the
ACE2 receptor and trick the virus into binding to them instead of other cells in
the body. Anything tagged by an antibody will eventually be eaten, digested and
disposed of by macrophages.

There are currently five vaccine candidates in clinical trials (and there will
probably be more when you read this article). They all use fairly recent
technologies that are actively under research, some of which have never been
featured in a licensed vaccine for the masses.[^3] In this post I summarize what
I learned about these technologies, as they were new to me. A disclaimer is,
therefore, in order: in spite of my best efforts, what I say might be inaccurate
and/or incomplete, and the references might not be the most appropriate, so take
all of this with a grain of salt. I certainly cannot make any kind of educated
guess on which vaccine has the best chance to succeed.

## mRNA-1273
Developed by [Moderna](https://www.modernatx.com/) and tested in clinical trial
[NCT04283461](https://clinicaltrials.gov/ct2/show/NCT04283461), mRNA-1273 is a
novel lipid nanoparticle (LNP)-encapsulated mRNA-based vaccine that encodes for
a full-length, prefusion stabilized spike (S) protein of SARS-CoV-2.

As explained above, the Spike (S) protein is used by the coronavirus to hook the
ACE2 receptor and enter into the cell. When this happens, the S protein will
fold and pull the virus to the cell surface so that the two membranes can merge.
In order to block SARS-CoV-2, antibodies must target the S protein before it
binds to ACE2, therefore it is fundamental to train them using its prefusion
form. On its own, however, this configuration is quite unstable, which means
that S proteins delivered as part of a drug might break down before they have a
chance to educate the immune system. In this vaccine, therefore, the S protein
is slightly modified to keep in the desired prefusion configuration. A method to
do so was reported for SARS's spike protein,[^1] and I presume this could work
for the novel coronavirus without too many changes.

Unfortunately, mRNA is also unstable and would be quickly degraded before it
could be picked up by the antigen presenting cells. This is where nanoparticles
come into play: they are spherical shells that insulate the mRNA from the
dangerous environment outside cells. These sturdy structures last long enough to
be found by antigen presenting cells, but once inside they can be easily
disassembled and expose their payload. The shell is made from lipids
("oily/fatty substances") because they are non-toxic, and a solid form allows
to control how quickly the drug is released.[^2]

<figure style="display:table; margin: auto; margin-bottom: 15px">
  <img
    src="https://www.precisionnanosystems.com/images/default-source/branding/pni-branding/particle.png"
    alt="3d model of a solid lipid nanoparticle" width="80%" style="margin: auto">

  <figcaption style="display:table-caption; caption-side:right; width: 30%; vertical-align: middle">

  <p>
  A three dimensional visualization of a solid lipid nanoparticle. The drug is
  represented as double-stranded DNA helixes, in green. The orange spheres
  constituting the surface are lipids.
  </p>

  <p>
  Image credit: <a
    href="https://www.precisionnanosystems.com/areas-of-interest/formulations/lipid-nanoparticles"
    > Precision Nanosystems </a> (no affiliation).
  </p>
  </figcaption>
</figure>

Once inside cells, the mRNA antigen is copied, and some of these copies are then
presented on the surface of the cell. When this happens in professional antigen
presenting cells, lymphocytes are trained to recognize the antigen, and can
start hunting for it.


## Ad5-nCoV
From [CanSino Biologics Inc.](http://www.cansinotech.com/) and tested in
clinical trial [NCT04313127](https://clinicaltrials.gov/ct2/show/NCT04313127),
Ad5-nCov is a recombinant adenovirus type 5 vector that expresses the S protein.

Adenoviruses are fairly common, so much so that a considerable portion of people
have been unknowingly infected and recovered at some point in their lives. Their
natural infective capabilities can be exploited to deliver vaccines or other
types of drugs. Adenoviruses, especially of type 5, are well understood and
frequently used to treat a wide variety of diseases.[^4] [^5]

<figure style="display:table; margin: auto; margin-bottom: 15px;">
  <img
    src="http://dxline.info/img/new_ail/adenovirus_2.jpg"
    alt="a picture of adenovirus particles" width="80%" style="margin: auto">

  <figcaption style="display:table-caption; caption-side:right; width: 30%; vertical-align: middle">

  <p>
  An image of adenovirus particles.
  </p>

  <p>
  Image credit: <a
    href="http://dxline.info/diseases/adenovirus"
    >Drugs and Diseases Reference Index - Adenovirus</a>.
    </p>
  </figcaption>
</figure>


This is done by genetically engineering the virus to either (a) display selected
antigens on its surface or (b) produce copies of the desired drug when it
infects a cell. The description of the clinical trial makes me guess that
Ad5-nCov follows the latter option. Adenoviruses can be further modified to
remove their replication capabilities, so that upon infection only the desired
drug is produced. This is done in most modern adenovirus-based therapies.


## INO-4800
By [Inovio Pharmaceuticals](https://www.inovio.com/) and tested in clinical
trial [NCT04336410](https://clinicaltrials.gov/ct2/show/record/NCT04336410),
INO-4800 is a DNA plasmid encoding the S protein delivered by electroporation.

DNA plasmids are ring-shaped DNA molecules.[^6] [^8] They encode the antigen of
interest, in this case again SARS-CoV-2's spike protein, together with some
elements that stimulate and facilitate copying the antigen. Antigens encoded in
DNA vaccines must be copied into RNA, which is then copied again to produce a
new instance of the antigen. Antigens in RNA vaccines, being already made of
RNA, can skip the first copying step altogether. However, the DNA plasmids
reside in the cell nucleus, which means that new copies of the antigen can be
produced even a long time after the RNA is discarded.

<figure style="display:table; margin: auto; margin-bottom: 15px;">
  <img
    src="https://media.sciencephoto.com/image/g1100058/800wm/G1100058-False-col_TEM_plasmids_of_bacterial_DNA_of_E_Coli.jpg"
    alt="picture of plasmids" width="60%" style="margin: auto; transform: rotate(90deg) translateY(-25%); margin: -50px">

  <figcaption style="display:table-caption; caption-side:right; width: 30%; vertical-align: middle">

  <p>
  False color image of DNA plasmids from E. Coli.
  </p>

  <p>
  Image credit: <a
    href="https://www.sciencephoto.com/media/209601/view/false-col-tem-plasmids-of-bacterial-dna-of-e-coli"
    >Science photo library</a>.
    </p>
  </figcaption>
</figure>


Electroporation is a procedure that makes it easier for the plasmids to enter
inside cells.[^7] After delivery of the vaccine, brief electrical pulses are
applied to the area of injection. These pulses create small temporary holes in
the surface of nearby cells, thanks to which the plasmids can enter. This can
increase the effectiveness of the vaccine by orders of magnitude.

## LV-SMENP-DC
Proposed by the [Shenzhen Geno-Immune Medical
Institute](http://szgimi.org/en/index.php), it is evaluated in clinical trial
[NCT04276896](https://clinicaltrials.gov/ct2/show/NCT04276896). That page
explains it well:

> Based on detailed analysis of the viral genome and search for potential
> immunogenic targets, a synthetic minigene has been engineered based on
> conserved domains of the viral structural proteins and a polyprotein protease.
> The infection of Covid-19 is mediated through binding of the Spike protein to
> the ACEII receptor, and the viral replication depends on molecular mechanisms
> of all of these viral proteins. This trial proposes to develop and test
> innovative Covid-19 minigenes engineered based on multiple viral genes, using
> an efficient lentiviral vector system (NHP/TYF) to express viral proteins and
> immune modulatory genes to modify dendritic cells (DCs) and to activate T
> cells

Unlike the vaccines discussed above that only used the spike protein, the
antigen in this vaccine is created by joining together several pieces of the
coronavirus. These pieces come from its structural proteins, i.e. the parts that
make up its external shell. The "SMENP" in the vaccine name is an acronym from
the five structural proteins: spike, membrane, nucleocapsid, envelope and
protease.

Conserved domains are parts of the virus that rarely change because of
mutations. Mutations are one of the main mechanisms that viruses use to avoid
recognition by the immune system. Some parts, however, cannot change, because
are essential for the functioning of the virus. By comparing the hundreds of
published coronavirus genomes, it is possible to find regions with few mutations
that are still recognizable by the immune system, and create an artificial
antigen based on them. This technology is actually [the main focus of my PhD]({%
post_url 2019-08-16-what_is_my_phd_about %}). If you want to know more, you can
read the two papers[^16] [^17] I have worked on until now.

The antigen in this vaccine is delivered through modified dendritic cells.
Dendritic cells are one of the main professional antigen presenting cells
described in the introduction of this post. The other vaccines count on them to
eventually pick up the antigen and present it to lymphocytes. This vaccine takes
an entire different route: specific kinds of cells are harvested from the
patient, stimulated to grow into dendritic cells, forcefully modified to present
the engineered antigen, then injected into the patient so that they can do their
own thing.[^11] Using lentiviruses to modify the dendritic cells is an
especially effective strategy.[^9] Lentiviruses incorporate their DNA with the
DNA of the cells they infect, so that for this vaccine these dendritic cells are
continuously producing and presenting the synthetic minigene derived from the
coronavirus. For good measure, some T cells are activated in the lab and
delivered to the patient together with the modified dendritic cells. Note,
however, that the modified dendritic cells can activate B cells once delivered
to the patient, so this vaccine can be used for prevention, too.

<figure style="display:table; margin: auto; margin-bottom: 15px;">
  <img
    src="https://www.researchgate.net/publication/23500266/figure/fig1/AS:277395241226242@1443147587861/Analysis-of-porcine-dendritic-cells-by-scanning-electron-microscopy-Immature-porcine.png"
    alt="a picture of inactivated and activated dendritic cells" width="90%" style="margin: auto">

  <figcaption style="display:table-caption; caption-side:right; width: 40%; vertical-align: middle">

  <p> An image showing immature (left) and activated (right) dendritic cells.
  Immature dendritic cells look for antigens to display, while activated
  dendritic cells are actively displaying antigens on their surface. </p>

  <p>
  Image credit: <a
    href="http://dxline.info/diseases/adenovirus"
    >Drugs and Diseases Reference Index - Adenovirus</a>.
    </p>
  </figcaption>
</figure>

## Pathogen-specific aAPC
From the same developers as the previous vaccine, and tested in clinical trial
[NCT04299724](https://clinicaltrials.gov/ct2/show/NCT04299724), this vaccine is
quite similar from the previous one. Instead of growing dendritic cells from
cells harvested from the patient, here they try to use artificial antigen
presenting cells. The hope is to avoid the need to harvest cells from the
patients that should receive the vaccine, and instead use universal, pre-made
antigen presenting cells.[^13] This would make the vaccine much easier to
produce and deliver. Some of these artificial cells are grown by modifying
suitable cells, but many alternatives that are not based on cells at all are
being explored.

## Conclusion
As you realized, a wide variety of technologies is being tested. Most of them
are fairly new and under active development. Another challenge facing vaccine
developers is comparing the results of the clinical trials to establish the best
vaccine.[^18] I am looking forward to reading the results of these clinical
trials. Without a doubt, these findings will spur considerable enthusiasm
towards successful technologies and accelerate their application to other
diseases.

If you want to stay informed about these developments, I found articles in
Nature Reviews [Immunology](https://www.nature.com/nri/) and [Drug
Discovery](https://www.nature.com/nrd/), as well as [Nature News
Feature](https://www.nature.com/nature/articles?type=news-feature) a very
interesting source of news that are particularly accessible and clearly
explained. In particular, _The race for coronavirus vaccines: a graphical
guide_[^15] is a good complement to this blog post, with beautiful images
explaining the same biological processes involved.

## Bibliography
[^1]: Kirchdoerfer, R. N. et al. Stabilized coronavirus spikes are resistant to conformational changes induced by receptor recognition or proteolysis. Scientific Reports 8, (2018).
[^2]: Mehnert, W. & Mäder, K. Solid lipid nanoparticles. Advanced Drug Delivery Reviews 64, 83–101 (2012).
[^3]: [Le, T. T. et al. The COVID-19 vaccine development landscape. Nature Reviews Drug Discovery (2020) doi:10.1038/d41573-020-00073-5.](https://www.nature.com/articles/d41573-020-00073-5)
[^4]: Wold, W. S. M. & Toth, K. Adenovirus Vectors for Gene Therapy, Vaccination and Cancer Gene Therapy. Curr Gene Ther 13, 421–433 (2013).
[^5]: Zhang, C. & Zhou, D. Adenoviral vector-based strategies against infectious disease and cancer. Human Vaccines & Immunotherapeutics 12, 2064–2074 (2016).
[^6]: Kutzler, M. A. & Weiner, D. B. DNA vaccines: ready for prime time? Nature Reviews Genetics 9, 776–788 (2008).
[^7]: Khan, A. S., Broderick, K. E. & Sardesai, N. Y. Clinical Development of Intramuscular Electroporation: Providing a “Boost” for DNA Vaccines. in Electroporation Protocols (eds. Li, S., Cutrera, J., Heller, R. & Teissie, J.) vol. 1121 279–289 (Springer New York, 2014).
[^8]: Gary, E. N. & Weiner, D. B. DNA vaccines: prime time is now. Current Opinion in Immunology 65, 21–27 (2020).
[^9]: He, Y., Zhang, J., Mi, Z., Robbins, P. & Falo, L. D. Immunization with Lentiviral Vector-Transduced Dendritic Cells Induces Strong and Long-Lasting T Cell Responses and Therapeutic Immunity. The Journal of Immunology 174, 3808–3817 (2005).
[^11]: Sabado, R. L., Balan, S. & Bhardwaj, N. Dendritic cell-based immunotherapy. Cell Research 27, 74–95 (2017).
[^12]: Naldini, L., Trono, D. & Verma, I. M. Lentiviral vectors, two decades later. Science 353, 1101–1102 (2016).
[^13]: Kim, J. V., Latouche, J.-B., Rivière, I. & Sadelain, M. The ABCs of artificial antigen presentation. Nature Biotechnology 22, 403–410 (2004).
[^14]: McKay, P. F. et al. Self-amplifying RNA SARS-CoV-2 lipid nanoparticle vaccine induces equivalent preclinical antibody titers and viral neutralization to recovered COVID-19 patients. bioRxiv 2020.04.22.055608 (2020) doi:10.1101/2020.04.22.055608.
[^15]: [Callaway, E. The race for coronavirus vaccines: a graphical guide. Nature 580, 576–577 (2020).](https://www.nature.com/articles/d41586-020-01221-y)
[^16]: [Graph-Theoretical Formulation of the Generalized Epitope-based Vaccine Design Problem]({% post_url 2019-11-18-the_first_project_of_my_phd %})
[^17]: [Joint epitope selection and spacer design for string-of-beads vaccines]({% post_url 2020-04-27-jessev %})
[^18]: [Callaway, E. Scores of coronavirus vaccines are in competition — how will scientists choose the best? Nature (2020)](https://www.nature.com/articles/d41586-020-01247-2)
