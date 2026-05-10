# Answer: Bias-Variance Decomposition

## Key Idea / Intuition

The expected prediction error has three distinct sources: noise you can never escape ($\sigma^2$), systematic error from model assumptions being wrong (bias), and sensitivity to the particular training data you got (variance). The decomposition is just a careful application of "add and subtract the mean" — the same trick that gives $\mathbb{E}[X^2] = \text{Var}(X) + (\mathbb{E}[X])^2$. The tradeoff is inevitable because making a model more flexible reduces bias but amplifies variance, and vice versa.

---

## Formal Proof / Solution

**Step 1: Separate noise from estimation error.**

Write $Y = f(x_0) + \varepsilon$. Since $\varepsilon$ is independent of $\hat{f}(x_0)$ (which depends only on training data, not on the new noise):

$$\text{EPE}(x_0) = \mathbb{E}\left[(f(x_0) + \varepsilon - \hat{f}(x_0))^2\right]$$

Let $u = f(x_0) - \hat{f}(x_0)$, so we need $\mathbb{E}[(u + \varepsilon)^2]$. Expanding:

$$\mathbb{E}[(u + \varepsilon)^2] = \mathbb{E}[u^2] + 2\mathbb{E}[u\,\varepsilon] + \mathbb{E}[\varepsilon^2]$$

Since $\varepsilon$ is independent of $\hat{f}$ (and hence of $u$), and $\mathbb{E}[\varepsilon] = 0$:

$$\mathbb{E}[u\,\varepsilon] = \mathbb{E}[u]\cdot\mathbb{E}[\varepsilon] = 0$$

Therefore:

$$\text{EPE}(x_0) = \mathbb{E}\left[(f(x_0) - \hat{f}(x_0))^2\right] + \sigma^2$$

**Step 2: Decompose the mean squared error term.**

Now add and subtract $\mu := \mathbb{E}[\hat{f}(x_0)]$ inside the square:

$$\mathbb{E}\left[(f(x_0) - \hat{f}(x_0))^2\right] = \mathbb{E}\left[(f(x_0) - \mu + \mu - \hat{f}(x_0))^2\right]$$

Let $a = f(x_0) - \mu$ (a constant with respect to the expectation) and $b = \mu - \hat{f}(x_0)$ (zero-mean random variable since $\mathbb{E}[b] = 0$):

$$= \mathbb{E}[(a + b)^2] = a^2 + 2a\,\mathbb{E}[b] + \mathbb{E}[b^2] = a^2 + 0 + \mathbb{E}[b^2]$$

Substituting back:

$$= \underbrace{(f(x_0) - \mathbb{E}[\hat{f}(x_0)])^2}_{\text{Bias}^2} + \underbrace{\mathbb{E}\left[(\hat{f}(x_0) - \mathbb{E}[\hat{f}(x_0)])^2\right]}_{\text{Var}(\hat{f}(x_0))}$$

**Step 3: Collect everything.**

$$\boxed{\text{EPE}(x_0) = \sigma^2 + \text{Bias}^2(\hat{f}(x_0)) + \text{Var}(\hat{f}(x_0))}$$

---

**Why can't we minimize all three simultaneously?**

- $\sigma^2$ is **irreducible** — no model can remove measurement noise.
- **Bias** decreases as model complexity increases (e.g., high-degree polynomial fits the training signal closely).
- **Variance** *increases* as model complexity increases (a high-degree polynomial is very sensitive to which exact training points were drawn).

**Concrete example — polynomial regression:**

| Model | Bias | Variance |
|-------|------|----------|
| Constant fit ($\hat{f} = \bar{y}$) | High | Very low |
| Degree-$n$ polynomial (interpolates all data) | ~0 | Huge |
| Degree-2 fit for truly quadratic $f$ | 0 | Moderate |

As you increase the degree beyond the true complexity, bias keeps dropping toward zero but variance explodes. The optimal model lives at the sweet spot where $\frac{d}{d\lambda}[\text{Bias}^2 + \text{Var}] = 0$. This is the fundamental reason regularization (ridge, LASSO) and cross-validation exist: they deliberately introduce a little bias to dramatically cut variance, reducing total EPE.

> **The punchline:** The decomposition is exact and additive — there is no "free lunch." Any change to the model that reduces bias must work against reducing variance, making the tradeoff a mathematical inevitability, not just a heuristic.
