# Answer: The Factorization That Can't Make Up Its Mind: Non-Uniqueness of NMF

## Key Idea / Intuition

Read $X = WH$ row by row: each data point (a row of $X$) must be a non-negative combination of the "parts" (the rows of $H$). The parts themselves must lie in the non-negative orthant. So the cone spanned by the parts must be squeezed between two cones: it must contain the cone of the data, and it must sit inside the orthant.

If there is "open space" between the data cone and the coordinate axes, the parts can slide around freely in that gap. Then $W$ and $H$ are not identifiable, even though the non-negativity constraints look rigid algebraically.

Part (a) shows why the non-uniqueness is subtle. The new factorizations are not obtained from a non-negative $Q$ with non-negative inverse. Instead, $Q$ has negative entries, and they happen to be cancelled by the slack in the data.

---

## Formal Proof / Solution

### (a) Non-negative matrices with non-negative inverses are monomial

Let $P = Q^{-1}$, so $QP = I$. For $i \ne j$,
$$0 = (QP)_{ij} = \sum_k q_{ik}\,p_{kj}.$$
Every term is $\ge 0$, so every term vanishes:
$$q_{ik}>0 \;\Longrightarrow\; p_{kj}=0 \text{ for all } j\neq i. \tag{$*$}$$
In words, if $q_{ik}>0$, then row $k$ of $P$ is supported only in column $i$, i.e. it is a multiple of $e_i^T$.

Suppose some row $i$ of $Q$ had two positive entries $q_{ik}, q_{il}$ with $k\ne l$. By $(*)$, rows $k$ and $l$ of $P$ would both be multiples of $e_i^T$. They would then be linearly dependent, contradicting the invertibility of $P$.

Each row of $Q$ is nonzero, since $Q$ is invertible. So each row of $Q$ has exactly one positive entry. These entries must lie in distinct columns, again by invertibility. Hence $Q = (\text{permutation})\times(\text{positive diagonal})$. $\blacksquare$

### (b) A two-parameter family of factorizations

**Reformulate geometrically.** Write $x_1=(2,1)$ and $x_2=(1,2)$ for the rows of $X$, and $h_1, h_2$ for the rows of $H$. Then $X = WH$ says
$$x_i = w_{i1}h_1 + w_{i2}h_2,\qquad w_{ik}\ge 0.$$
So both data points must lie in $\operatorname{cone}(h_1,h_2)$, and $h_1,h_2 \in \mathbb{R}^2_{\ge 0}$.

**Both factors are invertible.** Since $\det X = 3 \neq 0$, both $W$ and $H$ must be invertible. In particular $h_1, h_2$ are independent, so $W = XH^{-1}$ is uniquely determined by $H$.

**Parametrize the parts.** Normalize the rows of $H$ to sum to $1$, so that $h = (a, 1-a)$ with $a\in[0,1]$. A direction in the orthant is then recorded by the single number $a$:
- $x_1$ corresponds to $a = 2/3$,
- $x_2$ corresponds to $a = 1/3$.

**Containment condition.** In two dimensions, $\operatorname{cone}(h_1,h_2)$ is the set of directions with $a$ between $a_1$ and $a_2$. It contains both data directions if and only if (after ordering)
$$a_1 \in \left[\tfrac23,\,1\right],\qquad a_2\in\left[0,\,\tfrac13\right].$$
Every such choice works: $W = XH^{-1}$ is then non-negative, because the coefficients of a point in a 2D cone with respect to its two generators are non-negative.

**Conclusion.** The normalized, ordered factorizations are exactly
$$H=\begin{pmatrix} a & 1-a\\ b & 1-b\end{pmatrix},\quad a\in[\tfrac23,1],\ b\in[0,\tfrac13],\qquad W = XH^{-1}.$$
This is a full two-parameter family. By part (a), none of these factorizations is related to another by a trivial rescaling or permutation.

**Two extreme members:**
- $a=1,\ b=0$: $H=I$ and $W=X$. The parts are the coordinate axes.
- $a = 2/3,\ b=1/3$: $H = \tfrac13 X$ and $W = 3I$. The parts are the data points themselves.

An intermediate example comes from $h_1 \propto (1,t)$ and $h_2\propto(t,1)$, giving
$$W=\frac{1}{1-t^2}\begin{pmatrix}2-t&1-2t\\1-2t&2-t\end{pmatrix},\qquad t\in[0,\tfrac12].$$
At $t=\tfrac12$ this gives $W = 2I$ and $H=\begin{pmatrix}1&\frac12\\ \frac12&1\end{pmatrix}$. Check: $WH = \begin{pmatrix}2&1\\1&2\end{pmatrix}$.

**Picture.** Both data rays lie strictly inside the open quadrant. The wedges between the data cone and each axis are "open space", and each part can be placed anywhere in its wedge.

### (c) Why $X = I_2$ is different

Now the data points are $e_1$ and $e_2$, which already lie on the boundary of the orthant. The cone of the parts must contain both axes and stay inside the orthant, so it must equal the orthant. This forces $a_1 = 1$ and $b = 0$, hence $H = I$ and $W = I$ up to trivial ambiguity.

Equivalently, any factorization $I = WH$ has $H = W^{-1}$ with both $W$ and $H$ non-negative. Part (a) then says $W$ is monomial.

**Moral.** NMF is identifiable only when the data "touch the walls" of the orthant, i.e. when the data cone is pinned against the coordinate axes. Donoho–Stodden make this precise with separability-type conditions. When the data float in the interior, the factorization slides freely. The Lee–Seung multiplicative algorithm then returns whichever member of the family its initialization leads to, and the "parts" it finds are partly an artifact of where it started.
