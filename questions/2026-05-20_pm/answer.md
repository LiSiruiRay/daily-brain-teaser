# Answer: Broken Bar Triangle Probability

## Key Idea / Intuition

The three pieces form a triangle exactly when no single piece is "too long" — specifically, each piece must be strictly less than $1/2$ (the triangle inequality forces this). The sample space is a unit square, and we need to find the area of the region where all three resulting lengths are less than $1/2$. The geometry turns out to be elegant: the "bad" regions (where one piece is $\geq 1/2$) are three non-overlapping triangles, each of area $1/4$, leaving probability $1/4$ for success.

---

## Formal Proof / Solution

**Setup.** Let the two break points be $U$ and $V$, chosen independently and uniformly on $[0,1]$. The sample space is the unit square $[0,1]^2$.

Without loss of generality, let $x = \min(U,V)$ and $y = \max(U,V)$. Then the three pieces have lengths:
$$a = x, \quad b = y - x, \quad c = 1 - y.$$

**Triangle condition.** Three lengths form a triangle iff each length is strictly less than the sum of the other two — for lengths summing to 1, this is equivalent to:
$$a < \tfrac{1}{2}, \quad b < \tfrac{1}{2}, \quad c < \tfrac{1}{2}.$$

**Working directly in $(U,V)$ coordinates.** Rather than conditioning on the ordering, work directly on the full unit square. Let $U$ and $V$ be the two break points (unordered). The three pieces are:

- $\min(U,V)$
- $|U - V|$
- $1 - \max(U,V)$

The triangle condition becomes:
$$U < \tfrac{1}{2}, \quad V < \tfrac{1}{2}, \quad |U - V| < \tfrac{1}{2}, \quad \min(U,V) < \tfrac{1}{2}, \quad 1 - \max(U,V) < \tfrac{1}{2}.$$

More cleanly, if we let $x = \min(U,V), y = \max(U,V)$, the three conditions are:

$$x < \frac{1}{2}, \qquad y - x < \frac{1}{2}, \qquad 1 - y < \frac{1}{2}.$$

This is equivalent to working on the triangle $0 \le x \le y \le 1$ (area $= 1/2$) and finding the sub-region satisfying all three inequalities.

**Geometric computation.** The favorable region in the ordered triangle $\{0 \le x \le y \le 1\}$ is:
$$x < \frac{1}{2}, \qquad y > \frac{1}{2}, \qquad y - x < \frac{1}{2}.$$

This is a small triangle with vertices at $\left(\frac{1}{2}, \frac{1}{2}\right)$, $\left(0, \frac{1}{2}\right)$, $\left(\frac{1}{2}, 1\right)$ — actually the triangle with vertices:
$$\left(0, \frac{1}{2}\right), \quad \left(\frac{1}{2}, \frac{1}{2}\right), \quad \left(\frac{1}{2}, 1\right).$$

Its area is $\frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$.

Since the ordered region $\{x \le y\}$ has area $\frac{1}{2}$, the probability is:
$$P(\text{triangle}) = \frac{1/8}{1/2} = \frac{1}{4}.$$

**Alternatively (full square view).** By symmetry, the three bad events are:
- $A_1$: piece 1 $\ge 1/2$ (i.e., $U \le 1/2$ and $V \le 1/2$... no — directly: both break points fall in $[1/2, 1]$... 

Let's redo this cleanly. In the **full** unit square with coordinates $(U,V)$:

- "Piece $a = \min(U,V) \ge 1/2$": both $U \ge 1/2$ and $V \ge 1/2$ — area $= 1/4$.
- "Piece $c = 1 - \max(U,V) \ge 1/2$": both $U \le 1/2$ and $V \le 1/2$ — area $= 1/4$.
- "Piece $b = |U-V| \ge 1/2$": the two strips where $U - V \ge 1/2$ or $V - U \ge 1/2$ — total area $= 1/4$.

These three events are **mutually exclusive** (only one piece can be $\ge 1/2$ at a time, since they sum to 1). So:

$$P(\text{no triangle}) = \frac{1}{4} + \frac{1}{4} + \frac{1}{4} = \frac{3}{4}.$$

$$\boxed{P(\text{triangle}) = \frac{1}{4}.}$$

**Intuition check.** The answer $1/4$ is clean and perhaps surprisingly small — most random breaks do *not* yield a triangle. This matches the elegant geometric picture: exactly one quarter of the unit square corresponds to the "balanced" configuration.
