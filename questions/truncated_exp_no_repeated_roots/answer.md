# Truncated Exponential Has No Repeated Roots — Answer

## Key Identity

Observe that consecutive truncated exponentials differ by exactly one term:
$$p_n(x) = p_{n-1}(x) + \frac{x^n}{n!} \tag{$*$}$$

And differentiating $p_n$ gives:
$$p_n'(x) = p_{n-1}(x) \tag{$**$}$$

---

## Proof

Suppose $r \in \mathbb{R}$ is a **repeated root** of $p_n$. Then:

$$p_n(r) = 0 \quad \text{and} \quad p_n'(r) = 0$$

From $(**)$: $p_n'(r) = p_{n-1}(r) = 0$.

Substituting both $p_n(r) = 0$ and $p_{n-1}(r) = 0$ into $(*)$:
$$0 = 0 + \frac{r^n}{n!}$$

So $r^n = 0$, which forces $r = 0$.

But $p_n(0) = 1 \neq 0$, contradicting $p_n(r) = 0$. $\blacksquare$

---

## Why the Identity $(*)$ Is the Right Tool

A repeated root $r$ of a polynomial $f$ is a common root of $f$ and $f'$. Normally, finding $\gcd(f, f')$ requires the Euclidean algorithm. Here, the relationship $p_n' = p_{n-1}$ means $f'$ is almost $f$ itself — just with the leading term removed. That's what makes $(*)$ lethal: it directly computes $f - \text{(leading term)} = f'$, so any common root must kill the leading term.

---

## Bonus: Behavior of Roots

- For $n$ odd: $p_n(x) \to \pm\infty$ as $x \to \pm\infty$, so $p_n$ has at least one real root (in fact, exactly one).
- For $n$ even: $p_n(x) \to +\infty$ as $x \to \pm\infty$, and $p_n > 0$ everywhere (since the minimum of $e^x - p_n(x)$, which is $\sum_{k>n} x^k/k!$, is non-negative for even $n$ and $x \geq 0$). So $p_n$ has no real roots at all when $n$ is even.

In all cases, no real root is repeated.
