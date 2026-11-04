---
name: "Winning an Unfair Game"
type: "Probability"
tags: ["binomial distribution", "optimal stopping length", "boundary-case comparison", "counterintuitive", "Mosteller"]
date: "2026-11-04"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Frederick Mosteller, Fifty Challenging Problems in Probability with Solutions, Problem 44"
---
# Winning an Unfair Game

You play a series of independent games against an opponent. You win each game with probability $p$, where $0 < p < \tfrac12$. So every single game is unfavorable to you.

Before play begins, you may choose the total number of games $N$. There are two rules:

- $N$ must be **even**: $N \in \{2, 4, 6, \dots\}$.
- You win the match only if you win **strictly more than half** of the $N$ games. A tie counts as a loss.

**(a)** Intuition says you should keep the match as short as possible, so $N = 2$, because the law of large numbers works against you. Is that right? For example, what is the best $N$ when $p = 0.45$?

**(b)** Find the optimal $N$ as a function of $p$.

*(Bonus: if odd $N$ were also allowed, what would the best choice be, and why does the "even" rule change everything?)*
