# Answer: Precision Matrix and Conditional Independence

## Key Idea / Intuition

For a Gaussian, everything is determined by means and covariances — and conditional distributions are still Gaussian. The key insight is that **conditioning on other variables corresponds to a partial regression**, and the precision matrix entry $\theta_{ij}$ is (up to scaling) precisely the **partial correlation** between $X_i$ and $X_j$ after removing the linear influence of all other variables. When this partial correlation is zero, the two variables are conditionally independent — because for Gaussians, zero correlation equals independence.

---

## Formal Proof / Solution

**Step 1: Partition and the conditional distribution.**

Without loss of generality, consider variables $X_1, X_2$, and $X_{\text{rest}} = (X_3, \ldots, X_p)$. Write the joint density as

$$f(x) \propto \exp\!\left(-\tfrac{1}{2} x^T \Theta x\right).$$

We want to check whether $X_1 \perp\!\!\!\perp X_2 \mid X_{\text{rest}}$.

**Step 2: Factor the exponent.**

The conditional density of $(X_1, X_2)$ given $X_{\text{rest}}$ is proportional to $f(x)$ viewed as a function of $(x_1, x_2)$ with $x_{\text{rest}}$ fixed. The cross-term between $x_1$ and $x_2$ in the exponent is

$$x^T \Theta x \supset 2\theta_{12} x_1 x_2.$$

All other terms involving $x_1$ or $x_2$ factor into functions of $x_1$ alone or $x_2$ alone (after completing the square in $x_{\text{rest}}$).

So the conditional density factors as:

$$f(x_1, x_2 \mid x_{\text{rest}}) \propto \exp\!\left(-\theta_{12} x_1 x_2 - \tfrac{1}{2}\theta_{11}x_1^2 - \tfrac{1}{2}\theta_{22}x_2^2 + \text{(linear terms in } x_1, x_2\text{)}\right).$$

**Step 3: Conditional independence iff no cross term.**

The conditional density of $(X_1, X_2) \mid X_{\text{rest}}$ factors into $g(x_1, x_{\text{rest}}) \cdot h(x_2, x_{\text{rest}})$ **if and only if** there is no $x_1 x_2$ cross-term in the exponent, i.e.,

$$\theta_{12} = 0.$$

When $\theta_{12} = 0$, the joint conditional density factors, so $X_1 \perp\!\!\!\perp X_2 \mid X_{\text{rest}}$.

**Step 4: The precision entry is the partial correlation (up to scaling).**

One can make this even more concrete. By the formula for the inverse of a partitioned matrix, the $(1,2)$ entry of $\Theta = \Sigma^{-1}$ satisfies

$$\theta_{12} = -\frac{\text{Cov}(X_1, X_2 \mid X_{\text{rest}})}{\text{Var}(X_1 \mid X_{\text{rest}}) \cdot \text{Var}(X_2 \mid X_{\text{rest}})},$$

which is (up to sign and scaling) the **partial correlation** $\rho_{12 \cdot \text{rest}}$. So:

$$\theta_{12} = 0 \iff \rho_{12 \cdot \text{rest}} = 0 \iff X_1 \perp\!\!\!\perp X_2 \mid X_{\text{rest}} \quad \text{(Gaussian case)}.$$

**Summary:**

$$\boxed{\theta_{ij} = 0 \iff X_i \perp\!\!\!\perp X_j \mid X_{\text{rest}}}$$

This is why the **sparsity pattern of $\Theta$** is the Gaussian graphical model: an edge is absent between $i$ and $j$ exactly when $\theta_{ij} = 0$, i.e., when $X_i$ and $X_j$ are conditionally independent. Estimating $\Theta$ with an $\ell_1$ penalty (graphical lasso) thus directly recovers the graph structure by driving small $\theta_{ij}$ entries to zero.
