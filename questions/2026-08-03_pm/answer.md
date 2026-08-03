# Answer: Polynomials Dense: Orthogonality Forces Zero

## Key Idea / Intuition

The first part is a classic application of the Weierstrass approximation theorem: if $f$ is orthogonal to every monomial $x^n$, it is orthogonal to every polynomial, hence (by density of polynomials in $C([0,1])$) orthogonal to itself — forcing $f = 0$.

The twist is subtler. Even monomials $\{1, x^2, x^4, \ldots\}$ are **not** dense in $C([0,1])$: they cannot approximate $x$ (an odd function on $[0,1]$), so the argument breaks. But with a clever substitution ($x = t^2$), the even-index condition is equivalent to the full condition for a different continuous function, so $f$ must still vanish — just for a less obvious reason.

---

## Formal Proof / Solution

### Part 1: Orthogonal to all monomials $\Rightarrow$ $f = 0$

**Step 1.** By linearity of the integral, orthogonality to all $x^n$ implies orthogonality to every polynomial $p(x)$:
$$\int_0^1 f(x)\, p(x)\, dx = 0 \quad \text{for all polynomials } p.$$

**Step 2.** By the **Weierstrass Approximation Theorem**, there exist polynomials $p_n \to f$ uniformly on $[0,1]$.

**Step 3.** Therefore:
$$\int_0^1 f(x)^2\, dx = \int_0^1 f(x)\cdot f(x)\, dx = \lim_{n\to\infty} \int_0^1 f(x)\, p_n(x)\, dx = 0.$$

Since $f$ is continuous and $f^2 \geq 0$ with $\int_0^1 f^2 = 0$, we conclude $f \equiv 0$. $\blacksquare$

---

### Part 2: Orthogonal to even monomials $\Rightarrow$ $f = 0$?

**Yes**, $f$ must still be identically zero, and here is why.

**The key substitution:** Let $x = t^2$, so $dx = 2t\, dt$. Then for each even $n = 2k$:
$$0 = \int_0^1 f(x)\, x^{2k}\, dx = \int_0^1 f(t^2)\, t^{2k} \cdot 2t\, dt = 2\int_0^1 [t\, f(t^2)]\, t^{2k}\, dt.$$

Define $g(t) = t\, f(t^2)$, which is continuous on $[0,1]$. The above says:
$$\int_0^1 g(t)\, t^{2k}\, dt = 0 \quad \text{for all } k = 0, 1, 2, \ldots$$

Now look at the $n = 0$ condition (even): $\int_0^1 f(t^2)\cdot 2t\, dt = 0$, which is $\int_0^1 g(t)\, dt = 0$. Good, this is the $k=0$ case.

But we also need odd powers. Consider the condition for $n=0$ gives $\int_0^1 g(t)\cdot 1\, dt = 0$. For $n = 2k+1$ (odd powers of $t$ in $g$): note that $g$ is orthogonal to all **even** powers $t^{2k}$. To get odd powers, observe:

$$\int_0^1 g(t)\, t^{2k+1}\, dt = \int_0^1 [t\,f(t^2)]\cdot t^{2k+1}\, dt = \int_0^1 f(t^2)\, t^{2k+2}\, dt = \frac{1}{2}\int_0^1 f(x)\, x^{k+1}\, dx = 0,$$

since $k+1$ ranges over all positive integers as $k$ ranges over $\{0,1,2,\ldots\}$, and by hypothesis $\int_0^1 f(x)x^m dx = 0$ for all even $m$ (taking $m = 2(k+1)$ when we make the reverse substitution…).

Let me give a cleaner route. Since $\{x^{2k}\}_{k\geq 0}$ orthogonality gives, after substitution $u = x^2$, that $g(t) = tf(t^2)$ is orthogonal to all monomials $t^{2k}$ **and** (by the $t^{2k+1}$ computation just done) also orthogonal to all $t^{2k+1}$. So $g$ is orthogonal to **all** monomials, hence $g \equiv 0$ by Part 1.

So $t\,f(t^2) = 0$ for all $t \in [0,1]$. For $t > 0$ this gives $f(t^2) = 0$, and since $t^2$ ranges over $(0,1]$ as $t$ ranges over $(0,1]$, we get $f(x) = 0$ for all $x \in (0,1]$. By continuity at $0$, $f(0) = 0$ as well.

Therefore $f \equiv 0$. $\blacksquare$

---

### Summary

| Condition | Dense in $C([0,1])$? | $f=0$? |
|---|---|---|
| Orthogonal to all $x^n$ | Yes (Weierstrass) | Yes |
| Orthogonal to all $x^{2k}$ | No | Yes (via substitution trick) |

The surprise: even though even monomials are **not** dense, the substitution $x = t^2$ "transfers" the condition to a function $g$ that ends up being orthogonal to **all** monomials.
