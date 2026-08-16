# Answer: 2026-08-16_am

## Key Idea / Intuition

Minimizing cross-entropy on training data is a maximum likelihood procedure — it finds $\hat{\beta}$ that makes the training labels look as probable as possible. When features are plentiful relative to data points ($p/n$ not negligible), the MLE **overshoots**: it inflates the magnitude of $\hat{\beta}$ to push training probabilities toward 0 and 1, fitting the noise. On new data, these extreme predicted probabilities are systematically wrong — the model is **overconfident**. The fix is elegant: just rescale (divide) the logit by a temperature $T > 1$, which geometrically "squashes" the sigmoid back toward the center.

---

## Formal Proof / Solution

### Part 1: What Happens When $p/n \to c > 0$

**Setup.** In logistic regression, we maximize the log-likelihood:
$$\ell(\beta) = \sum_{i=1}^n \left[ y_i \log \sigma(x_i^\top \beta) + (1-y_i)\log(1 - \sigma(x_i^\top \beta)) \right]$$
where $\sigma(t) = 1/(1+e^{-t})$.

**The classical regime** ($p$ fixed, $n \to \infty$): MLE is consistent, $\hat{\beta} \to \beta^*$.

**The proportional regime** ($p/n \to c \in (0,1)$): A landmark result (Sur & Candès, 2019, building on earlier work) shows that MLE is **not consistent**. Specifically:

- The MLE exists and is finite only when the data are not perfectly separable.
- But even when it exists, $\|\hat{\beta}\|$ is systematically **inflated** relative to $\|\beta^*\|$ by a factor $> 1$ that depends on $c$.
- Intuitively: with $p \approx cn$ free parameters, the optimizer finds directions in $\mathbb{R}^p$ that separate training points better than the truth does.

**Consequence for probabilities.** The predicted probability for a new point $x$ is:
$$\hat{p}(x) = \sigma(x^\top \hat{\beta})$$

Since $\|\hat{\beta}\| > \|\beta^*\|$, the logits $x^\top \hat{\beta}$ are inflated in magnitude, pushing $\hat{p}(x)$ toward 0 or 1 even when the true probability is moderate (say, 0.6 or 0.4). This is **overconfidence**.

**A toy example to see it clearly.** Suppose the true $\beta^* = e_1$ (unit vector), but the MLE returns $\hat{\beta} = 2e_1$. Then:
- True probability at $x = (1, 0, \ldots, 0)$: $\sigma(1) \approx 0.73$
- Predicted probability: $\sigma(2) \approx 0.88$

The model is far more confident than it should be.

---

### Part 2: Training Cross-Entropy Minimization ≠ Calibration

**The clean argument:**

Calibration means: among all examples where the model predicts probability $p$, approximately fraction $p$ should actually be positive. Formally, we want:
$$\mathbb{P}(Y = 1 \mid \hat{p}(X) = p) = p \quad \text{for all } p \in [0,1].$$

Training cross-entropy minimization gives us:
$$\hat{\beta} = \arg\min_\beta - \frac{1}{n}\sum_{i=1}^n \left[ y_i \log \hat{p}(x_i) + (1-y_i)\log(1-\hat{p}(x_i)) \right]$$

This only enforces that predictions match **training labels**, not the **true conditional distribution**. Specifically:

- If the model overfits, it memorizes training labels. A training point with $y_i = 1$ gets $\hat{p}(x_i) \approx 1$ even if the true $P(Y=1 \mid x_i) = 0.7$.
- The **empirical cross-entropy** is minimized, but the **population cross-entropy** (which would ensure calibration) is not.

Formally, perfect calibration requires:
$$\mathbb{E}_{(X,Y)\sim P_{\text{test}}}[-\log \hat{p}(X)^Y (1-\hat{p}(X))^{1-Y}]$$
to be minimized over the **test distribution**, not the training distribution.

Overfitting breaks this: minimizing training loss inflates $\hat{\beta}$, and the resulting $\hat{p}$ is no longer the minimizer of the population cross-entropy.

---

### Part 3 (Bonus): Temperature Scaling

**The fix:** After training, find a scalar $T > 1$ and replace all predicted logits $z = x^\top \hat{\beta}$ with $z/T$:
$$\hat{p}_{\text{calibrated}}(x) = \sigma\!\left(\frac{x^\top \hat{\beta}}{T}\right)$$

$T$ is chosen to minimize cross-entropy on a **held-out validation set**.

**Why it works — geometrically:**

The sigmoid $\sigma(t)$ maps $\mathbb{R} \to (0,1)$. Dividing by $T > 1$ **compresses** the logit, which moves predicted probabilities away from the extremes (0 and 1) toward the center (0.5).

$$\sigma(t/T) \longrightarrow 0.5 \text{ as } T \to \infty, \qquad \sigma(t/T) \to \sigma(t) \text{ as } T \to 1$$

This is the **Platt scaling** idea. It doesn't change the model's **ranking** of predictions (monotone transformation), only their **magnitude** — correcting the systematic overconfidence from inflated $\|\hat{\beta}\|$ without retraining.

**Why $T > 1$ (not $T < 1$)?** Modern neural networks and logistic regression in high dimensions are overconfident (not underconfident), so we need to flatten the distribution, not sharpen it. $T > 1$ does exactly this.

---

## Summary Table

| Regime | $\hat{\beta}$ behavior | Calibration |
|---|---|---|
| $p \ll n$ | Consistent | Good |
| $p/n \to c > 0$ | Inflated magnitude | Overconfident |
| $p > n$, separable | $\|\hat{\beta}\| \to \infty$ | Completely broken |
| After temperature scaling | Logits divided by $T > 1$ | Restored |

Written to: [question file](./questions/2026-06-17_am.md)
