# Answer: The Gaussian-Polynomial Integral

## Key Idea / Intuition

The Gaussian integral $\int_0^\infty e^{-x^2}dx = \frac{\sqrt{\pi}}{2}$ is the seed. Differentiating with respect to a parameter inserted into the exponent generates the $x^4$ factor "for free," turning a hard-looking integral into a consequence of the most famous integral in mathematics. Each differentiation brings down two extra powers of $x$, so two differentiations give $x^4$.

---

## Formal Proof / Solution

**Step 1: Introduce a parameter.**

Define
$$I(t) = \int_0^\infty e^{-t x^2} \, dx, \quad t > 0.$$

By the standard substitution $u = \sqrt{t}\, x$,
$$I(t) = \frac{1}{\sqrt{t}} \int_0^\infty e^{-u^2} du = \frac{\sqrt{\pi}}{2} \cdot t^{-1/2}.$$

**Step 2: Differentiate under the integral sign (Feynman's trick).**

$$\frac{d}{dt} I(t) = \int_0^\infty \frac{\partial}{\partial t} e^{-tx^2} dx = -\int_0^\infty x^2 e^{-tx^2} dx.$$

So
$$\int_0^\infty x^2 e^{-tx^2} dx = -I'(t) = \frac{\sqrt{\pi}}{4} t^{-3/2}.$$

**Step 3: Differentiate again.**

$$\frac{d^2}{dt^2} I(t) = \int_0^\infty x^4 e^{-tx^2} dx.$$

Computing:
$$I''(t) = \frac{d}{dt}\left(-\frac{\sqrt{\pi}}{4} t^{-3/2}\right) = \frac{3\sqrt{\pi}}{8} t^{-5/2}.$$

**Step 4: Evaluate at $t = 1$.**

$$I = \int_0^\infty x^4 e^{-x^2} dx = I''(1) = \frac{3\sqrt{\pi}}{8}.$$

**Sanity check via Gamma function:** Using $\int_0^\infty x^{2n} e^{-x^2}dx = \frac{(2n-1)!!}{2^{n+1}}\sqrt{\pi}$ with $n=2$:
$$\frac{3!!}{2^3}\sqrt{\pi} = \frac{3}{8}\sqrt{\pi}. \checkmark$$

$$\boxed{I = \dfrac{3\sqrt{\pi}}{8}}$$
