---
name: "Consecutive Subsum Divisible by n"
type: "Putnam"
tags: ["Pigeonhole", "Partial sums", "Divisibility", "Modular arithmetic"]
date: "2026-04-03"
solved: false
comments: ""
related: []
redo: 0
---
# Consecutive Subsum Divisible by $n$

## Problem

Let $a_1, a_2, \ldots, a_n$ be any $n$ integers. Prove that there exist indices $1 \leq i \leq j \leq n$ such that

$$n \mid a_i + a_{i+1} + \cdots + a_j$$

---

## Field
Putnam / Combinatorics / Number Theory

## Why It's Beautiful

No matter what $n$ integers you choose — positive, negative, huge, tiny — you are **guaranteed** a consecutive block that sums to a multiple of $n$. The result feels surprising because there are no restrictions on the integers at all.

The proof is a one-paragraph application of the **Pigeonhole Principle** on partial sums, which reduces a statement about consecutive blocks into a statement about remainders. It is a model of elegant combinatorial reasoning.

## Key Idea / Trick

Consider the $n+1$ partial sums $S_0 = 0,\, S_1 = a_1,\, S_2 = a_1+a_2,\, \ldots,\, S_n = a_1+\cdots+a_n$.

There are $n+1$ sums but only $n$ possible remainders mod $n$, so by **Pigeonhole**, two partial sums must be congruent mod $n$: say $S_i \equiv S_j \pmod{n}$ with $i < j$.

Then $a_{i+1} + \cdots + a_j = S_j - S_i \equiv 0 \pmod{n}$.

## Difficulty
2 / 5

## Tags
Putnam, Pigeonhole principle, Partial sums, Divisibility, Modular arithmetic, Combinatorics
