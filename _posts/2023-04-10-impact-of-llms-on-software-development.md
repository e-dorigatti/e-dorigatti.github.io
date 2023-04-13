---
layout: post
title: "Thoughts on the Impact of Large Language Models on Software Development"
date: 2023-04-10 12:00:00 +0200
categories:
 - Development
 - Deep Learning
---

I believe that large language models (LLMs) such as ChatGPT, Copilot, GPT-4, etc., will become ubiquitous in software development.
This will ultimately lead to even more software being written, and of lesser quality, more bloated and with more bugs.
Additionally, good software developers will become harder to find.
Obviously, making predictions about the future is difficult, and I realize there are many points in my argument that one could argue about.

<!-- more -->

TL;DR: I will make a connection with the lemon market hypothesis,[^lm] and argue that LLMs will make it worse.

## Software developers will still be around

First, let me get this straight: **I do not think that LLMs will replace software developers.**
People who think this either have misconceptions on what developer work entails, or are (in my opinion) excessively optimistic about the rate of progress in artificial intelligence.

To clear up the misconception, coding is a relatively minor and fairly straightforward responsibility of software developers.
The main function of developers is to translate business requirements, as defined in, for example, a user story in the Scrum Agile framework, into a formal specification for the machine.
Business requirements in general are, by their nature, incomplete and ambiguous, because they rely on many unstated assumptions and a shared understanding of the world, including the domain in which the software operates, how the users interact with it, etc.
In fact, if writing exhaustive and unambiguous business requirements was easy, Agile project management would not have been invented, and everybody would still be doing waterfall.

It is conceivable that, in the medium term, LLMs will acquire the ability to translate business requirements into formal specifications that are 80% correct 80% of the time, perhaps even inserting approximately correct code at the approximately correct position in the code-base, but the remaining 20% will necessarily require some form of human intervention, be it fixing the input to the LLM or its output (i.e., its prompt, or the code it generates).
I think that most business folks will not be willing to do this on their own, because troubleshooting complex systems still requires an intimate knowledge of the system itself, much deeper than that of project managers, as well as lots of time and energy.
<!--as well as a certain detail-oriented, thorough, methodological and precise personality that I feel like business people, who are inclined to be high-level big-picture thinkers, tend to look down to (and the feeling is often mutual).-->

This is not the first time that a new tool promises to make developers obsolete, consider for example SQL and graphical programming languages: in the end, they did not replace developers simply because dealing with software is simply a complex task that requires dedicated people with a certain expertise.
LLMs will make some things easier, especially for common use-cases such as REST-based CRUD applications (ugh), but the fact remains that troubleshooting takes time away from thinking at the business, hence some people, whose main responsibility is to build and troubleshoot software, will always be needed, and those people are known as software developers.
The way they work may change, but the essence will not.

One could also think that the state of artificial intelligence will advance enough that LLMs will be able to deal with all of this complexity on their own.
That could be possible, but at this time I do not think that anybody can give any sort of meaningful and informed answer, given how fast things are moving.
I personally believe that, if this is even possible, it will not come from making LLMs even larger but will require additional breakthroughs about knowledge representation, causal reasoning, world models (yes, LLMs do seem to form internal world models, sometimes,[^ot] but to what extent and how effectively is still unknown), etc.
In any case, I think that the Pareto principle,[^pp] or the 80-20 rule, is a good heuristic to think at these situations.
According to it, 80% of the feature take 20% of the effort, and the remaining 20% of the features need 80% of the effort to be done.
I think that LLMs today haven't even reached that initial 80% of features, and although they required herculean efforts to train, I believe that fine-tuning their abilities to deal with large and complex code-bases will take quite some time.
But predictions are hard, so who knows.

## Everybody will get better at coding

