# Answer: The Plane Cannot Be Sliced into Circles

## Key Idea / Intuition

Suppose such a partition existed. Pick any circle and look at its center. The circle through that center is trapped inside the first disk, and it has at most half the radius. Repeating this gives a nested sequence of disks shrinking to a single point $p$. The circle through $p$ has some fixed positive radius, yet it is trapped inside every one of these ever-smaller disks, which is impossible. Compactness supplies the point $p$, and the shrinking radii defeat its circle.

---

## Formal Proof / Solution

**Answer: No.**

Suppose $\mathbb{R}^2 = \bigsqcup_{\alpha} C_\alpha$ is a partition into disjoint circles. For a circle $C$, let $D(C)$ denote the closed disk it bounds and $\operatorname{int} D(C)$ its open interior.

**Trapping lemma.** Let $C$ be a circle of the partition and $C'$ another one with $C' \cap \operatorname{int} D(C) \neq \varnothing$. Then $C' \subset \operatorname{int} D(C)$.

*Proof.* $C'$ is connected and disjoint from $C$. The complement $\mathbb{R}^2 \setminus C$ is the disjoint union of the open sets $\operatorname{int} D(C)$ and $\mathbb{R}^2 \setminus D(C)$. A connected set meeting the first must lie entirely in it. $\square$

**Step 1: Build a shrinking nested sequence.** Start with any circle $C_1$ of the partition, with center $c_1$ and radius $r_1$.

The center $c_1$ lies on some circle $C_2$ of the partition. Since $c_1 \in \operatorname{int} D(C_1)$, the lemma gives $C_2 \subset \operatorname{int} D(C_1)$.

Now bound the radius $r_2$ of $C_2$. The point of $C_2$ diametrically opposite $c_1$ is at distance $2r_2$ from $c_1$. It lies strictly inside $D(C_1)$, so
$$2r_2 < r_1, \qquad\text{i.e.}\qquad r_2 < \tfrac{1}{2} r_1.$$

Also, since $C_2 \subset \operatorname{int} D(C_1)$, the disk it bounds satisfies $D(C_2) \subset \operatorname{int} D(C_1)$.

Repeat this with $C_2$ in place of $C_1$, and so on. This gives circles $C_1, C_2, C_3, \dots$ in the partition with
$$D(C_1) \supset D(C_2) \supset D(C_3) \supset \cdots, \qquad D(C_{n+1}) \subset \operatorname{int} D(C_n), \qquad r_n < \frac{r_1}{2^{n-1}} \to 0.$$

**Step 2: Find the limit point.** The sets $D(C_n)$ are nonempty, compact and nested. By the Cantor intersection theorem, $\bigcap_n D(C_n) \neq \varnothing$. Since the diameters tend to $0$, the intersection is a single point $p$.

**Step 3: Contradiction.** The point $p$ lies on some circle $C$ of the partition, with radius $r > 0$.

For every $n$ we have $p \in D(C_{n+1}) \subset \operatorname{int} D(C_n)$. So $p \notin C_n$, which means $C \neq C_n$. Since $C$ meets $\operatorname{int} D(C_n)$ at $p$, the lemma gives
$$C \subset \operatorname{int} D(C_n) \quad\text{for every } n.$$

Hence the diameter of $C$ is at most the diameter of $D(C_n)$:
$$2r \le 2r_n \longrightarrow 0.$$

This contradicts $r > 0$. Therefore no such partition exists. $\blacksquare$

---

### Remarks

- **The same proof works for any Jordan curves** whose diameters can be forced to shrink. For partitions into arbitrary simple closed curves, the same nesting idea combined with a Zorn-type or compactness argument still shows that the plane cannot be partitioned into them.
- **Removing points helps.** The plane minus one point *can* be partitioned into circles: use the concentric circles around the missing point. The argument above fails here because the nested disks could shrink onto the puncture. The punctured point is exactly the "hole" that compactness was detecting.
- **Bonus answer ($\mathbb{R}^3$):** Yes, $\mathbb{R}^3$ *is* a disjoint union of round circles. One construction starts by partitioning $\mathbb{R}^3$ minus a line into tori, and the leftover points are handled by a clever arrangement. Explicit constructions are due to Szulkin (*Amer. Math. Monthly* 90, 1983). A transfinite-induction proof also works, even with circles of radius $1$ only (Conway–Croft). The extra dimension gives a circle room to "link" around a point instead of being trapped in a disk around it.
