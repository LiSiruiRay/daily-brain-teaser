# Answer: Cofinite Topology: T₁ but Not Hausdorff

## Key Idea / Intuition

The cofinite topology is "just barely $T_1$": you can separate any point from any other by removing finitely many points, but any two non-empty open sets must overlap because their complements are finite — so they can never be made disjoint. The subtlety is that $T_1$ only asks for one-sided separation (keep $x$, exclude $y$, or vice versa), while Hausdorff demands simultaneous disjoint separation. The infinite set is "too large" to be split by finite complements.

---

## Formal Proof / Solution

### (a) $T_1$ property

Let $x \neq y \in X$. Define:

$$U = X \setminus \{y\}, \qquad V = X \setminus \{x\}.$$

Both are open in the cofinite topology because their complements $\{y\}$ and $\{x\}$ are finite (in fact singletons).

- $x \in U$ and $y \notin U$ ✓  
- $y \in V$ and $x \notin V$ ✓  

So $(X, \tau_\text{cof})$ is $T_1$. $\square$

---

### (b) Not Hausdorff

Suppose for contradiction that distinct $x, y \in X$ can be separated by disjoint open sets $U \ni x$ and $V \ni y$ with $U \cap V = \emptyset$.

Since $U$ and $V$ are non-empty open sets in the cofinite topology, their complements are finite:

$$|X \setminus U| < \infty, \qquad |X \setminus V| < \infty.$$

Therefore:

$$X \setminus (U \cap V) = (X \setminus U) \cup (X \setminus V)$$

is a finite union of finite sets, hence finite. So $U \cap V$ is **cofinite**, in particular non-empty (since $X$ is infinite).

This contradicts $U \cap V = \emptyset$. $\square$

---

### (c) The Gap: $T_1 \not\Rightarrow$ Hausdorff

The cofinite topology on any infinite set provides a clean counterexample. What goes wrong conceptually:

- **$T_1$** only requires: for each *ordered* pair $(x, y)$, an open set containing $x$ but not $y$. Complements of singletons do this perfectly.
- **Hausdorff** requires: for each *unordered* pair $\{x, y\}$, *simultaneous* disjoint open neighborhoods. In the cofinite topology, non-empty open sets always have cofinite (hence huge) intersection — they can never be pulled apart.

The hierarchy of separation axioms is strict:

$$T_0 \subsetneq T_1 \subsetneq T_2\text{ (Hausdorff)} \subsetneq \cdots$$

and the cofinite topology on an infinite set witnesses the strict inclusion $T_1 \subsetneq T_2$.