I believe that **eventually LLMs will make most developers better, and that this gain will be largest for low-skilled developers and smallest for high-skilled ones.**
While there is no reliable measurement or even agreed-upon definition of developer skill, I would consider a highly-skilled developer somebody who can maintain and extend code-bases of at least a million lines of code for years on end without setting the whole thing on fire (yes, lines of code is not a very good measurement and complexity also depends on the language, but whatever, I think you get the idea).
This leads me to the following conjectures:
 1. **In general, current average developers will become moderately more productive.**
     Actually writing code is a relatively minor task of software developers, I would estimate it at 30% or so, with the remaining time spent in thinking and discussing what needs to be done, how to best do it, and verifying that it was done properly.
     In this case, assuming that LLMs will make them five times more productive (according to a recent study[^cop] this number may be closer to twice as productive), the overall productivity gain will be 32%.
     Even assuming, generously, a 50% of purely coding workload, the productivity gain would be of 67%.
     These are considerable numbers for sure, but not as groundbreaking as some would lead you to believe.
     And yes, the demos of LLMs writing code for simple apps and websites are truly impressive, but the vast majority of the time is spent modifying old node, not writing new code.
     This forecast could also be somewhat less reliable for the medium term, in case LLMs really do revolutionize development beyond fancy auto-completion; for example, some demos already show LLMs completely automating certain tasks, such that it is not even necessary to write a single line of code.
 1. **Most developers will be forced to use LLMs**, simply because missing on these productivity gains will put them into a lower league, with lower salary and worse colleagues.
 1. **The best developers will not become better developers by using LLMs**
     The previous two points were related to speed, and while most developers will be faster at typing code, good developers will see limited benefits from LLMs.
     As I argued above, the main bottleneck for developers is not typing but thinking, and good developers do not need suggestions on that.
     Referring to the millions-lines-of-code criterion I mentioned above, the main problem of implementing new features and fixing bugs in such a code-base is figuring out which of the twenty ways of doing it is the best one.
     Choosing a sub-optimal way will not have any negative impact in the short term, but consistently choosing worse alternatives leads to a slow but sure accumulation of technical debt, i.e., a decrease in code quality that eventually reflects in slower velocity when implementing new features, and an increased rate of bugs.
     High-skilled developers know how to avoid or delay this as much as possible, and I believe that LLMs will not help much in this for quite a long time, because these choices depend on trade-offs and background knowledge about the domain and possible future directions of the software.
     Again, it may be possible to describe enough of this to a LLM that it provides a sensible solution, but the mere act of describing the issue accurately and comprehensively is already a skill that only very good developers have.
 1. **LLMs will create a lot of new, mostly low-skilled developers.**
     LLMs will make learning to code possible for many people who would not otherwise be successful at it, for example because they would have given up in frustration, or giving them that little extra push they need before some concept "clicks" in their head.
     Most of these new coders will, however, not acquire a high-skilled status, because that still requires plenty of time, dedication, effort, discipline, and study.
     I believe that the only way to *really* learn and get good at practical skills, such as coding, is to make plenty of mistakes and learning from them.
     This takes time and dedication, with or without LLMs.
     At the same time, many more people will be able to write simple scripts and apps to scratch an itch they have, and in this regard LLMs could have a similar effect as that of Excel, i.e., empowering non-technical users to perform relatively simple tasks through programming.

## Will the average quality of software developers decrease?

Given that I just presented four reasons as for why all developers will benefit from LLMs, you would think that obviously the average skill will increase, but that is not necessarily the case.
To see why, consider that, according to the last point above, many *new* developers of lower-than-average skill would enter the software development market just because of LLMs.
If they outnumber the "traditional" developers, who could leverage LLMs to upskill themselves but did not need them to land a developer job, then the average will go down.

Admittedly, this is likely the most controversial statement in this post, and I believe it is the hardest to argue for or against.
However, just to prove that this is not a contradiction, but is *in principle* possible, consider the following simulation.
Let there be three levels of developer skill, low, medium, and high, and a certain number of developers with each of level skill.
Let us use a parameter, called skill factor, to determine how many developers are in a skill group compared to the lower group.
For example, a skill factor of 0.2 means that the number of high-skill developers is 20% that of medium-skill developers, which itself is 20% that of low-skill developers.
The introduction of LLMs will cause a certain fraction of developers to upskill and move to the next skill level.
At the same time, it will also create new developers with a lower skill factor, i.e., with a distribution that is more skewed towards the lower end, according to the earlier conjecture.
By adding these two factors together, we can compute the skill distribution of developers before and after the introduction of LLMs:

