# Answer: Ridge Regression as Augmented OLS

## Key Idea / Intuition

Ridge regression penalizes large coefficients by adding $\lambda\|\beta\|^2$. The augmentation trick makes this penalty *literal*: we append $p$ fake observations with input $\sqrt{\lambda}\,e_j$ (the $j$-th standard basis vector) and response $0$. Predicting $0$ for these fake points forces the model to keep $\beta_j$ small — otherwise it pays a residual cost. The penalty term in ridge is thus reinterpreted as a genuine least-squares fit to artificial "zero-response" data.

---

## Formal Proof / Solution

**Step 1: Write the augmented OLS objective.**

The OLS loss on the augmented data $(\tilde{X}, \tilde{y})$ is

$$\|\tilde{y} - \tilde{X}\beta\|^2 = \left\|\begin{pmatrix} y \\ 0 \end{pmatrix} - \begin{pmatrix} X \\ \sqrt{\lambda}\,I \end{pmatrix}\beta\right\|^2.$$

Expanding the block structure:

$$= \|y - X\beta\|^2 + \|\sqrt{\lambda}\,\beta - 0\|^2 = \|y - X\beta\|^2 + \lambda\|\beta\|^2.$$

This is exactly the ridge objective $\text{RSS}_\lambda(\beta)$.

**Step 2: Compute the OLS normal equations for $\tilde{X}$.**

$$\tilde{X}^T \tilde{X} = \begin{pmatrix} X^T & \sqrt{\lambda}\,I \end{pmatrix}\begin{pmatrix} X \\ \sqrt{\lambda}\,I \end{pmatrix} = X^T X + \lambda I.$$

$$\tilde{X}^T \tilde{y} = \begin{pmatrix} X^T & \sqrt{\lambda}\,I \end{pmatrix}\begin{pmatrix} y \\ 0 \end{pmatrix} = X^T y.$$

**Step 3: Solve.**

The OLS solution on the augmented data is

$$\hat{\beta} = (\tilde{X}^T \tilde{X})^{-1}\tilde{X}^T \tilde{y} = (X^T X + \lambda I)^{-1} X^T y = \hat{\beta}_{\text{ridge}}.$$

(Note: $X^T X + \lambda I$ is always positive definite for $\lambda > 0$, so the inverse exists even when $X^T X$ is singular — a secondary benefit of ridge.)

**Conceptual interpretation:**

The $p$ fake data points each "observe" a single coefficient in isolation and expect it to be zero. Adding more such points (larger $\lambda$) increases the pressure toward zero. Ridge shrinkage is literally the influence of these phantom zero-observations competing with the real data. This is an instance of the *hints* framework (Abu-Mostafa 1995): encode prior knowledge (here: "prefer small coefficients") as artificial training examples.
