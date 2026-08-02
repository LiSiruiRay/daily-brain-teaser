---
name: "PCA Reconstruction Error and Discarded Eigenvalues"
type: "ML/Stats"
tags: ["PCA", "SVD", "Frobenius norm", "Eckart-Young", "dimensionality reduction", "covariance matrix"]
date: "2026-08-02"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Ch. 3 & 14; standard linear algebra / ML folklore"
---
# The PCA Variance You're Not Capturing

You run PCA on a data matrix $X \in \mathbb{R}^{n \times p}$ (centered, $n > p$) and keep only the top $k < p$ principal components, obtaining a rank-$k$ approximation $\hat{X}$.

The **reconstruction error** is measured by:
$$\|X - \hat{X}\|_F^2$$

**Question:** Show that this equals the sum of the *discarded* eigenvalues of the sample covariance matrix $S = \frac{1}{n} X^T X$. That is, if $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p \geq 0$ are the eigenvalues of $S$, then:
$$\|X - \hat{X}\|_F^2 = n \sum_{j=k+1}^{p} \lambda_j$$

**Bonus:** What does this tell you about the *optimal* rank-$k$ approximation to $X$?
