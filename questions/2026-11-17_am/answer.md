# Answer: Loops in a Topological Group Commute

## Key Idea / Intuition

Concatenation means "do $f$, then do $g$." Pointwise multiplication means "do $f$ and $g$ simultaneously." These agree if you multiply "$f$ while $g$ waits at $e$" by "$g$ while $f$ waits at $e$." Waiting at $e$ costs nothing, because $e$ is the identity. The waiting can also be scheduled in the opposite order, so $f$-then-$g$ and $g$-then-$f$ both deform to the same simultaneous motion $f\cdot g$, and hence to each other.

---

## Formal Proof / Solution

Let $c$ denote the constant loop at $e$. Recall the standard path homotopies $f * c \simeq f$ and $c * g \simeq g$ (reparametrization).

**Step 1: Concatenation is a pointwise product.** Compute $(f*c)\cdot(c*g)$:

$$
\big((f*c)\cdot(c*g)\big)(s) =
\begin{cases}
f(2s)\cdot e = f(2s), & 0 \le s \le \tfrac12,\\[2pt]
e\cdot g(2s-1) = g(2s-1), & \tfrac12 \le s \le 1.
\end{cases}
$$

So $(f*c)\cdot(c*g) = f*g$ **exactly**. In the same way, $(c*f)\cdot(g*c) = g*f$.

**Step 2: The pointwise product respects homotopy.** Suppose $F: f_0 \simeq f_1$ and $G': g_0 \simeq g_1$ are path homotopies of loops at $e$. Then
$$H(s,t) = F(s,t)\,G'(s,t)$$
is continuous, because multiplication $G\times G\to G$ is continuous. At the endpoints, $H(0,t)=H(1,t)=e\cdot e=e$. Hence $H$ is a path homotopy $f_0\cdot g_0 \simeq f_1 \cdot g_1$.

**(a)** Combine Steps 1 and 2 with $f*c\simeq f$ and $c*g\simeq g$:
$$f * g = (f*c)\cdot(c*g) \;\simeq\; f\cdot g.$$

**(b)** Similarly,
$$g * f = (c*f)\cdot(g*c) \;\simeq\; f\cdot g.$$
Therefore $f*g \simeq g*f$, so $[f][g] = [g][f]$ in $\pi_1(G,e)$.

(In a path-connected group, the choice of basepoint does not matter. Note also that we never used inverses. The argument works for any **H-space**, meaning any space with a continuous multiplication having a two-sided identity.)

**(c)** It suffices to show that both fundamental groups are non-abelian.

- **Figure-eight:** $\pi_1(S^1\vee S^1)\cong F_2$, the free group on two generators $a,b$, and $ab\ne ba$ in $F_2$.
- **Klein bottle $K$:** $\pi_1(K) \cong \langle a, b \mid bab^{-1} = a^{-1}\rangle$. Map this group onto the infinite dihedral group of isometries of $\mathbb{R}$ by sending $a \mapsto (x\mapsto x+1)$ and $b \mapsto (x \mapsto -x)$.
  - The relation holds: $bab^{-1}(x) = -(-x+1) = x-1$, which is $a^{-1}(x)$.
  - The images do not commute: $a b(x) = 1-x$ while $ba(x) = -x-1$.
  
  So $\pi_1(K)$ is non-abelian.

By (b), neither space can carry a topological group structure. In fact, neither can even carry an H-space structure. $\blacksquare$

**Remark.** The same "interchange" trick, applied to the two coordinate directions of $[0,1]^n$, shows that $\pi_n(X)$ is abelian for every space $X$ when $n\ge 2$.
