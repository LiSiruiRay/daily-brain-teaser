---
name: "The Topologist's Sine Curve"
type: "topology"
tags: ["Connectedness", "Path-connectedness", "Closure", "Counterexample"]
date: "2026-04-21"
solved: false
comments: ""
related: []
redo: 0
---
# The Topologist's Sine Curve

---

## Problem

Define the **topologist's sine curve**:

$$S = \left\{ \left(x,\, \sin\tfrac{1}{x}\right) : x > 0 \right\} \subset \mathbb{R}^2$$

and let $\bar{S}$ be its closure in $\mathbb{R}^2$:

$$\bar{S} = S \cup \{(0, y) : y \in [-1, 1]\}$$

**Show that $\bar{S}$ is connected but not path-connected.**

---

## Why It's Interesting

This is the canonical counterexample separating two fundamental notions that beginners often conflate: **connectedness** (you cannot split the space into two disjoint open sets) and **path-connectedness** (any two points can be joined by a continuous path). $\bar{S}$ is connected — intuitively "one piece" — yet no path can cross from the vertical segment to the sine part. The obstruction is purely topological, not geometric, and reveals that the closure of a path-connected set need not be path-connected.

---

*Answer: [view](answer.md)*
