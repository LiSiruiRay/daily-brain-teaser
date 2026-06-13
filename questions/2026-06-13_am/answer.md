# Answer: Integral of sqrt(tan x)

## Key Idea / Intuition

The trick is to use the **self-complementary symmetry** of the integrand: if you substitute $x \mapsto \pi/2 - x$, then $\tan x \mapsto \cot x = 1/\tan x$, so $\sqrt{\tan x} \mapsto 1/\sqrt{\tan x}$. Adding $I$ to its reflected version gives something much simpler to integrate. Then a substitution $t = \sqrt{\tan x}$ reduces the sum to a classic rational integral that can be handled by partial fractions, yielding a clean $\pi/\sqrt{2}$ answer.

---

## Formal Proof / Solution

**Step 1: Symmetry observation.**

Let $I = \int_0^{\pi/2} \sqrt{\tan x}\, dx$. Under $x \mapsto \pi/2 - x$:

$$I = \int_0^{\pi/2} \sqrt{\cot x}\, dx = \int_0^{\pi/2} \frac{1}{\sqrt{\tan x}}\, dx$$

So:

$$2I = \int_0^{\pi/2} \left(\sqrt{\tan x} + \frac{1}{\sqrt{\tan x}}\right) dx = \int_0^{\pi/2} \frac{\tan x + 1}{\sqrt{\tan x}}\, dx$$

**Step 2: Substitution $t = \sqrt{\tan x}$.**

Let $t = \sqrt{\tan x}$, so $\tan x = t^2$, $x = \arctan(t^2)$, and:

$$dx = \frac{2t}{1 + t^4}\, dt$$

When $x = 0$, $t = 0$; when $x = \pi/2$, $t = \infty$. Then:

$$2I = \int_0^{\infty} \frac{t^2 + 1}{t} \cdot \frac{2t}{1+t^4}\, dt = 2\int_0^{\infty} \frac{t^2+1}{t^4+1}\, dt$$

So:

$$I = \int_0^{\infty} \frac{t^2 + 1}{t^4 + 1}\, dt$$

**Step 3: Evaluate the rational integral.**

Divide numerator and denominator by $t^2$:

$$I = \int_0^{\infty} \frac{1 + 1/t^2}{t^2 + 1/t^2}\, dt$$

Notice that $t^2 + 1/t^2 = (t - 1/t)^2 + 2$. Let $u = t - 1/t$, so $du = (1 + 1/t^2)\, dt$.

As $t: 0 \to \infty$, we have $u: -\infty \to \infty$. Therefore:

$$I = \int_{-\infty}^{\infty} \frac{du}{u^2 + 2} = \frac{1}{\sqrt{2}}\arctan\!\left(\frac{u}{\sqrt{2}}\right)\Bigg|_{-\infty}^{\infty} = \frac{1}{\sqrt{2}} \cdot \pi$$

**Result:**

$$\boxed{I = \dfrac{\pi}{\sqrt{2}}}$$

**Why it's beautiful:** Three elegant ideas click together — the reflection symmetry that pairs $\sqrt{\tan x}$ with $1/\sqrt{\tan x}$, the substitution that rationalizes the integral, and the classic "$t - 1/t$" trick that collapses a quartic into a quadratic.
