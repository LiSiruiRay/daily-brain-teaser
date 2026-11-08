---
name: "The Factorization That Can't Make Up Its Mind: Non-Uniqueness of NMF"
type: "ML/Stats"
tags: ["non-negative matrix factorization", "identifiability", "convex cones", "monomial matrices", "unsupervised learning"]
date: "2026-11-08"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Hastie, Tibshirani, Friedman — The Elements of Statistical Learning (2nd ed.), §14.6 and Figure 14.34 (after Donoho & Stodden, 2004)"
---
# The Factorization That Can't Make Up Its Mind: Non-Uniqueness of NMF

Non-negative matrix factorization (NMF) approximates a non-negative $N\times p$ data matrix as
$$X \approx WH,\qquad W\in\mathbb{R}_{\ge 0}^{N\times r},\; H\in\mathbb{R}_{\ge 0}^{r\times p}.$$
Its selling point is interpretability: the rows of $H$ are supposed to be meaningful "parts", for example pieces of faces. Interpretability requires that the factorization be essentially unique.

Some ambiguity is unavoidable. For any invertible $r\times r$ matrix $Q$ we have $WH = (WQ)(Q^{-1}H)$. For a positive diagonal $D$ and a permutation $P$, the choice $Q = PD$ keeps both factors non-negative. This only rescales and relabels the parts, so call it the *trivial* ambiguity.

**(a)** Let $Q$ be an invertible $r\times r$ matrix such that both $Q$ and $Q^{-1}$ are entrywise non-negative. Prove that $Q$ is a permutation matrix times a positive diagonal matrix.

So the trivial ambiguity is the only one you get from a non-negative change of basis with a non-negative inverse. Does that make NMF unique up to trivial ambiguity?

**(b)** Let
$$X=\begin{pmatrix}2&1\\1&2\end{pmatrix}.$$
Find all exact factorizations $X = WH$ with $W,H\ge 0$ of size $2\times 2$. To remove the trivial ambiguity, normalize each row of $H$ to sum to $1$ and order its rows. Show that infinitely many essentially different factorizations remain, and describe them geometrically.

**(c)** Contrast this with $X = I_2$. What geometric feature of the data makes the difference?
