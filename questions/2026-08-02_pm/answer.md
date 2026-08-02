# Answer: PCA Reconstruction Error and Discarded Eigenvalues

## Key Idea / Intuition

The Frobenius norm of a matrix is just the sum of squared singular values, and singular values of $X$ are directly related to eigenvalues of $X^T X$. PCA throws away the directions corresponding to the smallest singular values, so the reconstruction error is precisely the total "energy" in those discarded directions. This is also the content of the **Eckart–Young theorem**: PCA gives the *best* possible rank-$k$ approximation in Frobenius norm.

---

## Formal Proof / Solution

**Setup via SVD.** Write the thin SVD of the centered matrix:
$$X = U \Sigma V^T$$
where $U \in \mathbb{R}^{n \times p}$ has orthonormal columns, $\Sigma = \mathrm{diag}(\sigma_1, \ldots, \sigma_p)$ with $\sigma_1 \geq \cdots \geq \sigma_p \geq 0$, and $V \in \mathbb{R}^{p \times p}$ is orthogonal.

**Relating singular values to covariance eigenvalues.** The sample covariance is:
$$S = \frac{1}{n} X^T X = \frac{1}{n} V \Sigma^2 V^T$$
So the eigenvalues of $S$ are $\lambda_j = \sigma_j^2 / n$, i.e., $\sigma_j^2 = n\lambda_j$.

**The rank-$k$ PCA approximation.** Keeping the top $k$ principal components means:
$$\hat{X} = U_k \Sigma_k V_k^T$$
where the subscript $k$ denotes the first $k$ columns/rows. This is exactly the best rank-$k$ approximation by the **Eckart–Young theorem**.

**Computing the reconstruction error.** The error matrix is:
$$X - \hat{X} = \sum_{j=k+1}^{p} \sigma_j u_j v_j^T$$

Taking the Frobenius norm and using orthonormality of $u_j, v_j$:
$$\|X - \hat{X}\|_F^2 = \left\|\sum_{j=k+1}^{p} \sigma_j u_j v_j^T\right\|_F^2 = \sum_{j=k+1}^{p} \sigma_j^2$$

since $\|u_i v_i^T\|_F = 1$ and cross terms vanish by orthogonality. Substituting $\sigma_j^2 = n\lambda_j$:

$$\boxed{\|X - \hat{X}\|_F^2 = n \sum_{j=k+1}^{p} \lambda_j}$$

**Bonus — Optimality.** The Eckart–Young theorem states that among *all* rank-$k$ matrices $B$:
$$\hat{X} = \arg\min_{\mathrm{rank}(B) \leq k} \|X - B\|_F^2$$

So PCA doesn't just minimize reconstruction error in some heuristic sense—it is provably the optimal rank-$k$ approximation. The proportion of variance retained is:
$$\frac{\sum_{j=1}^k \lambda_j}{\sum_{j=1}^p \lambda_j}$$
which is exactly the "explained variance ratio" reported by every PCA implementation. The reconstruction error formula makes this precise: you're losing exactly the variance in the dropped directions, nothing more and nothing less.
