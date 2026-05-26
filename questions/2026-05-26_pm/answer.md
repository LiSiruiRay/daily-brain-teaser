# Answer: Möbius Band Has Fundamental Group ℤ

## Key Idea / Intuition

The Möbius band deformation retracts onto its **central circle** — the image of the horizontal midline $[0,1] \times \{1/2\}$ under the identification. This central circle is a circle, and the deformation retract is the key: since $M$ deformation retracts onto $S^1$, we immediately inherit $\pi_1(M) \cong \pi_1(S^1) \cong \mathbb{Z}$.

The punchline of the follow-up: the boundary circle traverses the central circle **twice**, which reflects the famous "twist" — going around the boundary of a Möbius band brings you back having flipped once, so you need two full traversals to close up.

---

## Formal Proof / Solution

### Step 1: Construct the Deformation Retract

Define the **central circle** $C \subset M$ as the image of the midline:
$$C = \{ [(t, \tfrac{1}{2})] : t \in [0,1] \} \subset M.$$

Under the identification $(0, t) \sim (1, 1-t)$, the midpoint $t = 1/2$ satisfies $1 - 1/2 = 1/2$, so $(0, 1/2) \sim (1, 1/2)$: the midline glues to a genuine circle.

Define the map $H: M \times [0,1] \to M$ by:
$$H([(x, s)], \tau) = [(x,\ (1-\tau)s + \tau \cdot \tfrac{1}{2})].$$

This linearly moves the second coordinate toward $1/2$. One checks:
- $H([(x,s)], 0) = [(x,s)]$ — identity at time $0$.
- $H([(x,s)], 1) = [(x, \tfrac{1}{2})]$ — lands on $C$ at time $1$.
- $H$ respects the identification (since the identification acts on $s$ by $s \mapsto 1-s$, and the midpoint $1/2$ is the fixed point of this map).

So $H$ is a well-defined deformation retraction of $M$ onto $C \cong S^1$.

### Step 2: Conclude the Fundamental Group

Since deformation retracts induce isomorphisms on all homotopy groups:
$$\pi_1(M) \cong \pi_1(C) \cong \pi_1(S^1) \cong \mathbb{Z}.$$

A **generator** is the loop that traverses the central circle once:
$$\gamma(t) = [(t, \tfrac{1}{2})], \quad t \in [0,1].$$

### Step 3: The Boundary Circle (Follow-up)

The boundary $\partial M$ is the image of the edges $[0,1] \times \{0\}$ and $[0,1] \times \{1\}$ under the identification. Since $(0,0) \sim (1,1)$ and $(0,1) \sim (1,0)$, these two edges are **glued together into a single circle** (not two separate circles!).

Parametrize the boundary: start at $[(0,0)]$, travel along $[0,1]\times\{0\}$ to $[(1,0)] = [(0,1)]$, then travel along $[0,1]\times\{1\}$ back to $[(1,1)] = [(0,0)]$.

Under the deformation retract, this boundary loop maps to the central circle traversed **twice**:
$$[\partial M] = 2 \cdot [\gamma] \in \pi_1(M) \cong \mathbb{Z}.$$

This is the topological signature of the half-twist: the boundary of the Möbius band is "twice as long" as the core circle in $\pi_1$. This also explains why cutting the Möbius band along its center circle gives a cylinder with two full twists, not two separate pieces.

---

**Summary table:**

| Space | $\pi_1$ |
|---|---|
| Möbius band $M$ | $\mathbb{Z}$ |
| Central circle $C$ | $\mathbb{Z}$ |
| $[\partial M]$ in $\pi_1(M)$ | $2 \in \mathbb{Z}$ |
