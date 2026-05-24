# Answer: The Variance of Bagging

## Key Idea / Intuition

Averaging $B$ copies of a random variable reduces variance — but only the **independent part** of the variance vanishes. The **correlated part** is irreducible no matter how many copies you average. This is the core tension in bagging: bootstrap samples from the same training set are highly correlated, so the variance reduction hits a floor. Meanwhile, averaging never touches bias at all.

---

## Formal Proof / Solution

### Part (a): Variance of the Bagged Predictor

We expand directly:

$$\mathrm{Var}(\hat{f}_{\text{bag}}) = \mathrm{Var}\!\left(\frac{1}{B}\sum_{b=1}^B \hat{f}_b\right) = \frac{1}{B^2} \mathrm{Var}\!\left(\sum_{b=1}^B \hat{f}_b\right).$$

Expanding the variance of the sum:

$$\mathrm{Var}\!\left(\sum_{b=1}^B \hat{f}_b\right) = \sum_{b=1}^B \mathrm{Var}(\hat{f}_b) + \sum_{b \neq b'} \mathrm{Cov}(\hat{f}_b, \hat{f}_{b'}).$$

Since each $\hat{f}_b$ has variance $\sigma^2$ and each pair has covariance $\rho \sigma^2$:

$$= B\sigma^2 + B(B-1)\rho\sigma^2.$$

Therefore:

$$\boxed{\mathrm{Var}(\hat{f}_{\text{bag}}) = \frac{1}{B^2}\left[B\sigma^2 + B(B-1)\rho\sigma^2\right] = \frac{\sigma^2}{B} + \frac{B-1}{B}\rho\sigma^2.}$$

You can rewrite this cleanly as:

$$\mathrm{Var}(\hat{f}_{\text{bag}}) = \rho\sigma^2 + \frac{1-\rho}{B}\sigma^2.$$

The first term is the **irreducible correlated floor**, and the second term **decays with $B$**.

---

### Part (b): As $B \to \infty$

$$\mathrm{Var}(\hat{f}_{\text{bag}}) \xrightarrow{B\to\infty} \rho\sigma^2.$$

**Interpretation:**

- If $\rho = 0$ (independent predictors): variance $\to 0$. Perfect, unlimited reduction.
- If $\rho = 1$ (perfectly correlated, e.g., identical bootstrap samples): variance $\to \sigma^2$. No reduction at all.
- In practice, bootstrap samples from the same dataset have high $\rho$, so bagging gives **partial but limited** variance reduction.

This is exactly why **Random Forests** inject extra randomness (random feature subsets) — they lower $\rho$ between trees, pushing the floor $\rho\sigma^2$ down further.

---

### Part (c): Bias Under Bagging

Compute the bias of $\hat{f}_{\text{bag}}$:

$$E[\hat{f}_{\text{bag}}] = \frac{1}{B}\sum_{b=1}^B E[\hat{f}_b] = \frac{1}{B} \cdot B(f^* + \beta) = f^* + \beta.$$

**Averaging does not change the bias.** If each base learner is biased by $\beta$, the bag is also biased by $\beta$.

**Fundamental limitation of bagging:**

> Bagging is a **variance reduction** technique only. It cannot fix a biased model.

This is why you should bag **low-bias, high-variance** models (like deep trees), not high-bias models (like shallow stumps). A pruned tree with high bias does not benefit from bagging — its ensemble is still biased.

---

### Summary Table

| Quantity | Single Learner | Bagged ($B \to \infty$) |
|---|---|---|
| Variance | $\sigma^2$ | $\rho \sigma^2$ |
| Bias | $\beta$ | $\beta$ |
| MSE | $\sigma^2 + \beta^2$ | $\rho\sigma^2 + \beta^2$ |

The elegant punchline: **bagging attacks exactly one term of the bias-variance decomposition, and its power is limited by how correlated the bootstrap models are.**
