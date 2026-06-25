# Answer: Riemann's Removable Singularity via zf(z)→0

## Key Idea / Intuition

The condition $z f(z) \to 0$ is exactly what forces the singularity to be "fake." The trick is to construct a function $g(z) = z^2 f(z)$ that is holomorphic on the entire disk *including* the origin — we can verify differentiability at $z=0$ directly from the limit condition. Once we know $g$ is holomorphic and vanishes to second order at $0$, we can write $g(z) = z^2 h(z)$ for some holomorphic $h$, and then $h$ is the desired extension of $f$.

---

## Formal Proof / Solution

**Step 1: Define $g$ and show it is holomorphic on the full disk.**

Set
$$g(z) = \begin{cases} z^2 f(z) & z \neq 0, \\ 0 & z = 0. \end{cases}$$

For $z \neq 0$, $g$ is holomorphic (product of holomorphic functions). We need to check complex differentiability at $z = 0$.

Compute the difference quotient at the origin:
$$\frac{g(z) - g(0)}{z - 0} = \frac{z^2 f(z)}{z} = z f(z).$$

By hypothesis, $z f(z) \to 0$ as $z \to 0$. Therefore:
$$g'(0) = \lim_{z \to 0} \frac{g(z) - g(0)}{z} = \lim_{z \to 0} z f(z) = 0.$$

So $g$ is holomorphic on the entire disk $D(0, r)$, with $g(0) = 0$ and $g'(0) = 0$.

**Step 2: Factor out $z^2$ from $g$.**

Since $g$ is holomorphic on $D(0, r)$ with $g(0) = g'(0) = 0$, its Taylor series at $0$ has no constant or linear term:
$$g(z) = \sum_{n=2}^{\infty} a_n z^n = z^2 \sum_{n=0}^{\infty} a_{n+2} z^n.$$

Define
$$h(z) = \sum_{n=0}^{\infty} a_{n+2} z^n,$$
which converges on $D(0, r)$ and is holomorphic there.

**Step 3: Conclude that $h$ extends $f$.**

For $z \neq 0$:
$$h(z) = \frac{g(z)}{z^2} = \frac{z^2 f(z)}{z^2} = f(z).$$

So $h$ is a holomorphic function on all of $D(0, r)$ that agrees with $f$ on the punctured disk. The singularity is removable. $\blacksquare$

---

**Remark:** The classical statement of Riemann's theorem assumes only that $f$ is *bounded* near $0$. Boundedness implies $zf(z) \to 0$ (since $|zf(z)| \leq |z| \cdot M \to 0$), so the condition here is slightly weaker — it is in fact the sharp condition for removability.
