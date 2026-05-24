# Answer: The Double Descent Puzzle

## Key Idea / Intuition

When $p < n$, OLS has a unique solution and training error decreases as $p$ grows (more flexibility). At $p = n$, the model interpolates the data perfectly — training error hits **zero**. For $p > n$ there are infinitely many interpolating solutions; gradient descent initialized at zero (equivalently, the Moore–Penrose pseudoinverse) picks the **minimum $\ell_2$-norm** solution. This implicit bias toward small-norm solutions acts like an implicit regularizer, and for well-structured problems this can generalize surprisingly well — the heart of the **double descent** phenomenon.

---

## Formal Proof / Solution

### Part (a): Training Error as a Function of $p$

Let $X \in \mathbb{R}^{n \times p}$ be the design matrix and $y \in \mathbb{R}^n$ the response.

**Under-parameterized regime $p < n$:**  
OLS minimizes $\|y - X\beta\|^2$. The unique solution is $\hat\beta = (X^\top X)^{-1} X^\top y$ (assuming full column rank), and the fitted values are $\hat y = H y$ where $H = X(X^\top X)^{-1}X^\top$ is the hat matrix projecting onto the column space of $X$. Training error is:
$$\text{RSS} = \|y - \hat y\|^2 = \|(I - H)y\|^2 > 0 \quad \text{generically}.$$
As $p$ increases, the column space of $X$ grows, $H$ captures more of $y$, and training error **monotonically decreases**.

**Interpolation threshold $p = n$:**  
When $p = n$ and $X$ is square and invertible, $H = I$, so $\hat y = y$ exactly. Training error = **0**.

**Over-parameterized regime $p > n$:**  
There are infinitely many $\beta$ satisfying $X\beta = y$ (the system is underdetermined). Any such solution achieves training error = 0. The solution family is an affine subspace of dimension $p - n$.

---

### Part (b): Which Solution Does Gradient Descent Pick?

Among all interpolating solutions, gradient descent **initialized at $\beta_0 = 0$** converges to the one with **minimum Euclidean norm**:
$$\hat\beta_{\text{min-norm}} = X^\top (X X^\top)^{-1} y = X^+ y,$$
where $X^+$ is the Moore–Penrose pseudoinverse. This is because gradient descent on the squared loss stays in the row space of $X$ (it only moves in directions spanned by the gradient, which lives in $\text{rowspace}(X)$), and the minimum-norm interpolant is exactly the projection of $0$ onto the solution affine subspace — which lies in $\text{rowspace}(X)$.

**Why does minimum norm help generalization?**

Suppose the true signal is $y = X\beta^* + \varepsilon$. The test error of any interpolating $\hat\beta$ decomposes as:

$$\mathbb{E}[\text{test error}] \propto \|\hat\beta - \beta^*\|^2_{\text{signal directions}} + \text{noise amplification}.$$

The minimum-norm solution **distributes** the fit across many small coefficients rather than placing it on a few large ones. In high-dimensional settings where $\beta^*$ is itself small or sparse in some sense, this implicit $\ell_2$ regularization behaves like **ridge regression with a data-dependent effective regularization strength**.

Concretely, the bias–variance tradeoff for the minimum-norm estimator in the $p > n$ regime is:
$$\text{test MSE} = \underbrace{\|\text{bias}\|^2}_{\to 0 \text{ as } p \to \infty} + \underbrace{\sigma^2 \cdot \text{tr}(X^+ (X^+)^\top)}_{\text{noise amplification}}.$$

Near $p \approx n$, the singular values of $X$ near zero get **inverted** by the pseudoinverse, causing noise amplification to blow up — this is the **interpolation peak** (the right hump of double descent). As $p \gg n$, the many small singular values each contribute little individually, and the total noise term can **decrease** again.

---

### The Double Descent Picture

$$\boxed{\text{Test error} = \underbrace{\searrow}_{\text{classical regime } p < n} \nearrow_{\text{peak near } p = n} \searrow_{\text{modern regime } p \gg n}}$$

- **Classical regime** ($p \ll n$): bias dominates, more parameters reduce bias faster than variance grows.  
- **Interpolation peak** ($p \approx $n$): the model just barely interpolates; tiny perturbations cause wild swings in $\hat\beta$ (near-singular $X^\top X$).  
- **Modern regime** ($p \gg n$): minimum-norm interpolation re-emerges as a gentle implicit regularizer; test error descends again.

This explains why overparameterized neural networks — which also find low-norm (or otherwise "simple") solutions via gradient descent from near-zero initialization — can generalize well even with zero training error.

---

**Reference:** ESL Chapter 7 (Bias–Variance tradeoff) provides the classical picture; the double descent phenomenon is discussed in the context of modern ML (Hastie et al., *Surprises in High-Dimensional Ridgeless Least Squares Interpolation*, 2022).

Written to: [questions/2025-07-18_AM_double_descent_puzzle.md](questions/2025-07-18_AM_double_descent_puzzle.md)
