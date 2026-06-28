# Answer: The Irrelevant Feature Paradox: When Adding Noise Helps OLS

## Key Idea / Intuition

OLS always fits the training data as well as possible given the degrees of freedom — adding more columns (even pure noise) can only **decrease** training error, because OLS is projecting $y$ onto a larger subspace, getting a tighter fit. But this comes at a cost: each noise column "uses up" a degree of freedom, inflating out-of-sample error. The gap between training MSE and test MSE grows with every noise column added. This is the **optimism of training error** made vivid.

---

## Formal Proof / Solution

### Setup

Let $\tilde{X} = [X \mid Z] \in \mathbb{R}^{n \times (p+q)}$, and let $\hat{y} = \tilde{X}(\tilde{X}^\top \tilde{X})^{-1}\tilde{X}^\top y = H y$ be the OLS fit, where $H$ is the hat matrix (orthogonal projection onto the column space of $\tilde{X}$).

The hat matrix satisfies $\operatorname{tr}(H) = p + q$ (the number of columns, assuming full rank).

---

### Training MSE

The in-sample residual sum of squares is:

$$\text{RSS} = \|y - Hy\|^2 = \|(I-H)y\|^2$$

Since $y = X\beta^* + \varepsilon$ and $X\beta^*$ lies in the column space of $\tilde{X}$ (since $X$ is a sub-block), we have $(I-H)X\beta^* = 0$, so:

$$\text{RSS} = \|(I-H)\varepsilon\|^2$$

Taking expectations:

$$\mathbb{E}[\text{RSS}] = \sigma^2 \operatorname{tr}(I - H) = \sigma^2(n - p - q)$$

So the expected training MSE is:

$$\mathbb{E}\!\left[\frac{\text{RSS}}{n}\right] = \sigma^2 \cdot \frac{n - p - q}{n}$$

**As $q$ increases, training MSE decreases** — adding noise features always improves the apparent fit!

---

### Test MSE (Out-of-Sample)

For a new observation $y_0 = x_0^\top \beta^* + \varepsilon_0$, the expected prediction error decomposes as:

$$\text{EPE} = \text{Bias}^2 + \text{Variance} + \sigma^2$$

The OLS estimator $\hat{\beta}$ on $\tilde{X}$ is unbiased for the true $\beta^*$ (with zeros for the noise columns), so Bias $= 0$. The variance of $\hat{y}_0$ depends on how many columns are estimated. For simplicity, look at **expected in-sample prediction error** on a new $y$ drawn from the same $X$:

$$\mathbb{E}[\text{Test MSE}] = \sigma^2 \cdot \frac{n + p + q}{n}$$

(This follows from the standard optimism formula: $\text{Test EPE} = \text{Training EPE} + \frac{2\sigma^2 d}{n}$ where $d = p+q$.)

**As $q$ increases, test MSE increases** — each noise column costs exactly $\frac{2\sigma^2}{n}$ in optimism.

---

### The Paradox Summarized

| Quantity | Formula | Direction as $q \uparrow$ |
|---|---|---|
| Expected Training MSE | $\sigma^2(n-p-q)/n$ | **Decreases** ↓ |
| Expected Test MSE | $\sigma^2(n+p+q)/n$ | **Increases** ↑ |
| Optimism gap | $2\sigma^2(p+q)/n$ | **Widens** ↑↑ |

The training error is a **systematically biased estimator** of true prediction error, and the bias grows linearly with the number of predictors — even useless ones. This is why model selection and regularization are essential: the model does not "know" its columns are noise.

Notably, at $q = n - p$, the model would be exactly interpolating ($\text{RSS} = 0$) — perfect training fit, terrible generalization. This is the classical overfitting catastrophe.
