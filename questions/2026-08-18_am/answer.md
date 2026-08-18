# Answer: Closed Disk Minus a Boundary Arc: Contractible?

## Key Idea / Intuition

At first glance, removing an arc from the boundary of a disk feels like it might create a "hole" and a non-trivial fundamental group — after all, we're creating a gap. But the key insight is that **$X$ deformation retracts onto a contractible space**: you can push everything inward away from the missing arc, and the remaining boundary (a single open arc plus the interior) can all be collapsed to a point. The space $X$ is actually **contractible**, so $\pi_1(X) = 0$.

The intuition: $D^2$ itself is contractible. Removing a closed arc from the boundary is like having a disk with an "open mouth" — you can still flow everything to the center. The missing arc doesn't create a loop you can't contract, because any loop inside $X$ can be pushed into the interior of the disk (away from $A$) and then contracted there.

---

## Formal Proof / Solution

**Step 1: Identify $X$.**

$$X = D^2 \setminus A = \{(x,y): x^2+y^2 \leq 1\} \setminus \{(\cos\theta,\sin\theta): 0 \leq \theta \leq \pi\}.$$

So $X$ consists of the open interior $\text{int}(D^2)$ together with the lower boundary arc $B = \{(\cos\theta,\sin\theta): \pi < \theta < 2\pi\}$ (open arc, not including endpoints $(\pm 1, 0)$) and the two endpoints $(\pm 1, 0)$ (which lie on $S^1$ but not in $A$). More precisely, $X$ contains all boundary points **not** in $A$: the lower open semicircle plus $(\pm1,0)$.

**Step 2: Show $X$ is contractible via an explicit deformation retract.**

Define $H: X \times [0,1] \to X$ by

$$H(p, t) = (1-t)\,p.$$

- At $t=0$: $H(p,0) = p$ (identity).
- At $t=1$: $H(p,1) = (0,0)$ (contracts everything to the origin).

We must check that $H(p,t) \in X$ for all $p \in X$ and $t \in [0,1]$.

For $t \in [0,1)$: $\|(1-t)p\| = (1-t)\|p\| \leq (1-t) < 1$, so $(1-t)p$ lies in the **open interior** of $D^2$, which is certainly in $X$.

For $t = 1$: $H(p,1) = (0,0) \in \text{int}(D^2) \subset X$.

So $H(p,t) \in X$ for all $p \in X$, $t \in [0,1]$.

Moreover $H$ is continuous (it's a product of continuous functions). Therefore **$H$ is a homotopy from $\mathrm{id}_X$ to the constant map at the origin**, i.e., $X$ is contractible.

**Step 3: Conclude.**

Since $X$ is contractible, all homotopy groups are trivial:

$$\boxed{\pi_1(X) = 0.}$$

**Step 4: Why is removing an interior arc different?**

For contrast: if you remove a **closed arc in the interior** of $D^2$, the straight-line homotopy $H(p,t) = (1-t)p$ might pass through the removed arc (it could hit it on the way to the origin). That situation is genuinely harder. But for a **boundary** arc, the straight-line collapse to the origin always stays strictly inside the disk.

**Conceptual moral:** The disk is "fat enough" that removing boundary data doesn't obstruct contraction to the center. The fundamental group cares about **holes in the interior** — a missing boundary arc is not a hole in this sense.
