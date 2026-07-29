---
name: "The Coin That Remembers Its Past"
type: "Probability"
tags: ["parity", "random walk", "coin flipping", "telescoping", "elegant reduction"]
date: "2026-07-29"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore / probability puzzle"
---
# The Coin That Remembers Its Past

You flip a fair coin repeatedly. At each step, you record whether the flip matches the **previous** flip (call it a "match") or differs (a "change").

**Question:** Starting fresh (no previous flip), after $n$ flips, what is the probability that you have seen an **even number of changes**? (Count 0 as even.)

For concreteness: if the sequence is H H T H, the changes occur at positions 3 and 4, giving 2 changes — even. 

Surprisingly, the answer is not $\frac{1}{2}$. Find the exact probability.
