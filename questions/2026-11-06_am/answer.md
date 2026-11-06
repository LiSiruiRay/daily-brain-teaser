# Answer: Averaging a Matrix Group Gives a Projection

## Key Idea / Intuition

Averaging over a group produces something the group cannot move. Multiplying the sum $S = \sum M_i$ by any group element only permutes the terms, so $M_j S = S$. It follows that $S/r$ is idempotent, meaning it is a projection. The trace of a projection equals its rank, the dimension of the subspace it projects onto. So "total trace $= 0$" says the projection has rank $0$, and a rank-zero matrix is the zero matrix.

---

## Formal Proof / Solution

**Step 1: The sum is absorbed by the group.**
Let $S = \sum_{i=1}^r M_i$. Fix any $M_j \in G$. Because $G$ is a group, the map $M_i \mapsto M_j M_i$ is a bijection of $G$ onto itself. Therefore

$$M_j S = \sum_{i=1}^r M_j M_i = \sum_{M \in G} M = S.$$

This uses only the group structure, not that the identity is $I_n$.

**Step 2: $S/r$ is idempotent.**
Sum the identity from Step 1 over all $j$:

$$S^2 = \Big(\sum_{j} M_j\Big) S = \sum_{j=1}^r M_j S = rS.$$

Set $P = \tfrac{1}{r} S$. Then

$$P^2 = \frac{1}{r^2} S^2 = \frac{1}{r^2}\, rS = P.$$

**Step 3: For an idempotent, trace equals rank.**
Since $P^2 = P$, the minimal polynomial of $P$ divides $x^2 - x = x(x-1)$. This polynomial has distinct roots, so $P$ is diagonalizable with every eigenvalue equal to $0$ or $1$. Equivalently, $\mathbb{R}^n = \operatorname{im} P \oplus \ker P$, with $P$ acting as the identity on $\operatorname{im} P$ and as $0$ on $\ker P$. Hence

$$\operatorname{tr}(P) = \#\{\text{eigenvalues equal to } 1\} = \operatorname{rank}(P).$$

**Step 4: Conclude.**
By hypothesis,

$$\operatorname{tr}(P) = \frac{1}{r}\sum_{i=1}^r \operatorname{tr}(M_i) = 0.$$

So $\operatorname{rank}(P) = 0$, which means $P = 0$, and therefore $S = rP = 0$. $\blacksquare$

---

### Remarks

- **What $P$ projects onto.** When $G \subset GL_n(\mathbb{R})$, so that the identity of $G$ is $I_n$, the image of $P$ is exactly the space of vectors fixed by every element of $G$:
  - If every $M \in G$ fixes $v$, then $Pv = \frac{1}{r}\sum_i M_i v = v$.
  - Conversely, if $v = Pw$, then $M_j v = M_j P w = P w = v$ by Step 1.

  Therefore
  $$\frac{1}{r}\sum_{g\in G}\operatorname{tr}(g) = \dim\{v : gv = v \ \ \forall g \in G\}.$$
  This is the linear-algebra version of Burnside's lemma. It is also the statement "$\langle \chi, \mathbf{1}\rangle$ = multiplicity of the trivial representation" from character theory.

- **Corollary.** The average trace over a finite matrix group is always a non-negative integer. In particular, it can never be negative.
