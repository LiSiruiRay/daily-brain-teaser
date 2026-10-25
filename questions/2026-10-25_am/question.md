---
name: "Why the Wavelet Threshold Is σ√(2 log N)"
type: "ML/Stats"
tags: ["wavelets", "soft-thresholding", "Gaussian maxima", "union bound", "extreme values", "orthonormal transform"]
date: "2026-10-25"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning (2nd ed.), Hastie, Tibshirani, Friedman — Section 5.9, eq. (5.69); Donoho & Johnstone (1994)"
---
# Why the Wavelet Threshold Is $\sigma\sqrt{2\log N}$

In wavelet smoothing (ESL §5.9), we observe a signal on $N$ equally spaced points:
$$
\mathbf y = \mathbf f + \boldsymbol\varepsilon,\qquad \boldsymbol\varepsilon\sim N(0,\sigma^2 I_N).
$$
We apply an **orthonormal** wavelet transform $\mathbf y^* = W^\top \mathbf y$. We then **soft-threshold** each coefficient at level $\lambda$, which sets every coefficient with $|y^*_j|\le\lambda$ to zero, and transform back.

A popular default is the **universal threshold**
$$
\lambda = \sigma\sqrt{2\log N}.
$$

Explain where this number comes from. Consider the pure-noise case $\mathbf f\equiv 0$.

**(a)** Show that the wavelet coefficients $y^*_1,\dots,y^*_N$ are i.i.d. $N(0,\sigma^2)$.

**(b)** Show that
$$
P\Big(\max_{j\le N}|y^*_j| > \sigma\sqrt{2\log N}\Big)\;\longrightarrow\;0 \qquad (N\to\infty).
$$
So with high probability the universal threshold kills every pure-noise coefficient.

**(c)** Show the threshold is sharp: for every fixed $c<1$,
$$
P\Big(\max_{j\le N}|y^*_j| > c\,\sigma\sqrt{2\log N}\Big)\;\longrightarrow\;1 .
$$

Conclude that $\max_j|y^*_j|\big/\sigma\sqrt{2\log N}\to 1$ in probability.

*Field:* Statistics / ML (nonparametric smoothing, extreme values)

*Hint:* You only need the elementary Gaussian tail bound $\displaystyle 1-\Phi(t)\le \frac{\varphi(t)}{t}$ and a matching lower bound of the same order.
