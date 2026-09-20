# Answer: 2026-09-20_am

## Key Idea / Intuition

A "flat" prior is not a coordinate-free notion: flatness in one parametrization becomes a non-flat (informative) prior in another. The Jeffreys prior is the unique (up to normalization) prior that is **invariant under smooth reparametrization**, because it is built from the Fisher information, which transforms contravariantly in exactly the right way to cancel the Jacobian. Think of it as the "natural volume form" on the parameter space induced by the statistical model.

---

## Formal Proof / Solution

### Part (a): Uniform on $\theta$ ≠ Uniform on $\phi$

Let $\phi = g(\theta) = \sin^{-1}(\sqrt{\theta})$, so $\phi \in [0, \pi/2]$.

If $\theta \sim \text{Uniform}[0,1]$, then the density of $\phi$ is obtained by the change of variables:

$$\pi_\phi(\phi) = \pi_\theta(\theta) \left|\frac{d\theta}{d\phi}\right|.$$

We compute: $\theta = \sin^2(\phi)$, so $\frac{d\theta}{d\phi} = 2\sin(\phi)\cos(\phi) = \sin(2\phi)$.

Thus:

$$\pi_\phi(\phi) = 1 \cdot \sin(2\phi) = \sin(2\phi), \quad \phi \in [0, \pi/2].$$

This is **not uniform** on $\phi$ — it peaks at $\phi = \pi/4$ (i.e., $\theta = 1/2$) and vanishes at the endpoints. So the two priors are genuinely different. $\square$

---

### Part (b): Jeffreys Prior for the Binomial is Beta(1/2, 1/2)

For $X \sim \text{Binomial}(n, \theta)$, the log-likelihood is:

$$\ell(\theta) = X \log\theta + (n-X)\log(1-\theta) + \text{const.}$$

The Fisher information is:

$$I(\theta) = -\mathbb{E}\left[\frac{d^2\ell}{d\theta^2}\right].$$

We compute:

$$\frac{d\ell}{d\theta} = \frac{X}{\theta} - \frac{n-X}{1-\theta}, \qquad \frac{d^2\ell}{d\theta^2} = -\frac{X}{\theta^2} - \frac{n-X}{(1-\theta)^2}.$$

Taking expectation with $\mathbb{E}[X] = n\theta$:

$$I(\theta) = \frac{n\theta}{\theta^2} + \frac{n(1-\theta)}{(1-\theta)^2} = \frac{n}{\theta} + \frac{n}{1-\theta} = \frac{n}{\theta(1-\theta)}.$$

Therefore the Jeffreys prior is:

$$\pi_J(\theta) \propto \sqrt{I(\theta)} = \sqrt{\frac{n}{\theta(1-\theta)}} \propto \theta^{-1/2}(1-\theta)^{-1/2}.$$

This is exactly the $\text{Beta}(1/2, 1/2)$ density (up to normalization). $\square$

**Sanity check:** Beta$(1/2, 1/2)$ is the arcsine distribution, which concentrates near $0$ and $1$ — reflecting genuine uncertainty about extreme values, unlike the flat prior which assigns equal weight everywhere.

---

### Part (c): Reparametrization Invariance of the Jeffreys Prior

Let $\phi = g(\theta)$ be a smooth bijection. The Fisher information transforms as:

$$I_\phi(\phi) = I_\theta(\theta) \left(\frac{d\theta}{d\phi}\right)^2$$

because the score function $\frac{d\ell}{d\phi} = \frac{d\ell}{d\theta} \cdot \frac{d\theta}{d\phi}$, so its variance picks up the square of the Jacobian.

The Jeffreys prior on $\phi$ induced from $\pi_J(\theta)$ via change of variables is:

$$\tilde{\pi}(\phi) = \pi_J(\theta(\phi)) \left|\frac{d\theta}{d\phi}\right| \propto \sqrt{I_\theta(\theta(\phi))} \cdot \left|\frac{d\theta}{d\phi}\right|.$$

But the Jeffreys prior **directly defined** in the $\phi$ parametrization is:

$$\pi_J^{(\phi)}(\phi) \propto \sqrt{I_\phi(\phi)} = \sqrt{I_\theta(\theta(\phi)) \cdot \left(\frac{d\theta}{d\phi}\right)^2} = \sqrt{I_\theta(\theta(\phi))} \cdot \left|\frac{d\theta}{d\phi}\right|.$$

These are **identical**. $\square$

The Jacobian from the change-of-variables formula exactly cancels the Jacobian arising in the Fisher information transformation — a perfect algebraic conspiracy that makes the Jeffreys prior the canonical "non-informative" prior.

---

**Summary table:**

| Property | Flat Prior | Jeffreys Prior |
|---|---|---|
| Reparametrization invariant | ✗ | ✓ |
| Binomial model | $\text{Beta}(1,1)$ | $\text{Beta}(1/2,1/2)$ |
| Interpretation | Uniform in $\theta$ | Natural volume form |

Written to: [questions/2026-08-17_am.md](questions/2026-08-17_am.md) | Answer in: [questions/2026-08-17_am_answer.md](questions/2026-08-17_am_answer.md)
