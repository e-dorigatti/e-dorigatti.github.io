---
date: 2021-08-13 12:00:00 +0200
title: "Bouncing balls"
layout: post
categories: Math Riddles
---

A projectile is launched from the very center of the floor of a rectangular room
that is 40 feet wide with a very high ceiling. The projectile hits the wall at a
height exactly 10 feet above the floor, reflects off this wall (obeying the
"angle of incidence equals angle of reflection" rule), hits the opposite wall,
and reflects again, finally landing back exactly where it was launched, without
hitting the ceiling. This is possible because the projectile does not travel
along straight lines, but instead travels along parabolic segments due to
gravity. When the projectile is at its highest point, how high above the floor
is it?

<!-- more -->

This is problem 3.1.22 in "The Art and Craft of Problem Solving". It
demonstrates three strategies discussed in its chapter, namely to draw pictures,
leverage symmetries and to see things from other perspectives.

Let's start with drawing a picture of the problem:

![](/images/balls/intro.svg){: .center-image}

We are asked to find the highest point of the trajectory, knowing the ball was
launched in the center of the room (thus 20 feet from the wall) and hits the
wall 10 feet from the floor. Since the ball lands in exactly the same spot, it
does not matter whether it was launched to the left or to the right. The
trajectory is symmetrical, thus we can conclude that the ball bounces on the
opposite wall at the same height, and that the highest point is in the center of
the room, exactly above where the ball was launched. We may also assume,
somewhat unrealistically, that the ball starts at the same level of the floor,
but it should not be much more difficult to solve the problem considering the
height of whatever launched the ball in the first place.

Thinking at symmetries, what if there was no wall?

![](/images/balls/symmetry.svg){: .center-image}

The ball would keep flying in a parabola and eventually fall back to the floor.
The trajectory would be symmetrical, thus reach the highest point half room (20
feet) after the wall, falling back to a height of 10 feet after a room length
(40 feet), and falling to the floor half a room afterwards (20 more feet). The
question is, again, to find the highest point of the parabola.

Notice that at the top of the parabola the ball has exactly zero vertical speed,
it is only moving horizontally. Thus, you could as well imagine somebody kicking
a ball off a cliff:


![](/images/balls/newperspective.svg){: .center-image}

Now, knowing that the ball reaches the bottom after having traveled 40 feet
horizontally, how do we find the height of the "cliff"? As it stands, this
problem cannot be solved, because horizontal and vertical velocity are not tied
by anything. However, there is another piece of information that we know: after
being kicked from point A and traveling 20 feet horizontally, the ball is at
point B, 10 feet from the floor (point B):

![](/images/balls/laststep.svg){: .center-image}

The ball will touch the floor at point C, which is twice as far from A as it is
from B. Now, consider that the distance traveled horizontally grows linearly
with time, while the vertical distance grows quadratically. This means that, if
the horizontal distance between A and B is $x$, then the vertical distance is
$cx$ for some constant $c$. By the same reasoning, the horizontal distance
between A and C is $2x$, thus the vertical distance is $c\cdot(2x)^2=4cx^2$:

![](/images/balls/quadratic.svg){: .center-image}

This means that the vertical distance between B and C (which was 10 feet) is
also equal to $3cx^2$. Therefore the height of the cliff is 10 feet plus one
third of that:

$$
4cx^2=\frac 4 3 \cdot 3cx^2 =\frac 4 3 \cdot 10\,\text{ft} \approx 13.33\,\text{ft}
$$

If you are not convinced by this you may also follow the more mechanical
approach:

$$
\begin{cases}
\frac 1 2 g t^2 = h_1 \\
\frac 1 2 g (2t)^2 = h_2 \\
h_2 - h_1 = 10
\end{cases}
$$

Where $h_1$ and $h_2$ are the height differences between B and A and C and A
respectively (thus the problem is to find $h_2$). Since B is halfway between A
and C, the time traveled from A and C is double that from A and B. Expanding the
last equation:

$$
10=h_2-h_1=\frac 1 2 g \cdot (4t^2-t^2)
\Rightarrow t=\sqrt{\frac{10\cdot 2}{3\cdot g}}
$$

Plugging into the second equation:

$$
h_2=\frac 1 2 g\cdot 4t^2=\frac{1}{\cancel{2}} \cancel{g} \cdot4\frac{10\cdot\cancel{2}}{3\cdot\cancel{g}}=\frac{4}{3}\cdot 10
$$

As before.
