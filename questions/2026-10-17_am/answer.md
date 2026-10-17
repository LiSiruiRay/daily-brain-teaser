# Answer: Why π Is Less Than 22/7

## Key Idea / Intuition

Dividing a polynomial by $1+x^2$ leaves a polynomial quotient, which integrates to a rational number, plus a remainder over $1+x^2$, which produces $\arctan$ and hence $\pi$. The remainder is the polynomial's value at $x=i$, and $(1-i)^4 = -4$ is a real constant. So the remainder is just $-4$, and the "$\pi$ part" of the integral is exactly $-4\cdot\frac{\pi}{4} = -\pi$. The integrand is visibly positive, so $(\text{rational}) - \pi > 0$. The rational number turns out to be $22/7$.

---

## Formal Proof / Solution

**Step 1: Find the remainder without long division.**
Write $p(x) = x^4(1-x)^4 = q(x)(x^2+1) + r(x)$ with $\deg r \le 1$. Substituting $x = i$ gives

$$
r(i) = p(i) = i^4 (1-i)^4 = \big((1-i)^2\big)^2 = (-2i)^2 = -4 .
$$

Since $r$ has real coefficients, $r(i) = a i + b = -4$ forces $a = 0$ and $b = -4$. So the remainder is the constant $-4$.

**Step 2: Find the quotient.**
Expand the numerator:

$$
p(x) = x^8 - 4x^7 + 6x^6 - 4x^5 + x^4 .
$$

Then

$$
\frac{x^4(1-x)^4}{1+x^2} = x^6 - 4x^5 + 5x^4 - 4x^2 + 4 \;-\; \frac{4}{1+x^2}.
$$

Check: $(x^6 - 4x^5 + 5x^4 - 4x^2 + 4)(x^2+1) = x^8 - 4x^7 + 6x^6 - 4x^5 + x^4 + 4$. Subtracting $4$ gives $p(x)$. ✓

**Step 3: Integrate.**

$$
I = \frac17 - \frac46 + \frac55 - \frac43 + 4 - 4\arctan(1)
= \frac17 - \frac23 + 1 - \frac43 + 4 - \pi
= \frac{22}{7} - \pi .
$$

**Step 4: The inequality.**
On $(0,1)$ the integrand $\dfrac{x^4(1-x)^4}{1+x^2}$ is continuous, non-negative, and not identically zero. Hence $I > 0$, which gives

$$
\pi < \frac{22}{7}.
$$

**Step 5 (Bonus): Bracketing the error.**
On $[0,1]$ we have $1 \le 1+x^2 \le 2$, with strict inequalities on the interior. Therefore

$$
\frac12 \int_0^1 x^4(1-x)^4\,dx \;<\; I \;<\; \int_0^1 x^4(1-x)^4\,dx .
$$

The remaining integral is a Beta integral:

$$
\int_0^1 x^4(1-x)^4\,dx = B(5,5) = \frac{4!\,4!}{9!} = \frac{576}{362880} = \frac{1}{630}.
$$

Hence

$$
\frac{1}{1260} < \frac{22}{7} - \pi < \frac{1}{630},
$$

which gives $3.14127\ldots < \pi < 3.14206\ldots$.

---

### Remarks

- **Why the exponent 4?** You need $(1-i)^n$ to be real. Since $1-i = \sqrt2\,e^{-i\pi/4}$, this happens exactly when $4 \mid n$. With other exponents the remainder has an $x$-term, and integrating it produces a $\ln 2$ alongside $\pi$.
- **Generalization (Lucas, 2005):** The integrals $\displaystyle\int_0^1 \frac{x^{4n}(1-x)^{4n}}{1+x^2}\,dx$ all equal (rational) $\pm\,\pi$, up to a power-of-4 factor. As $n$ grows they give increasingly sharp rational approximations to $\pi$.
- **Sources:** Putnam 1968, Problem A1; D. P. Dalzell, *J. London Math. Soc.* 19 (1944).
