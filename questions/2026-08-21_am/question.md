---
name: "Central Binomial Coefficient mod Prime"
type: "Putnam"
tags: ["number theory", "binomial coefficients", "modular arithmetic", "Lucas theorem", "primes"]
date: "2026-08-21"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore / Putnam preparation; Lucas' theorem standard reference"
---
# The Sequence That Sums to an Integer

Let $a_1, a_2, \ldots, a_n$ be a permutation of $1, 2, \ldots, n$. Call such a permutation **sum-friendly** if

$$\frac{a_1}{1} + \frac{a_2}{2} + \frac{a_3}{3} + \cdots + \frac{a_n}{n} \in \mathbb{Z}.$$

Prove that for $n \geq 2$, if a permutation is sum-friendly, then it must swap at least one pair of elements (i.e., there exist $i \neq j$ such that $a_i = j$ and $a_j = i$).

Wait — actually, let's state the clean version:

**Problem (Putnam 2005 B-1).** Find a formula (closed form) for

$$\sum_{k=0}^{n} \binom{n}{k} \frac{(-1)^k}{k+1}.$$
