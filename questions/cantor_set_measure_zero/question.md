---
name: "The Cantor Set: Measure Zero yet Uncountable"
type: "analysis"
tags: ["Cantor set", "Measure theory", "Cardinality", "Uncountability"]
date: "2026-04-20"
solved: false
comments: ""
related: []
redo: 0
---
# The Cantor Set: Measure Zero yet Uncountable

---

## Problem

Construct the **Cantor set** $C$ by starting with $[0,1]$ and repeatedly removing the open middle third:

$$C_0 = [0,1], \quad C_1 = \left[0,\tfrac{1}{3}\right] \cup \left[\tfrac{2}{3},1\right], \quad C_2 = \left[0,\tfrac{1}{9}\right] \cup \left[\tfrac{2}{9},\tfrac{1}{3}\right] \cup \cdots, \quad \ldots$$

$$C = \bigcap_{n=0}^{\infty} C_n$$

Prove **both** of the following:

1. $C$ has **Lebesgue measure zero**.
2. $C$ is **uncountable**.

---

## Why It's Interesting

These two facts together are shocking: $C$ is "negligibly small" from the measure-theoretic viewpoint (you can cover it with intervals of total length $\varepsilon$ for any $\varepsilon > 0$), yet it is "as large as $[0,1]$" from the cardinality viewpoint. It demolished the naive intuition that "measure zero $\Rightarrow$ countable." It is also closed, nowhere dense, perfect, and totally disconnected — a remarkable object.

---

*Answer: [view](answer.md)*
