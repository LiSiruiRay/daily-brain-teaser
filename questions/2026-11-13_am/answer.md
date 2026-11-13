# Answer: The Geometric Mean Is Superadditive

## Key Idea / Intuition

Both sides scale the same way if you multiply a single pair $(a_i,b_i)$ by $\lambda>0$: each side picks up a factor $\lambda^{1/n}$. So you may rescale each coordinate independently and assume $a_i+b_i=1$ for every $i$. The right side then becomes $1$. The claim reduces to $G(a)+G(b)\le 1$, and $1$ is exactly $\mathrm{AM}(a)+\mathrm{AM}(b)$, because the $a_i$ and $b_i$ pair up to sum to $1$. Applying AM–GM twice finishes the proof.

---

## Formal Proof / Solution

**Step 1: Degenerate case.** Suppose $a_i+b_i=0$ for some $i$. Since both numbers are nonnegative, $a_i=b_i=0$. Then both products on the left vanish and the right side is $0$, so equality holds trivially. From now on assume $a_i+b_i>0$ for all $i$.

**Step 2: Normalize.** Set
$$
x_i=\frac{a_i}{a_i+b_i},\qquad y_i=\frac{b_i}{a_i+b_i},\qquad\text{so } x_i,y_i\ge 0,\quad x_i+y_i=1.
$$
Divide the desired inequality by $\big[\prod_i (a_i+b_i)\big]^{1/n}>0$. It becomes
$$
\Big(\prod_{i=1}^n x_i\Big)^{1/n}+\Big(\prod_{i=1}^n y_i\Big)^{1/n}\;\le\;1.
$$

**Step 3: Apply AM–GM twice.**
$$
\Big(\prod x_i\Big)^{1/n}\le \frac1n\sum_{i=1}^n x_i,
\qquad
\Big(\prod y_i\Big)^{1/n}\le \frac1n\sum_{i=1}^n y_i.
$$
Adding the two inequalities gives
$$
\Big(\prod x_i\Big)^{1/n}+\Big(\prod y_i\Big)^{1/n}\le \frac1n\sum_{i=1}^n (x_i+y_i)=\frac1n\cdot n=1.
$$
Multiplying back by $\big[\prod(a_i+b_i)\big]^{1/n}$ gives the original inequality. $\blacksquare$

**Equality.** Assume all $a_i+b_i>0$. Equality in AM–GM requires all $x_i$ equal, and then all $y_i=1-x_i$ are automatically equal. All $x_i$ equal means $a_i/(a_i+b_i)$ is constant, which is equivalent to $b_i/a_i$ being constant (allowing the value $\infty$). So equality holds exactly when the vectors $(a_1,\dots,a_n)$ and $(b_1,\dots,b_n)$ are proportional. Equality also holds trivially in the degenerate case $a_i=b_i=0$ for some $i$.

---

## Remarks

- **A convexity viewpoint.** Assume all $a_i>0$ and put $s_i=\log(b_i/a_i)$. The inequality becomes Jensen's inequality for the convex function $f(s)=\log(1+e^s)$:
  $$\frac1n\sum f(s_i)\ge f\Big(\frac1n\sum s_i\Big).$$
- **Concavity.** The geometric mean $G$ is homogeneous of degree $1$. For such functions, superadditivity is equivalent to concavity. So this problem is really the statement that $G$ is concave on the nonnegative orthant.
- **Matrix version.** For positive semidefinite $A,B$, the Minkowski determinant inequality states $\det(A+B)^{1/n}\ge\det A^{1/n}+\det B^{1/n}$. When $A$ and $B$ are positive definite, write $A=B^{1/2}CB^{1/2}$ with $C$ positive definite, and diagonalize $C$ in an orthonormal basis. The inequality then reduces to the diagonal case, which is exactly this problem.
