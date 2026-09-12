# Answer: The Integral That Squares Its Sine

## Key Idea / Intuition

The integrand $x/\tan x = x \cos x / \sin x$ looks unpleasant to integrate directly. The key insight is to introduce a **parameter** and differentiate under the integral sign (Feynman's trick), turning the problem into one we can handle via a known log-sine integral. Concretely, replace $x$ with $\alpha x$ and differentiate with respect to $\alpha$, reducing the derivative to a familiar form.

---

## Formal Proof / Solution

**Step 1: Parameterize.**

Define
$$I(\alpha) = \int_0^{\pi/2} \frac{\sin(\alpha x)}{\sin x}\, dx, \quad \alpha \geq 0.$$

Notice that
$$I'(\alpha) = \int_0^{\pi/2} x \cdot \frac{\cos(\alpha x)}{\sin x}\, dx.$$

At $\alpha = 1$ this is exactly our integral $I = I'(1)$.

**Step 2: Compute $I'(\alpha)$ directly.**

Differentiate $I(\alpha)$ again with respect to $\alpha$:
$$I''(\alpha) = -\int_0^{\pi/2} x^2 \frac{\sin(\alpha x)}{\sin x}\, dx.$$

That's getting harder. Let's try a different route.

**Step 3: Use integration by parts on the original integral.**

Write $I = \int_0^{\pi/2} x \cdot \frac{\cos x}{\sin x}\, dx$. Let $u = x$, $dv = \frac{\cos x}{\sin x}\,dx$, so $du = dx$, $v = \ln(\sin x)$. Then

$$I = \Big[x \ln(\sin x)\Big]_0^{\pi/2} - \int_0^{\pi/2} \ln(\sin x)\, dx.$$

**Step 4: Evaluate the boundary term.**

At $x = \pi/2$: $(\pi/2)\ln(\sin(\pi/2)) = (\pi/2)\ln 1 = 0$.

At $x = 0$: we need $\lim_{x\to 0^+} x\ln(\sin x)$. Since $\sin x \sim x$, we get $x \ln(x) \to 0$.

So the boundary term vanishes.

**Step 5: Recall the classic log-sine integral.**

$$\int_0^{\pi/2} \ln(\sin x)\, dx = -\frac{\pi}{2}\ln 2.$$

(This is a standard result, provable by the doubling argument using $\sin(2x) = 2\sin x\cos x$.)

**Step 6: Conclude.**

$$I = 0 - \left(-\frac{\pi}{2}\ln 2\right) = \boxed{\dfrac{\pi\ln 2}{2}}.$$

---

**Verification of the log-sine result (sketch):** Let $J = \int_0^{\pi/2}\ln(\sin x)\,dx$. By symmetry $J = \int_0^{\pi/2}\ln(\cos x)\,dx$, so $2J = \int_0^{\pi/2}\ln(\sin x \cos x)\,dx = \int_0^{\pi/2}\ln\!\left(\tfrac{1}{2}\sin 2x\right)dx = -\tfrac{\pi}{2}\ln 2 + J$, giving $J = -\tfrac{\pi}{2}\ln 2$. ✓
