# Answer: The Gaussian Integral's Elegant Cousin

## Key Idea / Intuition

The trick is to write $\frac{1}{\sqrt{x}}$ using a Gaussian integral — specifically, the identity $\frac{1}{\sqrt{x}} = \frac{2}{\sqrt{\pi}} \int_0^\infty e^{-t^2 x} dt$. This converts the oscillatory integral into a double integral where the $x$-integration becomes a known Laplace transform of $\sin x$, and the remaining $t$-integral is again Gaussian. The two worlds — oscillation and Gaussian decay — combine beautifully.

---

## Formal Proof / Solution

**Step 1: Represent $1/\sqrt{x}$ via a Gaussian.**

Use the substitution $u = t\sqrt{x}$ in $\int_0^\infty e^{-u^2} du = \frac{\sqrt{\pi}}{2}$ to get:

$$\int_0^\infty e^{-t^2 x} dt = \frac{\sqrt{\pi}}{2\sqrt{x}}$$

So:

$$\frac{1}{\sqrt{x}} = \frac{2}{\sqrt{\pi}} \int_0^\infty e^{-t^2 x} \, dt$$

**Step 2: Substitute into $I$.**

$$I = \int_0^\infty \sin x \cdot \frac{2}{\sqrt{\pi}} \int_0^\infty e^{-t^2 x} \, dt \, dx = \frac{2}{\sqrt{\pi}} \int_0^\infty \int_0^\infty e^{-t^2 x} \sin x \, dx \, dt$$

(Fubini is justified by absolute convergence after regularization, or by a standard dominated convergence argument with a regularizing factor $e^{-\epsilon x}$.)

**Step 3: Evaluate the inner $x$-integral.**

Use the standard Laplace transform:

$$\int_0^\infty e^{-ax} \sin x \, dx = \frac{1}{a^2 + 1}, \quad a > 0$$

With $a = t^2$:

$$\int_0^\infty e^{-t^2 x} \sin x \, dx = \frac{1}{t^4 + 1}$$

**Step 4: Evaluate the remaining $t$-integral.**

$$I = \frac{2}{\sqrt{\pi}} \int_0^\infty \frac{dt}{t^4 + 1}$$

Now use the known result (derivable via partial fractions or residues):

$$\int_0^\infty \frac{dt}{t^4 + 1} = \frac{\pi}{2\sqrt{2}}$$

**Quick derivation:** Factor $t^4 + 1 = (t^2 + \sqrt{2}\,t + 1)(t^2 - \sqrt{2}\,t + 1)$ and use partial fractions, or note by the residue theorem that $\int_{-\infty}^\infty \frac{dt}{t^4+1} = \frac{\pi}{\sqrt{2}}$, so the half-line integral is $\frac{\pi}{2\sqrt{2}}$.

**Step 5: Combine.**

$$I = \frac{2}{\sqrt{\pi}} \cdot \frac{\pi}{2\sqrt{2}} = \frac{\pi}{\sqrt{2\pi}} = \sqrt{\frac{\pi}{2}}$$

$$\boxed{I = \sqrt{\dfrac{\pi}{2}}}$$

---

**Why beautiful?** The answer $\sqrt{\pi/2}$ is the same as the famous Fresnel integral $\int_0^\infty \cos(x^2)\,dx$ — and indeed they are secretly the same integral under the substitution $x \mapsto x^2$. Both arise from the interaction of oscillation and Gaussian decay.

Written to [question file](questions/2025-07-12_AM_integration_gaussian_cousin.md) and [answer file](questions/2025-07-12_AM_integration_gaussian_cousin_answer.md).
