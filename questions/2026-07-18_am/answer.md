# Answer: Integral of ln(1+x)/(1+x²) via Feynman

## Key Idea / Intuition

This integral looks intimidating — you have a logarithm sitting over a rational function with no obvious antiderivative. The magic move is to introduce a **parameter** $a$ into the log and differentiate under the integral sign (Feynman's trick). Choosing $a$ cleverly turns a hard integral into a tractable one involving $\arctan$, and the answer comes out to a beautiful combination of $\pi$ and $\ln 2$.

---

## Formal Proof / Solution

**Step 1: Introduce a parameter.**

Define

$$I(a) = \int_0^1 \frac{\ln(1+ax)}{1+x^2}\,dx, \quad a \in [0,1].$$

We want $I(1)$. Note $I(0) = 0$.

**Step 2: Differentiate under the integral sign.**

$$I'(a) = \int_0^1 \frac{x}{(1+ax)(1+x^2)}\,dx.$$

**Step 3: Partial fractions.**

Decompose $\dfrac{x}{(1+ax)(1+x^2)}$. Write

$$\frac{x}{(1+ax)(1+x^2)} = \frac{A}{1+ax} + \frac{Bx + C}{1+x^2}.$$

Multiplying out and matching coefficients:

- From $1+ax = 0$ (i.e., $x = -1/a$): numerator $= -1/a$, denominator factor $1 + 1/a^2$, so $A = \dfrac{-1/a}{1+1/a^2} = \dfrac{-a}{1+a^2}$.

- Matching leading coefficient of $x^2$: $Aa^2 + B \cdot a \cdot 1 = 0$ isn't the cleanest route. Let's match directly.

$$x = A(1+x^2) + (Bx+C)(1+ax).$$

Set $x=0$: $0 = A + C$, so $C = -A = \dfrac{a}{1+a^2}$.

Set $x=1$: $1 = 2A + (B+C)(1+a)$.

Set $x=-1$: $-1 = 2A + (-B+C)(1-a)$.

Adding both equations: $0 = 4A + 2C(1-a^2)/(?)$... let's just match coefficients of $x^2$: coefficient of $x^2$ on the right is $A + Ba$, on the left is $0$, so $B = -A/a = \dfrac{1}{1+a^2}$.

Thus:

$$\frac{x}{(1+ax)(1+x^2)} = \frac{-a}{1+a^2}\cdot\frac{1}{1+ax} + \frac{1}{1+a^2}\cdot\frac{x}{1+x^2} + \frac{a}{1+a^2}\cdot\frac{1}{1+x^2}.$$

**Step 4: Integrate each piece from 0 to 1.**

$$I'(a) = \frac{1}{1+a^2}\left[-a\cdot\frac{\ln(1+ax)}{a}\Bigg|_0^1 + \frac{\ln(1+x^2)}{2}\Bigg|_0^1 + a\arctan(x)\Bigg|_0^1\right]$$

$$= \frac{1}{1+a^2}\left[-\ln(1+a) + \frac{\ln 2}{2} + \frac{\pi a}{4}\right].$$

**Step 5: Integrate $I'(a)$ from 0 to 1.**

$$I(1) = \int_0^1 \frac{-\ln(1+a) + \frac{\ln 2}{2} + \frac{\pi a}{4}}{1+a^2}\,da.$$

Split into three pieces:

$$I(1) = -I(1) + \frac{\ln 2}{2}\cdot\frac{\pi}{4} + \frac{\pi}{4}\cdot\frac{\ln 2}{2},$$

where we used $\int_0^1 \dfrac{da}{1+a^2} = \dfrac{\pi}{4}$, $\int_0^1 \dfrac{a}{1+a^2}\,da = \dfrac{\ln 2}{2}$, and $\int_0^1 \dfrac{\ln(1+a)}{1+a^2}\,da = I(1)$.

So:

$$I(1) = -I(1) + \frac{\pi \ln 2}{8} + \frac{\pi \ln 2}{8}.$$

$$2I(1) = \frac{\pi \ln 2}{4}.$$

$$\boxed{I = \frac{\pi \ln 2}{8}.}$$

---

**Why it's beautiful:** The answer $\dfrac{\pi \ln 2}{8}$ is a perfect marriage of the two great constants of calculus. The self-referential step — where $I(1)$ appears on both sides — is the satisfying click of the whole argument.
