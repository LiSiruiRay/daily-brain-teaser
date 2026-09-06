# Answer: The Posterior That Forgets the Prior

## Key Idea / Intuition

With a Gaussian likelihood, the posterior mean is a weighted average of the prior mean and the sample mean $\bar X_n$. As $n$ grows, the data swamps the prior — the weight on the prior shrinks to zero, and both posteriors converge to $\bar X_n$. The deeper insight is that this is not a special Gaussian feature: any two **fixed** proper priors get washed out by sufficient data, as long as the likelihood satisfies mild regularity (Bayesian consistency). The prior only matters in finite samples; asymptotically, the likelihood rules.

---

## Formal Proof / Solution

### Step 1: Gaussian case — explicit posterior means

For the Gaussian–Gaussian conjugate model $X_i \mid \theta \sim \mathcal{N}(\theta, 1)$ with prior $\theta \sim \mathcal{N}(0, \tau^2)$, the posterior is

$$\theta \mid X_1,\ldots,X_n \;\sim\; \mathcal{N}\!\left(\hat\theta_n,\, v_n\right)$$

where the posterior mean and variance are

$$\hat\theta_n = \frac{\tau^2}{\tau^2 + 1/n}\,\bar X_n + \frac{1/n}{\tau^2 + 1/n}\cdot 0 = \frac{n\tau^2}{n\tau^2 + 1}\,\bar X_n, \qquad v_n = \frac{\tau^2/n}{\tau^2 + 1/n}.$$

So for priors A and B:

$$\hat\theta_A = \frac{n \cdot 1}{n \cdot 1 + 1}\,\bar X_n = \frac{n}{n+1}\,\bar X_n, \qquad \hat\theta_B = \frac{n \cdot 1000}{n \cdot 1000 + 1}\,\bar X_n = \frac{1000n}{1000n+1}\,\bar X_n.$$

Their difference is

$$\hat\theta_A - \hat\theta_B = \left(\frac{n}{n+1} - \frac{1000n}{1000n+1}\right)\bar X_n.$$

Compute the coefficient:

$$\frac{n}{n+1} - \frac{1000n}{1000n+1} = n\left(\frac{1}{n+1} - \frac{1000}{1000n+1}\right) = n \cdot \frac{1000n+1 - 1000(n+1)}{(n+1)(1000n+1)} = n\cdot\frac{-999}{(n+1)(1000n+1)}.$$

So

$$|\hat\theta_A - \hat\theta_B| = \frac{999\,n}{(n+1)(1000n+1)}\,|\bar X_n| \;\sim\; \frac{999}{1000\,n}\,|\bar X_n| \;\to\; 0$$

since $\bar X_n \to \theta$ (a.s.) by the strong law. **Both posteriors converge to the true $\theta$, and their difference vanishes at rate $1/n$.**

The key structure: the weight on the prior mean is $\tfrac{1}{n\tau^2 + 1} \to 0$, regardless of $\tau^2$.

---

### Step 2: General proper priors — the Bernstein–von Mises heuristic

For any two fixed proper priors $\pi_A, \pi_B$ with densities, the posterior under $n$ i.i.d. observations satisfies the **Bernstein–von Mises theorem**: under regularity conditions (the true $\theta_0$ is in the support of both priors, the likelihood is smooth and identifiable), both posteriors converge to the same limiting distribution

$$\text{Posterior}_n(\theta) \;\xrightarrow{d}\; \mathcal{N}\!\left(\hat\theta_{\text{MLE}},\; \frac{1}{n\,I(\theta_0)}\right)$$

where $I(\theta_0)$ is the Fisher information. In particular, both posterior means converge to the MLE $\hat\theta_{\text{MLE}}$, which converges to $\theta_0$. The prior shape is completely irrelevant asymptotically.

**Intuition for why:** The log-posterior is
$$\log p(\theta \mid \mathbf{X}) = \log \pi(\theta) + \sum_{i=1}^n \log p(X_i \mid \theta) + \text{const}.$$
The prior contributes $O(1)$ terms; the likelihood contributes $O(n)$ terms. For large $n$, the likelihood dominates and peaks sharply at the MLE — the prior is a negligible additive constant relative to the towering log-likelihood peak.

---

### Step 3: When does the prior *not* get washed out?

The prior persists when:
1. **The prior is improper** and conflicts with the likelihood (posterior may not even be proper).
2. **The model is non-identified**: multiple $\theta$ values explain the data equally well — the likelihood never separates them, so the prior ratio persists forever.
3. **The number of parameters grows with $n$** (e.g., nonparametric models): there are always new directions the data hasn't "seen."
4. **The prior assigns zero mass to a region containing the truth**: the posterior is trapped away from $\theta_0$ (failure of support condition).

---

### Summary

| Situation | Prior washed out? |
|---|---|
| Fixed proper prior, regular model, $n\to\infty$ | ✅ Yes — Bernstein–von Mises |
| Non-identified model | ❌ No |
| Prior puts zero mass near truth | ❌ No |
| Gaussian conjugate, any $\tau^2 > 0$ | ✅ Yes, at rate $1/n$ |

The beautiful takeaway: **Bayesian and frequentist inference agree in the large-sample limit** — the prior is epistemically relevant in finite samples, but asymptotically the data speaks for itself.
