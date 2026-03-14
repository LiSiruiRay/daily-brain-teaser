# Answer: Integral of a Geometric Series

$$\int_0^{1/2} \left(\sum_{n=2}^{\infty} x^n\right) dx = \log(2) - \frac{5}{8}$$

---

## Step 1: Close the geometric series

Recall the standard geometric series formula for $|x| < 1$:

$$\sum_{n=0}^{\infty} x^n = \frac{1}{1-x}$$

Subtract the $n=0$ and $n=1$ terms:

$$\sum_{n=2}^{\infty} x^n = \frac{1}{1-x} - 1 - x = \frac{x^2}{1-x}$$

On $[0, 1/2]$ we have $|x| \leq 1/2 < 1$, so this is valid and the convergence is uniform, justifying swapping the sum and integral.

---

## Step 2: Rewrite the integrand

Do a simple algebraic decomposition of $\dfrac{x^2}{1-x}$.

Substitute $u = 1-x$ (i.e. $x = 1-u$):

$$\frac{x^2}{1-x} = \frac{(1-u)^2}{u} = \frac{1 - 2u + u^2}{u} = \frac{1}{u} - 2 + u$$

Back in terms of $x$ (with $u = 1-x$):

$$\frac{x^2}{1-x} = \frac{1}{1-x} - 1 - x$$

**Verification:** $\dfrac{1}{1-x} - 1 - x = \dfrac{1 - (1-x) - x(1-x)}{1-x} = \dfrac{x^2}{1-x}$ ✓

---

## Step 3: Integrate term by term

$$\int_0^{1/2} \frac{x^2}{1-x}\, dx = \int_0^{1/2} \left(\frac{1}{1-x} - 1 - x\right) dx$$

$$= \Big[-\ln(1-x) - x - \frac{x^2}{2}\Big]_0^{1/2}$$

Evaluate at $x = 1/2$:

$$-\ln\!\left(\frac{1}{2}\right) - \frac{1}{2} - \frac{1}{8} = \ln(2) - \frac{4}{8} - \frac{1}{8} = \ln(2) - \frac{5}{8}$$

Evaluate at $x = 0$: all terms are $0$.

---

## Result

$$\boxed{\int_0^{1/2} \left(\sum_{n=2}^{\infty} x^n\right) dx = \ln(2) - \frac{5}{8}}$$
