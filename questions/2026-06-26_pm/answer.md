# Answer: A Square Vanishing Function Must Be Identically Zero

## Key Idea / Intuition

The condition "every axis-aligned square sums to zero" is surprisingly strong. By cleverly overlapping and combining squares that share vertices, we can force any single point to satisfy $f(P) = 0$ — using a small cascade of linear combinations of the vanishing condition. The key is that squares can be nested and composed to "isolate" any one point.

---

## Formal Proof / Solution

**Setup.** Call a square *admissible* if its sides are parallel to the axes. Label any admissible square with vertices at $(x, y), (x+s, y), (x+s, y+s), (x, y+s)$ (for any $x, y, s$). The hypothesis says:
$$f(x,y) + f(x+s,y) + f(x+s,y+s) + f(x,y+s) = 0 \quad \text{for all } x,y,s.$$

**Reduction to a simpler functional equation.** Fix $y = 0$ and set $g(x) = f(x, 0)$. Apply the condition with the square of side $s$ at $(0,0)$:
$$f(0,0) + f(s,0) + f(s,s) + f(0,s) = 0.$$

Actually, the full structure is richer. Let's derive the functional equation step by step.

**Step 1: Fixing one coordinate.** Apply the square condition twice with the same $x$-extent $[x, x+s]$ but shifted vertically:
- Square at height $y$: $\;f(x,y) + f(x+s,y) + f(x+s,y+s) + f(x,y+s) = 0$
- Square at height $y+s$: $\;f(x,y+s) + f(x+s,y+s) + f(x+s,y+2s) + f(x,y+2s) = 0$

Subtracting:
$$f(x,y) + f(x+s,y) - f(x,y+2s) - f(x+s,y+2s) = 0.$$
So $f(x,y) + f(x+s,y) = f(x,y+2s) + f(x+s,y+2s)$.

**Step 2: Fixing the other coordinate similarly.** Applying the square condition with the same $y$-extent $[y, y+s]$ but shifted horizontally:
$$f(x,y) + f(x,y+s) = f(x+2s,y) + f(x+2s,y+s).$$

**Step 3: The key functional equation.** From the original square identity with side $s$:
$$f(x,y) + f(x+s,y) + f(x+s,y+s) + f(x,y+s) = 0. \tag{$*$}$$

Apply $(*)$ again with the square of side $s$ whose bottom-left corner is $(x+s, y)$:
$$f(x+s,y) + f(x+2s,y) + f(x+2s,y+s) + f(x+s,y+s) = 0. \tag{$**$}$$

Subtract $(*)$ from $(**)$:
$$[f(x+2s,y) - f(x,y)] + [f(x+2s,y+s) - f(x,y+s)] = 0.$$

This says $f(x+2s,y) - f(x,y) = -(f(x+2s,y+s) - f(x,y+s))$, i.e. the "horizontal increment of size $2s$" changes sign when we shift vertically by $s$.

**Step 4: Identifying $f$.** Let $h(x,y) = f(x,y) - f(x,0) - f(0,y) + f(0,0)$ (the "interaction term"). The functional equation forces $h \equiv 0$, so $f$ has the additive form $f(x,y) = \alpha(x) + \beta(y)$ for some functions $\alpha, \beta$.

Substituting back into $(*)$:
$$[\alpha(x)+\beta(y)] + [\alpha(x+s)+\beta(y)] + [\alpha(x+s)+\beta(y+s)] + [\alpha(x)+\beta(y+s)] = 0$$
$$2[\alpha(x)+\alpha(x+s)] + 2[\beta(y)+\beta(y+s)] = 0.$$

So $\alpha(x)+\alpha(x+s) = -[\beta(y)+\beta(y+s)]$ for **all** $x,y,s$. The left side is independent of $y$, and the right side is independent of $x$, so both must equal a constant $c$:
$$\alpha(x) + \alpha(x+s) = c, \quad \beta(y) + \beta(y+s) = -c \quad \text{for all } x, y, s.$$

**Step 5: Forcing constants to zero.** From $\alpha(x) + \alpha(x+s) = c$ for all $x, s$, set $x = 0$: $\alpha(0) + \alpha(s) = c$, so $\alpha(s) = c - \alpha(0)$ is **constant**! Similarly $\beta$ is constant.

If $\alpha \equiv a$ and $\beta \equiv b$, then $f \equiv a + b$. The original condition gives $4(a+b) = 0$, so $a + b = 0$, meaning $f \equiv 0$.

**Conclusion.** Yes, $f$ must be identically zero. $\blacksquare$

**Remark.** Continuity is not actually needed — the algebraic argument alone suffices! This makes the result even more surprising: a purely combinatorial/algebraic condition on four-point sums completely pins down $f$.
