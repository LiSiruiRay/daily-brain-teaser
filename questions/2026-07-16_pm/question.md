---
name: "Schwarz Reflection Principle via Morera"
type: "Complex Analysis"
tags: ["Schwarz reflection", "Morera's theorem", "analytic continuation", "Cauchy-Riemann", "symmetry"]
date: "2026-07-16"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Complex Analysis, Stein & Shakarchi, Chapter 2; classical folklore"
---
# The Reflection Principle for Holomorphic Functions

Let $f$ be a continuous function on the closed upper half-disk $\overline{D^+} = \{z : |z| \leq 1,\ \text{Im}(z) \geq 0\}$, holomorphic on the open upper half-disk $D^+ = \{z : |z| < 1,\ \text{Im}(z) > 0\}$, and **real-valued on the real segment** $(-1, 1)$ (i.e., $f(x) \in \mathbb{R}$ for $x \in (-1,1)$).

Define the extension:
$$F(z) = \begin{cases} f(z) & \text{Im}(z) \geq 0,\ |z| \leq 1 \\ \overline{f(\bar{z})} & \text{Im}(z) < 0,\ |z| < 1 \end{cases}$$

**Show that $F$ is holomorphic on the full open disk $D = \{|z| < 1\}$.**

What is the key principle at work, and why does the real-valued condition on the real segment make everything click?
