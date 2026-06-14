# Answer: The Infinite Ensemble That Doesn't Help

## Key Idea / Intuition

When classifiers are perfectly correlated, majority voting does nothing — they all vote the same way, so the ensemble error equals the individual error. Averaging only reduces the **variance** (the idiosyncratic, independent noise) not the **bias** (the shared, systematic error). This is the fundamental insight behind when bagging and ensemble methods actually help: they attack variance, not bias. If your models all fail in the same systematic way, throwing more of them together is useless.

---

## Formal Proof / Solution

### Part 1: Perfectly Correlated Classifiers

Since all classifiers are perfectly correlated, they all agree:

$$h_1(x) = h_2(x) = \cdots = h_n(x) \text{ almost surely.}$$

The majority vote is simply $h_1(x)$. Therefore:

$$P(\text{majority vote is wrong}) = P(h_1(x) \neq y^*) = 1 - p.$$

**The error rate is exactly $1-p$ for any $n$, even $n \to \infty$.** More classifiers provide zero benefit.

---

### Part 2: Bias-Variance Decomposition Under Averaging

Consider a **regression** setting. Let each model $\hat{f}_i(x)$ have:

$$\mathbb{E}[\hat{f}_i(x)] = \mu(x), \quad \text{Var}(\hat{f}_i(x)) = \sigma^2$$

Decompose the error of a single model:

$$\text{MSE} = \underbrace{(\mu(x) - f^*(x))^2}_{\text{bias}^2} + \underbrace{\sigma^2}_{\text{variance}}$$

Now form the average ensemble $\bar{f}(x) = \frac{1}{n}\sum_{i=1}^n \hat{f}_i(x)$.

**Bias of the average:**

$$\mathbb{E}[\bar{f}(x)] = \frac{1}{n}\sum_{i=1}^n \mathbb{E}[\hat{f}_i(x)] = \mu(x)$$

so the **bias is unchanged**: $\text{bias}^2(\bar{f}) = (\mu(x) - f^*(x))^2$.

**Variance of the average** (with pairwise correlation $\rho$):

$$\text{Var}(\bar{f}) = \frac{1}{n^2}\text{Var}\!\left(\sum_i \hat{f}_i\right) = \frac{1}{n^2}\left(n\sigma^2 + n(n-1)\rho\sigma^2\right) = \frac{\sigma^2}{n} + \frac{(n-1)}{n}\rho\sigma^2$$

As $n \to \infty$:

$$\text{Var}(\bar{f}) \;\longrightarrow\; \rho\,\sigma^2$$

| Correlation $\rho$ | Variance of ensemble | What happens |
|---|---|---|
| $\rho = 0$ (independent) | $\to 0$ | Full variance reduction |
| $0 < \rho < 1$ | $\to \rho\sigma^2 > 0$ | Partial reduction |
| $\rho = 1$ (perfectly correlated) | $= \sigma^2$ | No reduction at all |

---

### The Punchline

$$\boxed{\text{MSE}(\bar{f}) = \underbrace{(\mu - f^*)^2}_{\text{bias}^2,\ \text{unchanged}} + \underbrace{\rho\,\sigma^2}_{\text{residual variance}}}$$

**Ensembling helps only when:**
1. The models have **low bias** (they are "roughly right on average"), and
2. The models have **low correlation** (they make **different** mistakes).

This is exactly why **bagging** works well for high-variance, low-bias models like deep decision trees: each tree on a bootstrap sample is different enough ($\rho$ small) that the variance collapses. But for a misspecified linear model, no amount of bagging fixes the bias — you're averaging the same systematic error forever.

**Random Forests** take this further by decorrelating trees via random feature subsets, explicitly reducing $\rho$ to push residual variance toward zero.
