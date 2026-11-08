# Answer: Cover's Counting Theorem: Capacity of a Hyperplane

## Key Idea / Intuition

Add the points one at a time. When a new point $x_{N+1}$ arrives, each old dichotomy either extends to it in one forced way or in both ways. It extends both ways exactly when the old labeling can be realized by a hyperplane that also passes through $x_{N+1}$. Such hyperplanes live in one fewer dimension, so they are counted by $C(N,d-1)$. This gives Pascal's recursion $C(N+1,d)=C(N,d)+C(N,d-1)$, which is why binomial coefficients appear.

The answer then reads as a binomial tail: the fraction of separable labelings is $P(\mathrm{Bin}(N-1,\tfrac12)\le d-1)$. Symmetry of the binomial makes this exactly $1/2$ at $N=2d$. So a linear classifier in $d$ dimensions can memorize about $2d$ random labels. This is the classical "capacity of the perceptron," and the reason zero training error means nothing when $p\gtrsim N$.

---

## Formal Proof / Solution

**Step 1: When does an old dichotomy split?**

Fix a dichotomy $D$ of $x_1,\dots,x_N$. Let $K_D=\{w: \operatorname{sign}(w\cdot x_i)=y_i\ \forall i\}$. This set is an intersection of open half-spaces, so it is an open convex cone.

**Claim.** $D$ extends to $x_{N+1}$ with *both* signs if and only if $K_D$ contains some $w_0$ with $w_0\cdot x_{N+1}=0$.

- ($\Rightarrow$) Suppose $w_+,w_-\in K_D$ with $w_\pm\cdot x_{N+1}\gtrless 0$. The segment between them lies in $K_D$ by convexity. By continuity it meets the hyperplane $\{w\cdot x_{N+1}=0\}$.
- ($\Leftarrow$) Since $K_D$ is open, $w_0\pm\varepsilon x_{N+1}\in K_D$ for small $\varepsilon>0$. These give $\pm\varepsilon\|x_{N+1}\|^2$ on $x_{N+1}$, so both signs occur.

Every other realizable $D$ extends in exactly one way. Therefore
$$
C(N+1,d)=C(N,d)+\#\{D:\ K_D\cap x_{N+1}^{\perp}\neq\varnothing\}.
$$

**Step 2: The splitting dichotomies are counted by $C(N,d-1)$.**

Let $P$ be the orthogonal projection onto $H=x_{N+1}^\perp\cong\mathbb{R}^{d-1}$. For $w\in H$ we have $w\cdot x_i=w\cdot Px_i$. So the dichotomies realizable by some $w\in H$ are exactly the dichotomies of the projected points $Px_1,\dots,Px_N$ realizable by homogeneous classifiers in $H$.

The projected points are in general position in $H$. A set of at most $d-1$ of them, $\{Px_i\}_{i\in S}$, is dependent iff some nontrivial combination $\sum_{i \in S} c_i x_i$ lies in $\operatorname{span}(x_{N+1})$. That would mean $\{x_i\}_{i\in S}\cup\{x_{N+1}\}$ is dependent. But this set has at most $d$ elements, so general position forbids it.

Hence the count is $C(N,d-1)$. The same induction shows that $C$ depends only on $N$ and $d$, and we get
$$
C(N+1,d)=C(N,d)+C(N,d-1).
$$

**Step 3: Base cases and the formula.**

- $C(1,d)=2$ for $d \ge 1$: take $w=\pm x_1$.
- $C(N,1)=2$: in $\mathbb{R}^1$ the only classifiers are $w>0$ and $w<0$.

Define $F(N,d)=2\sum_{k=0}^{d-1}\binom{N-1}{k}$. It matches both base cases:
- $F(1,d)=2\binom00=2$.
- $F(N,1)=2\binom{N-1}{0}=2$.

It also satisfies the same recursion, by Pascal's rule $\binom{N}{k}=\binom{N-1}{k}+\binom{N-1}{k-1}$:
$$
F(N+1,d)=2\sum_{k=0}^{d-1}\binom{N-1}{k}+2\sum_{k=0}^{d-2}\binom{N-1}{k}=F(N,d)+F(N,d-1).
$$
Hence $C(N,d)=F(N,d)$, proving (a).

**Step 4: Random labels (part b).**

$$
\Pr(\text{separable})=\frac{C(N,d)}{2^N}=\frac{1}{2^{N-1}}\sum_{k=0}^{d-1}\binom{N-1}{k}=\Pr\!\big(B\le d-1\big),\qquad B\sim\mathrm{Bin}\!\left(N-1,\tfrac12\right).
$$

- If $N\le d$, then $d-1\ge N-1$, so the sum covers every $k$ and the probability is $1$. Every labeling is realizable.
- If $N=2d$, then $B\sim\mathrm{Bin}(2d-1,\tfrac12)$, which has an odd number of trials. The symmetry $B\mapsto 2d-1-B$ swaps the events $\{B\le d-1\}$ and $\{B\ge d\}$. These two events partition the sample space, so
$$
\Pr(B\le d-1)=\tfrac12 .
$$

For large $d$, the binomial concentrates around $(N-1)/2$. The probability therefore drops sharply from $\approx1$ to $\approx0$ as $N/d$ crosses $2$.

**ML remark.** A classifier with an intercept in $\mathbb{R}^p$ is homogeneous in $\mathbb{R}^{p+1}$, so set $d=p+1$.
- If $N\le p+1$, any labeling whatsoever, including pure noise, is fit perfectly.
- Random labels stay separable with probability at least $1/2$ until $N=2(p+1)$.

This is why, in the $p\gg N$ regime, training error is uninformative and regularization (e.g. shrunken centroids, ridge, or margins) is essential.
