---
name: "Weierstrass Product Convergence and Logarithmic Derivative"
type: "Complex Analysis"
tags: ["infinite products", "Weierstrass factors", "logarithmic derivative", "entire functions", "uniform convergence"]
date: "2026-08-06"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Complex Analysis (Stein–Shakarchi), Chapter 5; standard Weierstrass product theory"
---
# The Infinite Product That Counts Its Zeros

Let $f$ be an entire function with simple zeros exactly at the positive integers $1, 2, 3, \ldots$ and no other zeros, normalized so that $f(0) = 1$.

**Without using the Weierstrass factorization theorem machinery**, show directly that

$$\prod_{n=1}^{\infty} \left(1 - \frac{z}{n}\right)e^{z/n}$$

converges uniformly on compact subsets of $\mathbb{C}$ to an entire function, and then use the logarithmic derivative to identify its relationship to the digamma function:

$$\frac{f'(z)}{f(z)} = \sum_{n=1}^{\infty}\left(\frac{1}{z-n} + \frac{1}{n}\right).$$

More concretely: **verify** that for $|z| \leq R$ with none of $z = 1, 2, \ldots, \lfloor 2R \rfloor$ present, the partial products converge, by showing the series $\sum_{n=1}^\infty \log\!\left(1 - \tfrac{z}{n}\right) + \tfrac{z}{n}$ converges absolutely and uniformly on $|z| \leq R$.
