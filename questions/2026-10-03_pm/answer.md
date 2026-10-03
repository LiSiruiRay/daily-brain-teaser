# Answer: Frullani-Type Log Integral via Feynman

## Key Idea / Intuition

The integrand involves $\ln x$ in the denominator, which is the classic signal to use **Feynman's trick** (differentiation under the integral sign). The key observation is that $\frac{x^a - x^b}{\ln x}$ can be written as $\int_b^a x^t\, dt$, converting a single nasty integral into a double integral that factors cleanly. Swapping the order of integration then reduces everything to an elementary computation.

---

## Formal Proof / Solution

**Step 1: Rewrite the integrand as a parameter integral.**

Recall that for $x \in (0,1)$, $\ln x < 0$, and:

$$\frac{x^a - x^b}{\ln x} = \int_b^a x^t\, dt$$

because $\frac{d}{dt} x^t = x^t \ln x$, so $\int_b^a x^t \ln x\, dt = x^a - x^b$.

**Step 2: Swap the order of integration.**

$$I = \int_0^1 \int_b^a x^t\, dt\, dx = \int_b^a \left(\int_0^1 x^t\, dx\right) dt$$

The interchange is justified by Fubini's theorem since $x^t$ is non-negative and integrable on $[0,1]\times[b,a]$ for $t > -1$.

**Step 3: Evaluate the inner integral.**

$$\int_0^1 x^t\, dx = \frac{1}{t+1}, \qquad t > -1.$$

**Step 4: Evaluate the outer integral.**

$$I = \int_b^a \frac{dt}{t+1} = \ln(t+1)\Big|_b^a = \ln(a+1) - \ln(b+1) = \ln\!\frac{a+1}{b+1}.$$

**Result:**

$$\boxed{I = \ln\frac{a+1}{b+1}}$$

**Sanity check:** If $a = b$, then $I = 0$ trivially. ✓ If $b = 0$, $I = \ln(a+1)$, which matches the known integral $\int_0^1 \frac{x^a - 1}{\ln x}\,dx = \ln(a+1)$. ✓
