---
title: "Drug therapy for the Coronavirus"
layout: post
date: 2020-01-30 09:00:00 +0200
markdown: kramdown
---

## Introduction
Last month, a new epidemic started in Wuhan, China, and quickly spread all over
the world. As of now, there are reports of a few companies rushing to develop,
or having already developed, a vaccine for this virus.[^1] [^2] [^3] [^4] Thanks
to recent technological progress, the development of new vaccines is fairly
quick, and clinical trials can start only a few months after the pathogen was
sequenced.

However, availability of a vaccine to the public will be delayed by the clinical
trials necessary to ensure the vaccine works as intended and is not harmful. The
expected time-span for these tests is one or two years, as animal testing must
precede human testing. The issue is that vaccines behave slightly differently in
humans and in animals (usually mice and/or monkeys). In the early stages of
research, vaccines that worked well in animals were much weaker in humans. In
addition, vaccines can cause inflammation. Slight inflammation is good, and
makes the vaccine more effective, but strong inflammation can be
counterproductive and outright harmful. Because of differences between humans
and animals, a vaccine can be toxic for us but not for them (and vice-versa, but
in this case the vaccine would never be tested in humans).

Unfortunately I could not find any scientific publications about these alleged
vaccines, likely because of all the commercial interest behind them,[^5] [^6]
but most news sources seem to agree on the fact that it will be either a mRNA or
a DNA vaccine. These kind of vaccines are designed from scratch to match the
biological signature of a pathogen, without including unnecessary, and
potentially toxic, proteins. Developing these kind of vaccines is much easier,
as it does not require interacting with live pathogens, and they can be
manufactured cheaply.

## January 31st
Several articles have been published on biorxiv on the topic,[^7] and the
article that first shared the sequences of this virus has been read more than
150 000 times since it was posted seven days
ago.[^zhouDiscoveryNovelCoronavirus2020] As I said above, these sequences are
fundamental to develop drugs. There were several works modeling the outbreak and
studying how the virus spread, estimating the number of undiscovered cases and
the infectivity of the virus.[^chenMathematicalModelSimulating2020]
[^liuTransmissionDynamics20192020]

Others are comparing this strain of Coronavirus with old strains that caused
outbreaks in the past, finding very good agreement between the sequences, or at
least the parts essential for the life cycle of the virus
[^tianPotentBinding20192020]. This is great news: it means that drugs developed
for those strains can possibly work directly on the new Coronavirus, or require
little adaptation. This in turn means that clinical testing is not necessary, as
these drugs have already been tested. For now, several existing drugs have been
identified as effective inhibitors or potential
therapeutics,[^xuNelfinavirWasPredicted2020] [^liTherapeuticDrugsTargeting2020]
[^liuPotentialInhibitors2019nCoV2020] [^tianPotentBinding20192020] which might
speed up general availability as they have already undergone clinical trials.

In the next weeks, I will try to follow these developments and keep this post
updated. I hope to learn more about how vaccines are developed, as it is [very
relevant to my PhD]({% post_url 2019-08-16-what_is_my_phd_about %}), and
watching this process unfold live is fascinating.

## How does the Coronavirus work?
Viruses are at the boundary of things considered to be "alive". A virus only
contains what is strictly necessary to infect a cell and trick it into producing
copies of the virus itself. In a sense, the only purpose of a virus is to create
more copies of itself. This process proceeds more or less as follows: first, the
virus docks to the membrane of a cell, then it enters inside as a whole and gets
rid of its envelope. This exposes the genetic material contained inside the
virus, which will be copied by the host cell and assembled into a new copy. This
new organism can now exit the cell, potentially destroying it, and infect
others. There are lots of variations to this procedure, but it gives the basic
picture.

Coronaviruses, specifically, use the so-called Spike protein, a know region in
its genome, to enter inside cells. The Spike protein is divided into two
regions, S1 and S2; S1 binds to a receptor on the surface of the cell called
Angiotensin-converting enzyme 2, or ACE2 for short. This receptor normally
"listens" for a hormone called Angiotensin, which takes part in regulating blood
pressure. After the Coronavirus is bound to ACE2, the S2 portion will take care
of fusing the envelope of the virus with the cell's membrane,[^15] which causes
the content of the virus to be released inside the cell.

