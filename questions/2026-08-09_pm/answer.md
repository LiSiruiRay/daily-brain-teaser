# Answer: The Ghost Feature: Useless Predictor Inflates OLS Variance

## Key Idea / Intuition

Adding any new predictor to OLS can only decrease RSS — the model now has a strictly larger column space to project onto, so the residual vector can only get shorter (or stay the same). Yet the unbiased variance estimator $\hat{\sigma}^2 = \text{RSS}/(n-p)$ divides by the **degrees of freedom**, which drops by 1 each time we add a predictor. When the new predictor is useless, the decrease in RSS is tiny (it only absorbs noise), but we pay a full degree of freedom — so the denominator shrinks while the numerator barely budges, inflating the estimate. This is the statistical cost of overfitting: we spend a degree of freedom to fit noise.

---

## Formal Proof / Solution

### Part 1: $\widetilde{\text{RSS}} \leq \text{RSS}$

Let $H = X(X^\top X)^{-1}X^\top$ be the hat matrix for the original model, and $\hat{e} = (I - H)Y$ the residual vector, so $\text{RSS} = \|\hat{e}\|^2$.

The augmented model has column space $\mathcal{C}(\tilde{X}) = \mathcal{C}([X \mid z])$, which satisfies

$$\mathcal{C}(X) \subseteq \mathcal{C}(\tilde{X}).$$

OLS minimizes $\|Y - \tilde{X}\tilde{\beta}\|^2$ over all $\tilde{\beta}$, i.e., it projects $Y$ onto $\mathcal{C}(\tilde{X})$. Since projecting onto a **larger** subspace can only reduce (or maintain) the distance to $Y$:

$$\widetilde{\text{RSS}} = \|Y - \hat{P}_{\tilde{X}} Y\|^2 \leq \|Y - \hat{P}_X Y\|^2 = \text{RSS}.$$

**Equality condition.** Equality holds iff $\hat{P}_{\tilde{X}} Y = \hat{P}_X Y$, i.e., adding $z$ does not move the projection. This happens iff $z$ lies in $\mathcal{C}(X)$ **or** $z$ is orthogonal to $\hat{e}$ (the component of $Y$ outside $\mathcal{C}(X)$). More precisely, the augmented projection adds to $\hat{P}_X Y$ a component along the part of $z$ orthogonal to $\mathcal{C}(X)$. Let $z^\perp = (I-H)z$ be the residual of regressing $z$ on $X$. The extra reduction in RSS is

$$\text{RSS} - \widetilde{\text{RSS}} = \frac{(\hat{e}^\top z^\perp)^2}{\|z^\perp\|^2}$$

(by the formula for adding one predictor to OLS). This is zero iff $\hat{e} \perp z^\perp$, i.e., iff $\hat{e} \perp z$ (since $H\hat{e} = 0$). $\blacksquare$

---

### Part 2: The Paradox — RSS Falls but $\hat{\sigma}^2$ Rises

The unbiased estimator of $\sigma^2$ in each model is:

$$\hat{\sigma}^2_{\text{orig}} = \frac{\text{RSS}}{n - p}, \qquad \hat{\sigma}^2_{\text{aug}} = \frac{\widetilde{\text{RSS}}}{n - p - 1}.$$

When $z$ is a pure noise predictor independent of $Y$:

- The extra reduction $\text{RSS} - \widetilde{\text{RSS}} = \frac{(\hat{e}^\top z)^2}{\|z^\perp\|^2}$ is **small** — it is the squared correlation of $z$ with the residual, which is random noise of order $O(1)$.
- The denominator **drops from $n-p$ to $n-p-1$**, a fixed decrement of 1.

Concretely, one can show that if $z$ is genuinely orthogonal to the true signal:

$$\mathbb{E}[\widetilde{\text{RSS}}] = (n - p - 1)\sigma^2, \qquad \mathbb{E}[\text{RSS}] = (n-p)\sigma^2.$$

So dividing by the correct degrees of freedom restores unbiasedness in each case. But the augmented model *uses up* one degree of freedom fitting noise, leaving fewer to estimate $\sigma^2$ with, hence **higher variance** in the estimate and a numerically inflated value when the noise happens to fit in the "right" direction.

**One-line summary of the paradox:**

> RSS measures total unexplained variation; degrees of freedom measure how many independent errors remain. Adding a noise variable steals one degree of freedom while giving back almost no reduction in RSS — so the ratio goes *up*, not down.

This is precisely why adjusted $R^2$ and information criteria (AIC, BIC) penalize model complexity: raw RSS always decreases with more predictors, but the true noise floor estimate worsens.
