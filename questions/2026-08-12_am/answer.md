# Answer: The Clumsy Chemist's Cousin: Breaking at Two Random Points

## Key Idea / Intuition

For three lengths to form a triangle, each piece must be **strictly less than 1/2** (by the triangle inequality: the longest side must be less than the sum of the other two, which is equivalent to it being less than half the total length). So we need all three pieces shorter than 1/2. The sample space is a unit square, and the favorable region is a clean geometric shape inside it — the answer drops out as a ratio of areas.

---

## Formal Proof / Solution

**Setup.** Let the two break points be $U$ and $V$, chosen independently and uniformly on $[0,1]$. The three piece lengths depend on the order of $U$ and $V$.

Without loss of generality, let $X = \min(U,V)$ and $Y = \max(U,V)$. The three pieces have lengths:
$$a = X, \quad b = Y - X, \quad c = 1 - Y.$$

**Triangle condition.** Three lengths $a, b, c$ with $a+b+c = 1$ form a triangle if and only if each is **strictly less than** $1/2$:
$$a < \tfrac{1}{2}, \quad b < \tfrac{1}{2}, \quad c < \tfrac{1}{2}.$$

(If any piece were $\geq 1/2$, it would exceed the sum of the other two.)

**Geometric probability.** Work directly with $(U, V)$ in the unit square $[0,1]^2$. The three piece lengths are:
$$\text{smallest}, \quad \text{middle}, \quad \text{largest} \quad \text{(in some order)},$$
but we can write the triangle inequalities directly in terms of $U$ and $V$:

- **Case 1: $U < V$.**  Pieces are $U$, $V-U$, $1-V$. Conditions:
$$U < \tfrac{1}{2}, \quad V - U < \tfrac{1}{2}, \quad 1 - V < \tfrac{1}{2}.$$
This means $U < 1/2$, $V > 1/2$, and $V - U < 1/2$ (i.e., $V < U + 1/2$).

- **Case 2: $V < U$.** By symmetry, identical area.

**Area computation for Case 1** (the triangle $U < V$ occupies half the square):

The region in $[0,1]^2$ with $U < V$ satisfying all three conditions:
$$0 < U < \tfrac{1}{2}, \quad \tfrac{1}{2} < V < 1, \quad V < U + \tfrac{1}{2}.$$

This is the intersection of:
- The strip $0 < U < 1/2$
- The strip $1/2 < V < 1$  
- Below the line $V = U + 1/2$

The vertices of this region are:
- $U=0, V=1/2$ to $U=1/2, V=1/2$ (bottom edge, but $V$ must be $> 1/2$)
- The line $V = U + 1/2$ hits $V = 1/2$ at $U=0$ and hits $V=1$ at $U = 1/2$.

So the region is a **triangle** with vertices $(0, 1/2)$, $(1/2, 1/2)$, $(1/2, 1)$... wait, let's verify: at $U=1/2$, $V$ must satisfy $V > 1/2$ and $V < 1/2 + 1/2 = 1$, so $V \in (1/2, 1)$. At $U = 0$: $V \in (1/2, 1/2)$ — empty! The line $V = U + 1/2$ and the boundary $V = 1/2$ meet at $U=0$.

The region is a triangle with vertices $(0, 1/2)$, $(1/2, 1/2)$, $(1/2, 1)$, area $= \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$.

**Total probability:**

By symmetry, Case 2 ($V < U$) contributes another $1/8$. So:
$$P(\text{triangle}) = \frac{1/8 + 1/8}{1} = \boxed{\frac{1}{4}}.$$

**Sanity check via the principle of symmetry:** The three pieces are exchangeable (same marginal distribution by the symmetry principle). The event "piece $i \geq 1/2$" has probability $1/2 \cdot 1/2 = 1/4$... actually the slickest check is: the complement (at least one piece $\geq 1/2$) has probability $3/4$, since by symmetry each of the three pieces exceeds $1/2$ with probability $1/4$, and these events are mutually exclusive (only one piece can be $\geq 1/2$ at a time). So $P(\text{triangle}) = 1 - 3 \cdot \frac{1}{4} = \frac{1}{4}$. ✓

**The elegant quick argument:** The three pieces all lie in $[0,1]$ with sum 1. Each piece exceeds $1/2$ with probability $1/4$ (it's the largest of three uniform order statistics, or just: $P(a \geq 1/2) = P(U < 1/2, V < 1/2 \text{ both below} \ldots)$ — computed directly). The events "piece $i$ is too long" are **mutually exclusive**, so:
$$P(\text{no triangle}) = 3 \times \frac{1}{4} = \frac{3}{4}, \quad P(\text{triangle}) = \frac{1}{4}.$$
