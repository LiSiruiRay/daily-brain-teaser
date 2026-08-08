# Answer: Integral of 1/(1+tan^α x)

## Key Idea / Intuition

The exponent $\sqrt{2}$ looks alarming — surely the answer must depend on it? In fact, a single substitution $x \mapsto \frac{\pi}{2} - x$ turns the integrand into its own complement, so the two halves add to 1 and the integral is always $\frac{\pi}{4}$, **regardless of the exponent**. The trick works for any positive real exponent.

---

## Formal Proof / Solution

**Step 1: Set up the symmetry substitution.**

Let $\alpha = \sqrt{2}$ (but the argument works for any $\alpha > 0$). Write

$$I = \int_0^{\pi/2} \frac{1}{1 + \tan^{\alpha}(x)}\, dx.$$

Substitute $u = \frac{\pi}{2} - x$, so $du = -dx$. When $x=0$, $u=\frac{\pi}{2}$; when $x=\frac{\pi}{2}$, $u=0$. Also,

$$\tan\!\left(\tfrac{\pi}{2}-u\right) = \cot(u) = \frac{1}{\tan u}.$$

So the substituted integral is

$$J = \int_0^{\pi/2} \frac{1}{1 + \cot^{\alpha}(u)}\, du = \int_0^{\pi/2} \frac{1}{1 + \frac{1}{\tan^{\alpha}(u)}}\, du = \int_0^{\pi/2} \frac{\tan^{\alpha}(u)}{1 + \tan^{\alpha}(u)}\, du.$$

**Step 2: Add $I$ and $J$.**

Since $u$ is a dummy variable, $J = I$. Therefore:

$$2I = I + J = \int_0^{\pi/2} \left[\frac{1}{1+\tan^{\alpha}(x)} + \frac{\tan^{\alpha}(x)}{1+\tan^{\alpha}(x)}\right]dx = \int_0^{\pi/2} 1\, dx = \frac{\pi}{2}.$$

**Step 3: Conclude.**

$$\boxed{I = \frac{\pi}{4}.}$$

The exponent $\sqrt{2}$ is completely irrelevant — the answer is $\frac{\pi}{4}$ for any positive exponent $\alpha$.
