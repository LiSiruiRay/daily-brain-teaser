---
name: "Evening Sales: Poisson Parity via e^m + e^{-m}"
type: "Probability"
tags: ["Poisson distribution", "generating functions", "parity", "Taylor series", "elegant trick"]
date: "2026-07-22"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Fifty Challenging Problems in Probability with Solutions, Frederick Mosteller, Problem 30 (Evening the Sales)"
---
# The Evening Sales Twist: A Poisson Parity Puzzle

A bakery sells cakes according to a Poisson distribution with mean $m$. You are told that the probability of selling an **even** number of cakes (including zero) equals exactly $\frac{1}{2}$.

**Question:** What can you conclude about $m$?

Now, more interestingly: without any assumption on $m$, show that the probability of selling an even number of cakes is

$$P(\text{even}) = \frac{1 + e^{-2m}}{2}$$

and explain why this is always **strictly greater than** $\frac{1}{2}$ for any finite $m > 0$.
