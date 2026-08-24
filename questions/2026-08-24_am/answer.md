# Answer: The Continuous Function That Must Change Sign

## Key Idea / Intuition

The two integral conditions say that $f$ is orthogonal to both the constant function $1$ and to $x$. If $f$ had **at most one** sign change, it would look roughly like a single-signed bump or a function that crosses zero once — and you can show that any such function cannot be simultaneously orthogonal to both $1$ and $x$ unless it is identically zero. The trick is to construct a witness: a linear function $\ell(x) = a + bx$ that has the same sign pattern as $f$, making $\int_0^1 f \cdot \ell \, dx$ forced to be positive — but the two conditions say this integral is exactly zero, giving a contradiction.

---

## Formal Proof / Solution

**Claim:** Yes, $f$ must have at least two sign changes (provided $f \not\equiv 0$).

**Proof by contradiction.** Suppose $f$ is continuous, not identically zero, satisfies both integral conditions, but has **at most one** sign change on $(0,1)$.

### Case 1: $f$ has no sign change.

Then $f$ is either $\geq 0$ or $\leq 0$ on all of $[0,1]$ (with at least one point of strict sign, since $f\not\equiv 0$). But then $\int_0^1 f(x)\,dx \neq 0$, contradicting the first condition. ✗

### Case 2: $f$ has exactly one sign change at $c \in (0,1)$.

Without loss of generality, suppose $f(x) > 0$ on $(0,c)$ and $f(x) < 0$ on $(c,1)$ (the other case is symmetric).

Now choose the linear function
$$\ell(x) = x - c.$$

Note $\ell(x) = x - c$ satisfies:
- $\ell(x) < 0$ for $x \in (0, c)$,
- $\ell(x) > 0$ for $x \in (c, 1)$.

This is the **opposite** sign pattern to $f$. Therefore $f(x)\cdot \ell(x) \leq 0$ everywhere on $[0,1]$, and $f(x)\cdot\ell(x) < 0$ on a set of positive measure. Hence:
$$\int_0^1 f(x)\ell(x)\,dx < 0.$$

But expanding using linearity:
$$\int_0^1 f(x)\ell(x)\,dx = \int_0^1 f(x)(x - c)\,dx = \int_0^1 xf(x)\,dx - c\int_0^1 f(x)\,dx = 0 - c\cdot 0 = 0.$$

This is a **contradiction**: the integral must be strictly negative, but we computed it equals $0$.

### Conclusion

In both cases we reach a contradiction. Therefore $f$ must have **at least two** sign changes on $(0,1)$. $\blacksquare$

---

**Remark (geometric picture):** The two conditions $\int f = 0$ and $\int xf = 0$ say $f$ is orthogonal to all linear polynomials in $L^2([0,1])$. By the general principle, orthogonality to polynomials of degree $\leq n-1$ forces at least $n$ sign changes — this is a soft version of the **Chebyshev equioscillation** / **Descartes' rule** philosophy. Here $n=2$ (orthogonal to $\{1, x\}$), forcing $\geq 2$ sign changes.
