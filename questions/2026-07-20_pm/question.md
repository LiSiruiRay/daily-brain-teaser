---
name: "Dini's Theorem via Compactness"
type: "analysis"
tags: ["uniform convergence", "compactness", "Dini's theorem", "real analysis", "monotone sequences"]
date: "2026-07-20"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Weierstrass M-Test Isn't Needed: Uniform Convergence from Pointwise + Monotone

Let $f_n : [0,1] \to \mathbb{R}$ be a sequence of **continuous** functions converging **pointwise** to a function $f : [0,1] \to \mathbb{R}$, which is also **continuous**.

Suppose additionally that the convergence is **monotone**: for each $x \in [0,1]$,

$$f_1(x) \geq f_2(x) \geq f_3(x) \geq \cdots \geq f(x).$$

Prove that $f_n \to f$ **uniformly** on $[0,1]$.

> This is Dini's theorem — but prove it cleanly using a **compactness argument**, and appreciate why *each* hypothesis (continuity of limit, monotonicity, compactness of domain) is genuinely necessary.
