---
title: "Drug therapy for the Coronavirus"
layout: post
date: 2020-01-30 09:00:00 +0200
markdown: kramdown
---

Last month, a new epidemic started in Wuhan, China, and quickly spread all over
the world. As of now, there are reports of a few companies rushing to develop,
or having already developed, a vaccine for this virus.<!-- more -->[^1] [^2] [^3] [^4]
Thanks to recent technological progress, the development of new vaccines is fairly
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
vaccines (as of Jan. 30th), likely because of all the commercial interest behind
them, [^5] [^6] but most news sources seem to agree on the fact that it will be
either a mRNA or a DNA vaccine. These kind of vaccines are designed from scratch
to match the biological signature of a pathogen, without including unnecessary,
and potentially toxic, proteins. Developing these kind of vaccines is much
easier, as it does not require interacting with live pathogens, and they can be
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
outbreaks in the past, finding good agreement between the sequences, or at least
the parts essential for the life cycle of the virus
[^tianPotentBinding20192020]. This is great news: it means that drugs developed
for those strains can possibly work directly on the new Coronavirus, or require
little adaptation. (Addendum: I misunderstood what was said in that paper. Even
though they argue that the viruses work in the same way, they point out that
antibodies designed for the old strain are not very effective on the new
strain). This in turn means that clinical testing is not necessary, as these
drugs have already been tested. For now, several existing drugs have been
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
regions, S1 (surface unit) and S2 (transmembrane unit); S1 binds to a receptor
on the surface of the cell called Angiotensin-converting enzyme 2, or ACE2 for
short. This receptor normally "listens" for a hormone called Angiotensin, which
takes part in regulating blood pressure. After the Coronavirus is bound to ACE2,
the S2 portion will take care of fusing the envelope of the virus with the
cell's membrane, which causes the content of the virus to be released inside the
cell. More in detail, this happens because a protein of the host cell, called
type II transmembrane serine protease (TTSP) "cuts" the spike protein,
separating S1 and S2. This frees S2 to fuse with the membrane of the host cell,
allowing the virus to enter and infect the cell. There is also a second
mechanism that the Coronavirus can use to enter the host cell. In case TTSP is
not present to separate S1 and S2, the cell "pulls" the virus inside through a
process called endocytosis, in which the surface of the host cell folds inward,
surrounding the virus with a sort of bag which is then pulled inside the cell.
This causes a change in the chemical substances surrounding the virus,
triggering separation of S1 and S2. S2 is now free to merge with the bag and
free the content of the virus inside the host cell. This process is identical to
what happens on the outside of the cell. [^15]

Note: I am a bit confused about this. Two papers [^15] [^20] indicate that these
two mechanisms are separate, and the virus is able to perform both according to
the presence or absence of TTSP. But another paper [^25] explains that they
actually happen one after the other. However, in their explanation they cite
several articles that seem to confirm that the two mechanisms are separate.
[^27] [^26] [^28] I do not feel competent enough to say who is right, as I might
have misunderstood the literature, but it seems to me that there are indeed two
different and separate ways for the Coronavirus to enter a cell.

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

## February 14th
The volume of publications on biorxiv on the topic seems to have diminished, and
several are now focusing on the design of vaccines for the Coronavirus. These
are most interesting to me, so I will cover them in slightly more detail.

Ahmed et al. [^17] propose several B-cell and T-cell epitopes that can be
included in a vaccine. These epitopes are derived from the structural proteins
of the virus, i.e. the parts that keep it together. Besides the spike protein
(S), the virus also uses the envelope protein (E), membrane protein (M), and the
nucleocapsid protein (N). All of them take part in building the shell of the
virus, so a vaccine designed to look like these proteins can train the body to
spot the Coronavirus. This work essentially started from epitopes that were
confirmed experimentally for the SARS virus, and searched for them inside the
novel Coronavirus, then reduced the candidate set by choosing the epitopes that
cover as many people as possible. People respond differently to these epitopes,
so an effective vaccine should contain epitopes that are recognized by most
people.

Abdelmageed et al. [^16] also looked for epitopes for a potential vaccine.
Interestingly, they focused entirely on the envelope protein, while the previous
work focused on the spike and nucleocapsid proteins. This study used
bioinformatics tools to predict potential epitopes from conserved regions.
Conserved regions are those that do not mutate; this indicates importance for
the correct functioning of the virus, because mutation is an important mechanism
used to evade the defenses of the body. This work also filters epitopes for high
population coverage. However, despite the title, they do not design a vaccine,
but only propose epitopes to include in a vaccine.

