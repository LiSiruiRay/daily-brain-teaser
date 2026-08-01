# Answer: Integral of ln(x)/sqrt(x(1-x))

## Key Idea / Intuition

The weight $1/\sqrt{x(1-x)}$ is the density of a Beta$(1/2, 1/2)$ distribution (up to a constant), and the integral $\int_0^1 x^{s-1}(1-x)^{t-1}\,dx = B(s,t) = \Gamma(s)\Gamma(t)/\Gamma(s+t)$ is the Beta function. The trick is to **differentiate the Beta function with respect to a parameter**: write $x^{s-1}$ inside the integral, differentiate in $s$, and then evaluate at $s = 1/2$. The answer emerges from the digamma function $\psi = \Gamma'/\Gamma$.

---

## Formal Proof / Solution

**Step 1: Set up the parametric integral.**

Consider the Beta integral

$$B(s, \tfrac{1}{2}) = \int_0^1 x^{s-1}(1-x)^{-1/2}\,dx = \frac{\Gamma(s)\,\Gamma(\tfrac{1}{2})}{\Gamma(s + \tfrac{1}{2})}.$$

**Step 2: Differentiate under the integral sign.**

Differentiating both sides with respect to $s$:

$$\frac{d}{ds} B(s, \tfrac{1}{2}) = \int_0^1 x^{s-1} \ln(x)\,(1-x)^{-1/2}\,dx.$$

On the right-hand side of the closed form:

$$\frac{d}{ds}\left[\frac{\Gamma(s)\,\Gamma(\tfrac{1}{2})}{\Gamma(s+\tfrac{1}{2})}\right] = \Gamma(\tfrac{1}{2})\cdot \frac{\Gamma(s)}{\Gamma(s+\tfrac{1}{2})}\left[\psi(s) - \psi\!\left(s+\tfrac{1}{2}\right)\right],$$

where $\psi = \Gamma'/\Gamma$ is the digamma function.

**Step 3: Evaluate at $s = 1/2$.**

Setting $s = 1/2$:

$$I = \int_0^1 x^{-1/2}\ln(x)\,(1-x)^{-1/2}\,dx = \frac{\int_0^1 \ln x}{\sqrt{x(1-x)}}\,dx,$$

and the closed form gives

$$I = \Gamma(\tfrac{1}{2})\cdot \frac{\Gamma(\tfrac{1}{2})}{\Gamma(1)}\left[\psi(\tfrac{1}{2}) - \psi(1)\right].$$

Now use:
- $\Gamma(1/2) = \sqrt{\pi}$, so $\Gamma(1/2)^2 = \pi$ and $\Gamma(1) = 1$,
- $\psi(1) = -\gamma$ (Euler–Mascheroni constant),
- $\psi(1/2) = -\gamma - 2\ln 2$ (a classical identity).

Therefore:

$$\psi(\tfrac{1}{2}) - \psi(1) = (-\gamma - 2\ln 2) - (-\gamma) = -2\ln 2.$$

**Step 4: Conclude.**

$$I = \pi \cdot (-2\ln 2) = \boxed{-2\pi \ln 2}.$$

**Sanity check:** The integrand $\ln(x)/\sqrt{x(1-x)}$ is negative on $(0,1)$ since $\ln x < 0$ there, so a negative answer is correct.

---

**The beautiful punchline:** A seemingly complicated integral collapses to $-2\pi\ln 2$ — $\pi$ appears from the Beta function, and $\ln 2$ from the digamma difference. Two transcendental constants from one elegant differentiation trick.
