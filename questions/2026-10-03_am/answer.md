# Answer: The Integral That Knows About Primes

## Key Idea / Intuition

This integral is secretly connected to the famous approximation $\pi \approx 22/7$. The fraction $22/7 - \pi$ is a positive number, and this integral is exactly that difference! The key is to perform polynomial long division on the integrand, which splits it into a polynomial part plus a simple remainder involving $1/(1+x^2)$, whose integral gives arctan.

---

## Formal Proof / Solution

**Step 1: Polynomial long division.**

First expand $x^4(1-x)^4$:

$$x^4(1-x)^4 = x^4(1 - 4x + 6x^2 - 4x^3 + x^4) = x^4 - 4x^5 + 6x^6 - 4x^7 + x^8$$

Now divide by $1 + x^2$. We want to write:

$$\frac{x^8 - 4x^7 + 6x^6 - 4x^5 + x^4}{1+x^2} = Q(x) + \frac{R(x)}{1+x^2}$$

Performing long division step by step (repeatedly subtracting $(1+x^2)\cdot(\text{leading term})$):

$$x^8 - 4x^7 + 6x^6 - 4x^5 + x^4 = (1+x^2)\cdot Q(x) + R$$

Let's carry it out:

- $x^8 \div (1+x^2)$: leading term $x^6$, so subtract $x^6(1+x^2) = x^6 + x^8$. Remainder: $-4x^7 + 5x^6 - 4x^5 + x^4$
- $-4x^7 \div (1+x^2)$: leading term $-4x^5$, subtract $-4x^5(1+x^2) = -4x^5 - 4x^7$. Remainder: $5x^6 - 4x^5 + x^4 + 4x^7 - 4x^7 \to 5x^6 + 0 \cdot x^5 - 4x^5 + x^4$... 

Let me be systematic. Writing:

$$\frac{x^4(1-x)^4}{1+x^2} = x^6 - 4x^5 + 5x^4 - 4x^2 + 4 - \frac{4}{1+x^2}$$

**Verification of this identity** (multiply both sides by $1+x^2$):

$$(x^6 - 4x^5 + 5x^4 - 4x^2 + 4)(1+x^2) - 4$$
$$= x^6 + x^8 - 4x^5 - 4x^7 + 5x^4 + 5x^6 - 4x^2 - 4x^4 + 4 + 4x^2 - 4$$
$$= x^8 - 4x^7 + (1+5)x^6 - 4x^5 + (5-4)x^4 + (-4+4)x^2 + (4-4)$$
$$= x^8 - 4x^7 + 6x^6 - 4x^5 + x^4 \checkmark$$

**Step 2: Integrate term by term.**

$$I = \int_0^1 \left(x^6 - 4x^5 + 5x^4 - 4x^2 + 4 - \frac{4}{1+x^2}\right)dx$$

$$= \left[\frac{x^7}{7} - \frac{4x^6}{6} + \frac{5x^5}{5} - \frac{4x^3}{3} + 4x - 4\arctan x\right]_0^1$$

$$= \frac{1}{7} - \frac{2}{3} + 1 - \frac{4}{3} + 4 - 4\cdot\frac{\pi}{4}$$

$$= \frac{1}{7} - \frac{2}{3} + 1 - \frac{4}{3} + 4 - \pi$$

Combining the rational terms:

$$\frac{1}{7} + \left(-\frac{2}{3} - \frac{4}{3}\right) + (1 + 4) = \frac{1}{7} - 2 + 5 = \frac{1}{7} + 3 = \frac{22}{7}$$

Therefore:

$$\boxed{I = \frac{22}{7} - \pi}$$

**Step 3: Appreciate what this means.**

Since $0 \leq x \leq 1$ and $1+x^2 > 0$, the integrand is **strictly positive** on $(0,1)$. Therefore:

$$\frac{22}{7} - \pi = I > 0 \implies \pi < \frac{22}{7}$$

This integral gives a clean, calculus-based proof that $22/7$ overestimates $\pi$, and the value of the integral ($\approx 0.00126$) tells us exactly how bad the approximation is.

Written to: [questions/2026-09-21_am.md](questions/2026-09-21_am.md) | [questions/2026-09-21_am_answer.md](questions/2026-09-21_am_answer.md)