The virus can be stopped by using antibodies that are shaped like the ACE2
receptor. They will bind to the Spike protein and clog it, preventing the virus
to infect cells. Antibodies also signal other parts of the immune system to
collect and dispose of this virus.

## February 4th
Research continues on the applicability of existing drugs for the novel
Coronavirus. [^8] [^11] It is now well understood that this virus works in
essentially the same way as the old SARS- and MERS- Coronaviruses that caused
outbreaks in 2003 and 2012, with several confirmatory results.
[^tianPotentBinding20192020] [^9] [^13] [^14] The virus is able to infect cells
in the lungs,[^13] explaining the symptom of pneumonia (lung inflammation), but
the digestive system could be another possible route for infection. [^14] There
are projects that test the efficacy of known
antibodies[^tianPotentBinding20192020] or develop new ones specifically tailored
to the new strain. [^10] Computer simulations have concluded that the novel
Coronavirus binds less strongly to ACE2, resulting in lower infectivity. [^12]


## References
[^1]: [https://www.precisionvaccinations.com/inovio-ino-4800-coronavirus-vaccine-candidate-matched-novel-coronavirus-outbreak-discovered-china](https://www.precisionvaccinations.com/inovio-ino-4800-coronavirus-vaccine-candidate-matched-novel-coronavirus-outbreak-discovered-china)
[^2]: [https://www.cnbc.com/2020/01/27/jj-pretty-confident-it-can-create-china-coronavirus-vaccine.html](https://www.cnbc.com/2020/01/27/jj-pretty-confident-it-can-create-china-coronavirus-vaccine.html)
[^3]: [https://www.breitbart.com/national-security/2020/01/29/hong-kong-researchers-develop-coronavirus-vaccine-need-year-testing/](https://www.breitbart.com/national-security/2020/01/29/hong-kong-researchers-develop-coronavirus-vaccine-need-year-testing/)
[^4]: [https://cepi.net/news_cepi/cepi-to-fund-three-programmes-to-develop-vaccines-against-the-novel-coronavirus-ncov-2019/](https://cepi.net/news_cepi/cepi-to-fund-three-programmes-to-develop-vaccines-against-the-novel-coronavirus-ncov-2019/)
[^5]: [https://www.marketwatch.com/story/the-latest-coronavirus-stock-screamers-inovio-pharmaceuticals-co-diagnostics-2020-01-23?mod=newsviewer_click](https://www.marketwatch.com/story/the-latest-coronavirus-stock-screamers-inovio-pharmaceuticals-co-diagnostics-2020-01-23?mod=newsviewer_click)
[^6]: [https://www.nasdaq.com/articles/will-coronavirus-propel-this-vaccine-makers-stock-even-higher-2020-01-28](https://www.nasdaq.com/articles/will-coronavirus-propel-this-vaccine-makers-stock-even-higher-2020-01-28)
[^7]: [https://www.biorxiv.org/search/2019-nCoV%20numresults%3A10%20sort%3Apublication-date%20direction%3Adescending](https://www.biorxiv.org/search/2019-nCoV%20numresults%3A10%20sort%3Apublication-date%20direction%3Adescending)
[^zhouDiscoveryNovelCoronavirus2020]: [Zhou P, Yang X-L, Wang X-G, Hu B, Zhang L, Zhang W, et al. Discovery of a novel coronavirus associated with the recent pneumonia outbreak in humans and its potential bat origin. bioRxiv. 2020 Jan 23;2020.01.22.914952.](https://www.biorxiv.org/content/10.1101/2020.01.22.914952v2)
[^liuTransmissionDynamics20192020]: [Liu T, Hu J, Kang M, Lin L, Zhong H, Xiao J, et al. Transmission dynamics of 2019 novel coronavirus (2019-nCoV). bioRxiv. 2020 Jan 26;2020.01.25.919787.](https://www.biorxiv.org/content/10.1101/2020.01.25.919787v1)
[^chenMathematicalModelSimulating2020]: [Chen T, Rui J, Wang Q, Zhao Z, Cui J-A, Yin L. A mathematical model for simulating the transmission of Wuhan novel Coronavirus. bioRxiv. 2020 Jan 19;2020.01.19.911669.](https://www.biorxiv.org/content/10.1101/2020.01.19.911669v1)
[^xuNelfinavirWasPredicted2020]: [Xu Z, Peng C, Shi Y, Zhu Z, Mu K, Wang X, et al. Nelfinavir was predicted to be a potential inhibitor of 2019-nCov main protease by an integrative approach combining homology modelling, molecular docking and binding free energy calculation. bioRxiv. 2020 Jan 28;2020.01.27.921627.](https://www.biorxiv.org/content/10.1101/2020.01.27.921627v1)
[^liTherapeuticDrugsTargeting2020]: [Li Y, Zhang J, Wang N, Li H, Shi Y, Guo G, et al. Therapeutic Drugs Targeting 2019-nCoV Main Protease by High-Throughput Screening. bioRxiv. 2020 Jan 29;2020.01.28.922922.](https://www.biorxiv.org/content/10.1101/2020.01.28.922922v1)
[^liuPotentialInhibitors2019nCoV2020]: [Liu X, Wang X-J. Potential inhibitors for 2019-nCoV coronavirus M protease from clinically approved medicines. bioRxiv. 2020 Jan 29;2020.01.29.924100.](https://www.biorxiv.org/content/10.1101/2020.01.29.924100v1)
[^tianPotentBinding20192020]: [Tian X, Li C, Huang A, Xia S, Lu S, Shi Z, et al. Potent binding of 2019 novel coronavirus spike protein by a SARS coronavirus-specific human monoclonal antibody. bioRxiv. 2020 Jan 28;2020.01.28.923011.](https://www.biorxiv.org/content/10.1101/2020.01.28.923011v1)
[^8]: [Beck BR, Shin B, Choi Y, Park S, Kang K. Predicting commercially available antiviral drugs that may act on the novel coronavirus (2019-nCoV), Wuhan, China through a drug-target interaction deep learning model. bioRxiv. 2020 Feb 2;2020.01.31.929547.](https://www.biorxiv.org/content/10.1101/2020.01.31.929547v1)
[^9]: [Hoffmann M, Kleine-Weber H, Krueger N, Mueller MA, Drosten C, Poehlmann S. The novel coronavirus 2019 (2019-nCoV) uses the SARS-coronavirus receptor ACE2 and the cellular protease TMPRSS2 for entry into target cells. bioRxiv. 2020 Jan 31;2020.01.31.929042.](https://www.biorxiv.org/content/10.1101/2020.01.31.929042v1)
[^10]: [Lei C, Fu W, Qian K, Li T, Zhang S, Ding M, et al. Potent neutralization of 2019 novel coronavirus by recombinant ACE2-Ig. bioRxiv. 2020 Feb 2;2020.02.01.929976.](https://www.biorxiv.org/content/10.1101/2020.02.01.929976v1)
[^11]: [Lin S, Shen R, Guo X. Molecular Modeling Evaluation of the Binding Abilities of Ritonavir and Lopinavir to Wuhan Pneumonia Coronavirus Proteases. bioRxiv. 2020 Feb 3;2020.01.31.929695.](https://www.biorxiv.org/content/10.1101/2020.01.31.929695v1)
[^12]: [Huang Q, Herrmann A. Fast assessment of human receptor-binding capability of 2019 novel coronavirus (2019-nCoV). bioRxiv. 2020 Feb 3;2020.02.01.930537.](https://www.biorxiv.org/content/10.1101/2020.02.01.930537v1)
[^13]: [Zhao Y, Zhao Z, Wang Y, Zhou Y, Ma Y, Zuo W. Single-cell RNA expression profiling of ACE2, the putative receptor of Wuhan 2019-nCov. bioRxiv. 2020 Jan 26;2020.01.26.919985.](https://www.biorxiv.org/content/10.1101/2020.01.26.919985v1)
[^14]: [Zhang H, Kang Z, Gong H, Xu D, Wang J, Li Z, et al. The digestive system is a potential route of 2019-nCov infection: a bioinformatics analysis based on single-cell transcriptomes. bioRxiv. 2020 Jan 31;2020.01.30.927806.](https://www.biorxiv.org/content/10.1101/2020.01.30.927806v1)
[^15]: [Gallagher TM, Buchmeier MJ. Coronavirus Spike Proteins in Viral Entry and Pathogenesis. Virology. 2001 Jan;279(2):371–4.](https://linkinghub.elsevier.com/retrieve/pii/S0042682200907578)
