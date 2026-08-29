# Answer: The Integral That Loves a Log-Sine Cousin

## Key Idea / Intuition

This integral looks intimidating, but integration by parts converts it into something we already know: the beloved $\int_0^{\pi/2} \ln(\sin x)\,dx = -\frac{\pi}{2}\ln 2$. The boundary term vanishes by a well-known limit, and what remains is a clean classical value. The key insight is that $\cot x$ is the derivative of $\ln(\sin x)$, so IBP naturally hands the problem back to the log-sine world.

---

## Formal Proof / Solution

**Step 1: Integration by Parts**

Set $u = x$ and $dv = \cot x\, dx = \frac{d}{dx}[\ln \sin x]\,dx$. Then:
$$du = dx, \qquad v = \ln(\sin x).$$

$$I = \Big[x \ln(\sin x)\Big]_0^{\pi/2} - \int_0^{\pi/2} \ln(\sin x)\, dx.$$

**Step 2: Evaluate the Boundary Term**

At $x = \pi/2$: $\quad \frac{\pi}{2}\ln(\sin(\pi/2)) = \frac{\pi}{2}\ln 1 = 0.$

At $x = 0^+$: We need $\lim_{x\to 0^+} x\ln(\sin x)$.

Since $\sin x \approx x$ near $0$, we have $x \ln(\sin x) \approx x \ln x \to 0$ as $x \to 0^+$.

So the boundary term $= 0 - 0 = 0$.

**Step 3: Use the Classical Log-Sine Integral**

$$\int_0^{\pi/2} \ln(\sin x)\, dx = -\frac{\pi}{2}\ln 2.$$

(This is a classical result, provable by the duplication trick: write the integral as half of $\int_0^\pi \ln(\sin x)\,dx$, then use the identity $\sin x = 2\sin(x/2)\cos(x/2)$.)

**Step 4: Combine**

$$I = 0 - \left(-\frac{\pi}{2}\ln 2\right) = \boxed{\dfrac{\pi \ln 2}{2}}.$$

---

**Why this is satisfying:** The integral $\int_0^{\pi/2} x \cot x\,dx$ naively seems harder than the log-sine integral, but IBP shows it is *exactly the negative* of it (up to a vanishing boundary term). One classical integral unlocks another.