<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th colspan="3" style="text-align:center;">Developer skill</th>
    </tr>
    <tr>
      <th></th>
      <th>Skill Factor</th>
      <th>Total Count</th>
      <th>Low</th>
      <th>Medium</th>
      <th>High</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total devs before LLMs</td>
      <td><input type="text" id="before-skill-factor" value="0.3" style="width: 80px;"></td>
      <td><input type="text" id="before-count" value="10000" style="width:80px;"></td>
      <td id="before-low"></td>
      <td id="before-medium"></td>
      <td id="before-high"></td>
    </tr>
    <tr>
      <td>Devs upskilled by LLMs</td>
      <td><input type="text" id="upskilled-skill-factor" value="0.1" style="width:80px;"></td>
      <td id="upskilled-count"></td>
      <td id="upskilled-low"></td>
      <td id="upskilled-medium"></td>
      <td id="upskilled-high"></td>
    </tr>
    <tr>
      <td>Devs created by LLMs</td>
      <td><input type="text" id="created-skill-factor" value="0.2" style="width:80px;"></td>
      <td><input type="text" id="created-count" value="20000" style="width:80px;"></td>
      <td id="created-low"></td>
      <td id="created-medium"></td>
      <td id="created-high"></td>
    </tr>
    <tr>
      <td>Total devs after LLMs</td>
      <td>N/A</td>
      <td id="after-count"></td>
      <td id="after-low"></td>
      <td id="after-medium"></td>
      <td id="after-high"></td>
    </tr>
  </tbody>
</table>

<script>
  // Add event listeners to the text input elements
  const inputElements = document.querySelectorAll('input[type="text"]');
  inputElements.forEach(input => {
    input.addEventListener('input', () => {
      recomputeTable();
    });
  });

  function recomputeTable() {
    // compute total devs before
    var devsBefore = parseInt(document.querySelector("#before-count").value);
    if(devsBefore <= 0) return;
    var beforeFactor = parseFloat(document.querySelector("#before-skill-factor").value);
    if(beforeFactor < 0 || beforeFactor > 1) return;
    var beforeLow = devsBefore / (1 + beforeFactor + beforeFactor**2);
    var beforeMedium = beforeLow * beforeFactor;
    var beforeHigh = beforeMedium * beforeFactor;
    document.querySelector("#before-low").innerText = "" + Math.round(100 * beforeLow / devsBefore) + " %";
    document.querySelector("#before-medium").innerText = "" + Math.round(100 * beforeMedium / devsBefore) + " %";
    document.querySelector("#before-high").innerText = "" + Math.round(100 * beforeHigh / devsBefore) + " %";

    // compute devs upskilled
    var upskillFactor = parseFloat(document.querySelector("#upskilled-skill-factor").value);
    if(upskillFactor < 0 || upskillFactor > 1) return;
    var upskilledLow = beforeLow * (1 - upskillFactor);
    var upskilledMedium = beforeLow * upskillFactor + (1 - upskillFactor) * beforeMedium;
    var upskilledHigh = beforeMedium * upskillFactor + beforeHigh;
    document.querySelector("#upskilled-count").innerText = devsBefore
    document.querySelector("#upskilled-low").innerText = "" + Math.round(100 * upskilledLow / devsBefore) + " %";
    document.querySelector("#upskilled-medium").innerText = "" + Math.round(100 * upskilledMedium / devsBefore) + " %";
    document.querySelector("#upskilled-high").innerText = "" + Math.round(100 * upskilledHigh / devsBefore) + " %";

    // compute created devs
    var devsCreated = parseInt(document.querySelector("#created-count").value);
    if(devsCreated <= 0) return;
    var createdFactor = parseFloat(document.querySelector("#created-skill-factor").value);
    if(createdFactor < 0 || createdFactor > 1) return;
    var createdLow = devsCreated / (1 + createdFactor + createdFactor**2);
    var createdMedium = createdLow * createdFactor;
    var createdHigh = createdMedium * createdFactor;
    document.querySelector("#created-low").innerText = "" + Math.round(100 * createdLow / devsCreated) + " %";
    document.querySelector("#created-medium").innerText = "" + Math.round(100 * createdMedium / devsCreated) + " %";
    document.querySelector("#created-high").innerText = "" + Math.round(100 * createdHigh / devsCreated) + " %";

    // compute total devs afer
    var afterLow = upskilledLow + createdLow;
    var afterMedium = upskilledMedium + createdMedium;
    var afterHigh = upskilledHigh + createdHigh;
    var devsAfter = afterLow + afterMedium + afterHigh;
    document.querySelector("#after-count").innerText = Math.round(devsAfter);
    document.querySelector("#after-low").innerText = "" + Math.round(100 * afterLow / devsAfter) + " %";
    document.querySelector("#after-medium").innerText = "" + Math.round(100 * afterMedium / devsAfter) + " %";
    document.querySelector("#after-high").innerText = "" + Math.round(100 * afterHigh / devsAfter) + " %";
  }

  window.addEventListener('DOMContentLoaded', recomputeTable());