Sarkar et al. [^18] proposes three complete vaccines for the Coronavirus. The
initial stages are very similar to the two previous works, [^17] [^16] using the
same bioinformatics tools to identify epitopes. This work carries things further
by filtering epitopes based on allergenicity and toxicity, and computing the
ease by which these epitopes dock to the MHC by analyzing how well the folds of
the two sequences (epitope and MHC) match. Binding between epitopes and MHC is
fundamental for the body to learn to recognize the epitopes. Next, they assemble
these epitopes in three vaccines, that differ by which adjuvant they use.
Adjuvants are substances that further increase the sensitivity of the body to
the epitopes in the vaccine. Then they again analyze toxicity and allergenicity
of the vaccines, predict how they are going to fold, and improve their stability
to make the protein less brittle. Finally, they adapt the sequence so that it
can be easily produced.

Another paper [^22] looked for potential epitopes in the Coronavirus.
Interestingly, they found that the spike protein of 2019-nCov is quite different
from that of SARS, and suggest that antibodies tailored to SARS might not be
effective for the novel Coronavirus. This is consistent with what reported
previously, however some drugs seem to work with lower effectivity. This work
also postulates that the Chinese population might be more vulnerable to the
novel Coronavirus, and that the virus might mutate in the same regions where
SARS and MERS did. Nothing new, but it is good to have several confirmations of
the same facts.

Several papers focus on the entry mechanism of the Coronavirus. As described
earlier, entry in the host cells is mediated by the surface unit of the spike
protein docking to the ACE2 receptor, and TTSP cleaving the spike protein,
priming S2 to fuse with the cell membrane. A paper [^20] identifies where the
cells expressing ACE2 and TTSP are located in the body, and shows that a
mutation in the novel Coronavirus that is believed to increase the activity of a
specific type of TTSP, making the virus more infective compared to SARS. This
type of TTSP is also involved in SARS and influenza infections. [^24]
Interestingly, this seems to contradict a previous result [^12] that used
computer simulations to conclude that this virus is _less_ infective. This
conclusion was supported by the fact that the spike protein binds less strongly
to ACE2, but they did not consider the activity of TTSP. These two papers
actually studied the two different entry mechanisms of the Coronavirus, so they
are not directly contradicting each other. With a similar approach to [^20],
another paper [^21] shows that the ACE2 receptor is also found in certain liver
cells, explaining the symptoms observed in some patients.

A paper [^19] designs anti-Coronavirus drugs that inhibit the activity of its
protease. The viral protease helps in producing the final proteins needed to
assemble a new copy of the virus, after its genetic material has been copied by
the infected cell. The same authors also use the same tools to identify protease
inhibitors designed for SARS that are effective for the novel Coronavirus. [^23]
Finally, a study [^29] identifies another antibiotic used for Ebola, SARS and MERS
that works for the Coronavirus, preventing cellular entry.

