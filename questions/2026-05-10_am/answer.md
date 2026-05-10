# Answer: Optimism of Training Error

## Key Idea / Intuition

Training error is optimistic — it underestimates true prediction error — because the model was *fit to the same data it is evaluated on*. The key insight is that the bias comes entirely from the **covariance** between predictions $\hat{y}_i$ and the training responses $y_i$: when your model has "seen" $y_i$, it adjusts $\hat{y}_i$ toward it, making the training loss look artificially small. The optimism measures exactly how much the model overfits, in units of covariance.

---

## Formal Proof / Solution

**Setup.** Assume an additive noise model:
$$y_i = f(x_i) + \varepsilon_i, \quad \varepsilon_i \sim (0, \sigma^2_\varepsilon)$$
and $Y_i^0 = f(x_i) + \varepsilon_i^0$ is an independent fresh observation at $x_i$ (same distribution as $y_i$, but independent of the training set).

**Step 1: Expand $\text{Err}_{\text{in}}$.**

$$\mathbb{E}\left[\text{Err}_{\text{in}}\right] = \frac{1}{N}\sum_{i=1}^N \mathbb{E}\left[(Y_i^0 - \hat{y}_i)^2\right]$$

Since $Y_i^0 \perp \hat{y}_i$ (fresh response, independent of training):
$$\mathbb{E}\left[(Y_i^0 - \hat{y}_i)^2\right] = \mathbb{E}\left[(Y_i^0 - f(x_i))^2\right] + \mathbb{E}\left[(f(x_i) - \hat{y}_i)^2\right]$$
$$= \sigma^2_\varepsilon + \mathbb{E}\left[(f(x_i) - \hat{y}_i)^2\right]$$

**Step 2: Expand $\overline{\text{err}}$.**

$$\mathbb{E}\left[\overline{\text{err}}\right] = \frac{1}{N}\sum_{i=1}^N \mathbb{E}\left[(y_i - \hat{y}_i)^2\right]$$

Write $y_i = f(x_i) + \varepsilon_i$ and add/subtract $f(x_i)$:
$$y_i - \hat{y}_i = \varepsilon_i - (\hat{y}_i - f(x_i))$$

So:
$$\mathbb{E}\left[(y_i - \hat{y}_i)^2\right] = \mathbb{E}[\varepsilon_i^2] - 2\mathbb{E}[\varepsilon_i(\hat{y}_i - f(x_i))] + \mathbb{E}[(\hat{y}_i - f(x_i))^2]$$
$$= \sigma^2_\varepsilon - 2\mathbb{E}[\varepsilon_i(\hat{y}_i - f(x_i))] + \mathbb{E}[(\hat{y}_i - f(x_i))^2]$$

**Step 3: Compute the optimism.**

$$\mathbb{E}\left[\text{Err}_{\text{in}} - \overline{\text{err}}\right] = \frac{1}{N}\sum_{i=1}^N \left(2\mathbb{E}[\varepsilon_i(\hat{y}_i - f(x_i))]\right)$$

$$= \frac{2}{N}\sum_{i=1}^N \mathbb{E}[\varepsilon_i \hat{y}_i] - \mathbb{E}[\varepsilon_i f(x_i)]$$

Since $f(x_i)$ is deterministic and $\mathbb{E}[\varepsilon_i] = 0$:
$$\mathbb{E}[\varepsilon_i f(x_i)] = f(x_i)\mathbb{E}[\varepsilon_i] = 0$$

So:
$$\mathbb{E}\left[\text{Err}_{\text{in}} - \overline{\text{err}}\right] = \frac{2}{N}\sum_{i=1}^N \mathbb{E}[\varepsilon_i \hat{y}_i]$$

**Step 4: Recognize the covariance.**

$$\text{Cov}(\hat{y}_i, y_i) = \text{Cov}(\hat{y}_i, f(x_i) + \varepsilon_i) = \text{Cov}(\hat{y}_i, \varepsilon_i) = \mathbb{E}[\hat{y}_i \varepsilon_i] - \mathbb{E}[\hat{y}_i]\mathbb{E}[\varepsilon_i]$$

Since $\mathbb{E}[\varepsilon_i] = 0$:
$$\text{Cov}(\hat{y}_i, y_i) = \mathbb{E}[\hat{y}_i \varepsilon_i]$$

Therefore:
$$\boxed{\mathbb{E}\left[\text{Err}_{\text{in}} - \overline{\text{err}}\right] = \frac{2}{N}\sum_{i=1}^N \text{Cov}(\hat{y}_i, y_i)}$$

**Conceptual meaning.** 
- For a **linear smoother** $\hat{y} = Sy$, we get $\sum_i \text{Cov}(\hat{y}_i, y_i) = \text{trace}(S)\sigma^2_\varepsilon$, which is why $\text{trace}(S)$ counts the *effective degrees of freedom*.
- For **OLS with $p$ parameters**, $\text{trace}(S) = p$, so optimism $= \frac{2p\sigma^2}{N}$, exactly the penalty in Mallows' $C_p$.
- The more the model adapts to training noise (high covariance), the more optimistic the training error is, and the larger the gap to test error.
