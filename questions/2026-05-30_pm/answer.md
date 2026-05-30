# Answer: Fresnel-Flavored Integral

## Key Idea / Intuition

The trick is to **get rid of the $\sqrt{x}$ in the denominator** by writing $\frac{1}{\sqrt{x}}$ as a Gaussian integral: $\frac{1}{\sqrt{x}} = \frac{2}{\sqrt{\pi}}\int_0^\infty e^{-t^2 x}\,dt$. This converts the problem into a double integral where the $x$-integral becomes a standard Laplace-transform type integral of $\sin x$, which is elementary. The two integrals then decouple beautifully.

---

## Formal Proof / Solution

**Step 1: Represent $1/\sqrt{x}$ as a Gaussian.**

From the Gaussian integral, substituting $u = t\sqrt{x}$:
$$\int_0^\infty e^{-t^2 x}\,dt = \frac{\sqrt{\pi}}{2\sqrt{x}},$$
so
$$\frac{1}{\sqrt{x}} = \frac{2}{\sqrt{\pi}}\int_0^\infty e^{-t^2 x}\,dt.$$

**Step 2: Substitute into $I$.**

$$I = \int_0^\infty \sin x \cdot \frac{2}{\sqrt{\pi}}\int_0^\infty e^{-t^2 x}\,dt\;dx = \frac{2}{\sqrt{\pi}}\int_0^\infty \int_0^\infty e^{-t^2 x}\sin x\;dx\;dt.$$

(Fubini is justified since the double integral converges absolutely after a small regularization argument.)

**Step 3: Evaluate the inner $x$-integral.**

For fixed $t > 0$, use the standard Laplace transform:
$$\int_0^\infty e^{-ax}\sin x\;dx = \frac{1}{1+a^2}, \quad a > 0.$$

With $a = t^2$:
$$\int_0^\infty e^{-t^2 x}\sin x\;dx = \frac{1}{1+t^4}.$$

**Step 4: Evaluate the outer $t$-integral.**

$$I = \frac{2}{\sqrt{\pi}}\int_0^\infty \frac{dt}{1+t^4}.$$

Now compute $\displaystyle J = \int_0^\infty \frac{dt}{1+t^4}$. Factor $1+t^4 = (t^2+\sqrt{2}\,t+1)(t^2-\sqrt{2}\,t+1)$ and use partial fractions, or use the residue theorem. The standard result is:
$$J = \frac{\pi}{2\sqrt{2}}.$$

*(Quick derivation: by the substitution $t \mapsto 1/t$ and symmetry, one can show $J = \frac{\pi}{2\sqrt 2}$ via residues at $e^{i\pi/4}$ and $e^{3i\pi/4}$.)*

**Step 5: Assemble.**

$$I = \frac{2}{\sqrt{\pi}}\cdot\frac{\pi}{2\sqrt{2}} = \frac{\pi}{\sqrt{2\pi}} = \sqrt{\frac{\pi}{2}}.$$

$$\boxed{I = \sqrt{\dfrac{\pi}{2}}.}$$

**Why this is beautiful:** Three seemingly unrelated objects — the Gaussian, Laplace transforms of $\sin$, and a rational integral — combine to give the clean answer $\sqrt{\pi/2}$, the same constant that appears in the normal distribution.
