# Answer: Hawaiian Earring Is Not Semi-Locally Simply Connected

## Key Idea / Intuition

The Hawaiian earring has circles piling up at $p$ with radii $\to 0$. Any open neighborhood $U$ of $p$, no matter how small, must contain **entire small circles** $C_n$ for all sufficiently large $n$ (because eventually $C_n \subset U$). Each such circle represents a loop that is **not contractible in $H$** — it wraps around a hole that genuinely exists in the global space. Since $U$ cannot "kill" the loop (the loop goes around a hole in the ambient $H$, not just in $U$), the semi-local simple connectivity condition fails.

The punchline: this failure is exactly what **blocks the existence of a universal cover** for $H$. The standard theorem says a path-connected, locally path-connected space has a universal cover **if and only if** it is semi-locally simply connected. The Hawaiian earring is a clean counterexample showing why that hypothesis is necessary.

---

## Formal Proof / Solution

**Setup.** Let $U$ be any open neighborhood of $p = (0,0)$ in $H$. We need to find a loop $\gamma$ based at $p$, lying entirely in $U$, such that the induced homomorphism

$$i_* : \pi_1(U, p) \to \pi_1(H, p)$$

does not send $[\gamma]$ to $0$.

**Step 1: Every small neighborhood contains an entire circle $C_n$.**

Since $U$ is open in $H$ and $p \in U$, there exists $\varepsilon > 0$ such that $B(p, \varepsilon) \cap H \subset U$, where $B(p,\varepsilon)$ is the Euclidean open ball. The circle $C_n$ has center $(1/n, 0)$ and radius $1/n$, so every point of $C_n$ satisfies

$$\|(x,y) - p\| \leq \|(x,y) - (1/n,0)\| + \|(1/n,0) - p\| = \frac{1}{n} + \frac{1}{n} = \frac{2}{n}.$$

For all $n > 2/\varepsilon$, every point of $C_n$ lies within distance $\varepsilon$ of $p$, so $C_n \subset U$.

**Step 2: The loop around $C_n$ is nontrivial in $\pi_1(H,p)$.**

Fix such an $n$. Let $\gamma_n$ be the loop that traverses $C_n$ once (based at $p$, the unique point of $C_n \cap \{p\}$). We claim $[\gamma_n] \neq 0$ in $\pi_1(H, p)$.

Consider the retraction $r: H \to C_n$ defined by:
$$r(x) = \begin{cases} x & \text{if } x \in C_n, \\ p & \text{if } x \in C_k,\ k \neq n. \end{cases}$$
This map is **continuous**: on each $C_k$ it is continuous, and at $p$ it sends every neighborhood to a neighborhood of $r(p) = p$. (Continuity at $p$ follows because any open set in $C_n$ containing $p$ pulls back to an open set in $H$ containing $p$, as the circles only meet at $p$.)

Since $r$ is a continuous retraction onto $C_n \cong S^1$, it induces a surjection

$$r_* : \pi_1(H, p) \to \pi_1(C_n, p) \cong \mathbb{Z}.$$

But $r_*([\gamma_n]) = [\gamma_n] \in \pi_1(C_n, p)$, which is a generator of $\mathbb{Z}$, hence **nonzero**. Therefore $[\gamma_n] \neq 0$ in $\pi_1(H,p)$.

**Step 3: The inclusion $i: U \hookrightarrow H$ does not kill $[\gamma_n]$.**

The loop $\gamma_n$ lies in $U$ (by Step 1) and $i_*([\gamma_n]) = [\gamma_n] \neq 0$ in $\pi_1(H,p)$ (by Step 2). Hence the homomorphism $i_*: \pi_1(U,p) \to \pi_1(H,p)$ does not send $[\gamma_n]$ to the identity. $\blacksquare$

**Consequence.** Since every neighborhood $U$ of $p$ fails to "kill" some loop, $H$ is **not semi-locally simply connected** at $p$.

By the **Fundamental Theorem of Covering Space Theory** (Munkres §82, Lee Chapter 12):

> A path-connected, locally path-connected space $X$ admits a universal covering space if and only if $X$ is semi-locally simply connected.

The Hawaiian earring is path-connected and locally path-connected, but fails the third condition — so it has **no universal cover**. This is the canonical example showing the hypothesis is not vacuous.

**Remark on $\pi_1(H,p)$.** The fundamental group of the Hawaiian earring is genuinely exotic: it is **not** the free group on countably many generators (which would be the naïve guess). It contains elements corresponding to infinite products of loops $\gamma_1 \gamma_2 \gamma_3 \cdots$, since such infinite concatenations converge uniformly to a continuous loop (the speed can be arranged so the $n$-th circle is traversed in time $1/2^n$). This makes $\pi_1(H,p)$ an uncountable, non-free group — a beautiful pathology.
