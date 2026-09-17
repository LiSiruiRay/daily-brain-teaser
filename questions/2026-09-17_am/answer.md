# Answer: The Conformal Map That Doubles Its Angle

## Key Idea / Intuition

The Joukowski map $f(z) = z + 1/z$ is one of the most celebrated maps in classical complex analysis and aerodynamics. The core insight is that writing $z = r e^{i\theta}$ separates the map into a real part depending on $\cos\theta$ and an imaginary part depending on $\sin\theta$, weighted by $r + 1/r$ and $r - 1/r$ respectively. When $r = 1$ the imaginary part vanishes (the circle *collapses* to a segment), and for $r \neq 1$ you get an ellipse whose axes are controlled by those two weights.

---

## Formal Proof / Solution

### Setup: polar decomposition

Write $z = r e^{i\theta}$. Then

$$f(z) = re^{i\theta} + \frac{1}{r}e^{-i\theta} = \left(r + \frac{1}{r}\right)\cos\theta + i\left(r - \frac{1}{r}\right)\sin\theta.$$

So if we set $u = \operatorname{Re} f(z)$ and $v = \operatorname{Im} f(z)$:

$$u = \left(r + \frac{1}{r}\right)\cos\theta, \qquad v = \left(r - \frac{1}{r}\right)\sin\theta.$$

---

### Part (a): Unit circle $r = 1$

When $r = 1$:

$$u = 2\cos\theta, \qquad v = 0.$$

So $f(e^{i\theta}) = 2\cos\theta \in \mathbb{R}$. As $\theta$ ranges over $(0, \pi)$, $\cos\theta$ ranges over $(-1, 1)$, so $f$ maps the **upper unit semicircle bijectively onto the open interval $(-2, 2)$** on the real axis. $\blacksquare$

This is the key *degeneration*: the circle collapses to a segment because the imaginary coefficient $r - 1/r = 0$.

---

### Part (b): Circle of radius $r \neq 1$

For fixed $r \neq 1$, let

$$A = r + \frac{1}{r} > 0, \qquad B = \left|r - \frac{1}{r}\right| > 0.$$

Then $u = A\cos\theta$, $v = \pm B\sin\theta$ (sign depending on whether $r > 1$ or $r < 1$). Eliminating $\theta$:

$$\frac{u^2}{A^2} + \frac{v^2}{B^2} = \cos^2\theta + \sin^2\theta = 1.$$

So the image is the **ellipse** with semi-major axis $A = r + 1/r$ (along the real axis) and semi-minor axis $B = |r - 1/r|$ (along the imaginary axis). $\blacksquare$

**Check:** As $r \to 1$, $B \to 0$ and the ellipse degenerates to the segment $[-2,2]$, consistent with part (a).

---

### Part (c): The full picture and applications

- **Circles $|z| = r$** map to confocal ellipses with foci at $\pm 2$:

$$\text{foci at } \pm\sqrt{A^2 - B^2} = \pm\sqrt{\left(r+\frac{1}{r}\right)^2 - \left(r - \frac{1}{r}\right)^2} = \pm\sqrt{4} = \pm 2.$$

All these ellipses share the same foci $\pm 2$, regardless of $r$!

- **Rays $\arg(z) = \theta = \text{const}$**: here $r$ varies and $\theta$ is fixed. Then $u = (r+1/r)\cos\theta$, $v = (r-1/r)\sin\theta$. Eliminating $r$ gives

$$\frac{u^2}{\cos^2\theta} - \frac{v^2}{\sin^2\theta} = \left[\left(r+\frac{1}{r}\right)^2 - \left(r - \frac{1}{r}\right)^2\right] = 4,$$

i.e., **confocal hyperbolas** with the same foci $\pm 2$.

So the Joukowski map sends the orthogonal coordinate grid of *circles and rays* to the orthogonal grid of *confocal ellipses and hyperbolas* — this is the **elliptic coordinate system**.

**In the wild:** The Joukowski map (and its cousins $z + c/z$) are the foundation of **Joukowski airfoil theory** in aerodynamics — a circle in the $z$-plane maps to a wing-shaped profile in the $w$-plane, and potential flow (which is governed by harmonic functions / holomorphic maps) around a circle can be pulled back to give lift calculations around an airfoil. This is a triumph of conformal mapping.
