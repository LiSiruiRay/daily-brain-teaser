# Answer: Fisher Information Curvature Identity

## Key Idea / Intuition

The identity comes from differentiating the constraint $\int p_\theta(x)\,dx = 1$ twice with respect to $\theta$. The first derivative gives the well-known fact that the score has mean zero; the second derivative reveals that the variance of the score (Fisher information) equals the negative expected second derivative of the log-likelihood. Intuitively, a sharper (more curved) log-likelihood means the data can pin down $\theta$ more precisely — the peak is narrower, so small changes in $\theta$ cause large changes in probability, meaning the data carries more information.

---

## Formal Proof / Solution

**Step 1: The score has mean zero.**

Start from the normalisation identity:
$$\int p_\theta(x)\,dx = 1.$$

Differentiate both sides with respect to $\theta$:
$$\frac{\partial}{\partial\theta}\int p_\theta(x)\,dx = \int \frac{\partial p_\theta(x)}{\partial\theta}\,dx = 0.$$

Write $\frac{\partial p_\theta}{\partial\theta} = p_\theta \cdot \frac{\partial \log p_\theta}{\partial\theta} = p_\theta \cdot s(\theta)$, so:
$$\mathbb{E}_\theta[s(\theta)] = \int s(\theta)\, p_\theta(x)\,dx = 0. \tag{1}$$

**Step 2: Differentiate the score-mean equation.**

Differentiate (1) again with respect to $\theta$:
$$\frac{\partial}{\partial\theta}\int \frac{\partial \log p_\theta}{\partial\theta}\, p_\theta(x)\,dx = 0.$$

Apply the product rule inside the integral:
$$\int \frac{\partial^2 \log p_\theta}{\partial\theta^2}\, p_\theta\,dx + \int \frac{\partial \log p_\theta}{\partial\theta}\cdot\frac{\partial p_\theta}{\partial\theta}\,dx = 0.$$

The first integral is $\mathbb{E}_\theta\!\left[\frac{\partial^2 \log p_\theta}{\partial\theta^2}\right]$.

For the second integral, substitute $\frac{\partial p_\theta}{\partial\theta} = p_\theta\cdot s(\theta)$:
$$\int \left(\frac{\partial \log p_\theta}{\partial\theta}\right)^2 p_\theta\,dx = \mathbb{E}_\theta[s(\theta)^2] = I(\theta).$$

**Step 3: Combine.**

Putting it together:
$$\mathbb{E}_\theta\!\left[\frac{\partial^2 \log p_\theta}{\partial\theta^2}\right] + I(\theta) = 0,$$

$$\boxed{I(\theta) = -\mathbb{E}_\theta\!\left[\frac{\partial^2 \log p_\theta}{\partial\theta^2}\right].}$$

---

**Intuitive explanation of the curvature interpretation:**

Think of the log-likelihood $\ell(\theta; X) = \log p_\theta(X)$ as a landscape with a peak near the true $\theta$. The **second derivative** measures how sharply the log-likelihood curves downward at the peak:

- If $\ell(\theta)$ is **steeply curved** (large negative second derivative), the peak is narrow: even a small deviation in $\theta$ produces a very different log-probability. The data strongly discriminates between nearby parameter values → **high Fisher information**.
- If $\ell(\theta)$ is **flat** (small second derivative), many values of $\theta$ explain the data almost equally well → the data is uninformative about $\theta$ → **low Fisher information**.

This is precisely what the Cramér–Rao bound captures: $\mathrm{Var}(\hat\theta) \geq 1/I(\theta)$, so high information forces low variance for any unbiased estimator.
