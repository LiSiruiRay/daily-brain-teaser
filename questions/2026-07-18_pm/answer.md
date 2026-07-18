# Answer: Integral of ln(1+x)/(1+x²) via Feynman Self-Reference

## Key Idea / Intuition

The integrand mixes $\ln(1+x)$ with $1/(1+x^2)$ in a way that resists direct antidifferentiation. The Feynman trick introduces a parameter $t$ to "scale" the argument of the logarithm, turning the integral into a function of $t$ whose derivative is a rational integral you can evaluate exactly. The final answer combines $\pi$ and $\ln 2$ in a pleasing way — a hallmark of integrals sitting at the intersection of logarithmic and trigonometric worlds.

---

## Formal Proof / Solution

**Step 1: Introduce the parameter.**

Define
$$I(t) = \int_0^1 \frac{\ln(1+tx)}{1+x^2}\,dx, \qquad t \in [0,1].$$

We want $I(1)$, and clearly $I(0) = 0$.

**Step 2: Differentiate under the integral sign.**

$$I'(t) = \int_0^1 \frac{x}{(1+tx)(1+x^2)}\,dx.$$

**Step 3: Partial fractions.**

Decompose:
$$\frac{x}{(1+tx)(1+x^2)} = \frac{A}{1+tx} + \frac{Bx + C}{1+x^2}.$$

Multiply through by $(1+tx)(1+x^2)$:
$$x = A(1+x^2) + (Bx+C)(1+tx).$$

Setting $x = -1/t$: $\quad -1/t = A(1+1/t^2)$, so $A = \dfrac{-t}{1+t^2}.$

Comparing $x^2$ terms: $0 = A + Bt$, so $B = \dfrac{1}{1+t^2}.$

Comparing constant terms: $0 = A + C$, so $C = \dfrac{t}{1+t^2}.$

Thus:
$$I'(t) = \frac{-t}{1+t^2}\int_0^1\frac{dx}{1+tx} + \frac{1}{1+t^2}\int_0^1\frac{x\,dx}{1+x^2} + \frac{t}{1+t^2}\int_0^1\frac{dx}{1+x^2}.$$

**Step 4: Evaluate each sub-integral.**

$$\int_0^1 \frac{dx}{1+tx} = \frac{\ln(1+t)}{t}, \qquad (t>0)$$

$$\int_0^1 \frac{x\,dx}{1+x^2} = \frac{\ln 2}{2},$$

$$\int_0^1 \frac{dx}{1+x^2} = \frac{\pi}{4}.$$

So:
$$I'(t) = \frac{-t}{1+t^2}\cdot\frac{\ln(1+t)}{t} + \frac{1}{1+t^2}\cdot\frac{\ln 2}{2} + \frac{t}{1+t^2}\cdot\frac{\pi}{4}.$$

$$= \frac{-\ln(1+t)}{1+t^2} + \frac{\ln 2}{2(1+t^2)} + \frac{\pi t}{4(1+t^2)}.$$

**Step 5: Integrate from 0 to 1.**

$$I(1) = \int_0^1 I'(t)\,dt = -I(1) + \frac{\ln 2}{2}\cdot\frac{\pi}{4} + \frac{\pi}{4}\cdot\frac{\ln 2}{2}.$$

Wait — let's be careful:

$$\int_0^1 \frac{-\ln(1+t)}{1+t^2}\,dt = -I(1) \quad \text{(that's exactly our original integral!)}$$

$$\int_0^1 \frac{\ln 2}{2(1+t^2)}\,dt = \frac{\ln 2}{2}\cdot\frac{\pi}{4} = \frac{\pi \ln 2}{8}.$$

$$\int_0^1 \frac{\pi t}{4(1+t^2)}\,dt = \frac{\pi}{4}\cdot\frac{\ln 2}{2} = \frac{\pi \ln 2}{8}.$$

So:
$$I(1) = -I(1) + \frac{\pi\ln 2}{8} + \frac{\pi\ln 2}{8}.$$

$$2I(1) = \frac{\pi \ln 2}{4}.$$

$$\boxed{I = \dfrac{\pi \ln 2}{8}.}$$

**Sanity check:** The answer $\pi \ln 2 / 8 \approx 0.2722$ is in $(0,1)$, which matches the integrand being bounded above by $\ln 2 \approx 0.693$ on $[0,1]$.
