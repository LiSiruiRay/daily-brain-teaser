# Answer: The Logistic Regression Coefficient That Goes to Infinity

## Key Idea / Intuition

When the data are linearly separable, logistic regression can achieve **zero training loss** in the limit — but only by pushing the coefficient vector to infinity. The log-likelihood never actually attains its supremum; it approaches it asymptotically as $\|\beta\| \to \infty$ along the separating direction. The MLE **does not exist** as a finite vector. This is a clean example where the optimization problem is unbounded above on the feasible domain, yet the algorithm keeps making progress forever.

---

## Formal Proof / Solution

**Setup.** The logistic regression log-likelihood for $n$ observations $(x_i, y_i)$ with $y_i \in \{0,1\}$ is:

$$\ell(\beta) = \sum_{i=1}^n \left[ y_i \log \sigma(\beta^\top x_i) + (1-y_i)\log(1-\sigma(\beta^\top x_i)) \right]$$

where $\sigma(t) = 1/(1+e^{-t})$.

**Step 1: Separability means the supremum is 0.**

Note that $\ell(\beta) \leq 0$ always (since each term is a log of a probability $\in (0,1)$), and $\ell(\beta) = 0$ would require each predicted probability to be exactly 1 for class-1 points and exactly 0 for class-0 points. That would require $\sigma(\beta^\top x_i) = 1$ for $y_i=1$ and $\sigma(\beta^\top x_i) = 0$ for $y_i=0$, which happens only in the limit $\|\beta\| \to \infty$.

**Step 2: Along the separating direction, the likelihood increases without bound.**

Let $w$ be a separating direction: $y_i = 1 \Rightarrow w^\top x_i > 0$ and $y_i = 0 \Rightarrow w^\top x_i < 0$. Set $\beta = tw$ for $t > 0$. Then:
- For $y_i = 1$: $\sigma(t \cdot w^\top x_i) \to 1$ as $t \to \infty$ (since $w^\top x_i > 0$), so $\log \sigma(\cdot) \to 0$.
- For $y_i = 0$: $\sigma(t \cdot w^\top x_i) \to 0$ as $t \to \infty$ (since $w^\top x_i < 0$), so $\log(1 - \sigma(\cdot)) \to 0$.

Therefore $\ell(tw) \to 0^-$ as $t \to \infty$, so $\sup_\beta \ell(\beta) = 0$, but this supremum is **never achieved** at any finite $\beta$.

**Step 3: The MLE does not exist.**

Since $\ell(\beta) < 0$ for all finite $\beta$ (probabilities are always strictly between 0 and 1 for finite inputs), and the sup is 0, the maximum is not attained. The log-likelihood surface is **unbounded** — there is no finite maximizer.

**Step 4: Algorithmic consequence.**

Any gradient-based optimizer (gradient ascent, Newton–Raphson) will keep increasing $\|\beta\|$ forever:
- The gradient never vanishes at a finite point.
- Newton's method may diverge or oscillate.
- Training accuracy reaches 100% quickly, but $\|\hat\beta\| \to \infty$.

The norm of $\beta$ grows roughly like $O(t)$ under gradient ascent, or even faster under Newton steps.

**Step 5: The implicit bias connection.**

A beautiful modern observation: gradient descent on logistic loss with separable data converges in **direction** to the **maximum-margin classifier** (the SVM solution). The coefficients diverge in norm, but $\beta / \|\beta\|$ converges to the hard-margin SVM hyperplane. So logistic regression, run long enough, secretly finds the SVM solution — even without any explicit margin constraint.

**Summary table:**

| Condition | MLE exists? | Training loss |
|-----------|-------------|--------------|
| Non-separable | ✓ Finite unique MLE | > 0 |
| Separable | ✗ MLE $= \infty$ | $\to 0$ as $\|\beta\| \to \infty$ |

**Practical implication:** In separable settings, you must use regularization (e.g., $\ell_2$ penalty $\lambda \|\beta\|^2$) to obtain a finite, well-defined solution. Ridge-penalized logistic regression always has a unique finite minimizer.
