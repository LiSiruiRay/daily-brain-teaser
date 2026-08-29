# Answer: The Integral That Completes the Square in the Exponent

## Key Idea / Intuition

The cosine can be "absorbed" into the Gaussian by completing the square in the exponent. Writing $\cos(2bx) = \operatorname{Re}(e^{2ibx})$, the product $e^{-x^2} e^{2ibx}$ becomes $e^{-(x-ib)^2} \cdot e^{-b^2}$. The extra factor $e^{-b^2}$ pops out, and the remaining integral over the shifted Gaussian still equals $\frac{\sqrt{\pi}}{2}$ by contour integration (the integrand decays fast enough that we can shift the contour without picking up any residues).

---

## Formal Proof / Solution

**Step 1: Bring cosine into the exponential.**

Since $\cos(2bx) = \operatorname{Re}(e^{2ibx})$, we have

$$I = \operatorname{Re} \int_0^\infty e^{-x^2 + 2ibx}\, dx.$$

**Step 2: Complete the square.**

$$-x^2 + 2ibx = -(x^2 - 2ibx) = -(x - ib)^2 - b^2.$$

So

$$I = \operatorname{Re}\left[ e^{-b^2} \int_0^\infty e^{-(x-ib)^2}\, dx \right].$$

**Step 3: Shift the contour.**

Consider the contour integral of $e^{-z^2}$ over the rectangle with vertices $0, R, R-ib, -ib$ (where we take $b > 0$ for concreteness; the case $b < 0$ is symmetric). Since $e^{-z^2}$ is entire, the integral over the closed rectangle is $0$.

The contributions from the vertical sides $[R, R-ib]$ and $[0, -ib]$ vanish as $R \to \infty$ (since $e^{-z^2}$ decays rapidly on the right vertical side, and the left vertical side is finite). Therefore

$$\int_0^\infty e^{-(x-ib)^2}\, dx = \int_0^\infty e^{-t^2}\, dt = \frac{\sqrt{\pi}}{2},$$

where we set $t = x - ib$ and shift the real contour back.

More precisely: the horizontal contour at $\operatorname{Im}(z) = -b$ from $0-ib$ to $\infty - ib$ equals the horizontal contour at $\operatorname{Im}(z) = 0$ from $0$ to $\infty$, because the closing vertical segments contribute zero.

**Step 4: Read off the answer.**

Since $e^{-b^2}$ and $\frac{\sqrt{\pi}}{2}$ are both real,

$$I = e^{-b^2} \cdot \frac{\sqrt{\pi}}{2}.$$

$$\boxed{I = \frac{\sqrt{\pi}}{2}\, e^{-b^2}.}$$

**Why this is beautiful:** The result says that the Gaussian $e^{-b^2}$ is its own Fourier transform (up to constants). Completing the square turns a hard oscillatory integral into a pure Gaussian one — the oscillation is "hidden" inside the shifted exponent, and the only trace left is the decay factor $e^{-b^2}$. This is the computation that underlies the entire theory of Fourier analysis on $\mathbb{R}$.
