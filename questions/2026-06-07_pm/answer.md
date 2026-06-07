# Answer: Optimism of Training Error and the LOO Shortcut

## Key Idea / Intuition

Training error is optimistic because the model was *tuned on* the training data — it gets to "see the answers" before being tested. The gap between training and test error is precisely the **in-sample optimism**, which grows with model complexity (degrees of freedom used). When $p = n$, OLS interpolates perfectly and training error collapses to zero — a complete breakdown of it as a quality measure. LOO-CV corrects for this by simulating a held-out test, and the hat-matrix shortcut works because removing one point and refitting is equivalent (for linear smoothers) to rescaling the residual by how much that point influenced its own fitted value.

---

## Formal Proof / Solution

### Part (a): Training error is optimistically biased

For a linear model with $p$ parameters fit by OLS, the fitted values are $\hat{y} = Hy$ where $H = X(X^TX)^{-1}X^T$ has trace $\text{tr}(H) = p$.

The **optimism** of training error is defined as:
$$\text{op} = \text{Err} - \widehat{\text{err}}_{\text{train}}$$

A classical result (ESL §7.4) gives:
$$\mathbb{E}[\text{op}] = \frac{2}{n} \sum_{i=1}^n \text{Cov}(\hat{y}_i, y_i)$$

For OLS with noise variance $\sigma^2$:
$$\text{Cov}(\hat{y}_i, y_i) = \sigma^2 H_{ii}$$

so:
$$\mathbb{E}[\text{op}] = \frac{2\sigma^2}{n} \text{tr}(H) = \frac{2\sigma^2 p}{n}$$

Therefore:
$$\boxed{\mathbb{E}[\text{Err}] = \mathbb{E}[\widehat{\text{err}}_{\text{train}}] + \frac{2\sigma^2 p}{n}}$$

The gap grows with $p$ (complexity) and shrinks with $n$ (more data). This is exactly the correction used by **Mallows' $C_p$** and **AIC**.

---

### Part (b): Interpolation when $p = n$

When $p = n$ and $X$ is invertible, OLS fits the data exactly:
$$\hat{y} = Hy = Iy = y \quad \Longrightarrow \quad \widehat{\text{err}}_{\text{train}} = 0$$

Meanwhile, the true test error is:
$$\mathbb{E}[\text{Err}] = 0 + \frac{2\sigma^2 \cdot n}{n} = 2\sigma^2$$

(or more precisely, grows with the noise level). Training error is **maximally misleading**: it says the model is perfect, while the actual generalization error can be arbitrarily bad. This makes training error useless for model selection in overparameterized regimes — exactly the regime of modern neural networks.

---

### Part (c): The LOO shortcut and the meaning of $H_{ii}$

**What is $H_{ii}$?** The diagonal entry $H_{ii} = x_i^T(X^TX)^{-1}x_i$ measures the **leverage** of point $i$ — how much point $i$ influences its own fitted value. High leverage means: "if I move $y_i$, my prediction $\hat{y}_i$ moves a lot."

**The LOO shortcut.** When you remove point $i$ and refit, the new prediction at $x_i$ is:
$$\hat{y}_i^{(-i)} = \hat{y}_i - H_{ii}(y_i - \hat{y}_i) \cdot \frac{1}{1 - H_{ii}} \cdot (1-H_{ii})$$

More precisely, the Sherman-Morrison-Woodbury identity gives:
$$y_i - \hat{y}_i^{(-i)} = \frac{y_i - \hat{y}_i}{1 - H_{ii}}$$

**Intuition for the correction:** The residual $y_i - \hat{y}_i$ when point $i$ is *included* is artificially small — the model pulled $\hat{y}_i$ toward $y_i$ by a fraction $H_{ii}$. Dividing by $(1-H_{ii})$ **inflates** the residual back to what it would have been if point $i$ hadn't been used in fitting. 

- If $H_{ii} \approx 0$: point $i$ has little influence; residual is already honest.  
- If $H_{ii} \approx 1$: the model fits point $i$ almost perfectly regardless of $y_i$; the correction is huge, reflecting that $\hat{y}_i^{(-i)}$ would be very different from $y_i$.

This is why the LOO-CV formula:
$$\text{CV}_{(n)} = \frac{1}{n}\sum_{i=1}^n \left(\frac{y_i - \hat{y}_i}{1 - H_{ii}}\right)^2$$

is computable from **a single fit** — no refitting required. It is one of the most elegant computational shortcuts in statistics.
