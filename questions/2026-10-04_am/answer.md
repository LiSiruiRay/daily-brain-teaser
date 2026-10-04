# Answer: The EM Algorithm That Overshoots: Why Hard Assignment Fails

## Key Idea / Intuition

Soft EM genuinely maximizes the observed-data log-likelihood by carefully averaging over all possible hidden-variable assignments, weighted by their posterior probability. Hard assignment instead maximizes a **lower bound** called the **complete-data log-likelihood with the most probable assignment** — effectively it optimizes a different, cruder objective that ignores the uncertainty in cluster membership. Because it commits to one discrete assignment and never hedges, it is equivalent to K-means (when variances are equal and isotropic), which minimizes within-cluster sum of squares, not the true log-likelihood.

---

## Formal Proof / Solution

### Setup

Let $\mathbf{x} = \{x_1,\ldots,x_n\}$ be observed data, and $\mathbf{z} = \{z_1,\ldots,z_n\}$ latent component indicators ($z_i \in \{1,2\}$). The observed log-likelihood is:

$$\ell(\theta) = \sum_{i=1}^n \log \sum_{k=1}^2 \pi_k \, \mathcal{N}(x_i; \mu_k, \sigma^2)$$

---

### What Soft EM Maximizes

The EM algorithm introduces a variational distribution $q(z_i)$ over latent variables and maximizes the **Evidence Lower Bound (ELBO)**:

$$\mathcal{L}(q,\theta) = \sum_i \sum_k q(z_i=k)\log\frac{\pi_k\,\mathcal{N}(x_i;\mu_k,\sigma^2)}{q(z_i=k)}$$

At the E-step, $q$ is set to the exact posterior:

$$q^\star(z_i=k) = \gamma_{ik} = \frac{\pi_k\,\mathcal{N}(x_i;\mu_k,\sigma^2)}{\sum_{j}\pi_j\,\mathcal{N}(x_i;\mu_j,\sigma^2)}$$

This choice makes the ELBO **tight**: $\mathcal{L}(q^\star,\theta) = \ell(\theta)$. So the M-step actually increases the true log-likelihood.

---

### What Hard Assignment Maximizes

In hard assignment, we replace the soft responsibilities $\gamma_{ik}$ with:

$$\hat{z}_i = \arg\max_k \gamma_{ik}, \qquad q^{\text{hard}}(z_i=k) = \mathbf{1}[k=\hat{z}_i]$$

Now the ELBO becomes:

$$\mathcal{L}(q^{\text{hard}},\theta) = \sum_i \log \pi_{\hat{z}_i} + \sum_i \log \mathcal{N}(x_i;\mu_{\hat{z}_i},\sigma^2)$$

This is exactly the **complete-data log-likelihood** under the hard assignment — not the observed log-likelihood. The gap is:

$$\ell(\theta) - \mathcal{L}(q^{\text{hard}},\theta) = \underbrace{\sum_i \text{KL}(q^{\text{hard}}_{i} \,\|\, p(z_i|x_i,\theta))}_{\geq\, 0}$$

Hard assignment inflates this KL term because it concentrates all mass on one component, ignoring uncertainty.

---

### The K-means Connection

When $\sigma^2$ is fixed and equal, maximizing the complete-data log-likelihood reduces to:

$$\max_{\mu_1,\mu_2,\hat{z}} \sum_i \log \mathcal{N}(x_i;\mu_{\hat{z}_i},\sigma^2) = -\frac{1}{2\sigma^2}\sum_i (x_i - \mu_{\hat{z}_i})^2 + \text{const}$$

This is precisely **minimizing within-cluster sum of squares** — the K-means objective. So hard-assignment EM is K-means.

---

### Why Hard Assignment Is Generally Worse

| Property | Soft EM | Hard EM (K-means) |
|---|---|---|
| Objective | True log-likelihood $\ell(\theta)$ | Complete-data log-likelihood |
| KL gap at E-step | Zero (tight bound) | $> 0$ (inflated by assignment uncertainty) |
| Handles overlap | Yes, via soft responsibilities | No, forces crisp boundaries |
| Sensitive to initialization | Less | More |

**Summary:** Hard assignment optimizes a lower bound of the log-likelihood, not the log-likelihood itself. The tightness gap is the KL divergence between the hard distribution and the true posterior, which is nonzero whenever clusters overlap. Soft EM closes this gap exactly at each E-step, guaranteeing monotone increase of the true log-likelihood.
