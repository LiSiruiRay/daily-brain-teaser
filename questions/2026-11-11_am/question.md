---
name: "Rolling for a Six, Seeing Only Evens"
type: "Probability"
tags: ["conditional expectation", "geometric distribution", "selection bias", "paradox", "independence"]
date: "2026-11-11"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore (popularized by Elchanan Mossel)"
---
# Rolling for a Six, Seeing Only Evens

You roll a fair six-sided die repeatedly until the first $6$ appears. Let $N$ be the number of rolls, including the final $6$.

You are told that **every roll in the sequence was even**. In other words, no $1$, $3$, or $5$ appeared before the first $6$.

Compute
$$
\mathbb{E}\big[\,N \;\big|\; \text{all rolls were even}\,\big].
$$

Most people answer $3$. Their reasoning is that "given only evens, the die is effectively a fair 3-sided die $\{2,4,6\}$, so we wait a geometric time with success probability $1/3$."

Is that right? If not, what is the correct answer, and where does the reasoning fail?
