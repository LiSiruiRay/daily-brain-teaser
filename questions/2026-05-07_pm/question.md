---
name: "Entire Function Avoiding a Disk Must Be Constant"
type: "Complex Analysis"
tags: ["Liouville's theorem", "entire functions", "open mapping theorem", "image of holomorphic maps"]
date: "2026-05-07"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Complex Analysis, Stein & Shakarchi, Chapter 2; classical folklore"
---
# The Open Mapping Theorem: A Surprising Consequence

Let $f: \mathbb{C} \to \mathbb{C}$ be a non-constant holomorphic function. Prove that $f$ maps open sets to open sets.

As a striking application: suppose $f$ is holomorphic on the open unit disk $\mathbb{D} = \{|z| < 1\}$ and continuous on the closed disk $\overline{\mathbb{D}}$, with $|f(z)| = 1$ for all $|z| = 1$ (i.e., $f$ maps the boundary to the unit circle). Must $f$ be a finite Blaschke product? 

Actually, here is the elegant question to sit with:

**Show that if $f$ is a non-constant entire function, then the image $f(\mathbb{C})$ is dense in $\mathbb{C}$.**

Then use the Open Mapping Theorem to sharpen this: **show that in fact $f(\mathbb{C})$ omits at most one point** (Picard's Little Theorem in its "elementary" form is hard, but the Open Mapping Theorem alone gives density — prove that).

Finally, here is the clean problem to solve:

> **Problem.** Suppose $f: \mathbb{C} \to \mathbb{C}$ is entire and there exists a point $w_0 \in \mathbb{C}$ and $\epsilon > 0$ such that $|f(z) - w_0| \geq \epsilon$ for all $z \in \mathbb{C}$. Prove that $f$ is constant.
