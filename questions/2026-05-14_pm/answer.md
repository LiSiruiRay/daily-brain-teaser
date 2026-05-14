# Answer: Residue at Infinity and the Sum Rule

## Key Idea / Intuition

The Riemann sphere $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ is a compact surface. By the residue theorem applied to a large contour enclosing **all** finite poles, the sum of finite residues equals the integral around a big circle — but traversed in the **opposite** orientation relative to $\infty$. This sign flip is exactly what makes the total sum (finite + infinite) vanish. So for a rational function, computing the residue at $\infty$ is trivially free once you know all the finite residues.

---

## Formal Proof / Solution

### Part (a): Finite Residues

The poles of $f(z) = \dfrac{z^3}{z^2+1}$ are at $z = \pm i$ (simple poles).

$$\operatorname{Res}_{z=i} f = \lim_{z \to i}(z-i)\frac{z^3}{(z-i)(z+i)} = \frac{i^3}{2i} = \frac{-i}{2i} = -\frac{1}{2}.$$

$$\operatorname{Res}_{z=-i} f = \lim_{z \to -i}(z+i)\frac{z^3}{(z-i)(z+i)} = \frac{(-i)^3}{-2i} = \frac{i}{-2i} = -\frac{1}{2}.$$

So both finite residues equal $-\tfrac{1}{2}$, and their sum is $-1$.

---

### Part (b): Sum of All Residues Equals Zero

Let $f$ be a rational function. Choose $R$ large enough so that the disk $|z| \leq R$ contains all finite poles $z_1, \ldots, z_n$.

By the residue theorem (counterclockwise orientation):
$$\oint_{|z|=R} f(z)\,dz = 2\pi i \sum_{k=1}^n \operatorname{Res}_{z=z_k} f(z).$$

Now the residue at infinity is defined precisely so that:
$$\operatorname{Res}_{z=\infty} f(z) = -\frac{1}{2\pi i}\oint_{|z|=R} f(z)\,dz$$

(the minus sign comes from the fact that, from $\infty$'s perspective, the circle $|z|=R$ is traversed **clockwise**).

Therefore:
$$\sum_{k=1}^n \operatorname{Res}_{z=z_k} f + \operatorname{Res}_{z=\infty} f = 0.$$

**Alternatively via behavior at $\infty$:** For a rational function $f(z) = O(z^{-2})$ as $z \to \infty$ (e.g., degree of numerator $\leq$ degree of denominator $-2$), the integral over $|z|=R$ vanishes as $R \to \infty$ by the ML estimate, giving the same conclusion. For $f(z) = O(z^m)$ with $m \geq -1$, the residue at $\infty$ is defined via the local coordinate $w = 1/z$ and captures the remaining contribution.

---

### Part (c): Residue at $\infty$ by the Sum Rule

From part (b):
$$\operatorname{Res}_{z=\infty} f = -\left(\operatorname{Res}_{z=i} f + \operatorname{Res}_{z=-i} f\right) = -\left(-\frac{1}{2} - \frac{1}{2}\right) = \boxed{1}.$$

**Verification via definition:** Substituting $z = 1/w$:
$$\frac{1}{w^2}f\!\left(\frac{1}{w}\right) = \frac{1}{w^2}\cdot\frac{1/w^3}{1/w^2+1} = \frac{1}{w^3}\cdot\frac{1}{1+w^2} = \frac{1}{w^3}(1 - w^2 + \cdots).$$

The coefficient of $1/w$ (i.e., the $w^{-1}$ term) in this Laurent expansion is $-1$, so:
$$\operatorname{Res}_{z=\infty} f = -(-1) = 1. \checkmark$$

---

**The beautiful takeaway:** The Riemann sphere forces a global conservation law on residues. A rational function cannot have residues that "escape" — they must balance to zero over the compact surface $\hat{\mathbb{C}}$. This is the complex-analytic shadow of the fact that a compact manifold has no boundary.

Written to: [questions/2025-07-13_PM_residue_at_infinity.md](questions/2025-07-13_PM_residue_at_infinity.md)

Answer written to: [questions/2025-07-13_PM_residue_at_infinity_answer.md](questions/2025-07-13_PM_residue_at_infinity_answer.md)
