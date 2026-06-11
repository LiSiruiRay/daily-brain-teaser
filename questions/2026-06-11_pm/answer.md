# Answer: Möbius Transformation Fixed by Three Points

## Key Idea / Intuition

A Möbius transformation is determined by exactly 3 degrees of freedom (since we can normalize $ad - bc = 1$, leaving 3 free complex parameters). The beautiful rigidity here is: fixing three points "uses up" all those degrees of freedom, forcing the map to be the identity. The cleanest proof works by composing two transformations: if $f$ fixes three points, then $g = f \circ (\text{identity})^{-1}$ fixes three points, and we show any such $g$ solving $g(z) = z$ as a Möbius transformation equation must be identically $z$.

---

## Formal Proof / Solution

**Step 1: Reduce to an algebraic equation.**

Suppose $f(z) = \dfrac{az+b}{cz+d}$ fixes three distinct points $z_1, z_2, z_3 \in \mathbb{C} \cup \{\infty\}$.

First handle the case $c = 0$: then $f(z) = \frac{a}{d}z + \frac{b}{d}$, an affine map. If it fixes two finite points $z_1 \neq z_2$, then
$$\frac{a}{d}z_1 + \frac{b}{d} = z_1 \quad \text{and} \quad \frac{a}{d}z_2 + \frac{b}{d} = z_2.$$
Subtracting: $\frac{a}{d}(z_1 - z_2) = z_1 - z_2$, so $\frac{a}{d} = 1$, and then $\frac{b}{d} = 0$. Thus $f(z) = z$. ✓

**Step 2: Handle the case $c \neq 0$ with three finite fixed points.**

The fixed point equation is:
$$f(z) = z \implies \frac{az+b}{cz+d} = z \implies az + b = z(cz+d) \implies cz^2 + (d-a)z - b = 0.$$

This is a **quadratic** in $z$ (since $c \neq 0$), so it has **at most 2 solutions** in $\mathbb{C}$.

But we assumed $f$ fixes three distinct points. A quadratic equation cannot have three distinct roots. **Contradiction.**

**Step 3: Handle $\infty$ as a fixed point.**

If $f(\infty) = \infty$, then as $z \to \infty$, $f(z) \to \frac{a}{c}$. For this to equal $\infty$, we need $c = 0$, which reduces to Step 1.

So if $c \neq 0$, then $f(\infty) \neq \infty$. Combined with Step 2, three fixed points with $c \neq 0$ is impossible.

**Conclusion:** In all cases, three fixed points force $f(z) = z$. $\blacksquare$

---

**Bonus: Unique determination by three points.**

Given three distinct points $z_1, z_2, z_3$ and three distinct target points $w_1, w_2, w_3$, suppose two Möbius transformations $f$ and $g$ both send $z_i \mapsto w_i$. Then the composition $h = g^{-1} \circ f$ satisfies $h(z_i) = z_i$ for $i = 1, 2, 3$. By the theorem above, $h = \text{id}$, so $f = g$.

**This also explains the explicit formula:** the unique Möbius transformation sending $z_1 \mapsto 0$, $z_2 \mapsto 1$, $z_3 \mapsto \infty$ is the **cross-ratio**:
$$f(z) = \frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)}.$$
Any other three-point mapping is obtained by composing cross-ratios.
