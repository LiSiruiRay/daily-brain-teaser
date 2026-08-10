# Answer: Integral of the Cantor Function via Symmetry

## Key Idea / Intuition

The Cantor function has a beautiful **self-similar symmetry**: the graph of $f$ on $[0,1]$ is symmetric about the point $(\tfrac{1}{2}, \tfrac{1}{2})$. More precisely, $f(x) + f(1-x) = 1$ for all $x \in [0,1]$. This single symmetry immediately pins down the integral without any calculation involving the Cantor set's fractal structure.

---

## Formal Proof / Solution

**Step 1: Establish the symmetry $f(x) + f(1-x) = 1$.**

The Cantor set and the Cantor function are built symmetrically: at each stage of the construction, the removed middle-third intervals are placed symmetrically about $\tfrac{1}{2}$, and the function values are assigned symmetrically (the left half gets values in $[0,\tfrac{1}{2}]$, the right half in $[\tfrac{1}{2},1]$, mirrored). A formal induction shows that for all $x$,
$$f(x) + f(1-x) = 1.$$

**Step 2: Use the symmetry to evaluate the integral.**

Let $I = \displaystyle\int_0^1 f(x)\, dx$. Substitute $x \mapsto 1-x$:
$$I = \int_0^1 f(1-x)\, dx.$$

Add the two expressions:
$$2I = \int_0^1 \bigl[f(x) + f(1-x)\bigr]\, dx = \int_0^1 1\, dx = 1.$$

Therefore,
$$\boxed{I = \dfrac{1}{2}.}$$

**Why this is surprising.**

The function $f$ is *constant* on the complement of the Cantor set, which has measure $1$. So $f$ is "flat" almost everywhere — it does all its rising on a set of measure zero. Yet the integral comes out exactly $\tfrac{1}{2}$, just as it would for the identity function $g(x)=x$! The symmetry argument bypasses the fractal complexity entirely and gives the answer in two lines.

**Remark on integration theory.**

One can also see this via integration by parts (Lebesgue–Stieltjes):
$$\int_0^1 f\, dx = \bigl[x f(x)\bigr]_0^1 - \int_0^1 x\, df(x) = 1 - \int_0^1 x\, df(x).$$
By the same symmetry argument applied to $\int_0^1 x\, df(x)$ (substituting $x\mapsto 1-x$ and using $df(1-x) = df(x)$ by symmetry), one again gets $\int_0^1 x\,df(x) = \tfrac{1}{2}$, confirming $I = \tfrac{1}{2}$.
