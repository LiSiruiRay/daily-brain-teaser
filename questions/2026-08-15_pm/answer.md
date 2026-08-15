# Answer: The Integral That Hides a Telescoping Heart

## Key Idea / Intuition

The integrand has a suspicious $\frac{1}{\ln x}$ factor — whenever you see $\frac{x^a - x^b}{\ln x}$, the trick is to introduce a **Feynman parameter**: write $x^a - x^b = \int_b^a x^t\, dt$ and swap the order of integration. The inner integral in $x$ becomes trivial, and you're left with something elementary.

---

## Formal Proof / Solution

**Step 1: Introduce a parameter.**

Notice that for $x \in (0,1)$,

$$x - 1 = x^1 - x^0 = \int_0^1 x^t \ln x\, dt.$$

This is because $\frac{d}{dt} x^t = x^t \ln x$, so $\int_0^1 x^t \ln x\, dt = \left[x^t\right]_0^1 = x^1 - x^0$.

**Step 2: Substitute into the integral.**

$$I = \int_0^1 \frac{1}{\ln x} \int_0^1 x^t \ln x\, dt\, dx = \int_0^1 \int_0^1 x^t\, dx\, dt.$$

The $\ln x$ factors cancel perfectly.

**Step 3: Evaluate the inner integral.**

$$\int_0^1 x^t\, dx = \frac{x^{t+1}}{t+1}\Bigg|_0^1 = \frac{1}{t+1}, \quad t > -1.$$

**Step 4: Evaluate the outer integral.**

$$I = \int_0^1 \frac{1}{t+1}\, dt = \ln(t+1)\Big|_0^1 = \ln 2 - \ln 1 = \boxed{\ln 2}.$$

---

**Sanity check:** The integrand $\frac{x-1}{\ln x}$ is non-negative on $(0,1)$ (both $x - 1 < 0$ and $\ln x < 0$), so $I > 0$. And $\ln 2 \approx 0.693$ is a reasonable value for an integral of a bounded function on $[0,1]$.
