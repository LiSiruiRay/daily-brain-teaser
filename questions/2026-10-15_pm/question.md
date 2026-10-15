---
name: "The Monic Polynomial That Cannot Hide Below 1"
type: "Complex Analysis"
tags: ["maximum modulus", "reversed polynomial", "mean value property", "Parseval", "Chebyshev contrast"]
date: "2026-10-15"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
---
# The Monic Polynomial That Cannot Hide Below 1

Let
$$p(z) = z^n + a_{n-1}z^{n-1} + \cdots + a_1 z + a_0, \qquad a_k \in \mathbb{C},$$
be a monic polynomial of degree $n \ge 1$.

**(a)** Prove that
$$\max_{|z|=1} |p(z)| \;\ge\; 1.$$

**(b)** Show that equality holds if and only if $p(z) = z^n$.

*Warm-up thought:* You may choose the lower coefficients $a_0,\dots,a_{n-1}$ freely to make $p$ as small as possible on the unit circle. One might expect a clever choice to push the maximum below $1$. Show that no choice works.

*Contrast (no proof required):* On the real interval $[-1,1]$, the smallest possible value of $\max_{x\in[-1,1]}|p(x)|$ over monic $p$ is $2^{1-n}$. This value is attained by a rescaled Chebyshev polynomial. Why is the unit circle so much less forgiving than the interval?
