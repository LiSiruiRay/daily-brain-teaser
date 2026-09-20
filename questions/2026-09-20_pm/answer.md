# Answer: PCR Bias-Variance per Principal Component

## Key Idea / Intuition

OLS is unbiased but not necessarily low-variance. When $X$ has a tiny singular value $d_j \approx 0$, the OLS estimate amplifies that direction by $1/d_j^2$, causing enormous variance. PCR simply **hard-thresholds** the component contributions: each component is either kept (zero bias, variance $\sigma^2$) or discarded (variance zero, bias $(u_j^\top X\beta)^2$). The key insight is that discarding a **low-signal, high-variance** direction is a win — the bias you pay is small but the variance you eliminate is huge.

---

## Formal Proof / Solution

### Setup

Write the true signal in the principal component basis. Let $X = UDV^\top$ and define $\theta_j = u_j^\top X\beta = d_j (V^\top \beta)_j$, the projection of the true signal onto the $j$-th principal direction.

The OLS fitted values are

$$\hat{y} = \sum_{j=1}^p u_j (u_j^\top y), \qquad \hat{y}^{\text{PCR}} = \sum_{j=1}^M u_j (u_j^\top y).$$

Since $u_j^\top y = u_j^\top X\beta + u_j^\top \varepsilon = \theta_j + u_j^\top \varepsilon$, each coordinate $u_j^\top y$ is a **noisy observation of $\theta_j$ with noise variance $\sigma^2$**.

---

### Per-Component Bias and Variance

For each $j$, define the scalar estimator $\hat{\theta}_j^{\text{OLS}} = u_j^\top y$ and the contribution to fitted values $\hat{y}_j = u_j \hat{\theta}_j$.

**OLS contribution of component $j$:**

$$\mathbb{E}[\hat{\theta}_j^{\text{OLS}}] = \theta_j \quad \Rightarrow \quad \text{Bias}_j^2 = 0$$

$$\operatorname{Var}(\hat{\theta}_j^{\text{OLS}}) = \sigma^2$$

So in the $j$-th direction, OLS has zero bias and variance $\sigma^2$.

**PCR contribution of component $j$:**

- If $j \leq M$: keep it. Same as OLS: **Bias$^2 = 0$, Variance $= \sigma^2$**.
- If $j > M$: discard it. The estimate is $0$, so:

$$\text{Bias}_j^2 = \theta_j^2, \qquad \text{Variance}_j = 0.$$

---

### Total MSE

$$\text{MSE}(\hat{y}^{\text{PCR}}) = \underbrace{\sigma^2 M}_{\text{variance}} + \underbrace{\sum_{j=M+1}^{p} \theta_j^2}_{\text{bias}^2}$$

$$\text{MSE}(\hat{y}^{\text{OLS}}) = \sigma^2 p + 0.$$

---

### Why Small Singular Values Are Dangerous for OLS Coefficient Estimation

Although OLS fitted values have constant variance $\sigma^2$ per component, the **regression coefficients** tell a different story. The OLS coefficient is

$$\hat{\beta} = V D^{-1} U^\top y \quad \Rightarrow \quad \hat{\beta}_j^{\text{component}} = \frac{u_j^\top y}{d_j} v_j.$$

The variance of this contribution is

$$\operatorname{Var}\!\left(\frac{u_j^\top y}{d_j}\right) = \frac{\sigma^2}{d_j^2}.$$

When $d_j \to 0$ (near-multicollinearity), this variance **blows up**. While OLS fitted values remain stable, the coefficients become wildly unstable — and in prediction on new data (slightly off the training column space), this instability hurts.

---

### The Bias-Variance Tradeoff Is Controlled by $M$

| Component $j$ | PCR Bias$^2$ | PCR Variance |
|---|---|---|
| $j \leq M$ (kept) | $0$ | $\sigma^2$ |
| $j > M$ (dropped) | $\theta_j^2$ | $0$ |

Increasing $M$ decreases bias but increases variance at rate $\sigma^2$ per component. The optimal $M^*$ satisfies:

$$\text{Include component } j \iff \theta_j^2 > \sigma^2,$$

i.e., **include a direction if and only if its signal exceeds the noise level**. This is a signal-to-noise threshold — a beautiful and clean decision rule that makes PCR a form of **empirical Bayes hard thresholding** in the PC basis.

---

### Summary Punchline

OLS pays $\sigma^2$ per direction regardless of whether that direction carries signal. PCR trades a controlled amount of bias (dropping small-signal directions) for a proportional reduction in variance. When many directions have $\theta_j^2 \ll \sigma^2$ — which is common in high dimensions — PCR wins decisively.
