---
name: "The Ballot Box Surprise: Early Leader Locks In"
type: "Probability"
tags: ["ballot problem", "cycle lemma", "reflection principle", "symmetry", "combinatorics"]
date: "2026-10-14"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Mathematical folklore / Cycle Lemma (Dvoretzky & Motzkin)"
---
# The Ballot Box Surprise: Early Leader Locks In

A fair coin is flipped $2n$ times, giving exactly $n$ heads and $n$ tails. Given that the sequence is **not** tied at any point after the start (i.e., the running count of heads minus tails never returns to $0$ after the very first flip), what is the probability that heads is **always strictly ahead** throughout?

More precisely: among all sequences of $n$ heads and $n$ tails where the partial sums $H_k - T_k \neq 0$ for all $k = 1, 2, \ldots, 2n$, what fraction have $H_k - T_k > 0$ for all $k$?
