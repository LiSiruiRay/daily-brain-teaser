# Answer: The Softmax That Forgets Its Past: Invariance to Label Permutation vs. Feature Permutation

## Key Idea / Intuition

The softmax model is **not identifiable**: you can shift every coefficient vector by the same arbitrary vector $v$ — i.e., replace $\beta_k \mapsto \beta_k + v$ for all $k$ — and the predicted probabilities are completely unchanged for every input. This is because the softmax depends only on *differences* between the linear scores. No amount of data can break this symmetry, because the likelihood itself is flat along this entire affine subspace of parameters.

---

## Formal Proof / Solution

### Part (A): Label Permutation

If you swap class labels 1 and 2 and retrain, the new optimal classifier is obtained by swapping $\beta_1 \leftrightarrow \beta_2$ (and leaving all other $\beta_k$ unchanged). This is immediate from symmetry of the loss: the relabeled loss is the original loss with the roles of $\beta_1$ and $\beta_2$ exchanged. So yes — label permutation corresponds exactly to permuting the coefficient vectors.

### Part (B): Feature Sign Flip

If you replace $x \mapsto -x$ and retrain, the new optimal solution satisfies $\tilde{\beta}_k = -\beta_k$ for all $k$, since

$$\tilde{\beta}_k^\top(-x) = -\tilde{\beta}_k^\top x$$

and the model structure is preserved with $\tilde{\beta}_k = -\beta_k$. So yes — negating features corresponds to negating all coefficient vectors.

### The Identifiability Problem

**True.** The softmax has a fundamental non-identifiability.

**The transformation:** For any vector $v \in \mathbb{R}^p$, define

$$\beta_k' = \beta_k + v \quad \text{for all } k = 1, \ldots, K.$$

Then for every input $x$:

$$\frac{e^{(\beta_k')^\top x}}{\sum_j e^{(\beta_j')^\top x}} = \frac{e^{\beta_k^\top x + v^\top x}}{\sum_j e^{\beta_j^\top x + v^\top x}} = \frac{e^{v^\top x} \cdot e^{\beta_k^\top x}}{e^{v^\top x} \cdot \sum_j e^{\beta_j^\top x}} = \frac{e^{\beta_k^\top x}}{\sum_j e^{\beta_j^\top x}}.$$

The $e^{v^\top x}$ factor cancels in numerator and denominator. So **every predicted probability is identical** under this shift.

**Why more data cannot resolve it:**

Since the likelihood

$$\prod_{i=1}^n p(y_i \mid x_i; \{\beta_k\})$$

is identical for $\{\beta_k\}$ and $\{\beta_k + v\}$ for *every* data point, the log-likelihood surface is flat along the entire $(K \cdot p)$-dimensional family $\{\beta_k + v : v \in \mathbb{R}^p\}$. No data distinguishes these parameter values — the Fisher information matrix is singular.

**Standard fix:** Pin one class, say $\beta_K = 0$. This is why logistic regression for $K=2$ classes only needs one coefficient vector $\beta_1$ (the log-odds of class 1 vs. class 2). For general $K$, you effectively model $K-1$ free coefficient vectors, giving a well-identified model.

**Summary table:**

| Operation | Effect on $\{\beta_k\}$ |
|---|---|
| Swap labels $1 \leftrightarrow 2$ | Swap $\beta_1 \leftrightarrow \beta_2$ |
| Flip features $x \to -x$ | Negate all: $\beta_k \to -\beta_k$ |
| Shift all by $v$ | Leaves all probabilities **unchanged** — not identifiable |
