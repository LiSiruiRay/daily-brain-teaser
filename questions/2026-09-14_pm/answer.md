# Answer: Orthogonality to Monomials: Missing n=0

## Key Idea / Intuition

For the first part, the Weierstrass Approximation Theorem says polynomials are dense in $C([0,1])$, so if $f$ is orthogonal to every polynomial, it must be orthogonal to itself — forcing $f = 0$. For the second part, the subtlety is that we're missing the constant term. A function can vanish against all monomials $x, x^2, x^3, \ldots$ without being zero, provided its "net area" compensates. The function $f(x) = 1 - (n+1)x^n$ for appropriate $n$ won't work directly, but $f(x) = 1$ against $x^n$ for $n \geq 1$ gives $\int_0^1 x^n dx = \frac{1}{n+1} \neq 0$, so that fails too. The real key: for the second condition, $f \equiv 0$ is **still** forced, because $\{x^n : n \geq 1\}$ together with the missing constant is enough — specifically, the linear span of $\{x, x^2, \ldots\}$ is dense in $\{g \in C([0,1]) : g(0) = 0\}$, but by a continuity trick we can still conclude $f = 0$.

---

## Formal Proof / Solution

### Part 1: All $n \geq 0$

If $\int_0^1 f(x) x^n dx = 0$ for all $n \geq 0$, then by linearity, $\int_0^1 f(x) p(x)\, dx = 0$ for every polynomial $p$.

By the **Weierstrass Approximation Theorem**, there exist polynomials $p_k \to f$ uniformly on $[0,1]$. Then:
$$\int_0^1 f(x)^2\, dx = \lim_{k \to \infty} \int_0^1 f(x)\, p_k(x)\, dx = 0.$$

Since $f$ is continuous and $f^2 \geq 0$, we conclude $f \equiv 0$. $\checkmark$

---

### Part 2: All $n \geq 1$ only

**Claim:** $f \equiv 0$ is still forced.

**Proof.** The hypothesis gives $\int_0^1 f(x) x^n dx = 0$ for all $n \geq 1$.

**Step 1.** By linearity, $\int_0^1 f(x) q(x)\, dx = 0$ for every polynomial $q$ with **zero constant term**, i.e., $q(0) = 0$.

**Step 2.** Consider the function $g(x) = f(x) - c$ where $c = \int_0^1 f(x)\, dx$ is the "missing" piece. We don't directly control $c$, but we can use a different trick.

**Better approach.** Apply the substitution or use the fact that $x \mapsto x \cdot p(x)$ spans $\{$polynomials vanishing at $0\}$.

Polynomials $x, x^2, x^3, \ldots$ span a space that is dense in

$$\mathcal{A} = \{g \in C([0,1]) : g(0) = 0\}$$

by Weierstrass (approximate any $g$ with $g(0)=0$ by polynomials, then subtract the constant term — but the constant term is $g(0) = 0$, so the approximating polynomials can be taken to vanish at 0 by subtracting a small correction).

So we can find polynomials $q_k(x) = \sum_{j=1}^{m_k} a_j^{(k)} x^j$ (no constant term) with $q_k \to f(\cdot)$ uniformly... but wait, this would require $f(0) = \lim q_k(0) = 0$.

**We do not know $f(0) = 0$.** So we must be more careful.

**Correct Argument.** We know:

$$\int_0^1 f(x) x^n\, dx = 0 \quad \forall n \geq 1.$$

This means $f$ is orthogonal to $\{x, x^2, x^3, \ldots\}$ in $L^2([0,1])$.

Now take $n = 1$: $\int_0^1 x f(x)\, dx = 0$.

By the same Weierstrass argument applied to $x \cdot f(x)$: the function $h(x) = x f(x)$ satisfies $\int_0^1 h(x) x^{n-1} dx = 0$ for all $n \geq 1$, i.e., $\int_0^1 h(x) x^m\, dx = 0$ for all $m \geq 0$.

By Part 1, $h(x) = x f(x) \equiv 0$ on $[0,1]$.

Since $x f(x) = 0$ for all $x \in [0,1]$ and $x \neq 0$ on $(0,1]$, we get $f(x) = 0$ for all $x \in (0,1]$. By continuity of $f$, also $f(0) = 0$.

Therefore $f \equiv 0$. $\blacksquare$

---

### Summary

| Condition | Conclusion |
|-----------|-----------|
| $\int_0^1 f x^n dx = 0$ for $n \geq 0$ | $f \equiv 0$ via Weierstrass directly |
| $\int_0^1 f x^n dx = 0$ for $n \geq 1$ | $f \equiv 0$ via the trick $h(x) = xf(x)$, reducing to Part 1 |

The elegant trick: multiplying by $x$ shifts the index, turning "missing $n=0$" into "having all $n \geq 0$" for the product $xf(x)$.
