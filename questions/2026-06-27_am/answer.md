# Answer: Integral of ln(sin x) via Symmetry

## Key Idea / Intuition

The trick is to use a **symmetry duplication**: pair $\ln(\sin x)$ with $\ln(\cos x)$ by the substitution $x \mapsto \pi/2 - x$, which shows they contribute equally. Then invoke the **double-angle identity** $\sin(2x) = 2\sin x \cos x$ to reduce the integral to a rescaled copy of itself plus $\ln 2$. Solving the resulting equation gives $I$ exactly.

---

## Formal Proof / Solution

**Step 1: Symmetry.**

Let $J = \int_0^{\pi/2} \ln(\cos x)\,dx$. Substituting $x \mapsto \frac{\pi}{2} - x$ gives $J = \int_0^{\pi/2} \ln(\sin x)\,dx = I$. So $I = J$.

**Step 2: Add $I + J$.**

$$2I = I + J = \int_0^{\pi/2} \ln(\sin x)\,dx + \int_0^{\pi/2}\ln(\cos x)\,dx = \int_0^{\pi/2} \ln(\sin x \cos x)\,dx.$$

**Step 3: Apply the double-angle identity.**

$$\sin x \cos x = \frac{\sin 2x}{2},$$

so

$$2I = \int_0^{\pi/2} \ln\!\left(\frac{\sin 2x}{2}\right)dx = \int_0^{\pi/2} \ln(\sin 2x)\,dx - \int_0^{\pi/2}\ln 2\,dx.$$

The second integral is $\frac{\pi}{2}\ln 2$.

**Step 4: Substitute $u = 2x$ in the first part.**

$$\int_0^{\pi/2} \ln(\sin 2x)\,dx = \frac{1}{2}\int_0^{\pi}\ln(\sin u)\,du.$$

But $\ln(\sin u)$ is symmetric about $u = \pi/2$ on $[0,\pi]$, so

$$\frac{1}{2}\int_0^{\pi}\ln(\sin u)\,du = \frac{1}{2}\cdot 2\int_0^{\pi/2}\ln(\sin u)\,du = I.$$

**Step 5: Solve.**

$$2I = I - \frac{\pi}{2}\ln 2 \implies I = -\frac{\pi}{2}\ln 2.$$

$$\boxed{I = \int_0^{\pi/2}\ln(\sin x)\,dx = -\frac{\pi}{2}\ln 2.}$$

**Why beautiful?** The integral appears to depend on a transcendental function in a complicated way, yet the answer is a clean multiple of $\ln 2$. The entire computation reduces to an algebraic equation in $I$ — no special functions, no residues, just a slick symmetry argument.
