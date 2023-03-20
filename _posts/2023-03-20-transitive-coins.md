---
layout: post
title: "Transitive coins"
date: 2023-03-20 12:00:00 +0200
categories:
 - Math
 - riddles
---

Three coins each show heads with probability 3/5 and tails otherwise.
The first coin gives 10 points for a head and 2 for a tail, the second gives 4 points for both head and tail, and the third gives 3 points for a head and 20 for a tail.
You and your opponent each choose a coin; you cannot choose the same coin.
Each of you tosses your coin and the person with the larger score wins 10$.
Would you prefer to be the first to pick a coin or the second?

<!-- more -->

By the way, this problem is number 16 in Section 2.7 in the book "One thousands exercises in probability".
Intuitively I thought that going first would always be the best option, because it would allow the first player to choose the coin that gives the best chances of winning, while going second would put them at the mercy of their opponent.
The surprising solution comes from computing the optimal strategy, so let's get to it.

First, note the wrong approach to the problem, which is to go first and choose the coin that gives the best expected score.
The expected scores would be 10x3/5+2x2/5=20/5 for the first coin, 4x3/5+4x2/5=20/5 for the second, and 3x3/5+20x2/5=49/25 for the third, thus this strategy would pick the third coin.
However, note that in this way you have a probability of 3/5 of getting three points, which is worse than any outcome with the second coin and heads of the first coin, also happening with probability 3/5.
Therefore, this does not seem like a good strategy.

Let's instead pretend to be the first player, and compute the probability of winning for all possible choices of coin.
For convenience, here's a recap of how the score for each throw:

|        | Head (p=3/5) | Tail (p=2/5) |
|:-------|:-------------|:-------------|
| Coin 1 | 10           | 2            |
| Coin 2 | 4            | 4            |
| Coin 3 | 3            | 20           |

For the first case, assume that the first player picks coin 1 and the second player picks coin 2.
All possible outcomes of this match-up are summarized in this table:

| First player | Second player |             |                   |
| Coin 1       | Coin 2        | Probability | First player wins |
|:-------------|:--------------|:------------|:------------------|
| Head - 10 pt | Head - 4 pt   | 9/25        | Yes               |
| Head - 10 pt | Tail - 4 pt   | 6/25        | Yes               |
| Tail - 2 pt  | Head - 4 pt   | 6/25        | No                |
| Tail - 2 pt  | Tail - 4 pt   | 4/25        | No                |

Where the probability of each outcome is the product of the two probabilities, 3/5 for heads and 2/5 for tails, since the coins are independent.
In this case, the first player wins with probability 9/25+6/25=15/25 (we can sum the probabilities because the two events are mutually exclusive) and the second player wins with probability 1-15/25=10/25.
This situation is clearly symmetric, in the sense that if the first player picks the second coin, and the second player picks the first coin, the victory probabilities are reversed, i.e., 10/25 for the first player and 15/25 for the second player.

The second match-up is coin 1 versus coin 3:

| First player | Second player |             |                   |
|:-------------|:--------------|:------------|:------------------|
| Coin 1       | Coin 3        | Probability | First player wins |
| Head - 10 pt | Head - 3 pt   | 9/25        | Yes               |
| Head - 10 pt | Tail - 20 pt  | 6/25        | No                |
| Tail - 2 pt  | Head - 3 pt   | 6/25        | No                |
| Tail - 2 pt  | Tail - 20 pt  | 4/25        | No                |

In this case, the first player only wins with probability 9/25 and the second with probability 16/25.

The last match-up is coin 2 versus coin 3:

| First player | Second player |             |                   |
|:-------------|:--------------|:------------|:------------------|
| Coin 2       | Coin 3        | Probability | First player wins |
| Head - 4 pt  | Head - 3 pt   | 9/25        | Yes               |
| Head - 4 pt  | Tail - 20 pt  | 6/25        | No                |
| Tail - 4 pt  | Head - 3 pt   | 6/25        | Yes               |
| Tail - 4 pt  | Tail - 20 pt  | 4/25        | No                |

With the victory probabilities of 15/25 and 10/25 for the first and second player respectively.

Let's collect the probability of victory for the first player in a table, where the columns represent the choice of the first player, and rows represent the choice of the second player:

|        | Coin 1 | Coin 2 | Coin 3 |
|:-------|:-------|:-------|:-------|
| Coin 1 | -      | 10/25  | 16/25  |
| Coin 2 | 15/25  | -      | 10/25  |
| Coin 3 | 9/25   | 15/25  | -      |

Diagonal entries are blank because the players have to choose different coins.
Let's now analyze the strategy for the first player:

 - Suppose the first player chooses the first coin. The second player could pick the second coin, and win with probability 10/25, or choose the third coin, and win with probability 16/25. Thus, the second player would choose coin 3.
 - If the first player chooses coin 2, then the second player would choose coin 1 and win with probability 15/25.
 - Lastly, if the third player chooses the third coin, the second player would choose the coin 2, and win with probability 15/25.

In other words, **the second player wins the game with probability of 15/25 or larger, therefore, the solution to the riddle is to go second.**

As a side-note, the reasoning we performed above to find the best strategy is known in game theory as Minimax[^mmx].
Essentially, as the first player, we are looking for the option that results in the other player having the *min*imum *max*imum chance of winning.
In other words, given the first player's move, the second player rationally chooses the move that *max*imizes their chances of winning; therefore, as the first player, we should choose the move that *min*imizes the second player's *max*imum victory chances.
This principle underlies many methods in artificial intelligence under the name of *adversarial training*, in which two or more components of a system compete with each other.
Notable examples are Generative Adversarial Networks (GANs, Goodfellow et al. 2014[^gan]), which are used to generate new and realistic samples imitating a set of given examples.
GANs are composed by two separate components, a *generator* that generates new samples, and a *discriminator* that predicts whether the generated sample is real or artificial.
These two networks compete with each other, the generator trying to fool the discriminator, and the discriminator trying to uncover the generator.
When properly executed, the generator learns to fool the discriminator *and* to produce realistic samples at the same time.


 [^mmx]: https://en.wikipedia.org/wiki/Minimax
 [^gan]: Goodfellow, Ian, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. "Generative adversarial networks." Communications of the ACM 63, no. 11 (2020): 139-144.
