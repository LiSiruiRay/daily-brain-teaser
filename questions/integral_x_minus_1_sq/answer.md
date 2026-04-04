# Integral of $(x-1)^2 / (2e^x + x^2 + 1)$ — Answer

## Answer

$$\int \frac{(x-1)^2}{2e^x + x^2 + 1}\, dx = x - \ln(2e^x + x^2 + 1) + C$$

---

## Solution

Let $D = 2e^x + x^2 + 1$. Compute its derivative:
$$D' = 2e^x + 2x$$

Now split the numerator:
$$x^2 - 2x + 1 = \underbrace{(2e^x + x^2 + 1)}_{D} - \underbrace{(2e^x + 2x)}_{D'}$$

So:
$$\frac{(x-1)^2}{D} = \frac{D - D'}{D} = 1 - \frac{D'}{D}$$

Therefore:
$$\int \frac{(x-1)^2}{2e^x + x^2 + 1}\, dx = \int \left(1 - \frac{D'}{D}\right) dx = x - \ln|D| + C$$

$$= \boxed{x - \ln(2e^x + x^2 + 1) + C}$$

(No absolute value needed since $2e^x + x^2 + 1 > 0$ for all $x \in \mathbb{R}$.)

---

## Verification

Differentiate $x - \ln(2e^x + x^2 + 1)$:

$$\frac{d}{dx}\left[x - \ln(2e^x + x^2 + 1)\right] = 1 - \frac{2e^x + 2x}{2e^x + x^2 + 1} = \frac{(2e^x + x^2 + 1) - (2e^x + 2x)}{2e^x + x^2 + 1} = \frac{x^2 - 2x + 1}{2e^x + x^2 + 1} = \frac{(x-1)^2}{2e^x + x^2 + 1} \checkmark$$

---

## The Meta-Trick

The integrand was engineered so that:

$$\text{numerator} = \text{denominator} - \text{derivative of denominator}$$

Whenever you see an integral of the form $\int \frac{f(x)}{g(x)}\,dx$ where the denominator is a sum and the numerator looks "close" to the denominator, try computing $g'(x)$ and writing $f = g - g'$ (or some linear combination). This immediately gives a $1 - g'/g$ split integrating to $x - \ln g$.