## Conclusion
After this point, I have not seen any more new interesting findings related to
vaccines, and, to be honest, I stopped following preprints so closely. I focused
on more reputable and informative sources and I still learned a lot even though
I lost the novelty aspect of preprints. Anyway, the follow-up to this post is
[here]({% post_url 2020-05-03-covid19-vaccine-tech %}), enjoy.

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
[^16]: [Abdelmageed MI, Abdelmoneim AH, Mustafa MI, Elfadol NM, Murshed NS, Shantier SW, et al. Design of multi epitope-based peptide vaccine against E protein of human 2019-nCoV: An immunoinformatics approach. bioRxiv. 2020 Feb 11;2020.02.04.934232.](https://www.biorxiv.org/content/10.1101/2020.02.04.934232v1)
[^17]: [Ahmed SF, Quadeer AA, McKay MR. Preliminary identification of potential vaccine targets for 2019-nCoV based on SARS-CoV immunological studies. bioRxiv. 2020 Feb 4;2020.02.03.933226.](https://www.biorxiv.org/content/10.1101/2020.02.03.933226v1)
[^18]: [Sarkar B, Ullah MA, Johora FT, Taniya MA, Araf Y. The Essential Facts of Wuhan Novel Coronavirus Outbreak in China and Epitope-based Vaccine Designing against 2019-nCoV. bioRxiv. 2020 Feb 11;2020.02.05.935072.](https://www.biorxiv.org/content/10.1101/2020.02.05.935072v1)
[^19]: [Nguyen DD, Gao K, Wang R, Wei G. Machine intelligence design of 2019-nCoV drugs. bioRxiv. 2020 Feb 4;2020.01.30.927889.](https://www.biorxiv.org/content/10.1101/2020.01.30.927889v1)
[^20]: [Meng T, Cao H, Zhang H, Kang Z, Xu D, Gong H, et al. The transmembrane serine protease inhibitors are potential antiviral drugs for 2019-nCoV targeting the insertion sequence-induced viral infectivity enhancement. bioRxiv. 2020 Feb 11;2020.02.08.926006.](https://www.biorxiv.org/content/10.1101/2020.02.08.926006v1)
[^21]: [Chai X, Hu L, Zhang Y, Han W, Lu Z, Ke A, et al. Specific ACE2 Expression in Cholangiocytes May Cause Liver Damage After 2019-nCoV Infection. bioRxiv. 2020 Feb 4;2020.02.03.931766.](https://www.biorxiv.org/content/10.1101/2020.02.03.931766v1)
[^22]: [Zhu J, Kim J, Xiao X, Wang Y, Luo D, Chen R, et al. Profiling the immune vulnerability landscape of the 2019 Novel Coronavirus. bioRxiv. 2020 Feb 12;2020.02.08.939553.](https://www.biorxiv.org/content/10.1101/2020.02.08.939553v1)
[^23]: [Nguyen D, Gao K, Chen J, Wang R, Wei G. Potentially highly potent drugs for 2019-nCoV. bioRxiv. 2020 Feb 13;2020.02.05.936013.](https://www.biorxiv.org/content/10.1101/2020.02.05.936013v1)
[^24]: [Glowacka I, Bertram S, Muller MA, Allen P, Soilleux E, Pfefferle S, et al. Evidence that TMPRSS2 Activates the Severe Acute Respiratory Syndrome Coronavirus Spike Protein for Membrane Fusion and Reduces Viral Control by the Humoral Immune Response. Journal of Virology. 2011 May 1;85(9):4122–34.](http://jvi.asm.org/cgi/doi/10.1128/JVI.02232-10)
[^25]: [Zhang J, Ma X, Yu F, Liu J, Zou F, Pan T, et al. Teicoplanin potently blocks the cell entry of 2019-nCoV. bioRxiv. 2020 Feb 13;2020.02.05.935387.](https://www.biorxiv.org/content/10.1101/2020.02.05.935387v1)
[^26]: [Glowacka I, Bertram S, Muller MA, Allen P, Soilleux E, Pfefferle S, et al. Evidence that TMPRSS2 Activates the Severe Acute Respiratory Syndrome Coronavirus Spike Protein for Membrane Fusion and Reduces Viral Control by the Humoral Immune Response. Journal of Virology. 2011 May 1;85(9):4122–34.](http://jvi.asm.org/cgi/doi/10.1128/JVI.02232-10)
[^27]: [Matsuyama S, Ujike M, Morikawa S, Tashiro M, Taguchi F. Protease-mediated enhancement of severe acute respiratory syndrome coronavirus infection. Proceedings of the National Academy of Sciences. 2005 Aug 30;102(35):12543–7.](http://www.pnas.org/cgi/doi/10.1073/pnas.0503203102)
[^28]: [Simmons G, Gosalia DN, Rennekamp AJ, Reeves JD, Diamond SL, Bates P. Inhibitors of cathepsin L prevent severe acute respiratory syndrome coronavirus entry. Proceedings of the National Academy of Sciences. 2005 Aug 16;102(33):11876–81.](http://www.pnas.org/cgi/doi/10.1073/pnas.0505577102)
[^29]: [Zhang J, Ma X, Yu F, Liu J, Zou F, Pan T, et al. Teicoplanin potently blocks the cell entry of 2019-nCoV. bioRxiv. 2020 Feb 13;2020.02.05.935387.](https://www.biorxiv.org/content/10.1101/2020.02.05.935387v1)
