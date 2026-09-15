# Answer: Torus Knot Curve: Simple Closed Curve and Annular Complement

## Key Idea / Intuition

Think of the torus as a square $[0,1]^2$ with opposite sides identified. The curve $\gamma$ becomes a straight line of slope $q/p$ in the square — and because $\gcd(p,q)=1$, this line hits exactly the right lattice points to close up into a single embedded loop without self-intersection. When you "cut" the torus along this line, you're unzipping the identification along a diagonal, and what's left is topologically an annulus. The fundamental group of an annulus is $\mathbb{Z}$.

---

## Formal Proof / Solution

### Step 1: Visualizing $\gamma$ in the Square Model

Represent $T$ as $\mathbb{R}^2 / \mathbb{Z}^2$, i.e., the unit square $[0,1]^2$ with $(x,0)\sim(x,1)$ and $(0,y)\sim(1,y)$.

The curve $\gamma$ lifts to the straight line $\ell$ in $\mathbb{R}^2$ starting at $(0,0)$ with direction vector $(p,q)$:
$$\tilde{\gamma}(t) = (pt,\, qt), \quad t \in [0,1].$$

At $t=1$ we reach $(p,q)$, which maps to $(0,0)$ in $T$ (since both coordinates are integers), so $\gamma$ is indeed a closed loop representing $[a]^p[b]^q = p[a]+q[b]$ in $\pi_1(T)$.

### Step 2: $\gamma$ Is Simple (No Self-Intersections)

Suppose $\gamma(t_1) = \gamma(t_2)$ for $t_1 \neq t_2$ in $[0,1)$. Then
$$\tilde{\gamma}(t_1) \equiv \tilde{\gamma}(t_2) \pmod{\mathbb{Z}^2},$$
meaning $(p(t_1-t_2),\, q(t_1-t_2)) \in \mathbb{Z}^2$.

So $p(t_1-t_2) = m$ and $q(t_1-t_2) = n$ for integers $m,n$. Then:
$$t_1 - t_2 = \frac{m}{p} = \frac{n}{q} \implies mq = np.$$

Since $\gcd(p,q)=1$, we get $p \mid m$ and $q \mid n$, so $t_1 - t_2 \in \mathbb{Z}$. But $t_1, t_2 \in [0,1)$ means $t_1 = t_2$. **Contradiction.** Hence $\gamma$ is simple.

### Step 3: Cutting Along $\gamma$ Gives an Annulus

Since $\gcd(p,q)=1$, by Bézout's theorem there exist integers $r, s$ with $ps - qr = 1$.

Define a new basis for the lattice $\mathbb{Z}^2$:
$$\mathbf{u} = (p,q), \quad \mathbf{v} = (r,s).$$

The matrix $\begin{pmatrix} p & r \\ q & s \end{pmatrix}$ has determinant $ps - qr = 1$, so it's in $\text{SL}_2(\mathbb{Z})$: it's a **lattice automorphism** of $\mathbb{R}^2/\mathbb{Z}^2$.

In the new coordinates $(u,v)$ (where the $u$-direction corresponds to $\gamma$), the torus looks like the parallelogram spanned by $\mathbf{u}$ and $\mathbf{v}$, identified on opposite sides. The curve $\gamma$ is the segment from $(0,0)$ to $(1,0)$ in the $u$-coordinate.

**Cutting** along $\gamma$ means cutting the square $[0,1]^2$ (in new coordinates) along the edge $v=0$ (which, after identification, is exactly $\gamma$). This gives:
- A square $[0,1]^2$ where the **top and bottom are no longer identified** (they were the two sides of $\gamma$), but the **left and right are still identified**.
- That's exactly $[0,1] \times [0,1]$ with $(0,v) \sim (1,v)$, which is a **cylinder = annulus**.

### Step 4: Fundamental Group of $T \setminus \gamma$

The complement $T \setminus \gamma$ is an **open annulus** (the torus cut open along the simple closed curve $\gamma$). An open annulus deformation retracts onto its core circle $S^1$, so:

$$\boxed{\pi_1(T \setminus \gamma) \cong \mathbb{Z}.}$$

The generator is any loop that "links" $\gamma$ once — in coordinates, it's the loop in the $v$-direction (Bézout complement direction).

### Why $\gcd(p,q)=1$ Is Essential

If $\gcd(p,q) = d > 1$, then the "line" in the square would close up after time $1/d$, tracing the same path $d$ times — so $\gamma$ would self-intersect (or rather, be a $d$-fold cover of a simpler curve). The complement would then have a more complicated topology.
