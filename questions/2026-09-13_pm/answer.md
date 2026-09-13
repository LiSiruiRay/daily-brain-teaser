# Answer: The Gaussian That Knows Its Own Variance

## Key Idea / Intuition

The MLE is unbiased but can have large variance. A slightly shrunken estimator — choosing $c < 1$ — trades a little bias for a big reduction in variance, and the net effect is a lower MSE. This is the bias-variance tradeoff made completely explicit in a one-parameter family: the optimal $c^*$ is strictly less than 1, meaning the MLE is **inadmissible** in the MSE sense even for this simple problem.

---

## Formal Proof / Solution

**Setup.** Since $x \sim \mathcal{N}(0, \sigma^2)$, we have $x^2 / \sigma^2 \sim \chi^2_1$, so:

$$\mathbb{E}[x^2] = \sigma^2, \qquad \mathbb{E}[x^4] = 3\sigma^4$$

(using the fact that for $Z \sim \chi^2_1$, $\mathbb{E}[Z^2] = 3$, i.e., $\text{Var}(x^2) = \mathbb{E}[x^4] - (\mathbb{E}[x^2])^2 = 3\sigma^4 - \sigma^4 = 2\sigma^4$).

**Expand MSE.**

$$\text{MSE}(c) = \mathbb{E}[(cx^2 - \sigma^2)^2] = c^2\mathbb{E}[x^4] - 2c\sigma^2\mathbb{E}[x^2] + \sigma^4$$

Substituting:

$$= c^2 \cdot 3\sigma^4 - 2c\sigma^2 \cdot \sigma^2 + \sigma^4 = \sigma^4\left(3c^2 - 2c + 1\right)$$

**Minimize over $c$.**

$$\frac{d}{dc}\left(3c^2 - 2c + 1\right) = 6c - 2 = 0 \implies c^* = \frac{1}{3}$$

**Check MLE.** At $c = 1$:

$$\text{MSE}(1) = \sigma^4(3 - 2 + 1) = 2\sigma^4$$

At $c^* = 1/3$:

$$\text{MSE}(1/3) = \sigma^4\!\left(\frac{3}{9} - \frac{2}{3} + 1\right) = \sigma^4\!\left(\frac{1}{3} - \frac{2}{3} + 1\right) = \frac{2\sigma^4}{3}$$

So the optimal estimator achieves **one-third the MSE** of the MLE!

**Why the direction makes sense.** The MLE $x^2$ is unbiased but has very high variance ($2\sigma^4$). Since $x^2$ has a right-skewed distribution (chi-squared), the typical value of $x^2$ tends to **overestimate** $\sigma^2$ on average in terms of squared loss. Shrinking by $c^* = 1/3$ introduces downward bias but dramatically cuts variance. The bias-variance tradeoff strongly favors shrinkage here.

**Decomposition at $c^* = 1/3$:**
$$\text{Bias}^2 = \left(\frac{1}{3}\sigma^2 - \sigma^2\right)^2 = \frac{4\sigma^4}{9}, \qquad \text{Variance} = c^{*2} \cdot \text{Var}(x^2) = \frac{1}{9} \cdot 2\sigma^4 = \frac{2\sigma^4}{9}$$
$$\text{MSE} = \frac{4\sigma^4}{9} + \frac{2\sigma^4}{9} = \frac{6\sigma^4}{9} = \frac{2\sigma^4}{3} \checkmark$$

The MLE is unbiased but **not** MSE-optimal — a recurring theme in statistics.
