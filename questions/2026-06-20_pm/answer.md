# Answer: The Sinc Integral

## Key Idea / Intuition

The function $\sin x / x$ has no elementary antiderivative, so direct integration is hopeless. The key trick is to **introduce a parameter** under the integral sign (Feynman's differentiation trick / Laplace transform): replace the integral by $I(s) = \int_0^\infty e^{-sx} \frac{\sin x}{x}\,dx$, differentiate with respect to $s$ to kill the $x$ in the denominator, evaluate the resulting elementary integral, then integrate back and recover $I(0)$.

---

## Formal Proof / Solution

**Step 1: Introduce a parameter.**

Define
$$I(s) = \int_0^{\infty} e^{-sx} \frac{\sin x}{x}\, dx, \quad s > 0.$$

Note $I(0)$ is the desired integral.

**Step 2: Differentiate under the integral sign.**

$$I'(s) = -\int_0^{\infty} e^{-sx} \sin x\, dx.$$

This is a standard Laplace transform:
$$\int_0^{\infty} e^{-sx} \sin x\, dx = \frac{1}{s^2 + 1}.$$

*(Quick derivation: integrate by parts twice, or use $\sin x = \operatorname{Im}(e^{ix})$ to get $\operatorname{Im}\!\left(\frac{1}{s-i}\right) = \frac{1}{s^2+1}$.)*

So:
$$I'(s) = -\frac{1}{s^2 + 1}.$$

**Step 3: Integrate back.**

$$I(s) = -\arctan(s) + C.$$

**Step 4: Determine the constant.**

As $s \to \infty$, $e^{-sx} \to 0$ pointwise and $|\sin x / x| \le 1$, so by DCT, $I(s) \to 0$. Thus:
$$0 = -\frac{\pi}{2} + C \implies C = \frac{\pi}{2}.$$

**Step 5: Evaluate at $s = 0$.**

$$I(0) = -\arctan(0) + \frac{\pi}{2} = \frac{\pi}{2}.$$

$$\boxed{\int_0^{\infty} \frac{\sin x}{x}\, dx = \frac{\pi}{2}}$$

---

**Why this is beautiful:** The integrand $\sin x / x$ is perfectly smooth and bounded, yet resists elementary methods entirely. The parameter trick transforms an impossible integral into a trivial ODE, recovering a clean $\pi/2$ from essentially no information — a hallmark of Feynman's method at its best.

Written to: [questions/2026-06-17_pm.md](questions/2026-06-17_pm.md) | Answer: [answers/2026-06-17_pm.md](answers/2026-06-17_pm.md)
