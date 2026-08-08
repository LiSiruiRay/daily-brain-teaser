# Answer: The Integral That Wants to Be a Probability

## Key Idea / Intuition

The fraction $(1 - e^{-x})/x$ looks awkward by itself, but it secretly wants to be written as an integral: $\frac{1-e^{-x}}{x} = \int_0^1 e^{-tx}\,dt$. Once you swap the order of integration, you're left with a product of two exponentials, which integrates instantly. The answer falls out as a logarithm.

---

## Formal Proof / Solution

**Step 1: Write the numerator as an integral.**

Observe the key identity:
$$\frac{1 - e^{-x}}{x} = \int_0^1 e^{-tx} \, dt$$
(this follows from $\int_0^1 e^{-tx}\,dt = \left[-\frac{e^{-tx}}{x}\right]_0^1 = \frac{1-e^{-x}}{x}$).

**Step 2: Substitute and swap the order.**

$$I = \int_0^\infty \left(\int_0^1 e^{-tx}\,dt\right) e^{-x} \, dx = \int_0^1 \int_0^\infty e^{-(t+1)x}\,dx\,dt$$

Swapping is justified by Tonelli's theorem (the integrand is non-negative).

**Step 3: Evaluate the inner integral.**

$$\int_0^\infty e^{-(t+1)x}\,dx = \frac{1}{t+1}$$

**Step 4: Evaluate the outer integral.**

$$I = \int_0^1 \frac{1}{t+1}\,dt = \ln(t+1)\Big|_0^1 = \ln 2 - \ln 1 = \boxed{\ln 2}$$

---

**Remark:** This is a baby version of the Frullani integral philosophy: expressing a ratio $(f(0)-f(x))/x$ as $\int_0^1 f'(tx)\,dt$ and swapping order. Here $f(x) = e^{-x}$ makes everything explicit and clean.
