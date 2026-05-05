---
name: "An Impossible Integer Polynomial"
type: "Putnam"
tags: ["Polynomials", "Integer coefficients", "Divisibility", "Modular arithmetic"]
date: "2026-04-24"
solved: false
comments: ""
related: []
redo: 0
---
# Problem: An Impossible Integer Polynomial

## Problem Statement

Prove that there is **no polynomial** $P(x)$ with integer coefficients satisfying both

$$P(7) = 11 \quad \text{and} \quad P(11) = 13.$$

---

## Metadata

| Field | Details |
|---|---|
| **Field** | Putnam / Algebra / Number Theory |
| **Tags** | Polynomials, Integer coefficients, Divisibility, Modular arithmetic |
| **Difficulty** | 2 / 5 |
| **Date** | 2026-04-24 |

## Why It's Interesting

This problem looks like it should be impossible to rule out — there are infinitely many polynomials, and the two conditions seem easy to satisfy independently. The proof hinges on a single elegant lemma about integer polynomials that is surprising the first time you see it, and immediately becomes a tool you want to use everywhere.

## Key Idea / Hint

For any polynomial $P(x)$ with integer coefficients and any two integers $a, b$:

$$( a - b ) \mid (P(a) - P(b)).$$

Can you prove this lemma? And then what does it say about our specific values?

## Answer

See [answer.md](answer.md)
