# Answer: Two Laurent Series for One Function

## Key Idea / Intuition

A Laurent series is not just a property of a function — it is a property of a function *on an annulus*. The same meromorphic function can have completely different Laurent series in different annular regions, because each region "sees" different poles as being "inside" vs "outside." The coefficients are determined by residues and integrals that depend essentially on which singularities are enclosed. This is the heart of why Laurent series are attached to *domains*, not just to functions.

---

## Formal Proof / Solution

### Setup: Partial Fractions

First, decompose $f$ via partial fractions:
$$f(z) = \frac{1}{z(z-1)} = \frac{-1}{z} + \frac{1}{z-1}.$$

(Check: $\frac{-1}{z} + \frac{1}{z-1} = \frac{-(z-1) + z}{z(z-1)} = \frac{1}{z(z-1)}$. ✓)

The singularities are at $z = 0$ (pole) and $z = 1$ (pole).

---

### Part (a): Laurent Series on $0 < |z| < 1$

In this region, $|z| < 1$, so $\frac{1}{z-1} = \frac{-1}{1-z}$ can be expanded as a geometric series:
$$\frac{1}{z-1} = -\frac{1}{1-z} = -\sum_{n=0}^{\infty} z^n, \quad |z| < 1.$$

Therefore:
$$f(z) = -\frac{1}{z} + \left(-\sum_{n=0}^{\infty} z^n\right) = -\frac{1}{z} - 1 - z - z^2 - z^3 - \cdots$$

$$\boxed{f(z) = -\frac{1}{z} - \sum_{n=0}^{\infty} z^n, \quad 0 < |z| < 1.}$$

This has a **simple pole** at $z=0$ (the $-1/z$ term), as expected.

---

### Part (b): Laurent Series on $|z| > 1$

In this region, $|z| > 1$, so $\frac{1}{z-1}$ should be expanded in powers of $1/z$:
$$\frac{1}{z-1} = \frac{1}{z}\cdot\frac{1}{1 - 1/z} = \frac{1}{z}\sum_{n=0}^{\infty} \frac{1}{z^n} = \sum_{n=0}^{\infty} \frac{1}{z^{n+1}}, \quad |z| > 1.$$

Also, $\frac{-1}{z}$ is already a power of $1/z$. Combining:
$$f(z) = -\frac{1}{z} + \sum_{n=0}^{\infty} \frac{1}{z^{n+1}} = -\frac{1}{z} + \frac{1}{z} + \frac{1}{z^2} + \frac{1}{z^3} + \cdots$$

The $-1/z$ and $+1/z$ cancel!

$$\boxed{f(z) = \sum_{n=2}^{\infty} \frac{1}{z^n} = \frac{1}{z^2} + \frac{1}{z^3} + \frac{1}{z^4} + \cdots, \quad |z| > 1.}$$

This series has **no negative powers** beyond $z^{-2}$ — in particular, the residue at $\infty$ is zero, which is consistent with $f(z) \to 0$ as $|z| \to \infty$.

---

### Part (c): Conceptual Reason They Differ

The Laurent series on an annulus $r < |z| < R$ is **unique** — there is exactly one such series converging there. The two annuli $0 < |z| < 1$ and $|z| > 1$ are separated by the singularity at $z = 1$.

- On $0 < |z| < 1$: the singularity at $z=1$ is **outside** the disk, so $\frac{1}{z-1}$ expands in non-negative powers of $z$.
- On $|z| > 1$: the singularity at $z=1$ is **inside** the circle, so $\frac{1}{z-1}$ must be expanded in negative powers of $z$.

In the language of the Cauchy integral formula: the Laurent coefficients $c_n = \frac{1}{2\pi i}\oint_{|z|=r} f(z)z^{-n-1}\,dz$ depend on $r$. Crossing the singularity at $|z|=1$ changes which poles are enclosed, changing all the coefficients.

**The two series are genuinely different functions of their respective variables** — they just happen to represent the same meromorphic function in their respective domains of validity.
