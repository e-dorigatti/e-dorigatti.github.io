---
title: "Flippin' Cards"
layout: post
date: 2019-12-01 12:00:00 +0200
markdown: kramdown
categories: Riddles
---

Here's a riddle for you:

> A friend brings you in a dark room and hands you a shuffled deck of 40 cards,
> 10 of which are facing up and the other 30 are facing down. Your task, she
> tells you, is to come out of the room holding two decks that have the same
> number of cards facing up. As it is dark in the room, you cannot see anything,
> and the cards cannot be distinguished by touch. How can you do it?

<!-- more -->

No tricks are necessary, it can be done with logic alone. You might want to take
some time to think it through, before reading my solution.

Here are some things that you might have noticed:
 1. As the deck is already shuffled, there is no point in re-arranging the cards
    somehow.
 2. Flipping a card twice brings it back to how it was at the beginning, hence
    the problem actually consists in choosing which cards to flip.
 3. Since the cards cannot be told apart, the essence of the problem is to
    choose how many cards to flip.

Now this looks like a much simpler problem. The main idea is to split the deck
in two smaller decks, and flip the cards in one of them. The question is, how
many cards should be flipped?

Let's introduce some notation. Say we take the first $k$ cards and flip them,
and leave the remaining $40-k$ untouched (in light of point 1 above, it does not
matter which cards are flipped). Now, assign a binary variable to each card, so
that $x_i=1$ if and only if the $i$-th card is facing up. This allows us to
express the operation of "flipping the $i$-th card" as $1-x_i$.

Call $m$ and $n$ the number of cards facing up in each deck:

$$
\begin{equation}
\tag{1}
\sum_{i=1}^k x_i=m
\end{equation}
$$

$$
\begin{equation}
\tag{2}
\sum_{i=k+1}^{40} x_i=n
\end{equation}
$$

From the statement of the problem, we know that there are 10 cards facing up in
total, so that $m+n=10$. Now we flip the cards in the first deck, so that the
number of cards facing up in this deck becomes:

$$
\begin{equation}
\tag{3}
\sum_{i=1}^k (1-x_i)=k-\sum_{i=1}^k x_i=k-m
\end{equation}
$$

We want the decks to have the same number of cards facing up, which means:

$$
\begin{equation}
\tag{4}
k-m=n
\end{equation}
$$

or, by rearranging:

$$
\begin{equation}
\tag{5}
m+n=k
\end{equation}
$$

But we know that $m+n=10$, so $k$ must be 10, too! Note how it also works if you
flip the larger deck instead: Equation 3 would result in $40-k-n$ cards flipped,
and $40-k-n=m$ tells us that $k$ would need to be $30$ (i.e., the number of
cards in the larger deck would have to be 30, exactly as we found earlier).

Hence the solution is:

> Create a deck by taking any 10 cards, and a deck with the remaining 30. Flip
> either deck.
