---
name: "No Function with f(f(n)) = n + 2025"
type: "Putnam"
tags: ["Functions", "Involution", "Modular arithmetic", "Fixed points", "Parity"]
date: "2026-03-27"
solved: false
comments: ""
related: []
redo: 0
---
# No Function with $f(f(n)) = n + 2025$

## Problem

Prove that there is **no** function $f: \mathbb{Z} \to \mathbb{Z}$ satisfying
$$f(f(n)) = n + 2025 \quad \text{for all } n \in \mathbb{Z}.$$

---

## Field
Putnam / Combinatorics / Number Theory

## Why It's Beautiful

The problem looks like it's about functions and iteration — but the real obstruction is purely combinatorial: a **fixed-point-free involution** on a finite set requires the set to have even size. The number 2025 is odd, and that's the entire reason no such $f$ can exist.

The proof has a satisfying three-act structure:
1. Show $f$ induces a well-defined map on $\mathbb{Z}/2025\mathbb{Z}$.
2. Show that map is a fixed-point-free involution.
3. Derive a contradiction from the odd size of $\mathbb{Z}/2025\mathbb{Z}$.

The same argument kills $f(f(n)) = n + c$ for **any odd** $c$.

## Key Idea / Trick

Derive the periodicity $f(n + 2025) = f(n) + 2025$, which lets $f$ descend to a map $\bar{f}$ on $\mathbb{Z}/2025\mathbb{Z}$. Then show $\bar{f}^2 = \mathrm{id}$ (involution) and $\bar{f}$ has no fixed points. A fixed-point-free involution pairs elements into 2-element orbits, requiring an even-sized set — but $|\mathbb{Z}/2025\mathbb{Z}| = 2025$ is odd.

## Difficulty
3 / 5

## Tags
Putnam, Functions, Involution, Modular arithmetic, Parity, Fixed points, Combinatorics
