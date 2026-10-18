---
name: "Why ICA Cannot Unmix Gaussians"
type: "ML/Stats"
tags: ["ICA", "whitening", "identifiability", "kurtosis", "rotation invariance", "Darmois-Skitovich"]
date: "2026-10-18"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Hastie, Tibshirani, Friedman — The Elements of Statistical Learning (2nd ed.), Section 14.7 (Independent Component Analysis and Exploratory Projection Pursuit)"
---
# Why ICA Cannot Unmix Gaussians

Let $S=(S_1,S_2)^\top$ have **independent** components with $\mathbb E S_i=0$ and $\operatorname{Var} S_i=1$. We observe only the mixture
$$
X = AS,\qquad A\in\mathbb R^{2\times 2}\ \text{invertible, unknown}.
$$
Independent Component Analysis (ICA) tries to recover $A$, and hence $S$, from the distribution of $X$.

**(a)** Let $\Sigma=\operatorname{Cov}(X)$ and define the whitened data $Z=\Sigma^{-1/2}X$. Show that $Z=RS$ for some **orthogonal** matrix $R$. Conclude that the covariance of $X$ determines $A$ only up to an unknown rotation or reflection.

**(b)** Suppose $S_1,S_2\stackrel{iid}{\sim}N(0,1)$. Show that **no** method can recover that rotation. In other words, $A$ and $AQ$ give exactly the same distribution of $X$ for every orthogonal $Q$.

**(c)** Now let $S_1,S_2\stackrel{iid}{\sim}\mathrm{Unif}[-\sqrt3,\sqrt3]$. Rotate by $45^\circ$:
$$
Y_1=\tfrac{S_1+S_2}{\sqrt2},\qquad Y_2=\tfrac{S_1-S_2}{\sqrt2}.
$$
Show that $Y_1$ and $Y_2$ are uncorrelated but **not** independent by computing
$$
\mathbb E[Y_1^2Y_2^2]-\mathbb E[Y_1^2]\,\mathbb E[Y_2^2].
$$
Express the answer for general independent sources in terms of the excess kurtosis $\kappa_i=\mathbb E S_i^4-3$.

*Punchline to think about:* what does this say about the source of ICA's power to identify the mixing matrix?
