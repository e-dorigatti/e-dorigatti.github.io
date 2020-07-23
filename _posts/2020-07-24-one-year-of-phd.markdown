---
title: "One year of PhD: a retrospective"
layout: post
date: 2020-07-24 12:00:00 +0200
markdown: kramdown
---
<style type="text/css">
tbody:nth-child(odd) > tr > td { background: #ffffff;  border: none; }
tbody:nth-child(even) > tr > td { background: #f8f8f8;  border: none; }
</style>

After one year, it is time to reflect on my time as a PhD student: what was
good, what bad, what was difficult, and how to improve.

<!-- more -->

## Good things

I love it! My personal values are respected and fostered by the environment and
the people around me. Autonomy, openness, freedom, competence, reasonableness.
Within limits, of course, as we still need to earn our daily bread like
everybody else. I feel like this is quite close to what I want to do for a
living, but I am afraid finding such an environment after the PhD will not be
easy.

I really enjoyed using linear programming. It is much more powerful than what it
appears, and it is based on beautiful mathematics. More importantly, it just
works. As a comparison, I feel like most of my time doing deep learning is
wasted on some boring low-level issues with the optimization process, instead of
thinking about the problem at hand. You never know if it works until it does.
Linear programming is different: when the formulation is correct, the problem is
solved, easy. See, I have no problem waiting for three days if I am sure I will
get the correct solution in the end, but I am really not keen on waiting days
only to realize a model is overfitting.

The tools I am using. We received work laptops and I could finally go back to
working in a Linux environment after years of using Windows. I also made the
jump to using i3wm after a few months of KDE. I am also learning new features
for Emacs and Org mode, such as the agenda, Magit and layouts. I am quite happy
of my current setup, I feel much more productive now. Keyboard-based user
interfaces are way faster to use as everything I need is only a few keystrokes
away, which means less interruptions and more focus.
   
## Bad things

The pressure to always do more. This is not a consequence of the environment or
the people surrounding me, in particular my supervisors are very reasonable
people with very reasonable expectations. The fundamental issue is that the work
to be done is only limited by your personal capacity. Whatever you are doing,
there is always another project to get involved in, another book or paper to
read, another lecture to attend, another idea to try. Not knowing what will
(not) work and what will (not) be useful makes it seem like you have to pursue
everything. I am interested in a lot of things but I do not have the capacity to
pursue all of them. Pressure comes from lack of focus, and prioritization also
means saying no to things that are not worth your time. One could argue,
however, that at this early stage of my career breadth should be more important
than depth, as I need to try many things to form an intuition on what is worth
of being pursued.

Soft skills. Covid19 definitely did not help in this regard. I feel like I
sometimes have difficulty in making others understand me. I think this is
because I cut corners, trying to keep the explanation short and to the point,
and inevitably assume that the other person has some background information
while, in fact, they don't. One reason why I do this is that I really dislike
when people take too long to describe something, going into unnecessary details
or digressing too much. I don't think this happens when I am in the right
mindset, for example when I explain something to people whom I am reasonably
sure don't know the topic, so fixing this should not be too difficult.

Reading habit. I am still not reading consistently. I had something going for
some time, but I lost momentum when things got busier. I follow around 20 RSS
feeds, mostly from Nature, bioRxiv and Frontiers, which I used to check daily. I
don't have exact numbers, but that amounted to 60-80 papers per day, of which
about 5-10 had a title interesting enough to read the abstract, and 1-2 were
interesting enough to read partially or completely. Even though the whole
process took perhaps half an hour, it was exhausting. I think I should refine
the filters I use for bioRxiv, or skip it completely in favor of lesser journals
such as PLOS and OUP.

## Difficult things

Deep learning. I don't really like deep learning. There, I said it. As I
mentioned above, I find it so time consuming. It is too empirical. It is
difficult to know in advance what will work and what will not. And testing
things properly (tuning hyper-parameter with nested or repeated
cross-validation, ablation studies, and so on) requires way too many resources.
I would not mind fiddling and trying things out to build intuition if the
feedback loop was quick enough, but that does not work when every experiment
takes days. It also does not help that I feel like an [expert beginner][eb] in
this topic, stuck between understanding of the details and lack of the big
picture, without a clear way forward.

Generating ideas. Some people around me are idea factories, they always have
something new to try out. They see something new and quickly come up with
extensions or use cases. I am not like that. One reason is definitely that
bioinformatics and biology are huge fields that are still new to me. But even
outside of those fields I do not get a lot of ideas, I am not naturally a
creative person. Usually I am not looking for ways to put my knowledge in
practice, I like learning and researching purely for the joy of it and not for
practical needs. This is probably why I am blind to all the marvelous things
that are possible and so easily seen by others.

## Action points

Be more assertive in deciding what is worth pursuing. It's not about learning
how to say no, it's all about _what_ to say no to. I wanted to spend more time
studying. I did, and I got overwhelmed by the amount of material. I have to
learn to decide what I should be studying _right_ now, what can wait a few
months, and what is best left as a long term goal. For this, I first need
clarity in what I want and my goals are, then I should evaluate how much closer
to them something would bring me.

Be more involved with people. I want to keep working on my soft skills in
general, so I should spend more time around people. I started supervising a few
Master's theses. I will be teaching assistant again next semester. I became one
of the students' representatives of my graduate school. I took part in
interviewing candidates for a few PhD spots at my lab. All this is good, I think
my efforts are paying off and I should keep doing this.

## Lessons learned

After three large projects and several smaller ones, I am starting to see some
patterns emerge in the way I do and organize my work.

Create scripts and pipelines to run all experiments and leave a record of what
was done. Reproducibility is fundamental in research, and as a computational
scientist I have it much easier than my colleagues in the wet lab, but it still
requires a minimum of organization. As soon as I decide on an experiment to
perform, I put it into a script, and always run the experiment through that
script. And I never delete these scripts, even if I think I do not need the
experiment anymore. Complicated workflows made of several steps can be handled
easily with make or similar alternatives.

Save all inputs, intermediate outputs, and results. Even those that are not
needed anymore, keep as much as possible. Including log files. Each experiment
gets a script, as described above, and a folder with the results. Storing
intermediate outputs, when it makes sense, is a great way to run slight
variations of the same experiment and investigate what broke when things go
wrong.

Separate obtaining results from their analysis. Usually, in my work, the results
come out of an algorithm that takes quite a bit of time to run, for example a
machine learning model. It is much better to save its parameters and the
predictions on the test set, and leave the analysis to a separate script or
Jupyter notebook. You never know exactly in advance what kind of analyses you
will perform on those results, so having them handily available will save a ton
of time later on.

Embrace dependency injection. It will make your code a tad more complicated at
first, but much easier to extend and build upon. I find myself frequently adding
and testing new things and if things are built so that they can composed
together, replacing old parts or adding new ones will require little effort.
Start simple, but if a part is used or modified often it means it's worth being
abstracted away.


## How Covid19 changed my workflow

Honestly? Not much. The best thing about it is that I am not commuting anymore,
which is a great saving of time and energy. Grocery shopping and looking after
the apartment is also easier and less tiring. I do miss the day-to-day
interactions with others, having lunch or coffee together, talking about
research and what we have been up to. Networking is quite an important part that
is missing from remote work. However I was mostly working alone before the
pandemic already, so the only thing that changed is where I work. And, as an
introvert, I had no problems staying at home for months.

I do not mind having virtual meetings. Video conferencing makes it quite
convenient to meet with people that are physically located in different places,
which considerably simplifies my schedule. It is much easier to attend to video
lectures and presentations, and the number of events that is possible to attend
has increased a lot. The other side of the medal is that with such a great
availability of events it is easy to fall in the trap of binge watching and
procrastinating with the excuse that "I am learning". And while more convenient
for the viewers, presenting in a video conference is just awful. It is
much harder to read the room and connect with the public.

All in all, although working from home is great, social contact is severely
lacking, and that is why I think the best compromise is to work remotely only
two or three days a week.

## Working time analysis

This is how I have spent my time from the middle of January to the middle of
July (roughly 140 working days):

| Task           | Time (h:mm) |       % |
|----------------|-------------|---------|
| Research       |      417:40 |    41.6 |
| Learning       |      225:38 |    22.5 |
| Teaching       |       81:20 |     8.1 |
| Meetings       |       76:07 |     7.6 |
| Conferences    |       56:24 |     5.6 |
| Events         |       53:33 |     5.3 |
| Supervising    |       49:33 |     4.9 |
| Administration |       42:41 |     4.3 |
| *Total*        |   *1002:56* | *100.0* |

This averages to slightly more than seven working hours per day, which is a few
hours more than what I found in the previous retrospective. I believe one of the
reasons for this is the absence of commuting due to Covid19, previously almost
two hours per day. The 40% figure dedicated to research is very close to what I
found in the previous retrospective, while time for learning jumped from four to
23%. This is a great improvement as I explicitly mentioned I would like to spend
more time studying.

I am quite satisfied with having a solid 60% of time just for myself, whether
for studying or researching. It may not sound like a lot, but it's enough to get
things done. I do not think I can cut much from other activities, if you
consider that 5% of working time is only two hours per week.

## Meta-retrospective

It is actually useful to review [the retrospective]({% post_url
2020-01-14-retrospective %}) I wrote six months ago to see what changed
and what did not.

One of my action points was to spend more time reading. I used 23% of the time
to study, which includes reading and watching seminars and lectures. I also
noted that I probably got overwhelmed trying to keep up with my sources, so I
will shift my attention towards authoritative sources and only casually check
preprints.

I also wanted to find more people to collaborate with. I am now working on two
projects with others, one of which I am "leading". I am not satisfied at all
with my leadership there, I am communicating too little with the others, and
progress on their part is slow because I am not holding them accountable, I
think. This is still some progress, compared to six months ago.

I noted that coming up with experiments was not so easy, and I remember the
difficulty. This problem however did not occur for my second paper, even though
the topic was very similar. Also, the second paper was my idea, while the first
one was about implementing an idea my supervisor had. This means that the
difficulties I encountered the first time were due to the fact that (1) I was
still not very knowledgeable of the subject and (2) I could not see merits and
demerits of an idea that was not mine. Obviously these two reasons are not
orthogonal, which means that the difficulty in appreciating the advantages of my
supervisor's idea were due to my ignorance in the field. The conclusion is that
once you are into a subject it is easier to understand how a method compares to
others, and what is expected in a comparison.

Procrastination is still not a solved issue. It is easy to postpone things you
don't like, especially when you can find other things that are more enjoyable
(but perhaps of dubious value). I feel like procrastination tends to happen when
I have either too much or too little to do. Having little to do makes it hard to
avoid that task you dread, while having too much on your plate simply makes you
feel exhausted by only thinking about what to do next. And the uncertainty on
how to do things or the best approach to take makes everything worse;
procrastination tends to happen at the beginning of a project.

Finally, I am still using Emacs for my research diary. I learned how to properly
use the agenda so that even my calendar is in there. Having everything in one
place is extremely convenient: every morning I can easily see meetings and
deadlines in the next few weeks as well as unscheduled high priority tasks.
Within a few minutes I can come up with a plan for the day without switching
back and forth between three different web tools. I would be lost if something
happened to my notes there.


 [eb]: https://daedtech.com/how-developers-stop-learning-rise-of-the-expert-beginner/
