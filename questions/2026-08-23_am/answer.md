# Answer: EM Algorithm's Hidden Monotonicity

## Key Idea / Intuition

The observed-data likelihood $p(X \mid \theta)$ is obtained by **marginalizing out** the latent variables $Z$. The EM algorithm never directly maximizes $\ell(\theta)$ — instead it maximizes a **lower bound** on $\ell(\theta)$ that is tight at $\theta^{\text{old}}$. This lower bound is constructed using **Jensen's inequality** applied to the concave $\log$ function. Because the M-step raises (or maintains) the lower bound, and the bound was tight at $\theta^{\text{old}}$, the actual likelihood must go up.

---

## Formal Proof / Solution

### Step 1: Decompose the observed log-likelihood

By Bayes' theorem, for any distribution $q(Z)$ over the latent variables:

$$\log p(X \mid \theta) = \log \frac{p(X, Z \mid \theta)}{p(Z \mid X, \theta)}.$$

Take expectation under $q(Z) = p(Z \mid X, \theta^{\text{old}})$ on both sides. The left side doesn't depend on $Z$, so:

$$\ell(\theta) = \mathbb{E}_{Z \mid X, \theta^{\text{old}}}\left[\log \frac{p(X, Z \mid \theta)}{p(Z \mid X, \theta)}\right].$$

Write this as:

$$\ell(\theta) = \underbrace{\mathbb{E}_{Z \mid X, \theta^{\text{old}}}[\log p(X, Z \mid \theta)]}_{Q(\theta,\, \theta^{\text{old}})} - \underbrace{\mathbb{E}_{Z \mid X, \theta^{\text{old}}}[\log p(Z \mid X, \theta)]}_{H(\theta,\, \theta^{\text{old}})}.$$

### Step 2: Bound the $H$ term using Jensen

Consider the change in $H$ when moving from $\theta^{\text{old}}$ to $\theta^{\text{new}}$:

$$H(\theta^{\text{new}}, \theta^{\text{old}}) - H(\theta^{\text{old}}, \theta^{\text{old}}) = \mathbb{E}_{Z \mid X, \theta^{\text{old}}}\left[\log \frac{p(Z \mid X, \theta^{\text{new}})}{p(Z \mid X, \theta^{\text{old}})}\right].$$

By **Jensen's inequality** applied to the concave $\log$:

$$\mathbb{E}\left[\log \frac{p(Z \mid X, \theta^{\text{new}})}{p(Z \mid X, \theta^{\text{old}})}\right] \leq \log \mathbb{E}\left[\frac{p(Z \mid X, \theta^{\text{new}})}{p(Z \mid X, \theta^{\text{old}})}\right] = \log \int \frac{p(Z \mid X, \theta^{\text{new}})}{p(Z \mid X, \theta^{\text{old}})} p(Z \mid X, \theta^{\text{old}})\, dZ = \log 1 = 0.$$

This is precisely the statement that **KL divergence is non-negative**:

$$\text{KL}\!\left(p(Z \mid X, \theta^{\text{old}}) \;\|\; p(Z \mid X, \theta^{\text{new}})\right) \geq 0.$$

So: $H(\theta^{\text{new}}, \theta^{\text{old}}) \leq H(\theta^{\text{old}}, \theta^{\text{old}})$.

### Step 3: Combine

$$\ell(\theta^{\text{new}}) - \ell(\theta^{\text{old}}) = \underbrace{\bigl[Q(\theta^{\text{new}}, \theta^{\text{old}}) - Q(\theta^{\text{old}}, \theta^{\text{old}})\bigr]}_{\geq\, 0 \text{ (M-step maximizes } Q)} - \underbrace{\bigl[H(\theta^{\text{new}}, \theta^{\text{old}}) - H(\theta^{\text{old}}, \theta^{\text{old}})\bigr]}_{\leq\, 0 \text{ (KL ≥ 0)}} \geq 0.$$

Both terms work in our favour: the M-step ensures $Q$ goes up, and Jensen/KL ensures $H$ goes down (or stays).

### Summary of the beautiful structure

| Term | Direction | Reason |
|------|-----------|--------|
| $Q(\theta^{\text{new}}) - Q(\theta^{\text{old}})$ | $\geq 0$ | M-step definition |
| $H(\theta^{\text{new}}) - H(\theta^{\text{old}})$ | $\leq 0$ | Jensen / KL divergence $\geq 0$ |

Hence $\ell(\theta^{\text{new}}) \geq \ell(\theta^{\text{old}})$. $\blacksquare$

The deeper message: EM works by maximizing a **variational lower bound** (often called the ELBO). The KL non-negativity is precisely what keeps the bound valid, and Jensen is the engine behind KL non-negativity.
