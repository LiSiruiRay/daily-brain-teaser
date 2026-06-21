# Answer: SVM Margin Width: Why 2/‖β‖?

## Key Idea / Intuition

The SVM margin is just a **Euclidean distance between two parallel hyperplanes**. The key insight is that the functional margin (the value of $x^\top\beta + \beta_0$) is not scale-invariant — you can always rescale $\beta$ to make the constraints say anything you want. The SVM "pins" this freedom by canonically requiring that support vectors lie exactly on the $\pm 1$ level sets, which makes the geometric distance calculable as $2/\|\beta\|$. Maximizing this distance is then equivalent to minimizing $\|\beta\|$, giving a clean quadratic program.

---

## Formal Proof / Solution

### Part (a): The Margin Width

The two margin hyperplanes are:
$$H_+ : x^\top\beta + \beta_0 = +1, \qquad H_- : x^\top\beta + \beta_0 = -1.$$

Take any point $x_+$ on $H_+$ and project it onto $H_-$. The unit normal to both hyperplanes is $\hat{n} = \beta / \|\beta\|$.

The signed distance from a point $x$ to the hyperplane $x^\top\beta + \beta_0 = c$ is:

$$\text{dist}(x, H) = \frac{x^\top\beta + \beta_0 - c}{\|\beta\|}.$$

So the distance from $H_+$ to $H_-$ is:

$$\text{margin} = \frac{(+1) - (-1)}{\|\beta\|} = \frac{2}{\|\beta\|}.$$

This can also be seen concretely: if $x_+$ is a support vector on $H_+$, then moving in the $-\hat{n}$ direction by distance $d$ gives a point $x_+ - d\hat{n}$ on $H_-$:

$$\left(x_+ - d\frac{\beta}{\|\beta\|}\right)^\top \beta + \beta_0 = 1 - d\|\beta\| = -1 \implies d = \frac{2}{\|\beta\|}.$$

$$\boxed{\text{margin} = \frac{2}{\|\beta\|}.}$$

---

### Part (b): Maximizing Margin ↔ Minimizing $\|\beta\|^2$

Maximizing the margin $2/\|\beta\|$ over $\beta$ (subject to correct classification with functional margin $\geq 1$) is equivalent to:

$$\max_\beta \frac{2}{\|\beta\|} \iff \min_\beta \|\beta\| \iff \min_\beta \frac{1}{2}\|\beta\|^2.$$

The factor $\frac{1}{2}$ is a convenient constant for calculus (it kills the $2$ when differentiating), and the square is used because it's **strictly convex and smooth**, making the optimization problem a standard **quadratic program** with linear constraints:

$$\min_{\beta, \beta_0} \frac{1}{2}\|\beta\|^2 \quad \text{s.t.} \quad y_i(x_i^\top\beta + \beta_0) \geq 1,\; \forall i.$$

This is convex, has a unique global minimum, and can be solved efficiently via Lagrange duality.

---

### Part (c): The Surprise — Rescaling

If we replace $\beta \mapsto 2\beta$, $\beta_0 \mapsto 2\beta_0$:

- **The decision boundary** $\{x : x^\top\beta + \beta_0 = 0\}$ is **unchanged** (just multiply through by 2).
- **The geometric margin** becomes $\dfrac{2}{\|2\beta\|} = \dfrac{1}{\|\beta\|}$ — **it halves!**
- **The constraint values** become $y_i(x_i^\top(2\beta) + 2\beta_0) = 2 \cdot y_i(x_i^\top\beta + \beta_0) \geq 2$ — the constraints are now more than satisfied.

**The punchline:** The constraint $y_i(x_i^\top\beta + \beta_0) \geq 1$ is a **canonical normalization** that removes the scale ambiguity. Without it, you could inflate $\beta$ arbitrarily while maintaining the same geometry. The constraint anchors the scale so that the functional margin of support vectors equals exactly $1$, making $\|\beta\|$ a meaningful proxy for the inverse margin. This is sometimes called choosing the **canonical separating hyperplane**.

In other words: the SVM doesn't just find a separating hyperplane — it finds the **unique representative** in each equivalence class of rescaled hyperplanes, chosen so that the closest point has functional value exactly $\pm 1$.
