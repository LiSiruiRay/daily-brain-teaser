# Answer: Nonnegative Polynomials Are Sums of Squares

## Key Idea / Intuition

A nonnegative real polynomial should be a squared modulus $|h(x)|^2$ of some complex polynomial $h$, just as a nonnegative real number is $|z|^2$.

- The non-real roots of $p$ come in conjugate pairs. Put one root from each pair into $h$.
- The real roots must have even multiplicity, so put half of each into $h$.

Then $p = h\,\bar h$. Writing $h = t + iu$ with $t, u$ real polynomials gives $p = t^2 + u^2$. That is exactly two squares.

---

## Formal Proof / Solution

If $p \equiv 0$, take $f_1 = 0$. Assume from now on that $p \not\equiv 0$.

**Step 1: Real roots have even multiplicity.**

Let $r$ be a real root of multiplicity $m$. Write $p(x) = (x-r)^m g(x)$ with $g(r) \neq 0$.

- By continuity, $g$ has constant sign near $r$.
- If $m$ were odd, $(x-r)^m$ would change sign at $r$, so $p$ would too. This contradicts $p \ge 0$.

Hence $m$ is even.

**Step 2: The leading coefficient is positive.**

As $x \to +\infty$, the sign of $p(x)$ is the sign of its leading coefficient $a$. Since $p \ge 0$, we get $a > 0$.

**Step 3: Factor $p$.**

Over $\mathbb{C}$, the non-real roots of a real polynomial come in conjugate pairs $\alpha_j, \bar\alpha_j$. Combining this with Step 1, we can write

$$p(x) = a\, s(x)^2 \prod_{j=1}^{k} (x-\alpha_j)(x-\bar\alpha_j).$$

Here $s(x)$ is a real monic polynomial carrying half of each real root's multiplicity.

**Step 4: Choose "half" of $p$.**

Define the complex polynomial

$$h(x) = \sqrt{a}\; s(x) \prod_{j=1}^{k} (x - \alpha_j).$$

Let $\bar h$ denote the polynomial obtained by conjugating every coefficient of $h$. Then

$$\bar h(x) = \sqrt{a}\; s(x) \prod_{j=1}^{k} (x - \bar\alpha_j),$$

and therefore, as an identity of polynomials,

$$h(x)\,\bar h(x) = p(x).$$

**Step 5: Split into real and imaginary parts.**

Separate the real and imaginary parts of the coefficients: $h(x) = t(x) + i\,u(x)$ with $t, u \in \mathbb{R}[x]$. Then $\bar h(x) = t(x) - i\,u(x)$, so

$$p(x) = h\bar h = (t + iu)(t - iu) = t(x)^2 + u(x)^2.$$

This proves the statement, including the bonus, with $f_1 = t$ and $f_2 = u$. $\blacksquare$

---

### Alternative argument (more squares, no complex numbers)

Use induction on the degree.

- If $p$ has a real root, factor out $(x-r)^2$ and apply induction to the quotient.
- If $p$ has no real root, then $p > 0$ everywhere and $p \to +\infty$ at $\pm\infty$. So $p$ attains a minimum value $c > 0$.
- The polynomial $p - c$ is nonnegative and has a real root, so it is a sum of squares by the first case.
- Then $p = (p - c) + (\sqrt c)^2$ is also a sum of squares.

This gives some $k$, but not necessarily $k = 2$. You can also reach two squares from it by repeatedly applying the identity

$$(a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2,$$

which is just $|z|^2|w|^2 = |zw|^2$ in disguise.

### Remark: two variables

The answer to "food for thought" is no. Motzkin's polynomial

$$M(x,y) = x^4y^2 + x^2y^4 - 3x^2y^2 + 1$$

is nonnegative everywhere, by AM–GM applied to $x^4y^2,\ x^2y^4,\ 1$. However, it is **not** a sum of squares of polynomials.

Hilbert's 17th problem asked whether every nonnegative polynomial is a sum of squares of *rational functions*. Artin proved that it is (1927). The one-variable argument above works because $\mathbb{C}[x]$ factors completely into linear factors.
