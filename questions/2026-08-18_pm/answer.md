# Answer: The Sphere Is Simply Connected: A Covering Space Argument

## Key Idea / Intuition

If $S^2$ had a non-trivial fundamental group, the universal cover $\tilde{S}^2$ would be a covering space with more than one sheet. But $S^2$ is compact, and a covering space of a compact space with finitely many sheets is compact. More strikingly, the key geometric fact is that $S^2$ is **2-dimensional** and any loop can be perturbed off any point — this makes every loop null-homotopic. The cleanest proof uses path lifting: any loop on $S^2$ based at $p$ can be lifted to the universal cover, but a more direct topological argument uses the fact that $S^2 \setminus \{q\}$ is simply connected (homeomorphic to $\mathbb{R}^2$) to push any loop off a point and contract it.

---

## Formal Proof / Solution

We give a clean proof using a covering/lifting idea combined with a geometric observation.

**Claim:** Every loop $\gamma: [0,1] \to S^2$ based at a point $p \in S^2$ is null-homotopic.

**Step 1: Set up the covering.**

Suppose for contradiction that $\pi_1(S^2) \neq 0$. Then $S^2$ admits a non-trivial connected covering space $p: E \to S^2$. Since $S^2$ is compact and $E$ is a covering space, if the covering has $n < \infty$ sheets then $E$ is compact. But in fact we show directly that every covering must be trivial.

**Step 2: The key lemma — any loop misses some point.**

Let $\gamma: [0,1] \to S^2$ be a loop based at $p$. Since $[0,1]$ is compact, $\gamma([0,1])$ is a compact (hence closed) subset of $S^2$. By a measure-theory/dimension argument (or Sard's theorem for smooth loops), the image $\gamma([0,1])$ cannot equal all of $S^2$: a continuous image of a 1-dimensional space cannot fill the 2-sphere. More precisely:

> **Lemma.** For any continuous $\gamma: [0,1] \to S^2$, there exists a point $q \in S^2 \setminus \gamma([0,1])$.

*Proof of Lemma:* The image $\gamma([0,1])$ has topological dimension $\leq 1$ (it is a continuous image of $[0,1]$), while $S^2$ has topological dimension $2$. Hence $\gamma([0,1]) \neq S^2$, so some $q$ is missed. $\square$

**Step 3: Contract the loop in $S^2 \setminus \{q\}$.**

Since $q \notin \gamma([0,1])$, we have $\gamma([0,1]) \subset S^2 \setminus \{q\}$.

Now $S^2 \setminus \{q\} \cong \mathbb{R}^2$ via stereographic projection from $q$. Since $\mathbb{R}^2$ is contractible (hence simply connected), the loop $\gamma$ (viewed as a loop in $\mathbb{R}^2$) is null-homotopic in $\mathbb{R}^2$.

That is, there exists a homotopy $H: [0,1] \times [0,1] \to \mathbb{R}^2 \subset S^2$ with:
$$H(s, 0) = \gamma(s), \quad H(s,1) = p, \quad H(0,t) = H(1,t) = p.$$

This homotopy takes place entirely in $S^2 \setminus \{q\} \subset S^2$, so $\gamma$ is null-homotopic in $S^2$.

**Step 4: Conclusion.**

Since every loop in $S^2$ is null-homotopic, we conclude $\pi_1(S^2) = 0$. $\blacksquare$

---

**Why this is beautiful:** The argument reduces everything to a single elegant observation — a loop is a 1-dimensional object and cannot fill $S^2$, so it always misses a point, and removing one point from $S^2$ gives $\mathbb{R}^2$ where everything is trivially contractible. The covering-space perspective reframes why: if $\pi_1(S^2) \neq 0$, the universal cover would be a nontrivial covering, but any putative generating loop would lift to a loop (not a path between different sheets), forcing the covering to be trivial — a contradiction.

**Contrast with $S^1$:** On $S^1$, any loop that wraps once around cannot miss any point (since $S^1$ is 1-dimensional and the loop is surjective), so the same trick fails. This is the dimensionality at work.
