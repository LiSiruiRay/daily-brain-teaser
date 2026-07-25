# Answer: The Gaussian Meets Its Reflection

## Key Idea / Intuition

The trick is to **complete the square in the exponent**. The integrand $e^{-x^2}\cos(2bx)$ is really the real part of $e^{-x^2 + 2ibx}$, and the exponent $-x^2 + 2ibx$ can be written as $-(x-ib)^2 - b^2$. This shifts the Gaussian in the complex plane by an imaginary amount, but by contour integration (the rectangular contour closes without picking up extra residues), the integral over the shifted line equals the standard Gaussian integral. The $e^{-b^2}$ factor out front is the surprise: the answer is a **Gaussian in $b$**, reflecting the fact that the Fourier transform of a Gaussian is again a Gaussian.

---

## Formal Proof / Solution

**Step 1: Write as real part of a complex integral.**

Since $\cos(2bx) = \mathrm{Re}(e^{2ibx})$, we have

$$I = \mathrm{Re} \int_0^\infty e^{-x^2 + 2ibx}\, dx.$$

But since the integrand is even in $x$ (the real part is even, the imaginary part is odd), we can extend:

$$2I = \mathrm{Re} \int_{-\infty}^\infty e^{-x^2 + 2ibx}\, dx.$$

**Step 2: Complete the square.**

$$-x^2 + 2ibx = -(x^2 - 2ibx) = -(x - ib)^2 - b^2.$$

So

$$\int_{-\infty}^\infty e^{-x^2 + 2ibx}\, dx = e^{-b^2} \int_{-\infty}^\infty e^{-(x-ib)^2}\, dx.$$

**Step 3: Shift the contour.**

We need $\int_{-\infty}^\infty e^{-(x-ib)^2}\, dx$. This is the integral of $e^{-z^2}$ along the horizontal line $\mathrm{Im}(z) = -b$ in the complex plane. Consider the rectangular contour with vertices $\pm R$ and $\pm R - ib$. Since $e^{-z^2}$ is entire, the contour integral vanishes. The two vertical sides contribute $\to 0$ as $R \to \infty$ (because $|e^{-z^2}| = e^{-(x^2 - y^2)}$ and $x \to \pm\infty$ dominates). Therefore

$$\int_{-\infty}^\infty e^{-(x-ib)^2}\, dx = \int_{-\infty}^\infty e^{-x^2}\, dx = \sqrt{\pi}.$$

**Step 4: Conclude.**

$$\int_{-\infty}^\infty e^{-x^2+2ibx}\, dx = \sqrt{\pi}\, e^{-b^2},$$

which is real, so taking the real part is trivial. Thus

$$2I = \sqrt{\pi}\, e^{-b^2} \implies \boxed{I = \frac{\sqrt{\pi}}{2} e^{-b^2}}.$$

**Why this is beautiful:** The Fourier transform of $e^{-x^2}$ is again a Gaussian — one of the most elegant self-referential facts in analysis. The formula $I = \frac{\sqrt{\pi}}{2}e^{-b^2}$ encodes this: the "frequency content" of the Gaussian at frequency $b$ decays exactly as another Gaussian in $b$.