</script>

Feel free to adjust the numbers and try out different scenarios.
The default settings assume that, before LLMs, each of the higher skill levels contains 30% as many developers as the lower skill, which result in about one high-skilled developer for every 17 low-skilled ones.
The settings also assume that 10% of developers will be able to upskill by using LLMs; the more you are willing to assume that LLMs will disrupt software development, the larger this number should be.
The best case being that all existing devs will upskill by using LLMs, eliminating low-skilled developers and creating about three medium-skilled ones for each high-skilled developer.
Furthermore, the default settings assume that LLMs will create twice as many developers as currently existing, but with a skill factor of 20% that is lower than that of established developers.
This factor depends on how easy it will be for "outsiders" to learn programming with LLMs, which is why it I assume it is lower than the factor for pre-LLMs developers.


## The issue of measuring developer skill

Now that we have some ideas on how LLMs will influence the skill of developers, let's try to think at what could happen to employers.
Before completing the argument, however, I would like to briefly return to the issue of developer skill.

As I mentioned, **measuring developer skill and productivity is a hard, open problem** for which no good solution exists.
Metrics such as number of commits, numbers of lines of code, number of bugs fixed, etc., are all easy to gamify, and while they do have diagnostic value they are hardly correlated with the real productivity which is essentially user value.
Even understanding the skill of a software developer during job interviews is not easy, with whiteboard and leetcode-style problems merely filtering away those who did not spend an absurd amount of time preparing for irrelevant problems like those, and take-home assignments too simple to say much about the interviewee's skills.
I am also considerably simplifying the matter by assuming that there is a single dimension to skill.

To make things worse, I think that **LLMs will make it harder to measure developer skill**, especially for hiring decisions, by facilitating the creation of content, such as superficial posts on blogs and LinkedIn and buggy demo projects on GitHub, that low-skill developers can use to fool potential employers by giving an appearance of proficiency.
Moreover, employed low-skill developers that rely too much on LLMs will generate technical debt at a faster rate, jeopardizing progress in the long term while still appearing, to the uninformed managers, to be performing at a higher skill level.
Code reviews by and pair programming together with higher-skilled developers could prevent this from happening, but it will reduce the average productivity of the organization as the higher-skilled developers would spend less time coding and more time supervising.

## And its impact on the market for software developers

A lemon market[^lm] is feedback loop that drives down the average quality of sold goods.
The market of used cars and motorbikes is a typical example of a lemon market.
It is difficult for a buyer to determine the quality of an used car, because it is determined by factors, such as the driving style of the previous owner(s), whether maintenance was performed properly and regularly, etc., that are not visible to the buyer, and easily falsified by the seller.
Therefore, the rational buyer should assume a car is of average quality, and be prepared to spend an average price for it.
Sellers of good cars would demand a price that is higher than the average, and will not be able to sell their high-quality car because buyers cannot ascertain that the car is, in fact, in better condition than most others.
Therefore, as sellers of good cars cannot get a satisfactory price, they will choose not to sell the car after all, making the average quality of cars in the market lower, and leading buyers to revise their expectations, and thus their price, downwards.
This will, in turn, leading to sellers of moderately good cars not to sell, and so on, creating a feedback loop.
The name actually comes from a market of lemons (good cars) and peaches (bad cars), but I find the analogy with cars more intuitive.
I also cannot fathom how one cannot possibly distinguish a lemon from a peach.

