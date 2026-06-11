# Answer: Gauss–Lucas Theorem

## Key Idea / Intuition

The logarithmic derivative of $p$ is a sum of simple fractions $\frac{1}{z - z_k}$. If $z$ lies outside the convex hull of the roots, all the vectors $z - z_k$ point into a common open half-plane — meaning their reciprocals also all point into a common half-plane — so their sum cannot be zero. Hence $p'(z) \neq 0$ outside the convex hull.

---

## Formal Proof / Solution

### Part (a): Locating the zeros of $p'$

By the Gauss–Lucas theorem, all zeros of $p'(z)$ lie in the convex hull of $\{1, 2, 3, 4\}$. Since all roots are real, the convex hull is simply the interval $[1, 4]$ on the real line.

Moreover, since $p$ has only real roots, $p'$ is also a real polynomial (degree 3), so its zeros are either real or come in conjugate pairs. Since they must lie in $[1, 4] \subset \mathbb{R}$, all three zeros of $p'$ are **real** and lie in the interval $[1, 4]$.

By Rolle's theorem (which is the real-line version), there is exactly one zero of $p'$ in each of $(1,2)$, $(2,3)$, $(3,4)$ — Gauss–Lucas tells us this is the whole story even in $\mathbb{C}$.

---

### Part (b): Proof of the Gauss–Lucas Theorem

**Setup.** Write $p(z) = c\prod_{k=1}^n (z - z_k)$. Taking the logarithmic derivative:

$$\frac{p'(z)}{p(z)} = \sum_{k=1}^n \frac{1}{z - z_k}, \quad \text{for } z \notin \{z_1, \ldots, z_n\}.$$

**Goal.** Show that if $p'(w) = 0$, then $w$ lies in the convex hull $K = \operatorname{conv}\{z_1,\ldots,z_n\}$.

Equivalently, we show: if $w \notin K$, then $p'(w) \neq 0$.

**Key geometric step.** If $w \notin K$, by the separating hyperplane theorem (in $\mathbb{R}^2 \cong \mathbb{C}$), there exists a real linear functional — i.e., a direction $\xi \in \mathbb{C}$ with $|\xi|=1$ — such that:

$$\operatorname{Re}(\xi \cdot (w - z_k)) > 0 \quad \text{for all } k = 1, \ldots, n.$$

In other words, all the differences $w - z_k$ lie strictly on one side of a line through the origin.

**Consequence for the sum.** For each $k$:

$$\operatorname{Re}\!\left(\frac{\xi}{w - z_k}\right) = \frac{\operatorname{Re}(\xi\,\overline{(w-z_k)})}{|w-z_k|^2} = \frac{\operatorname{Re}(\xi(w-z_k))^*\text{-related}}{|w-z_k|^2}.$$

More carefully: since $\operatorname{Re}(\xi(w-z_k)) > 0$, taking the reciprocal preserves the real part's sign:

$$\operatorname{Re}\!\left(\frac{\bar{\xi}}{w-z_k}\right) = \frac{\operatorname{Re}\!\left(\overline{\xi(w-z_k)}\cdot\frac{1}{|w-z_k|^2}\cdot|w-z_k|^2\right)}{|w-z_k|^2}.$$

Let me write it cleanly. Write $w - z_k = r_k e^{i\theta_k}$. The assumption says $\operatorname{Re}(\xi \cdot r_k e^{i\theta_k}) > 0$ for all $k$, i.e., $\operatorname{Re}(\xi e^{i\theta_k}) > 0$. Then:

$$\operatorname{Re}\!\left(\bar\xi \cdot \frac{1}{w-z_k}\right) = \operatorname{Re}\!\left(\frac{\bar\xi}{r_k e^{i\theta_k}}\right) = \frac{1}{r_k}\operatorname{Re}(\bar\xi e^{-i\theta_k}) = \frac{1}{r_k}\operatorname{Re}\overline{(\xi e^{i\theta_k})} = \frac{1}{r_k}\operatorname{Re}(\xi e^{i\theta_k}) > 0.$$

Summing over $k$:

$$\operatorname{Re}\!\left(\bar\xi \sum_{k=1}^n \frac{1}{w-z_k}\right) = \sum_{k=1}^n \operatorname{Re}\!\left(\frac{\bar\xi}{w-z_k}\right) > 0.$$

**Conclusion.** Since the sum $\sum_k \frac{1}{w-z_k} \neq 0$, we get $\frac{p'(w)}{p(w)} \neq 0$, so $p'(w) \neq 0$.

Therefore, every zero of $p'(z)$ must lie inside (or on the boundary of) the convex hull of $\{z_1,\ldots,z_n\}$. $\blacksquare$

---

**Why this is beautiful:** The proof uses nothing but the separating hyperplane theorem and a one-line observation about complex reciprocals — yet it gives a nontrivial geometric constraint on the roots of derivatives.
