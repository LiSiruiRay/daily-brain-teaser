---
name: "The Möbius Transformation That Sends the Real Line to Itself"
type: "Complex Analysis"
tags: ["Möbius transformations", "real line", "three-point determination", "PGL2(R)", "cross-ratio"]
date: "2026-08-13"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Complex Analysis, Stein–Shakarchi, Chapter 8; classical folklore"
---
# The Möbius Transformation That Sends the Real Line to Itself

A Möbius transformation is a map of the form

$$f(z) = \frac{az + b}{cz + d}, \quad a, b, c, d \in \mathbb{C}, \quad ad - bc \neq 0.$$

**Problem:** Prove that a Möbius transformation $f$ maps the real line $\mathbb{R} \cup \{\infty\}$ to itself (as a set) if and only if $a, b, c, d$ can be chosen to be **real** (up to an overall complex scalar multiple).

In other words: $f(\mathbb{R} \cup \{\infty\}) = \mathbb{R} \cup \{\infty\}$ if and only if there exists $\lambda \in \mathbb{C}^\times$ such that $\lambda a, \lambda b, \lambda c, \lambda d \in \mathbb{R}$.