I would argue that **the market for software developers is (approximately) a lemon market, and LLMs will only make it worse.**
In the case of developers, the buyers are companies hiring, the sellers are the developers looking for a job, and the product sold is their software development ability.
A lemon market appears when the following conditions hold:[^lmc]
 1. Asymmetry of information, in which no buyers can accurately assess the value of a product through examination before sale is made and all sellers can more accurately assess the value of a product prior to sale; as discussed above, companies are definitely struggling to assess the skills of software developers both during hiring and when working.
    But to be fair, so is the same for other developers.
 1. An incentive exists for the seller to pass off a low-quality product as a higher-quality one; if you have ever been looking for a job you know this is true.
 1. Sellers have no credible disclosure technology (sellers with a great car have no way to disclose this credibly to buyers); if you have ever been looking for a job you know this is also true.
 1. Either a continuum of seller qualities exists or the average seller type is sufficiently low (buyers are sufficiently pessimistic about the seller's quality); the skill of software developers certainly lies on a continuum spread across several dimensions, although nobody knows in which way and how to quanify that (see above).
 1. Deficiency of effective public quality assurances (by reputation or regulation and/or of effective guarantees/warranties); I think it is not controversial to say that a degree in Computer Science does not say much about the ability of a graduate.
    Past job experience could help, but is also a noisy signal.

Determining whether the market for software developers a lemon market is certainly not straightforward, and one could easily argue that it is not, especially in regard to points (1) and (5).
That is a fair critique, however this is not a binary distinction, and realistically speaking every market has some degree of "lemon-ness" (or lemonade?).
Anyways, my point is that **LLMs will create more lemons and fewer peaches**, or, to be more precise, the lemon-to-peach ratio will increase.
This is in part due to the change in skill distribution, for example as simulated above, and in part due to the feedback loop inherent in lemon markets.
To see why, consider that, if LLMs will actually make it harder to measure developer skill, both the information asymmetry (point 1) and the credibility of disclosure mechanisms (point 3) will get worse (I was not helped by a LLM to write this post, by the way, but will you believe it if I told you?).
In the end, and especially if you think that the average skill of software developers will decrease, this translates to a more severe form of lemon market, with a stronger feedback loop driving peaches away and reducing developers' salary.

The consequences of this will be that some developers will choose to do something else, alternative career paths that pay better or similarly but require less effort.
At the same time, the increased supply of cheaper developers will enable companies to create even more software products, however, the number of bugs will increase in tandem as the average skill of developers will decrease.
It is also possible, on the contrary, that LLMs will increase the average skill enough to offset the changes in information asymmetry and disclosure mechanisms, thus resulting in the opposite effect.

It is really hard to predict the future.
Even if you do not agree with my conclusion, I hope that you enjoyed this line of thinking, and that I raised some interesting points for you to ponder about.
If this is the case, feel free to share this article and/or [get in touch](/about).
Obviously, other people who are smarter than I am also thought at these problems, and studied the impact of LLMs on the economy as a whole, so go read those as well.[^eco1][^eco2]

  [^pp]: [https://en.wikipedia.org/wiki/Pareto_principle](https://en.wikipedia.org/wiki/Pareto_principle)
  [^ot]: [https://thegradient.pub/othello/](https://thegradient.pub/othello/)
  [^cop]: [https://arxiv.org/abs/2302.06590](https://arxiv.org/abs/2302.06590)
  [^lm]: [https://en.wikipedia.org/wiki/The_Market_for_Lemons](https://en.wikipedia.org/wiki/The_Market_for_Lemons)
  [^lmc]: [https://en.wikipedia.org/wiki/The_Market_for_Lemons#Conditions_for_a_lemon_market](https://en.wikipedia.org/wiki/The_Market_for_Lemons#Conditions_for_a_lemon_market)
  [^eco1]: [https://arxiv.org/abs/2303.10130](https://arxiv.org/abs/2303.10130)
  [^eco1]: [https://arxiv.org/abs/2303.10130](https://arxiv.org/abs/2303.10130)
  [^eco2]: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4350925](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4350925)
