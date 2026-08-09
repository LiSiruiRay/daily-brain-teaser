# Answer: The Variance That Vanishes: Why PCA Features Are Uncorrelated

## Key Idea / Intuition

The sample covariance matrix $S$ captures all pairwise correlations among features. PCA finds an **orthogonal change of basis** that simultaneously diagonalizes $S$ — this is just the spectral theorem for symmetric matrices. In the new basis, the "variance budget" of the data is redistributed along directions of maximal spread, and the off-diagonal correlations literally become zero because the eigenvectors are orthogonal. The correlation didn't disappear — it was **rotated into pure variance** along each principal axis.

---

## Formal Proof / Solution

### Setup

The sample covariance matrix is $S = \frac{1}{n} X^T X$. Since $S$ is real symmetric, the spectral theorem gives

$$S v_k = \lambda_k v_k, \quad v_j^T v_k = \delta_{jk}.$$

### Part (a): Sample variance of scores equals $\lambda_k$

The score vector is $z_k = X v_k \in \mathbb{R}^n$.

The sample mean of $z_k$: since columns of $X$ are centered, $X^T \mathbf{1} = 0$, so $\mathbf{1}^T z_k = \mathbf{1}^T X v_k = 0$. The scores are automatically mean-zero.

The sample variance is:

$$\text{Var}(z_k) = \frac{1}{n} z_k^T z_k = \frac{1}{n} (X v_k)^T (X v_k) = \frac{1}{n} v_k^T X^T X v_k = v_k^T S v_k.$$

Since $S v_k = \lambda_k v_k$ and $v_k^T v_k = 1$:

$$\text{Var}(z_k) = v_k^T (\lambda_k v_k) = \lambda_k. \quad \checkmark$$

### Part (b): Scores are sample-uncorrelated

For $j \neq k$:

$$\frac{1}{n} z_j^T z_k = \frac{1}{n}(X v_j)^T (X v_k) = \frac{1}{n} v_j^T X^T X v_k = v_j^T S v_k.$$

Now use $S v_k = \lambda_k v_k$:

$$v_j^T S v_k = \lambda_k \, v_j^T v_k = \lambda_k \cdot 0 = 0,$$

since eigenvectors of a symmetric matrix for **distinct** eigenvalues are orthogonal (and even when $\lambda_j = \lambda_k$, we choose an orthonormal basis within each eigenspace). $\quad \checkmark$

> **Note:** This calculation is exactly the statement that $S$ is diagonalized by $V = [v_1 \cdots v_p]$:
> $$\frac{1}{n} (XV)^T (XV) = V^T S V = \Lambda = \mathrm{diag}(\lambda_1, \ldots, \lambda_p).$$

### Part (c): Where did the correlation go?

The original features correlate because they share underlying "directions of variation" — e.g., two financial stocks both driven by a common market factor. PCA identifies those directions explicitly: the first principal component points along the axis of maximum joint variation, the second along the next most, and so on, all forced to be **mutually perpendicular**. By projecting onto these axes, we decompose the total variance cleanly — each score captures one "pure" source of variation and is blind to the others. The correlations weren't destroyed; they were **reorganized**: what appeared as cross-feature covariance is now concentrated entirely on the diagonal (the eigenvalues), while the off-diagonal entries vanish by orthogonality. Think of it as rotating the data cloud so its principal axes align with the coordinate axes — a tilted ellipse becomes an axis-aligned one, and axis-aligned ellipses have uncorrelated coordinates.

---

### Summary Table

| Quantity | Value |
|---|---|
| $\text{Var}(z_k)$ | $\lambda_k$ |
| $\text{Cov}(z_j, z_k)$, $j\neq k$ | $0$ |
| Total variance preserved | $\sum_k \lambda_k = \text{tr}(S)$ |

The last row is the **trace invariance**: rotation preserves total variance, just redistributes it.
