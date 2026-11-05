# Answer: Iterates Cannot Escape Fixed Points

## Key Idea / Intuition

Picard's little theorem turns "omits two values" into "is constant." So the task is to build entire functions that are forced to omit $0$ and one other value.

1. The quotient $\dfrac{f(f(z)) - z}{f(z) - z}$ omits $0$ and $1$, so it is a constant $c$.
2. Differentiating the identity $f(f(z)) - z = c\,(f(z)-z)$ produces a product that is a nonzero constant. This forces $f'\circ f$ to omit two values, so $f'\circ f$ is constant too.
3. Hence $f'$ is constant, $f$ is linear, and the only fixed-point-free linear maps are translations.

---

## Formal Proof / Solution

**($\Leftarrow$)** If $f(z) = z+b$ with $b\neq 0$, then $f(f(z)) = z + 2b \neq z$ for every $z$.

**($\Rightarrow$)** Assume $f(f(z)) \neq z$ for all $z\in\mathbb{C}$.

**Step 0: $f$ has no fixed points and is non-constant.**
- If $f(z_0) = z_0$, then $f(f(z_0)) = f(z_0) = z_0$, which is a contradiction. So $f(z) - z \neq 0$ everywhere.
- If $f \equiv b$ were constant, then $f(b) = b$ would be a fixed point. So $f$ is non-constant.

**Step 1: A quotient omitting $0$ and $1$.**
Define
$$
g(z) = \frac{f(f(z)) - z}{f(z) - z}.
$$
The denominator never vanishes, so $g$ is entire.

- $g(z) \neq 0$, because the numerator never vanishes.
- Suppose $g(z_1) = 1$. Then $f(f(z_1)) = f(z_1)$, so $w = f(z_1)$ is a fixed point of $f$. This contradicts Step 0.

So $g$ omits $0$ and $1$. By Picard, $g \equiv c$ for a constant $c \notin\{0,1\}$. Hence
$$
f(f(z)) - z = c\,\big(f(z) - z\big)\qquad\text{for all } z.
$$

**Step 2: Differentiate.**
Differentiating gives
$$
f'(f(z))\,f'(z) - 1 = c\,f'(z) - c.
$$
Rearranging,
$$
f'(z)\,\big(f'(f(z)) - c\big) = 1 - c \neq 0 .
$$
Since the product is a nonzero constant, neither factor ever vanishes:
- $f'(z) \neq 0$ for all $z$. In particular $f'$ never takes the value $0$ anywhere, including at the points $f(z)$.
- $f'(f(z)) \neq c$ for all $z$.

Therefore the entire function $h = f'\circ f$ omits both $0$ and $c$, which are distinct since $c\neq 0$. By Picard again, $h$ is constant.

**Step 3: $f'$ is constant.**
Since $f$ is non-constant, the open mapping theorem says $f(\mathbb{C})$ is a nonempty open set. The function $f'$ is constant on this open set, so by the identity theorem $f'$ is constant on all of $\mathbb{C}$. Hence
$$
f(z) = az + b .
$$

**Step 4: Pin down $a$ and $b$.**
- If $a \neq 1$, then $z = b/(1-a)$ is a fixed point of $f$. This contradicts Step 0, so $a = 1$.
- Then $f(z) = z + b$, and $b\neq 0$, again because $f$ has no fixed points.

This completes the proof. $\blacksquare$

---

**Remark.** For $f(z) = z + e^z$ the theorem guarantees a solution of $f(f(z)) = z$. Since $f(f(z)) = z + e^z + e^{z+e^z}$, this is the equation
$$
e^z + e^{z + e^z} = 0 \iff e^{e^z} = -1 \iff e^z = (2k+1)\pi i.
$$
For example, $z = \log \pi + i\pi/2$ works, and there are infinitely many such solutions.

This result is due to P. C. Rosenbloom (1952). It is the starting point of the theory of fixed points of iterates of entire functions: for transcendental entire $f$, every iterate $f^{\circ n}$ with $n\ge 2$ has infinitely many fixed points.
