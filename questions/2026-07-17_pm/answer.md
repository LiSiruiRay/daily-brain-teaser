# Answer: A Polynomial Vanishing on All Lattice Points in a Strip

## Key Idea / Intuition

The lattice points $\{(m,n) : m \geq 0,\ 0 \leq n \leq m\}$ form an **infinite triangular array** — there are infinitely many of them, but they don't "fill" the plane in the way needed to force a polynomial to vanish. The key insight is to think about what happens when you fix $m$: for each fixed integer $m \geq 0$, the polynomial $p(m, y)$ (a polynomial in $y$ alone) vanishes at $m+1$ values $n = 0, 1, \ldots, m$. If the degree of $p$ in $y$ is $d$, then once $m \geq d$, there are **more zeros than the degree**, forcing $p(m, y) \equiv 0$ as a polynomial in $y$ for each sufficiently large integer $m$. That means every coefficient (a polynomial in $x$) vanishes at infinitely many $x$-values, forcing them all to be zero.

---

## Formal Proof / Solution

**Setup.** Write $p(x,y)$ as a polynomial in $y$ with coefficients that are polynomials in $x$:

$$p(x,y) = \sum_{k=0}^{d} a_k(x)\, y^k,$$

where each $a_k(x)$ is a polynomial in $x$, and $d$ is the degree of $p$ in $y$.

**Step 1: Fix a large integer $m$.** For any integer $m \geq d$, the polynomial in $y$:

$$q_m(y) := p(m, y) = \sum_{k=0}^{d} a_k(m)\, y^k$$

has degree at most $d$ in $y$. By hypothesis, $q_m(n) = 0$ for $n = 0, 1, 2, \ldots, m$. That gives $m+1 \geq d+1$ zeros. Since a nonzero polynomial of degree $\leq d$ can have at most $d$ roots, we conclude:

$$q_m(y) \equiv 0 \quad \text{as a polynomial in } y.$$

**Step 2: Each coefficient vanishes at infinitely many integers.** From Step 1, for every integer $m \geq d$ we have $a_k(m) = 0$ for all $k = 0, 1, \ldots, d$. This means the polynomial $a_k(x)$ vanishes at the **infinite** set $\{d, d+1, d+2, \ldots\}$.

**Step 3: Conclude.** A nonzero polynomial in one variable can only have finitely many roots. Since each $a_k(x)$ vanishes at infinitely many values of $x$, we must have:

$$a_k(x) \equiv 0 \quad \text{for all } k = 0, 1, \ldots, d.$$

Therefore $p(x,y) \equiv 0$.

**Answer:** Yes, $p$ must be identically zero. $\blacksquare$

---

**Why this is surprising:** The lattice points only occupy the triangular region $0 \leq n \leq m$, which is a *thin* subset of $\mathbb{Z}^2$ (in particular, a polynomial that vanishes on all of $\mathbb{Z}^2$ would obviously be zero, but this is less obvious). The trick is that the triangular array is *not* thin in the critical direction: for each fixed $m$, there are enough points to kill a polynomial in $y$.
