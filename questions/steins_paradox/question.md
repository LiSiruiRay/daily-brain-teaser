# Stein's Paradox

## Problem

You observe a single sample $X \sim \mathcal{N}(\mu, I_d)$ where $\mu \in \mathbb{R}^d$ is unknown. You want to estimate $\mu$ under **squared error loss**:
$$L(\hat{\mu}, \mu) = \|\hat{\mu} - \mu\|^2$$

The obvious estimator is the MLE: $\hat{\mu}_{\mathrm{MLE}} = X$, which has risk $\mathrm{MSE} = d$.

**For $d = 1$ and $d = 2$**: the MLE is optimal — no estimator can uniformly beat it.

**For $d \geq 3$**: show that the MLE is **inadmissible**, i.e., exhibit an estimator $\tilde{\mu}$ such that
$$E\|\tilde{\mu}(X) - \mu\|^2 < d \quad \text{for all } \mu \in \mathbb{R}^d.$$

The **James–Stein estimator** is:
$$\hat{\mu}_{JS} = \left(1 - \frac{d-2}{\|X\|^2}\right) X$$

Show that $E\|\hat{\mu}_{JS} - \mu\|^2 < d$ for all $\mu$ when $d \geq 3$.

---

## Field
Statistics / Machine Learning

## Why It's Beautiful

This is one of the most startling results in all of statistics. It says: **even if you are estimating $d \geq 3$ completely unrelated quantities** (e.g., the temperature in Toronto, the GDP of Peru, and the mass of Jupiter), you should **shrink all your estimates toward zero together** — and this provably beats treating each problem independently.

The result shattered the intuition that "optimal estimation of independent quantities should be done independently." It led directly to the development of **empirical Bayes methods**, **regularization** (ridge regression shrinks toward zero for exactly this reason), and **shrinkage estimators** throughout modern statistics and ML.

Efron called it "the most striking result in post-war mathematical statistics."

## Key Idea / Trick

Use **Stein's identity**: for $X \sim \mathcal{N}(\mu, I_d)$ and any weakly differentiable $g: \mathbb{R}^d \to \mathbb{R}^d$:
$$E\langle X - \mu,\ g(X)\rangle = E[\nabla \cdot g(X)]$$

Write $\hat{\mu}_{JS} = X + g(X)$ with $g(X) = -\frac{d-2}{\|X\|^2} X$, expand the squared loss, and apply the identity to evaluate the cross-term. The risk drops below $d$ precisely because $d - 2 > 0$.

## Difficulty
4 / 5

## Tags
Statistics, Estimation, Admissibility, James-Stein, Shrinkage, Stein's identity, Empirical Bayes, Regularization, MSE
