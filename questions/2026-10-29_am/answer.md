# Answer: The Circle Has Only One Entire Parametrization

## Key Idea / Intuition

Over $\mathbb{C}$, the circle $x^2+y^2=1$ is secretly a hyperbola. With $u = x+iy$ and $v = x-iy$ the equation becomes $uv = 1$, and this curve is just a copy of $\mathbb{C}^* = \mathbb{C}\setminus\{0\}$. So a solution $(f,g)$ is the same thing as an entire function $u = f+ig$ that never vanishes. Every nonvanishing entire function is $e^{(\text{entire})}$, because $\exp:\mathbb{C}\to\mathbb{C}^*$ is the universal cover and $\mathbb{C}$ is simply connected. Unwinding $u = e^{ih}$ forces $f=\cos h$ and $g = \sin h$.

---

## Formal Proof / Solution

**Answer.** The solutions are exactly
$$
f = \cos h, \qquad g = \sin h, \qquad h \text{ an arbitrary entire function}.
$$
The function $h$ is unique up to adding a constant $2\pi k$, $k\in\mathbb{Z}$.

**Step 1: Factor.** Since $f^2+g^2 = (f+ig)(f-ig)$, the equation reads
$$
(f+ig)(f-ig) = 1 .
$$
Set $u = f+ig$ and $v = f-ig$. Both are entire, and $uv \equiv 1$. Hence $u$ has no zeros and $v = 1/u$.

**Step 2: Take a logarithm.** $u$ is entire and nowhere zero, so $u'/u$ is entire. Since $\mathbb{C}$ is simply connected, $u'/u$ has an entire primitive $L$. Then
$$
\left(u e^{-L}\right)' = (u' - u L') e^{-L} = 0 .
$$
So $u = c\,e^{L}$ with $c \neq 0$. Absorbing $c$ into $L$ gives $u = e^{\tilde L}$ for an entire $\tilde L$. Write $\tilde L = i h$, which defines the entire function $h = -i\tilde L$. Then
$$
f + i g = e^{ih}, \qquad f - i g = e^{-ih}.
$$

**Step 3: Solve the linear system.** Adding and subtracting the two equations gives
$$
f = \frac{e^{ih}+e^{-ih}}{2} = \cos h, \qquad g = \frac{e^{ih}-e^{-ih}}{2i} = \sin h .
$$

**Step 4: Converse and uniqueness.** For any entire $h$, the identity $\cos^2 h + \sin^2 h = 1$ holds pointwise, so every such pair is a solution. Now suppose $e^{ih_1} = e^{ih_2}$. Then $h_1 - h_2$ is a continuous function taking values in the discrete set $2\pi\mathbb{Z}$. Since $\mathbb{C}$ is connected, it is constant. $\blacksquare$

So there are no exotic solutions. Every entire map of $\mathbb{C}$ into the complex circle factors through the "angle" map $h \mapsto (\cos h, \sin h)$.

---

## Follow-up: $f^n + g^n = 1$ for $n \ge 3$

For $n\ge 3$ the only entire solutions are **constants**.

Suppose $f^n+g^n=1$ and $g\not\equiv 0$. Let $\varphi = f/g$, which is meromorphic on $\mathbb{C}$. The equation becomes
$$
g^n(\varphi^n + 1) = 1 .
$$
Consider the values $\zeta$ with $\zeta^n = -1$:

- Where $g \neq 0$, we cannot have $\varphi^n = -1$, since then the left side would be $0$.
- Where $g = 0$, we have $f^n = 1$, so $f \neq 0$ and $\varphi = \infty$.

So $\varphi$ omits all $n$ roots of $\zeta^n=-1$. By Picard's theorem for meromorphic functions, a meromorphic function on $\mathbb{C}$ omitting $3$ values is constant. For $n\ge3$ this gives $\varphi \equiv c$. Then $g^n(c^n+1)=1$, so $g$ is constant, and therefore $f$ is constant too.

For $n=2$, $\varphi$ omits only the two values $\pm i$, so Picard gives no obstruction. Indeed $\varphi = \cot h$ in that case.

Geometrically, the Fermat curve $x^n+y^n=1$ has genus $(n-1)(n-2)/2$. For $n=2$ this is genus $0$, a punctured sphere $\cong \mathbb{C}^*$, which is covered by $\mathbb{C}$. For $n \ge 3$ the curve is hyperbolic, and Picard-type theorems forbid nonconstant entire curves in it.
