# Answer: Functional Equation: From Symmetry to a Difference

## Key Idea / Intuition

The functional equation says that if you "walk" $x \to y \to z \to x$ and sum up the $f$-values along each directed edge, you get zero — this is a cocycle condition. Such conditions always force $f$ to be a coboundary, i.e., a difference $g(x) - g(y)$. The trick is simply to **define** $g$ by fixing one argument of $f$, then verify it works by plugging into the original equation.

---

## Formal Proof / Solution

**Step 1: Define $g$.**

Fix any constant $c \in \mathbb{R}$ (say $c = 0$). Define

$$g(x) := f(x, c)$$

for all $x \in \mathbb{R}$.

**Step 2: Use the functional equation to extract $f(x,y)$.**

Apply the given identity with $z = c$:

$$f(x, y) + f(y, c) + f(c, x) = 0.$$

This gives

$$f(x, y) = -f(y, c) - f(c, x).$$

Now we need to express $f(c, x)$ in terms of $g$. Apply the identity with $x = y = z = c$:

$$3f(c, c) = 0 \implies f(c, c) = 0.$$

Apply the identity with $x \leftarrow c,\ y \leftarrow x,\ z \leftarrow c$:

$$f(c, x) + f(x, c) + f(c, c) = 0$$

$$f(c, x) + f(x, c) + 0 = 0$$

$$f(c, x) = -f(x, c) = -g(x).$$

**Step 3: Substitute back.**

$$f(x, y) = -f(y, c) - f(c, x) = -g(y) - (-g(x)) = g(x) - g(y).$$

**Step 4: Verify consistency.**

Check that $g(x) - g(y)$ satisfies the original equation:

$$(g(x) - g(y)) + (g(y) - g(z)) + (g(z) - g(x)) = 0. \checkmark$$

Thus $g(x) = f(x, c)$ is the desired function, and $f(x, y) = g(x) - g(y)$ for all $x, y \in \mathbb{R}$. $\blacksquare$

---

**Remark:** The choice of $c$ is irrelevant — if we had chosen $c'$ instead, we'd get $g'(x) = f(x, c') = g(x) - g(c')$, which differs from $g$ by a constant, and constants cancel in $g'(x) - g'(y)$.
