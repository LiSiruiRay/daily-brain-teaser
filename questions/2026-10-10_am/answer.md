# Answer: The Integral That Absorbs a Parameter

## Key Idea / Intuition

The trick is to notice that $\frac{x^a - x^b}{\ln x}$ looks like it wants to be an integral itself: differentiate $x^t = e^{t \ln x}$ with respect to $t$ and you get $x^t \ln x$, so dividing by $\ln x$ "undoes" that differentiation. This is classic **Feynman differentiation under the integral sign**: introduce a parameter $t$, differentiate in $t$ to kill the $\ln x$ in the denominator, evaluate the resulting elementary integral, then integrate back in $t$.

---

## Formal Proof / Solution

**Step 1: Introduce a parameter.**

Write $x^a - x^b = \int_b^a x^t \ln x\,dt$ (since $\frac{d}{dt}x^t = x^t \ln x$). Therefore:

$$I = \int_0^1 \frac{1}{\ln x}\int_b^a x^t \ln x\,dt\,dx = \int_0^1 \int_b^a x^t\,dt\,dx.$$

The $\ln x$ factors cancel perfectly.

**Step 2: Switch the order of integration.**

By Fubini (the integrand $x^t$ is non-negative and integrable for $t > -1$, $x \in (0,1)$):

$$I = \int_b^a \left(\int_0^1 x^t\,dx\right)dt.$$

**Step 3: Inner integral.**

$$\int_0^1 x^t\,dx = \frac{1}{t+1}, \qquad t > -1.$$

**Step 4: Outer integral.**

$$I = \int_b^a \frac{1}{t+1}\,dt = \Big[\ln(t+1)\Big]_b^a = \ln\!\left(\frac{a+1}{b+1}\right).$$

**Result:**

$$\boxed{I = \ln\!\left(\frac{a+1}{b+1}\right).}$$

**Sanity check:** When $a = b$, the integrand is identically $0$, and indeed $\ln\!\left(\frac{a+1}{a+1}\right) = 0$. ✓

When $a = 1, b = 0$:

$$\int_0^1 \frac{x-1}{\ln x}\,dx = \ln 2,$$

a classical result. ✓
