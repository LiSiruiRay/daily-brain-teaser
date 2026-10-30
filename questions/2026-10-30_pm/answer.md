# Answer: A Finite Set Closed Under Cross Product

## Key Idea / Intuition

The cross product can stretch and shrink lengths. If some nonzero vector had length $\neq 1$, you could cross with it repeatedly and produce infinitely many distinct vectors. So finiteness forces every nonzero element to be a **unit vector**.

Once all nonzero lengths are $1$, the identity $|s\times t|=\sin\theta$ forces every pair of vectors to be either parallel or orthogonal. What survives is an orthonormal frame together with its negatives and $0$. This is exactly $\{0,\pm i,\pm j,\pm k\}$, the "quaternion units," and it has $7$ elements.

**Answer: $n=1$ and $n=7$.**

---

## Formal Proof / Solution

**Step 0: $0\in S$.** The set $S$ is nonempty, so pick $v\in S$. Then $0=v\times v\in S$.

So $S=\{0\}$ works, and $n=1$ is possible. From now on, assume $S$ contains a nonzero vector.

**Step 1: every nonzero element of $S$ has a nonzero perpendicular partner in $S$.**
Let $s\in S$ with $s\neq 0$. Then $s=a\times b$ for some $a,b\in S$. Since $s\ne 0$, we have $a\neq 0$, and $s\perp a$.

**Step 2: every nonzero element of $S$ is a unit vector.**
Take $s$ and $a$ as in Step 1, so $s\perp a$ and both are nonzero elements of $S$. For any vector $x\perp s$, the BAC–CAB rule gives

$$(s\times x)\times s \;=\; -\,s\times(s\times x)\;=\; -\big(s\,(s\cdot x)-x\,|s|^2\big)\;=\;|s|^2\,x .$$

Set $a_0=a$ and $a_{k+1}=(s\times a_k)\times s$. Each $a_k$ is a multiple of $a$, so it stays perpendicular to $s$. Since $S$ is closed under $\times$, each $a_k$ lies in $S$. The formula above gives

$$a_k=|s|^{2k}\,a .$$

If $|s|\neq 1$, these vectors have distinct lengths, so $S$ would be infinite. Hence $|s|=1$.

**Step 3: nonzero elements are pairwise parallel or orthogonal.**
For nonzero $s,t\in S$ at angle $\theta$, the vector $s\times t$ lies in $S$ and has length $\sin\theta$. By Step 2, this length must be $0$ or $1$. Therefore $\theta\in\{0,\pi/2,\pi\}$.

**Step 4: identifying $S$.**
Pick a nonzero $s\in S$ and write $s=a\times b$ with $a,b\in S$. Then $a$ and $b$ are nonzero unit vectors, and $\sin\angle(a,b)=|s|=1$, so $a\perp b$. Thus $(a,b,s)$ is a right-handed orthonormal frame, and

$$b\times a=-s,\quad s\times a=b,\quad a\times s=-b,\quad b\times s=a,\quad s\times b=-a .$$

So $S\supseteq\{0,\pm a,\pm b,\pm s\}$.

Now take any nonzero $t\in S$. It is a unit vector, and by Step 3 it is parallel or orthogonal to each of $a$, $b$, $s$. It cannot be orthogonal to all three, since they span $\mathbb{R}^3$. So $t$ is parallel to one of them, which means $t\in\{\pm a,\pm b,\pm s\}$.

Hence
$$S=\{0,\pm a,\pm b,\pm s\},\qquad |S|=7 .$$

**Step 5: $n=7$ really works.** Take $S=\{0,\pm e_1,\pm e_2,\pm e_3\}$.

- **Closure:** each product $e_i\times e_j$ lies in $\{0,\pm e_k\}$, so all cross products stay in $S$.
- **Every element is attained:** $0=e_1\times e_1$, and $\pm e_3=\pm e_1\times e_2$. The other basis vectors are handled the same way by cyclic symmetry.

So $S=\{v\times w : v,w\in S\}$.

$$\boxed{n\in\{1,7\}}$$

**Remark.** For pure quaternions, $v\times w$ is the imaginary part of the product $vw$. The 7-element set is the quaternion group $\{\pm1,\pm i,\pm j,\pm k\}$ with $\pm1$ replaced by $0$, because the real part has been discarded.
