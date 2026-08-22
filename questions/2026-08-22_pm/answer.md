# Answer: The Integral That Walks Down Stairs

## Key Idea / Intuition

The function $(x-1)/\ln x$ has no elementary antiderivative, so direct integration is hopeless. The trick is to **introduce a parameter**: write $x - 1 = \int_0^1 x^t\, dt$ (since $\int_0^1 x^t\, dt = [x^t/\ln x]_0^1$... hmm wait — actually the key move is to notice that $\frac{x^t - 1}{\ln x}$ differentiates nicely with respect to $t$). We use **Feynman's trick (differentiation under the integral sign)**: define $I(t) = \int_0^1 \frac{x^t - 1}{\ln x}\, dx$, so that $I(0) = 0$ and $I(1) = I$, and differentiating in $t$ gives a clean integral.

---

## Formal Proof / Solution

**Step 1: Introduce a parameter.**

Define
$$I(t) = \int_0^1 \frac{x^t - 1}{\ln x}\, dx, \qquad t \geq 0.$$

Then $I(0) = 0$ and $I(1) = I$ (the desired integral).

**Step 2: Differentiate under the integral sign.**

$$I'(t) = \frac{d}{dt} \int_0^1 \frac{x^t - 1}{\ln x}\, dx = \int_0^1 \frac{\partial}{\partial t}\left(\frac{x^t - 1}{\ln x}\right) dx = \int_0^1 \frac{x^t \ln x}{\ln x}\, dx = \int_0^1 x^t\, dx.$$

This is simply:
$$I'(t) = \int_0^1 x^t\, dx = \frac{1}{t+1}.$$

**Step 3: Integrate back.**

$$I(t) = \int_0^t \frac{1}{s+1}\, ds = \ln(t+1) + C.$$

Since $I(0) = 0$, we get $C = 0$, so $I(t) = \ln(t+1)$.

**Step 4: Evaluate at $t = 1$.**

$$I = I(1) = \ln 2.$$

---

**Answer:**
$$\boxed{\int_0^1 \frac{x-1}{\ln x}\, dx = \ln 2.}$$

**Why this is beautiful:** The integrand looks intractable, yet a one-line differentiation converts it into $1/(t+1)$, one of the simplest functions imaginable. The answer $\ln 2$ is clean and surprising, arriving from a function with no elementary antiderivative.
