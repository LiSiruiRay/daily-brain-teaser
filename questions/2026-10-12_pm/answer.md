# Answer: The Function That Is Its Own Average

## Key Idea / Intuition

The condition says $f(x)$ equals the running average of itself. Intuitively, if a continuous function always equals its own average over $[0,x]$, it must be "flat" — any deviation from a constant would break the averaging condition. The key move is to differentiate both sides and watch the function force itself to be constant.

---

## Formal Proof / Solution

**Step 1: Rewrite the condition.**

Define $F(x) = \int_0^x f(t)\, dt$. The condition says:

$$F(x) = x \cdot f(x) \quad \text{for all } x \in (0,1].$$

**Step 2: Differentiate both sides.**

Since $f$ is continuous, $F$ is differentiable and $F'(x) = f(x)$. Differentiating $F(x) = x f(x)$:

$$f(x) = f(x) + x f'(x).$$

This simplifies to:

$$x f'(x) = 0 \quad \text{for all } x \in (0,1].$$

Since $x > 0$, we conclude $f'(x) = 0$ for all $x \in (0,1]$.

**Step 3: Conclude.**

$f'(x) = 0$ on $(0,1]$ means $f$ is constant on $(0,1]$. By continuity of $f$ at $0$, the constant extends to $x=0$ as well. Hence:

$$\boxed{f \equiv c \text{ for some constant } c \in \mathbb{R}.}$$

**Step 4: Verify.**

Any constant function $f \equiv c$ satisfies $\frac{1}{x}\int_0^x c\, dt = c$. ✓

**Remark:** Note also that continuity at $x=0$ is needed: we need $f(0) = \lim_{x \to 0^+} f(x)$ to be well-defined, which is guaranteed by the hypothesis.
