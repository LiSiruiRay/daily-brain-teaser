# Answer: Peano Curves Exist, but Peano Bijections Don't

## Key Idea / Intuition

The argument has two steps.

1. **The inverse is continuous for free.** A continuous bijection from a compact space onto a Hausdorff space cannot "tear" anything, so it is a homeomorphism. A Peano bijection would therefore make the interval and the square topologically identical.
2. **The two spaces are not identical.** Removing an interior point cuts the interval into two pieces. Removing any point from the square leaves it in one piece, since you can always walk around a single missing point.

In short: compactness upgrades "bijection" to "homeomorphism", and connectedness then sees the difference between dimension 1 and dimension 2.

---

## Formal Proof / Solution

**Step 1: Compact $\to$ Hausdorff continuous bijections are homeomorphisms.**

Let $f : X \to Y$ be a continuous bijection with $X$ compact and $Y$ Hausdorff. We show $f$ is a closed map.

- Let $C \subseteq X$ be closed. A closed subset of a compact space is compact, so $C$ is compact.
- Continuous images of compact sets are compact, so $f(C)$ is compact.
- A compact subset of a Hausdorff space is closed, so $f(C)$ is closed in $Y$.

A bijection that maps closed sets to closed sets has continuous inverse, because $(f^{-1})^{-1}(C) = f(C)$. Hence $f$ is a homeomorphism (Munkres, Thm 26.6).

**Step 2: Apply this to a hypothetical Peano bijection.**

Suppose $f : [0,1] \to [0,1]^2$ is a continuous bijection. The interval $[0,1]$ is compact and the square $[0,1]^2$ is Hausdorff, so by Step 1, $f$ is a homeomorphism.

A homeomorphism restricts to a homeomorphism of complements of corresponding points. Let $p = f(1/2)$. Then
$$f|_{[0,1]\setminus\{1/2\}} : [0,1]\setminus\{1/2\} \;\xrightarrow{\ \cong\ }\; [0,1]^2 \setminus \{p\}.$$

**Step 3: The two sides differ in connectedness.**

- **The left side is disconnected.** We have $[0,1]\setminus\{1/2\} = [0,\tfrac12) \cup (\tfrac12, 1]$, a union of two disjoint nonempty relatively open sets.
- **The right side is path-connected.** Let $a, b \in Q := [0,1]^2 \setminus \{p\}$.
  - The lines $\ell_a$ (through $a$ and $p$) and $\ell_b$ (through $b$ and $p$) cover only a measure-zero part of the square. So we can choose $c \in [0,1]^2$ lying on neither line. In particular $c \neq p$.
  - The square is convex, so the segments $[a,c]$ and $[c,b]$ lie in $[0,1]^2$.
  - The segment $[a,c]$ would contain $p$ only if $p$ were on the line through $a$ and $c$. That would force $c \in \ell_a$, which we excluded. The same argument applies to $[c,b]$.
  - So the polygonal path $a \to c \to b$ lies in $Q$.

Connectedness is a topological invariant, so a disconnected space cannot be homeomorphic to a connected one. This is a contradiction. $\blacksquare$

Consequently, every continuous surjection $[0,1]\to[0,1]^2$ fails to be injective. The same proof shows there is no continuous bijection $[0,1] \to [0,1]^n$ for any $n \ge 2$.

---

**Bonus.** Define
$$g(t) = (\cos 2\pi t,\ \sin 2\pi t), \qquad t \in [0,1).$$

- **It is a continuous bijection.** It is continuous, and it is bijective onto $S^1$ because $t \mapsto 2\pi t$ hits each angle in $[0,2\pi)$ exactly once.
- **Its inverse is not continuous at $(1,0) = g(0)$.** Points on the circle just below $(1,0)$ pull back to $t$ near $1$, not near $0$.
- **Topological confirmation.** Removing $1/2$ disconnects $[0,1)$, while removing any point leaves $S^1$ connected. So the two spaces are not homeomorphic at all.

Step 1 is what fails: $[0,1)$ is not compact. Concretely, the closed set $[1/2, 1)$ maps to a set that is not closed in $S^1$, because its closure also contains $(1,0)$.

Compactness is exactly the hypothesis that prevents a bijection from secretly "gluing" the ends of a space together.
