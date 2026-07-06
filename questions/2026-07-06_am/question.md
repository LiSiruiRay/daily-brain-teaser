---
name: "Generic Continuous Function Is Nowhere Differentiable"
type: "analysis"
tags: ["Baire category", "nowhere differentiable", "C([0,1])", "residual set", "meager sets"]
date: "2026-07-06"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Rudin, Real and Complex Analysis; also mathematical folklore / Banach 1931"
---
# The Weierstrass Nowhere-Dense Ghost: A Dense $G_\delta$ of Non-Differentiability

Let $f: [0,1] \to \mathbb{R}$ be a continuous function. Define the set

$$E = \left\{ x \in [0,1] : \limsup_{h \to 0} \frac{|f(x+h) - f(x)|}{|h|} = +\infty \right\}$$

to be the set of points where $f$ has infinite upper Dini derivative (informally, where $f$ "blows up" in difference quotients).

**Question:** Must $E$ be empty? Can $E$ be all of $[0,1]$? If so, give a clean reason why a generic continuous function satisfies $E = [0,1]$, i.e., is **nowhere differentiable**.

More precisely: show that the set

$$\mathcal{ND} = \{ f \in C([0,1]) : f \text{ is nowhere differentiable on } [0,1] \}$$

is **residual** (comeager) in $C([0,1])$ with the uniform norm. That is, $\mathcal{ND}$ contains a dense $G_\delta$.

*Hint: Think about what Baire category says about $C([0,1])$, and how to express "has a finite derivative at some point" as a countable union of closed sets.*
