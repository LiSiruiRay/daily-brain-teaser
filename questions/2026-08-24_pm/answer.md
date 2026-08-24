# Answer: The Measurable Set That Fills Every Interval

## Key Idea / Intuition

The condition says $E$ is "fat" everywhere — it meets every interval in positive measure — yet its complement is also "fat" everywhere. This rules out open and closed sets immediately: a nonempty open set contains an interval entirely, and a closed set of full measure in some interval would have to contain that interval (by regularity). The construction uses a **fat Cantor set** as a building block, sprinkled densely via a countable union.

---

## Existence and Construction

**Step 1: Fat Cantor sets.**

Recall that for any $\varepsilon \in (0,1)$, one can construct a **Cantor-like (fat Cantor) set** $C \subseteq [0,1]$ that is closed, nowhere dense (contains no interval), yet has measure $m(C) = 1 - \varepsilon$. Its complement is open and dense.

**Step 2: The construction of $E$.**

Let $\{(a_n, b_n)\}_{n \geq 1}$ be an enumeration of all open intervals with rational endpoints in $[0,1]$.

Inside each interval $(a_n, b_n)$, place a fat Cantor set $C_n \subseteq (a_n, b_n)$ with

$$m(C_n) = \tfrac{1}{2}(b_n - a_n).$$

Define

$$E = \bigcup_{n=1}^\infty C_n.$$

**Step 3: Verify the condition.**

For any open interval $(a,b) \subseteq [0,1]$, it contains some rational-endpoint interval $(a_n, b_n)$, so

$$m(E \cap (a,b)) \geq m(C_n) = \tfrac{1}{2}(b_n - a_n) > 0.$$

Thus $m(E \cap (a,b)) > 0$. ✓

Now we need $m(E \cap (a,b)) < b - a$, i.e., $m(E^c \cap (a,b)) > 0$. Apply the same argument to $E^c$: since each $C_n$ is **nowhere dense**, $E = \bigcup_n C_n$ is a countable union of nowhere dense sets, hence **meager** (first category). By the Baire category theorem applied to $[0,1]$, $E$ cannot be all of $(a,b)$.

Actually, let us give a direct measure argument. Inside $(a_n, b_n)$, the complement $C_n^c \cap (a_n, b_n)$ has measure $\frac{1}{2}(b_n - a_n)$. More carefully: construct $E$ so that also $E^c$ hits every interval positively. Apply the same rational-interval enumeration to construct $F = \bigcup_n D_n$ where $D_n \subseteq (a_n,b_n)$ is another fat Cantor set disjoint from $C_n$ with $m(D_n) = \frac{1}{4}(b_n - a_n)$. Then $E \supseteq \bigcup C_n$ and $E^c \supseteq \bigcup D_n$, so both hit every interval positively.

**Step 4: $E$ cannot be open.**

If $E$ were open and nonempty, it would contain some interval $(c,d)$, giving $m(E \cap (c,d)) = d - c$, violating the upper bound.

**Step 5: $E$ cannot be closed.**

If $E$ were closed, then $E^c$ is open. If $E^c$ is nonempty (which it must be, since $E^c$ hits every interval), $E^c$ contains an interval $(c,d)$, giving $m(E \cap (c,d)) = 0$, violating the lower bound.

---

## The Conceptual Punch

Such a set $E$ is sometimes called a **Bernstein-like** or **density-nowhere-extreme** set. It cannot be Borel in any "simple" sense: its indicator function $\mathbf{1}_E$ has the property that for every $x \in [0,1]$,

$$\text{the density of } E \text{ at } x \text{ is neither } 0 \text{ nor } 1,$$

i.e., $x$ is never a **Lebesgue density point** of $E$ or of $E^c$ in a strong uniform sense. This is an existence that lives firmly in the measurable-but-not-nice world, unreachable by topological simplicity.

---

*Written to:* [`questions/2026-08-16_pm.md`](questions/2026-08-16_pm.md) and [`answers/2026-08-16_pm.md`](answers/2026-08-16_pm.md)
