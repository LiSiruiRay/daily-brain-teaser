# Answer: Fundamental Group of the Circle Is ℤ

## Key Idea / Intuition

The real line $\mathbb{R}$ is the "unrolled" version of $S^1$: the covering map $\varepsilon(t) = e^{2\pi i t}$ wraps $\mathbb{R}$ around $S^1$ like a helix over a circle. Every loop in $S^1$ based at $1$ lifts uniquely to a path in $\mathbb{R}$ starting at $0$, and the **endpoint** of that lifted path must be an integer (since it also maps to $1 \in S^1$). That integer — the **winding number** — is a homotopy invariant because homotopies lift to homotopies, and a continuous deformation can't jump the endpoint from one integer to another. This single integer completely classifies loops, giving $\pi_1(S^1) \cong \mathbb{Z}$.

---

## Formal Proof / Solution

### Setup: Lifting paths to $\mathbb{R}$

The covering map $\varepsilon : \mathbb{R} \to S^1$, $\varepsilon(t) = e^{2\pi i t}$, has the **path lifting property**: for every path $\gamma$ in $S^1$ with $\gamma(0) = 1$ there is a unique lift $\tilde{\gamma} : [0,1] \to \mathbb{R}$ with $\tilde{\gamma}(0) = 0$ such that $\varepsilon \circ \tilde{\gamma} = \gamma$.

Since $\gamma$ is a **loop** ($\gamma(1) = 1$), we need $\varepsilon(\tilde{\gamma}(1)) = 1$, i.e., $e^{2\pi i \tilde{\gamma}(1)} = 1$, so $\tilde{\gamma}(1) \in \mathbb{Z}$.

**Definition.** The *winding number* of $\gamma$ is $n(\gamma) := \tilde{\gamma}(1) \in \mathbb{Z}$.

---

### Part (a): $\gamma_1 \not\simeq \gamma_2$

The lift of $\gamma_n(s) = e^{2\pi i n s}$ starting at $0$ is simply $\tilde{\gamma}_n(s) = ns$, so

$$\tilde{\gamma}_1(1) = 1, \qquad \tilde{\gamma}_2(1) = 2.$$

**Claim:** If $\gamma \simeq \gamma'$ (homotopy of based loops), then $n(\gamma) = n(\gamma')$.

*Proof of claim:* Let $H : [0,1] \times [0,1] \to S^1$ be a based homotopy ($H(s,0) = \gamma$, $H(s,1) = \gamma'$, $H(0,t) = H(1,t) = 1$). By the **homotopy lifting property** of covering spaces, $H$ lifts to $\tilde{H} : [0,1]^2 \to \mathbb{R}$ with $\tilde{H}(0,0) = 0$.

- Since $H(0,t) = 1$ for all $t$, the path $t \mapsto \tilde{H}(0,t)$ is a lift of the constant loop at $1$ starting at $0$; by uniqueness it equals $0$ for all $t$.
- Since $H(1,t) = 1$ for all $t$, the path $t \mapsto \tilde{H}(1,t)$ is a lift of the constant loop at $1$ starting at $\tilde{H}(1,0) = n(\gamma) \in \mathbb{Z}$; by uniqueness it equals $n(\gamma)$ for all $t$.
- In particular, $\tilde{H}(1,1) = n(\gamma)$, but $\tilde{H}(1,1)$ is also the endpoint of the lift of $\gamma'$, so $n(\gamma') = n(\gamma)$. $\square$

Since $n(\gamma_1) = 1 \neq 2 = n(\gamma_2)$, the loops $\gamma_1$ and $\gamma_2$ are **not homotopic**.

---

### Part (b): $\pi_1(S^1, 1) \cong \mathbb{Z}$

Define the map

$$\Phi : \pi_1(S^1, 1) \to \mathbb{Z}, \qquad [\gamma] \mapsto n(\gamma).$$

**Well-defined & injective:** Shown above — the winding number is a homotopy invariant, and two loops with equal winding numbers have lifts with the same endpoints.

For injectivity: if $n(\gamma) = n(\gamma')$, then $\tilde{\gamma}$ and $\tilde{\gamma}'$ are paths in $\mathbb{R}$ from $0$ to the same integer $n$. Since $\mathbb{R}$ is **simply connected** (contractible), there is a homotopy $\tilde{H}$ between them in $\mathbb{R}$, and $\varepsilon \circ \tilde{H}$ descends to a homotopy between $\gamma$ and $\gamma'$ in $S^1$.

**Surjective:** The loop $\gamma_n(s) = e^{2\pi i ns}$ has winding number $n$, so every integer is achieved.

**Homomorphism:** Concatenation of loops corresponds to addition of winding numbers:
$$n(\gamma * \gamma') = n(\gamma) + n(\gamma'),$$
because the lift of $\gamma * \gamma'$ travels from $0$ to $n(\gamma)$, then continues to $n(\gamma) + n(\gamma')$.

Hence $\Phi$ is a group isomorphism, and

$$\boxed{\pi_1(S^1, 1) \cong \mathbb{Z}.}$$

**Geometric meaning:** The integer $n(\gamma)$ is the **winding number** — how many times (and in which direction) the loop wraps around the circle. Counterclockwise counts as $+1$, clockwise as $-1$.
