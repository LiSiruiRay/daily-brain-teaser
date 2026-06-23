# Answer: Suspension Kills Fundamental Group

## Key Idea / Intuition

The suspension $SX$ is covered by two open "cones" — an upper cone capped at $N$ and a lower cone capped at $S$. Each cone is contractible (you can push everything toward the pole), so each piece has trivial fundamental group. The two cones overlap in a region homeomorphic to $X \times (-1,1)$, which is path-connected (since $X$ is). Van Kampen's theorem then forces $\pi_1(SX) = 0$: the amalgamated free product of two trivial groups, over any group, is trivial.

The bonus: $S(\text{two points})$ is the suspension of a **discrete** two-point space, which is *not* path-connected, so our hypothesis fails and $\pi_1(S^1) = \mathbb{Z}$ is perfectly consistent.

---

## Formal Proof / Solution

**Step 1: Cover $SX$ with two contractible opens.**

Define:
$$U = \{ [x, t] \in SX : t > -1 \} \quad \text{and} \quad V = \{ [x, t] \in SX : t < 1 \}.$$

Both $U$ and $V$ are open in $SX$:
- $U$ is the image of $X \times (-1, 1]$, with the top $X \times \{1\}$ collapsed to $N$.
- $V$ is the image of $X \times [-1, 1)$, with the bottom $X \times \{-1\}$ collapsed to $S$.

**$U$ is contractible:** The straight-line homotopy $[x, t] \mapsto [x, (1-s)t + s]$ for $s \in [0,1]$ pushes every point toward $[x, 1] = N$. So $U$ deformation retracts onto $\{N\}$, giving $\pi_1(U) = 0$.

**$V$ is contractible:** Similarly, $V$ deformation retracts onto $\{S\}$, giving $\pi_1(V) = 0$.

**Step 2: Identify the intersection.**

$$U \cap V = \{ [x, t] : -1 < t < 1 \} \cong X \times (-1, 1).$$

Since $X$ is path-connected and $(-1,1)$ is path-connected, their product $X \times (-1,1)$ is path-connected. Hence $U \cap V$ is **path-connected**.

**Step 3: Apply the Seifert–Van Kampen theorem.**

Since $U$, $V$, and $U \cap V$ are all path-connected, Van Kampen gives:
$$\pi_1(SX) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V) = \{e\} *_{\pi_1(U\cap V)} \{e\}.$$

No matter what group $\pi_1(U \cap V)$ is, the amalgamated free product of two trivial groups is trivial:
$$\{e\} *_{G} \{e\} \cong \{e\}.$$

Therefore $\pi_1(SX) = 0$. $\blacksquare$

---

**Resolution of the bonus puzzle:**

The "two-point space" $\{N, S\}$ with the discrete topology is *not* path-connected ($N$ and $S$ lie in different path components). Our theorem required $X$ to be path-connected. Indeed, $S(\{N,S\}) \cong S^1$, whose $\pi_1 = \mathbb{Z}$. This is not a contradiction — it just shows the hypothesis is sharp.

---

**Takeaway:** Suspension is a topological "smearing" operation that makes spaces simply connected by providing two contractible patches whose overlap retains just enough connectivity to apply Van Kampen. This is the same mechanism behind why $S^n$ is simply connected for $n \geq 2$ (they are suspensions of connected spaces).
