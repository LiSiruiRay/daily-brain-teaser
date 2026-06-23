# Answer: Hawaiian Earring vs Infinite Wedge: Compact vs Not

## Key Idea / Intuition

The Hawaiian Earring and the infinite wedge look identical combinatorially — both are "infinitely many circles glued at a point." The difference is purely topological: **how open sets near the basepoint behave**. In the Hawaiian Earring, every neighborhood of the origin must contain *entire* small circles (since those circles shrink to the origin), forcing compactness. In the infinite wedge, you can choose open sets that contain only a small arc of each circle, so no finite subcover works, and the space is not compact. Compactness is a topological invariant, so they cannot be homeomorphic.

---

## Formal Proof / Solution

### Step 1: The Hawaiian Earring $H$ Is Compact

Recall $H = \bigcup_{n=1}^{\infty} C_n \subset \mathbb{R}^2$, where $C_n$ is the circle of radius $1/n$ centered at $(1/n, 0)$.

**Claim:** $H$ is compact.

$H$ is a subspace of $\mathbb{R}^2$. We show it is closed and bounded.

- **Bounded:** Every point of $H$ lies on some $C_n$, which is contained in the closed disk of radius $2/n \leq 2$ centered at the origin. So $H \subset \overline{B(0,2)}$.

- **Closed:** Let $(x_k, y_k) \in H$ with $(x_k, y_k) \to (x, y)$. If infinitely many terms lie on a single $C_n$, then $(x,y) \in C_n \subset H$. Otherwise, the terms lie on circles $C_{n_k}$ with $n_k \to \infty$; since $C_{n_k}$ has diameter $2/n_k \to 0$ and all pass through the origin, we get $(x,y) = (0,0) \in H$.

So $H$ is closed and bounded in $\mathbb{R}^2$, hence **compact** by Heine–Borel.

---

### Step 2: The Infinite Wedge $W$ Is Not Compact

Give $W = \bigvee_{n=1}^{\infty} S^1$ the standard **quotient/CW topology**: a set is open in $W$ if and only if its preimage in $\bigsqcup_{n=1}^\infty S^1$ is open in the disjoint union.

**Claim:** $W$ is not compact.

Construct an open cover with no finite subcover. For each $n$, let $U_n$ be the open set in $W$ consisting of:

$$U_n = \{\text{basepoint}\} \cup \bigcup_{k=1}^{n} S^1_k \cup \bigcup_{k > n} \left(S^1_k \setminus \{q_k\}\right)$$

where $q_k$ is some non-basepoint on $S^1_k$. More directly:

For each circle $S^1_n$ in $W$, pick a non-basepoint $q_n \in S^1_n$. Let

$$V_n = W \setminus \{q_n\}.$$

Each $V_n$ is open in $W$ (since $\{q_n\}$ is closed), and $\bigcup_{n=1}^\infty V_n = W$ because each point $q_n$ is covered by $V_m$ for any $m \neq n$.

However, **no finite subcollection covers $W$**: any finite set $\{V_{n_1}, \ldots, V_{n_k}\}$ fails to cover the point $q_{n_j}$ for $j$ not in $\{n_1, \ldots, n_k\}$... 

Let us give a cleaner argument. Consider the open cover $\{U_n\}_{n \geq 1}$ where

$$U_n = \{\text{basepoint}\} \cup \bigcup_{k=1}^{n} S^1_k \cup \bigcup_{k > n} A_k$$

with $A_k = S^1_k \setminus \{\text{antipodal point of basepoint on } S^1_k\}$ being a proper open arc. Alternatively, the simplest argument:

**Direct argument:** The CW topology on $W$ makes each circle $S^1_n$ a closed subspace. For each $n$, pick a point $p_n \in S^1_n$ distinct from the basepoint. The set $\{p_n : n \geq 1\}$ is closed and discrete in $W$ (each $S^1_n$ contributes exactly one point, and they don't accumulate anywhere in $W$ because any compact subset of $W$ meets only finitely many circles non-trivially). An infinite closed discrete set in a compact space is impossible (it would have a limit point, but there is none). Hence $W$ is **not compact**.

---

### Step 3: Conclusion

Since compactness is a topological invariant:

$$H \text{ is compact}, \quad W \text{ is not compact} \implies H \not\cong W.$$

---

### Bonus Intuition: What Goes Wrong at the Basepoint?

In $H$: any open neighborhood of the origin **must contain all of $C_n$ for sufficiently large $n$** (since the circles shrink to the origin). This "swallowing" of small circles is exactly what forces compactness.

In $W$: a neighborhood of the basepoint can be chosen to contain only a tiny arc of each $S^1_n$, with no obligation to "swallow" anything. The circles don't shrink, so they remain independent — and this independence is what prevents compactness.

This is a beautiful illustration of how **the same combinatorial data (countably many circles at a point) can yield topologically inequivalent spaces** depending on how limits behave near the gluing point.
