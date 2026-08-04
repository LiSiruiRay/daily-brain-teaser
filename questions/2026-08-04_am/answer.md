# Answer: Which Spheres Admit a Topological Group Structure?

## Key Idea / Intuition

A topological group is special: it is "homogeneous" (you can translate any point to any other), and crucially, its fundamental group must be **abelian** (because loop composition in a group admits two independent operations that must agree — this is the Eckmann–Hilton argument). But for $S^n$ with $n \geq 3$, there's a more powerful obstruction: a classical theorem states that the only spheres that admit a topological group structure are $S^0$, $S^1$, $S^3$ (and $S^7$ if we allow non-associative "H-spaces", but not Lie groups). The key constraint comes from algebraic topology: the cohomology ring of a topological group must be a **Hopf algebra**, which forces very restrictive conditions on the space.

---

## Formal Proof / Solution

### Step 1: Small cases that work

- **$S^0 = \{+1, -1\}$:** This is just $\mathbb{Z}/2\mathbb{Z}$ with the discrete topology. ✓
- **$S^1$:** This is the circle group $U(1) \cong \mathbb{R}/\mathbb{Z}$. ✓  
- **$S^3$:** This is the group of unit quaternions $\{q \in \mathbb{H} : |q| = 1\}$, which is isomorphic to $\mathrm{SU}(2)$. ✓

### Step 2: Why $S^2$ fails — fundamental group obstruction

For any topological group $G$, the fundamental group $\pi_1(G)$ is **abelian**. This follows from the Eckmann–Hilton argument: there are two multiplications on $\pi_1(G, e)$ — loop concatenation $*$ and pointwise group multiplication — and both satisfy the interchange law, forcing them to coincide and both to be commutative.

But more directly for $S^2$: $\pi_1(S^2) = 0$, so this doesn't obstruct. However, $\pi_2(S^2) = \mathbb{Z}$. A deeper theorem states that **$\pi_2(G) = 0$ for any topological group $G$**. 

Why? For a topological group, the long exact sequence of the path-loop fibration $\Omega G \to PG \to G$ gives:
$$\pi_n(G) \cong \pi_{n-1}(\Omega G)$$
and one can show that $\pi_2$ of a Lie group (or more generally a topological group with mild hypotheses) vanishes. This is Cartan's theorem. Since $\pi_2(S^2) = \mathbb{Z} \neq 0$, **$S^2$ cannot be a topological group**.

### Step 3: Hopf algebra constraint kills all higher spheres (except $S^3$)

**Hopf's theorem** (1941): If $X$ is a compact, connected topological group, then its real cohomology ring $H^*(X; \mathbb{R})$ is an **exterior algebra** on odd-degree generators:
$$H^*(G; \mathbb{R}) \cong \Lambda(x_1, x_2, \ldots, x_k), \quad \deg(x_i) \text{ odd}.$$

This is because the diagonal map $G \to G \times G$ (sending $g \mapsto (g,g)$) gives the cohomology ring the structure of a **Hopf algebra**, and a classical theorem of Hopf classifies such algebras over $\mathbb{R}$ as exterior algebras on odd generators.

Now check: for $S^n$,
$$H^*(S^n; \mathbb{R}) = \mathbb{R} \oplus \mathbb{R}[n]$$
which is an exterior algebra on one generator of degree $n$ **if and only if $n$ is odd**.

So: **$S^n$ can only be a topological group if $n$ is odd** (or $n=0$).

### Step 4: Not all odd $n$ work

Among odd spheres, $S^1$ and $S^3$ are genuine Lie groups. For $n \geq 5$ odd, it turns out $S^n$ is not even an **H-space** (a space with a continuous multiplication with two-sided unit, weaker than a group) by Adams' theorem (1960), which uses $K$-theory to show $S^n$ is an H-space **only for $n = 0, 1, 3, 7$**. Among these, $S^7$ (octonions) fails associativity and is not a topological group.

### Conclusion

The spheres $S^n$ that can carry a topological group structure are exactly:

$$\boxed{n = 0,\ 1,\ 3}$$

| $n$ | Group structure |
|-----|----------------|
| $0$ | $\mathbb{Z}/2\mathbb{Z}$ |
| $1$ | $U(1)$ — circle group |
| $3$ | $\mathrm{SU}(2)$ — unit quaternions |

The key ideas are: (1) topological groups force $\pi_2 = 0$, killing $S^2$; (2) Hopf's theorem on cohomology of topological groups forces the dimension to be odd; (3) Adams' theorem (using $K$-theory) rules out $S^5, S^7, \ldots$
