# Answer: Precision Matrix and Conditional Independence

## Key Idea / Intuition

For a Gaussian, all conditional distributions are still Gaussian, and conditional independence is captured entirely by second-order structure. The precision matrix $\Theta = \Sigma^{-1}$ encodes **partial correlations** — correlation after removing the linear effect of all other variables. A zero entry $\Theta_{ij} = 0$ means that once you control for everything else, $X_i$ and $X_j$ carry no additional information about each other. This is fundamentally different from $\Sigma_{ij} = 0$ (marginal independence), which is a much stronger and less common condition. The miracle: **invert the covariance matrix, and read off the graph directly**.

---

## Formal Proof / Solution

### Step 1: Conditional distribution of a Gaussian

Partition $X = (X_A, X_B)$ where $A = \{i, j\}$ and $B$ is everything else. The conditional distribution $X_A \mid X_B = x_B$ is Gaussian with:

$$X_A \mid X_B \sim \mathcal{N}\!\left(\mu_A + \Sigma_{AB}\Sigma_{BB}^{-1}(x_B - \mu_B),\ \Sigma_{AA} - \Sigma_{AB}\Sigma_{BB}^{-1}\Sigma_{BA}\right)$$

So $X_i \perp X_j \mid X_{-ij}$ iff the conditional covariance $(\Sigma_{AA\mid B})_{ij} = 0$.

### Step 2: Schur complement and the precision matrix

The **Schur complement** identity says: if we write the block structure

$$\Theta = \Sigma^{-1} = \begin{pmatrix} \Theta_{AA} & \Theta_{AB} \\ \Theta_{BA} & \Theta_{BB} \end{pmatrix},$$

then the inverse of the Schur complement gives:

$$\Sigma_{AA} - \Sigma_{AB}\Sigma_{BB}^{-1}\Sigma_{BA} = \Theta_{AA}^{-1}.$$

So the conditional covariance of $(X_i, X_j)$ given the rest is exactly $\Theta_{AA}^{-1}$, the $2\times 2$ submatrix of $\Theta$ involving just rows/columns $i, j$, **inverted**.

### Step 3: The key identity

For two variables, the $2\times 2$ matrix

$$\Theta_{AA} = \begin{pmatrix} \Theta_{ii} & \Theta_{ij} \\ \Theta_{ji} & \Theta_{jj} \end{pmatrix}$$

has inverse

$$\Theta_{AA}^{-1} = \frac{1}{\Theta_{ii}\Theta_{jj} - \Theta_{ij}^2}\begin{pmatrix} \Theta_{jj} & -\Theta_{ij} \\ -\Theta_{ji} & \Theta_{ii} \end{pmatrix}.$$

The off-diagonal entry of the conditional covariance (i.e., $\text{Cov}(X_i, X_j \mid X_{-ij})$) is proportional to $-\Theta_{ij}$.

Therefore:

$$X_i \perp X_j \mid X_{-ij} \iff \text{Cov}(X_i, X_j \mid X_{-ij}) = 0 \iff \Theta_{ij} = 0. \quad \blacksquare$$

---

### Step 4: A concrete 3-variable example

Let $X_1 \to X_2 \leftarrow X_3$ be a "common cause" structure — actually let's do a chain: $X_1 \to X_2 \to X_3$.

Take:
$$X_1 \sim \mathcal{N}(0,1), \quad X_2 = X_1 + \varepsilon_2, \quad X_3 = X_2 + \varepsilon_3$$

with $\varepsilon_2, \varepsilon_3 \overset{iid}{\sim} \mathcal{N}(0,1)$ independent. Then:

$$\Sigma = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 3 \end{pmatrix}.$$

Note $\Sigma_{13} = 1 \neq 0$, so $X_1$ and $X_3$ are **marginally correlated**.

Computing $\Theta = \Sigma^{-1}$:

$$\Theta = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}.$$

The $(1,3)$ entry is $\Theta_{13} = 0$! So $X_1 \perp X_3 \mid X_2$, which makes perfect sense: in the chain $X_1 \to X_2 \to X_3$, once you know $X_2$, knowing $X_1$ tells you nothing extra about $X_3$ (d-separation / Markov property).

---

### Why This Is Deep

The moral: **correlation is not conditional independence**. The covariance matrix $\Sigma$ tells you about marginal relationships; the precision matrix $\Theta = \Sigma^{-1}$ tells you about the **conditional graph structure**. This is the foundation of Gaussian graphical models and the graphical LASSO (glasso), which estimates a sparse $\Theta$ to learn which edges are truly present in the dependency graph.

The partial correlation between $X_i$ and $X_j$ given all others is:

$$\rho_{ij \mid \text{rest}} = \frac{-\Theta_{ij}}{\sqrt{\Theta_{ii}\Theta_{jj}}}.$$

So reading off partial correlations from the precision matrix is as easy as reading marginal correlations from the covariance matrix.
