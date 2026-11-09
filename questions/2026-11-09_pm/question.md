---
name: "Shrinking Without Contracting: Edelstein's Fixed Point Theorem"
type: "analysis"
tags: ["fixed point", "compactness", "metric spaces", "counterexample", "contraction mapping"]
date: "2026-11-09"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# Shrinking Without Contracting: Edelstein's Fixed Point Theorem

Call a map $f : X \to X$ on a metric space $(X,d)$ **strictly shrinking** if
$$
d\big(f(x), f(y)\big) < d(x,y) \qquad \text{for all } x \neq y .
$$
This is weaker than being a **contraction** in Banach's sense, which requires $d(f(x),f(y)) \le c\, d(x,y)$ for one fixed constant $c<1$.

**(a)** Let $X$ be **compact** and $f$ strictly shrinking. Prove that $f$ has exactly one fixed point.

**(b)** Show that "compact" cannot be weakened to "complete". Find a strictly shrinking map $f:\mathbb{R}\to\mathbb{R}$ with **no** fixed point.

**(c) (Bonus)** In the setting of (a), let $p$ be the fixed point. Prove that for every starting point $x$, the iterates $f^n(x)$ converge to $p$.

*Note:* Banach's contraction principle does not apply in (a), because the shrinking ratio $d(f(x),f(y))/d(x,y)$ may approach $1$.
