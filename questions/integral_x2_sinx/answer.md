# Integral of $x^2 \sin(x)$ — Answer

## Answer

$$\int x^2 \sin(x)\, dx = 2x\sin(x) - (x^2 - 2)\cos(x) + C$$

---

## Solution via Tabular Method

Set up the table: differentiate the polynomial column until it hits 0, integrate the trig column, alternate signs $+, -, +, \ldots$

| Sign | Differentiate | Integrate |
|------|--------------|-----------|
| $+$ | $x^2$ | $\sin(x)$ |
| $-$ | $2x$ | $-\cos(x)$ |
| $+$ | $2$ | $-\sin(x)$ |
| $-$ | $0$ | $\cos(x)$ |

Multiply diagonally (each row's sign × left entry × right entry of next row) and sum:

$$= (+)(x^2)(-\cos x) + (-)(2x)(-\sin x) + (+)(2)(\cos x)$$
$$= -x^2\cos(x) + 2x\sin(x) + 2\cos(x) + C$$

Factoring:
$$= 2x\sin(x) - (x^2 - 2)\cos(x) + C$$

---

## Verification

Differentiate the answer:
$$\frac{d}{dx}\left[2x\sin x - (x^2-2)\cos x\right]$$
$$= 2\sin x + 2x\cos x - 2x\cos x + (x^2-2)\sin x$$
$$= 2\sin x + (x^2-2)\sin x = x^2 \sin x \checkmark$$
