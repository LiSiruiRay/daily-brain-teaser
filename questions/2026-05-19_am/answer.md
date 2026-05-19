# Answer: Baire Category: Q Is Not a G-delta

## Key Idea / Intuition

The Baire Category Theorem says a complete metric space is "topologically fat" — it cannot be covered by countably many "thin" (nowhere dense) pieces. If $\mathbb{Q}$ were a $G_\delta$, then both $\mathbb{Q}$ and $\mathbb{R} \setminus \mathbb{Q}$ would be $G_\delta$ sets, which would force $\mathbb{R}$ itself to be a countable union of nowhere dense sets — contradicting Baire. It's a beautiful argument where a purely topological theorem rules out an analytic set-theoretic configuration.

---

## Formal Proof / Solution

### Step 1: The Baire Category Theorem

**Theorem (Baire):** If $X$ is a complete metric space, then $X$ is **not** a countable union of nowhere dense sets. Equivalently, a countable intersection of open dense sets is dense.

*Proof sketch:* Suppose $X = \bigcup_{n=1}^\infty F_n$ with each $F_n$ closed and nowhere dense. We construct a contradiction via a nested sequence of closed balls.

Since $F_1$ is nowhere dense, $X \setminus F_1$ is open and dense. Pick a closed ball $\overline{B}(x_1, r_1)$ with $r_1 < 1$ inside $X \setminus F_1$.

Since $F_2$ is nowhere dense, $X \setminus F_2$ is open and dense, so it intersects the interior of $\overline{B}(x_1, r_1)$. Pick a closed ball $\overline{B}(x_2, r_2) \subset \overline{B}(x_1, r_1) \setminus F_2$ with $r_2 < \frac{1}{2}$.

Continuing, we get nested closed balls $\overline{B}(x_n, r_n)$ with $r_n \to 0$ and $\overline{B}(x_n, r_n) \cap F_n = \emptyset$.

By completeness, $\bigcap_{n=1}^\infty \overline{B}(x_n, r_n) \neq \emptyset$, say $x$ is in this intersection. But then $x \notin F_n$ for all $n$, contradicting $X = \bigcup F_n$. $\square$

---

### Step 2: $\mathbb{Q}$ Is a Countable Union of Nowhere Dense Sets

Each singleton $\{q\}$ for $q \in \mathbb{Q}$ is closed and nowhere dense in $\mathbb{R}$. So:
$$\mathbb{Q} = \bigcup_{q \in \mathbb{Q}} \{q\}$$
is a countable union of nowhere dense sets — i.e., $\mathbb{Q}$ is **meager** (first category).

---

### Step 3: $\mathbb{Q}$ Is Not a $G_\delta$

**Suppose for contradiction** that $\mathbb{Q} = \bigcap_{n=1}^\infty U_n$ where each $U_n$ is open.

Since $\mathbb{Q}$ is dense, each $U_n$ must also be dense (it contains $\mathbb{Q}$).

Now consider the irrationals $\mathbb{R} \setminus \mathbb{Q}$. It is also a countable union of nowhere dense sets... wait, actually let us be careful. Write:

$$\mathbb{R} \setminus \mathbb{Q} = \bigcup_{q \in \mathbb{Q}} (\mathbb{R} \setminus \{q\}) \setminus \mathbb{Q}$$

Better: enumerate $\mathbb{Q} = \{q_1, q_2, \ldots\}$. Then:
$$\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q}) = \left(\bigcap_{n=1}^\infty U_n\right) \cup \left(\bigcap_{n=1}^\infty (\mathbb{R}\setminus\{q_n\})\right)$$

No — let's use the cleanest argument:

If $\mathbb{Q} = \bigcap_{n=1}^\infty U_n$ with $U_n$ open dense, then $\mathbb{R} \setminus \mathbb{Q} = \bigcup_{n=1}^\infty (\mathbb{R} \setminus U_n)$ where each $\mathbb{R} \setminus U_n$ is closed and nowhere dense (since $U_n$ is dense).

So $\mathbb{R}$ would equal:
$$\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q}) = \underbrace{\bigcup_{q \in \mathbb{Q}} \{q\}}_{\text{countably many nowhere dense sets}} \cup \underbrace{\bigcup_{n=1}^\infty (\mathbb{R} \setminus U_n)}_{\text{countably many nowhere dense sets}}$$

This writes $\mathbb{R}$ as a **countable union of nowhere dense sets**, contradicting the Baire Category Theorem applied to $\mathbb{R}$ (which is complete).

**Therefore, $\mathbb{Q}$ is not a $G_\delta$ set.** $\blacksquare$

---

### Why This Is Surprising

$\mathbb{Q}$ is dense, and it seems "analytically nice," yet it is topologically pathological: it cannot be described as a countable intersection of open sets. Meanwhile $\mathbb{R} \setminus \mathbb{Q}$ (the irrationals) *is* a $G_\delta$ — it equals $\bigcap_{q \in \mathbb{Q}} (\mathbb{R} \setminus \{q\})$, a countable intersection of open dense sets. So the irrationals are topologically "larger" than the rationals in the Baire sense, despite both being dense.
