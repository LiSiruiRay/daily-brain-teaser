---
name: "Devil's Staircase: FTC Fails Without Absolute Continuity"
type: "analysis"
tags: ["Cantor function", "absolute continuity", "FTC", "Lebesgue integration", "measure zero"]
date: "2026-06-22"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Rudin, Real and Complex Analysis, Chapter 7; Stein & Shakarchi, Real Analysis, Chapter 3"
---
# The Cantor Function Is Continuous but Its Derivative Vanishes a.e. Yet It Climbs from 0 to 1

Let $f : [0,1] \to [0,1]$ be the **Cantor function** (also called the Devil's Staircase): the unique non-decreasing, continuous function that is constant on each interval of $[0,1] \setminus C$ (where $C$ is the Cantor set) and satisfies $f(0)=0$, $f(1)=1$.

**(a)** Show that $f'(x) = 0$ for **almost every** $x \in [0,1]$.

**(b)** Yet $f$ is not constant. Explain why this does **not** contradict the fundamental theorem of calculus, and conclude:

$$\int_0^1 f'(x)\, dx = 0 \neq 1 = f(1) - f(0).$$

Why does the usual FTC formula $f(1) - f(0) = \int_0^1 f'(x)\, dx$ **fail** here?
