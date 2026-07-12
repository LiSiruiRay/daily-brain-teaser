# Answer: Precision Matrix and Partial Correlations

## Key Idea / Intuition

In a Gaussian, all the action of conditional distributions is controlled by **partial correlations** — correlations after "regressing out" the effect of other variables. The precision matrix $\Theta = \Sigma^{-1}$ encodes exactly these residual relationships: $\Theta_{ij}$ measures the direct linear connection between $X_i$ and $X_j$ after removing all indirect paths through other variables. Zero covariance only says $X_i$ and $X_j$ are marginally uncorrelated — but conditioning on other variables can *create* dependence (Berkson's paradox). Zero in $\Theta$ is the right notion because the Gaussian density factors precisely when the off-diagonal precision entry vanishes.

---

## Formal Proof / Solution

### Warm-up: Why $\Sigma_{ij} = 0$ is not enough

Consider $X_1, X_2 \overset{\text{iid}}{\sim} N(0,1)$ and $X_3 = X_1 + X_2$. Then $\text{Cov}(X_1, X_2) = 0$, so marginally they are independent. But given $X_3$, knowing $X_1$ tells you exactly $X_2 = X_3 - X_1$ — they are perfectly conditionally dependent. Conditioning can introduce dependence where none existed marginally (Berkson's paradox / collider effect).

---

### The Gaussian Conditional Distribution

Partition $X = (X_i, X_j, X_{\text{rest}})$ and consider the joint Gaussian. For the bivariate case, it suffices to look at $(X_i, X_j) \mid X_{\text{rest}}$.

The conditional distribution of $(X_i, X_j) \mid X_{\text{rest}}$ is Gaussian with **partial covariance matrix**:

$$\Sigma_{ij \mid \text{rest}} = \Sigma_{aa} - \Sigma_{ab}\Sigma_{bb}^{-1}\Sigma_{ba}$$

where $a = \{i,j\}$ and $b = \text{rest}$. This is the Schur complement.

**Key algebraic fact:** By the block matrix inversion formula,

$$(\Sigma_{aa} - \Sigma_{ab}\Sigma_{bb}^{-1}\Sigma_{ba})^{-1} = \Theta_{aa}$$

where $\Theta_{aa}$ is the $2\times 2$ submatrix of $\Theta = \Sigma^{-1}$ corresponding to indices $\{i,j\}$.

So the **conditional precision** of $(X_i, X_j) \mid X_{\text{rest}}$ is exactly $\Theta_{aa} = \begin{pmatrix} \Theta_{ii} & \Theta_{ij} \\ \Theta_{ji} & \Theta_{jj} \end{pmatrix}$.

---

### Conditional Independence ↔ $\Theta_{ij} = 0$

For jointly Gaussian variables, conditional independence $X_i \perp X_j \mid X_{\text{rest}}$ is equivalent to:

$$\text{Cov}(X_i, X_j \mid X_{\text{rest}}) = 0$$

i.e., the off-diagonal entry of the conditional covariance $\Sigma_{ij\mid\text{rest}} = 0$.

The conditional covariance matrix is $\Theta_{aa}^{-1}$. For a $2\times 2$ matrix:

$$\Theta_{aa}^{-1} = \frac{1}{\Theta_{ii}\Theta_{jj} - \Theta_{ij}^2} \begin{pmatrix} \Theta_{jj} & -\Theta_{ij} \\ -\Theta_{ij} & \Theta_{ii} \end{pmatrix}$$

The off-diagonal entry of $\Theta_{aa}^{-1}$ is $\propto -\Theta_{ij}$.

Therefore:

$$\text{Cov}(X_i, X_j \mid X_{\text{rest}}) = 0 \iff \Theta_{ij} = 0$$

---

### The Density Factorization Perspective

The multivariate Gaussian log-density is:

$$\log p(x) = -\frac{1}{2} x^T \Theta\, x + \text{linear terms} + \text{const}$$

The quadratic form expands as:

$$x^T \Theta\, x = \sum_{k,l} \Theta_{kl}\, x_k x_l$$

The cross-term between $x_i$ and $x_j$ is $2\Theta_{ij} x_i x_j$. If $\Theta_{ij} = 0$, this cross term vanishes, so the density **factors** in $(x_i, x_j)$ given the rest — which is precisely conditional independence.

---

### The Partial Correlation Formula

The **partial correlation** between $X_i$ and $X_j$ given the rest is:

$$\rho_{ij \mid \text{rest}} = -\frac{\Theta_{ij}}{\sqrt{\Theta_{ii}\Theta_{jj}}}$$

(the minus sign comes from the inverse formula above). So not only does $\Theta_{ij} = 0$ encode conditional independence — the magnitude of $\Theta_{ij}$ encodes the **strength** of the direct connection, making $\Theta$ the natural object for **Gaussian graphical models** (draw an edge $i \sim j$ iff $\Theta_{ij} \neq 0$).

---

### Summary

| Object | What it encodes |
|---|---|
| $\Sigma_{ij} = 0$ | Marginal independence (only!) |
| $\Theta_{ij} = 0$ | Conditional independence given all others |

This is why methods like the **graphical LASSO** penalize entries of $\Theta$ rather than $\Sigma$ — they are recovering the graph of direct dependencies.
