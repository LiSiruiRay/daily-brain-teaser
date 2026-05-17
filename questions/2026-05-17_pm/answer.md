# Answer: Variance of OLS Along Singular Directions and Ridge Shrinkage

## Key Idea / Intuition

The OLS estimator's variance matrix is $(X^TX)^{-1}\sigma^2$. The directions in which the data $X$ has the *least* spread (smallest singular values) are exactly the directions where the estimator is most uncertain — because the data gives you almost no information about $\beta$ in those directions. Ridge regression simply *inflates* the denominator in those directions, shrinking the estimate toward zero and dramatically reducing variance at the cost of introducing some bias.

---

## Formal Proof / Solution

### Step 1: Variance of OLS in the SVD basis

Using $X = UDV^T$, we get:

$$X^TX = VD^2V^T$$

so the OLS covariance matrix is:

$$\text{Var}(\hat{\beta}) = (X^TX)^{-1}\sigma^2 = V D^{-2} V^T \cdot \sigma^2$$

In the orthonormal basis given by the columns $v_j$ of $V$, the variance in direction $v_j$ is:

$$\frac{\sigma^2}{d_j^2}$$

**Key observation:** small singular value $d_j$ $\Rightarrow$ large variance $\sigma^2/d_j^2$. The directions $X$ barely "sees" are exactly the directions where OLS is wildly uncertain.

### Step 2: Why this makes geometric sense

The singular value $d_j$ measures how much $X$ stretches direction $v_j$: the column $Xv_j = d_j u_j$. If $d_j \approx 0$, then many different values of $\beta$ along $v_j$ produce nearly the same predictions $X\beta$, so the data cannot distinguish them — OLS variance blows up.

### Step 3: What ridge regression does

The ridge estimator covariance is:

$$\text{Var}(\hat{\beta}_\lambda) = (X^TX + \lambda I)^{-1} X^TX (X^TX + \lambda I)^{-1} \sigma^2 = V \cdot \text{diag}\!\left(\frac{d_j^2}{(d_j^2+\lambda)^2}\right) \cdot V^T \cdot \sigma^2$$

The variance in direction $v_j$ becomes:

$$\frac{d_j^2 \sigma^2}{(d_j^2 + \lambda)^2}$$

Compare:

| Direction | OLS variance | Ridge variance |
|-----------|-------------|---------------|
| Large $d_j$ | $\sigma^2/d_j^2$ (small) | $\approx \sigma^2/d_j^2$ (almost unchanged) |
| Small $d_j$ | $\sigma^2/d_j^2$ (**huge**) | $\approx d_j^2\sigma^2/\lambda^2$ (**tiny**) |

Ridge massively shrinks variance in the dangerous low-$d_j$ directions.

### Step 4: The bias-variance trade-off in one sentence

Ridge shrinks $\hat{\beta}_\lambda$ toward zero along the low-variance-data directions (introducing bias $\propto \lambda \cdot \beta_j / (d_j^2 + \lambda)$), but in return achieves a dramatic reduction in variance, so for an appropriate $\lambda$ the **mean squared error** $= \text{Bias}^2 + \text{Variance}$ is smaller than OLS — this is the classic bias-variance trade-off.

### Summary picture

$$\underbrace{\frac{\sigma^2}{d_j^2}}_{\text{OLS variance}} \xrightarrow{\text{ridge}} \underbrace{\frac{d_j^2 \sigma^2}{(d_j^2+\lambda)^2}}_{\text{ridge variance}} + \underbrace{\frac{\lambda^2 \beta_j^2}{(d_j^2+\lambda)^2}}_{\text{bias}^2}$$

The smallest singular values contribute the biggest variance reduction and the biggest bias — ridge is trading one for the other, and the optimal $\lambda$ balances them.
