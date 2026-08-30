# Answer: LOO Risk That Knows Its Smoother

## Key Idea / Intuition

The hat matrix $\mathbf{H}$ is linear, so adding a synthetic point $(x_i, \hat{y}_i^{(-i)})$ to the training data — which the model already predicts perfectly — doesn't change the fit. This self-consistency condition creates a fixed-point equation relating the full-data fit $\hat{y}_i$ to the LOO fit $\hat{y}_i^{(-i)}$, and solving it yields the diagonal shortcut. The denominator $1 - H_{ii}$ measures how much observation $i$ "influences" its own prediction.

---

## Formal Proof / Solution

### Setup

We want to find $\hat{y}_i^{(-i)}$ — the fitted value at $x_i$ when observation $i$ is left out — without actually refitting the model.

### Step 1: Augment the LOO model with a synthetic point

Consider fitting the model on the **full** data, but replace the $i$-th response $y_i$ with a free parameter $z$. By linearity of the smoother, the fitted value at position $i$ is:

$$\hat{y}_i(z) = H_{ii} \cdot z + \sum_{j \neq i} H_{ij} y_j.$$

This is because $\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}$, and only the $i$-th entry of $\mathbf{y}$ changes.

### Step 2: Self-consistency argument (ESL Exercise 5.13 logic)

Now, the **LOO fit** $\hat{y}_i^{(-i)}$ is by definition the prediction at $x_i$ using only $\{(x_j, y_j)\}_{j \neq i}$.

**Key observation:** If we augment the LOO training set with the synthetic pair $(x_i, \hat{y}_i^{(-i)})$ — a point the model already predicts correctly — the fit doesn't change. So the augmented fit at position $i$ satisfies the **fixed-point condition**:

$$z = \hat{y}_i^{(-i)} \implies \hat{y}_i(z) = z.$$

That is, when $z = \hat{y}_i^{(-i)}$, the model predicts $z$ at position $i$, so adding this point is redundant.

### Step 3: Solve the fixed-point equation

Set $\hat{y}_i(z) = z$:

$$H_{ii} \cdot z + \sum_{j \neq i} H_{ij} y_j = z.$$

Solve for $z$:

$$z - H_{ii} z = \sum_{j \neq i} H_{ij} y_j$$

$$(1 - H_{ii}) z = \sum_{j \neq i} H_{ij} y_j.$$

Now note that the full-data fit is:

$$\hat{y}_i = H_{ii} y_i + \sum_{j \neq i} H_{ij} y_j \implies \sum_{j \neq i} H_{ij} y_j = \hat{y}_i - H_{ii} y_i.$$

Substitute:

$$(1 - H_{ii}) z = \hat{y}_i - H_{ii} y_i = \hat{y}_i - H_{ii} y_i.$$

Add and subtract $H_{ii} \hat{y}_i$... more cleanly:

$$(1 - H_{ii}) z = (\hat{y}_i - y_i) + y_i - H_{ii} y_i = (\hat{y}_i - y_i) + (1 - H_{ii}) y_i.$$

So:

$$z = y_i + \frac{\hat{y}_i - y_i}{1 - H_{ii}} \cdot \frac{1-H_{ii}}{1-H_{ii}} \cdot \ldots$$

More directly:

$$z = \frac{\hat{y}_i - H_{ii} y_i}{1 - H_{ii}} = \frac{\hat{y}_i - H_{ii} y_i}{1 - H_{ii}}.$$

### Step 4: Compute the LOO residual

$$\hat{e}_i^{(-i)} = y_i - z = y_i - \frac{\hat{y}_i - H_{ii} y_i}{1 - H_{ii}} = \frac{y_i(1 - H_{ii}) - \hat{y}_i + H_{ii} y_i}{1 - H_{ii}} = \frac{y_i - \hat{y}_i}{1 - H_{ii}}.$$

$$\boxed{\hat{e}_i^{(-i)} = \frac{y_i - \hat{y}_i}{1 - H_{ii}}}$$

### Why this is beautiful

- **One fit, $n$ folds:** The LOO-CV score $\frac{1}{n}\sum_i (\hat{e}_i^{(-i)})^2$ can be computed from one model fit in $O(n)$ operations, once $\mathbf{H}$ is known.
- **$H_{ii}$ as influence:** If $H_{ii} \approx 1$, observation $i$ completely determines its own fit (high leverage), and the LOO residual blows up — correctly signaling overfitting to that point.
- **Generalizes broadly:** This works for smoothing splines, ridge regression, kernel smoothers — any linear smoother. For smoothing splines, $\text{tr}(\mathbf{H})$ is the effective degrees of freedom, making this formula central to model selection via GCV.
