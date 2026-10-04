# Answer: Cross-Entropy Decomposition: Entropy + KL Divergence

## Key Idea / Intuition

When you predict a constant $\hat{p}$ for all examples, the cross-entropy loss is a function of $\hat{p}$ alone, and it turns out to be the **KL divergence** from the true empirical distribution $(\bar{y}, 1-\bar{y})$ to your predicted distribution $(\hat{p}, 1-\hat{p})$, plus the entropy $H(\bar{y})$. Since KL divergence is always non-negative and vanishes only when the two distributions match, the minimum is achieved exactly at $\hat{p} = \bar{y}$, yielding $H(\bar{y})$.

The deeper message: cross-entropy = entropy + KL divergence. The entropy part is irreducible (it depends only on the labels, not your model). The KL part is the "extra cost" of miscalibration.

---

## Formal Proof / Solution

**Step 1: Simplify $L$ for constant $\hat{p}$.**

Since all $\hat{p}_i = \hat{p}$:

$$L = -\frac{1}{n}\sum_{i=1}^n \left[y_i \log \hat{p} + (1-y_i)\log(1-\hat{p})\right]$$

$$= -\bar{y}\log \hat{p} - (1-\bar{y})\log(1-\hat{p}).$$

**Step 2: Decompose into entropy plus KL divergence.**

Add and subtract $H(\bar{y}) = -\bar{y}\log\bar{y} - (1-\bar{y})\log(1-\bar{y})$:

$$L = \underbrace{-\bar{y}\log\bar{y} - (1-\bar{y})\log(1-\bar{y})}_{H(\bar{y})} + \underbrace{\bar{y}\log\frac{\bar{y}}{\hat{p}} + (1-\bar{y})\log\frac{1-\bar{y}}{1-\hat{p}}}_{D_{\mathrm{KL}}(\bar{y} \,\|\, \hat{p})}.$$

So:
$$L = H(\bar{y}) + D_{\mathrm{KL}}(\bar{y} \,\|\, \hat{p}).$$

**Step 3: Apply non-negativity of KL divergence.**

By **Gibbs' inequality** (or Jensen's inequality applied to the convex function $-\log$):

$$D_{\mathrm{KL}}(\bar{y} \,\|\, \hat{p}) = \bar{y}\log\frac{\bar{y}}{\hat{p}} + (1-\bar{y})\log\frac{1-\bar{y}}{1-\hat{p}} \geq 0,$$

with equality if and only if $\hat{p} = \bar{y}$.

**Step 4: Conclude.**

$$L = H(\bar{y}) + D_{\mathrm{KL}}(\bar{y} \,\|\, \hat{p}) \geq H(\bar{y}),$$

with equality if and only if $\hat{p} = \bar{y}$. $\blacksquare$

---

**Why this is the right intuition for ML:**

The decomposition $\text{Cross-Entropy} = \text{Entropy} + \text{KL}$ is fundamental:

- $H(\bar{y})$ is the **irreducible uncertainty** — you cannot do better than this with a constant predictor, no matter how you set $\hat{p}$.
- $D_{\mathrm{KL}}(\bar{y} \| \hat{p})$ measures your **miscalibration penalty** — it is zero only when your predicted probability matches the empirical frequency.

This generalizes: for any model (not just constant predictors), minimizing cross-entropy is equivalent to minimizing KL divergence between the true conditional label distribution $p(y|x)$ and your model's output $\hat{p}(y|x)$.
