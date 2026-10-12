# Answer: Gradient Boosting Secret: Why Each Tree Fits Residuals

## Key Idea / Intuition

For squared error loss, the negative gradient with respect to the current prediction is literally the residual — so fitting trees to "pseudo-residuals" (negative gradients) is just fitting trees to actual residuals. The surprise is that **this residual-fitting story generalizes**: for *any* differentiable loss, we can define "pseudo-residuals" as negative gradients and run the same algorithm. This turns boosting from an ad hoc trick into a **gradient descent in function space**.

---

## Formal Proof / Solution

### Step 1: Compute the Negative Gradient

Define the pointwise loss at observation $i$ as a function of the current model output $F = F_{m-1}(x_i)$:

$$L_i(F) = \frac{1}{2}(y_i - F)^2$$

The **negative gradient** with respect to $F$ is:

$$-\frac{\partial L_i}{\partial F}\bigg|_{F = F_{m-1}(x_i)} = -\frac{\partial}{\partial F}\left[\frac{1}{2}(y_i - F)^2\right]_{F_{m-1}(x_i)}$$

$$= -\cdot(-(y_i - F_{m-1}(x_i))) = y_i - F_{m-1}(x_i) = r_i$$

So the pseudo-residual equals the true residual. $\square$

---

### Step 2: Why Is This Surprising?

The naive story: *"boosting fits trees to residuals because residuals capture what the current model missed."* This sounds like a clever but specific trick.

The deeper story: **gradient boosting is gradient descent, but in function space**.

In ordinary gradient descent on parameters $\theta$, we update:
$$\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}$$

In gradient boosting, the "parameter" is the function $F$ itself, living in an infinite-dimensional space. We can't move in the direction of $-\nabla_F \mathcal{L}$ directly (that would require adding an arbitrary function), so we **project** the negative gradient onto the space of trees by fitting a tree to it.

The pseudo-residuals for other losses:

| Loss | $-\partial L / \partial F$ | Pseudo-residual |
|---|---|---|
| Squared error | $y_i - F(x_i)$ | True residual |
| Absolute error | $\text{sign}(y_i - F(x_i))$ | $\pm 1$ (direction only) |
| Log-loss (classification) | $y_i - p_i$ | Residual in probability |

For **absolute error**, the pseudo-residuals are signs $\pm 1$ — this gives a boosting algorithm robust to outliers (since large residuals don't dominate). For **log-loss**, pseudo-residuals are $y_i - \hat{p}_i$, connecting gradient boosting to logistic regression.

---

### Step 3: The Unifying Framework

Total loss: $\mathcal{L}(F) = \sum_{i=1}^N L(y_i, F(x_i))$

At step $m$, define pseudo-residuals:
$$\tilde{r}_i^{(m)} = -\left[\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}\right]_{F = F_{m-1}}$$

Fit a regression tree $h_m$ to $\{(x_i, \tilde{r}_i^{(m)})\}$, then update:
$$F_m = F_{m-1} + \eta \cdot h_m$$

This is **Friedman's gradient boosting machine** (2001). The key insight: once you recognize boosting as gradient descent, you can "boost" with *any differentiable loss function* — the algorithm structure is identical, only the pseudo-residuals change.

This reveals that residual fitting is not the cause of boosting's success; it is a **special case of a much more general principle**.
