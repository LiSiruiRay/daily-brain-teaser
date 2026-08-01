# Answer: The Integral That Swaps Its Limits

## Key Idea / Intuition

The integrand has no elementary antiderivative in terms of $x$ alone — but it has a **hidden parameter** waiting to be introduced. The classic Feynman/Leibniz trick is to replace the numerator $x - 1$ with $x^t - 1$ for a parameter $t$, differentiate under the integral sign with respect to $t$, evaluate the resulting clean integral, then integrate back in $t$. The result is a logarithm that evaluates to $\ln 2$.

---

## Formal Proof / Solution

**Step 1: Introduce a parameter.**

Define

$$I(t) = \int_0^1 \frac{x^t - 1}{\ln x}\, dx, \qquad t \geq 0.$$

Note $I(0) = 0$ and $I(1) = I$ (our target).

**Step 2: Differentiate under the integral sign.**

$$I'(t) = \frac{d}{dt} \int_0^1 \frac{x^t - 1}{\ln x}\, dx = \int_0^1 \frac{\partial}{\partial t}(x^t - 1) \cdot \frac{1}{\ln x}\, dx.$$

Since $\frac{\partial}{\partial t} x^t = x^t \ln x$, we get

$$I'(t) = \int_0^1 \frac{x^t \ln x}{\ln x}\, dx = \int_0^1 x^t\, dx = \frac{1}{t+1}.$$

**Step 3: Integrate back.**

$$I(t) = \int_0^t \frac{1}{s+1}\, ds + C = \ln(t+1) + C.$$

Using $I(0) = 0$: $C = 0$. So

$$I(t) = \ln(t+1).$$

**Step 4: Evaluate at $t = 1$.**

$$I = I(1) = \ln 2.$$

**Verification of the trick's validity:** The interchange of differentiation and integration is justified by dominated convergence on $[0,1]$, since $|x^t \ln x|$ is integrable uniformly for $t$ in any compact set. Also note that $\frac{x^t - 1}{\ln x} \to 0$ as $x \to 0^+$ and equals $t$ at $x = 1$ by L'Hôpital, so the integrand is bounded and continuous on $(0,1]$.

**Answer:**

$$\boxed{I = \ln 2}$$
