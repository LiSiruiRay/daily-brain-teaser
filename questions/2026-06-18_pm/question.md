---
name: "Schwarz–Pick Lemma: Holomorphic Maps Contract the Disk"
type: "Complex Analysis"
tags: ["Schwarz Lemma", "Möbius transformations", "hyperbolic geometry", "holomorphic maps", "unit disk"]
date: "2026-06-18"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Stein & Shakarchi, Complex Analysis, Chapter 8; classical folklore"
---
# The Schwarz–Pick Lemma: Holomorphic Maps Contract the Disk

Let $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ be the open unit disk. Suppose $f : \mathbb{D} \to \mathbb{D}$ is holomorphic (not necessarily a bijection).

**Prove** that for any two points $z, w \in \mathbb{D}$,

$$\left| \frac{f(z) - f(w)}{1 - \overline{f(w)}\, f(z)} \right| \leq \left| \frac{z - w}{1 - \bar{w}\, z} \right|.$$

In other words, $f$ does **not** increase the **pseudo-hyperbolic distance** on $\mathbb{D}$.

*Bonus insight:* When does equality hold?
