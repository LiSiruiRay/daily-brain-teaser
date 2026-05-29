# Answer: A Determinant of Sums

## Key Idea / Intuition

The matrix looks complicated, but a clever sequence of row operations strips it down to something triangular almost immediately. The key observation is: **subtract each row from the one below it**. Since adjacent rows of $A$ differ by at most one entry, this telescoping turns the dense matrix into a bidiagonal upper-triangular matrix, whose determinant reads off instantly from the diagonal.

---

## Formal Proof / Solution

**Step 1: Row reduction.**

Perform the row operations $R_k \leftarrow R_k - R_{k-1}$ for $k = n, n-1, \ldots, 2$ (in that order, working from the bottom up).

For the original matrix, row $k$ has entries:
$$A_{k,j} = \min(k,j).$$

After subtracting row $k-1$ from row $k$, the new row $k$ (for $k \geq 2$) has entries:
$$\min(k,j) - \min(k-1,j).$$

Now observe:
- If $j < k$: $\min(k,j) = j = \min(k-1,j)$, so the difference is $0$.
- If $j = k$: $\min(k,k) - \min(k-1,k) = k - (k-1) = 1$.
- If $j > k$: $\min(k,j) = k$ and $\min(k-1,j) = k-1$, so the difference is $1$.

So the new row $k$ (for $k \geq 2$) is:
$$(\underbrace{0, \ldots, 0}_{k-1 \text{ zeros}}, 1, 1, \ldots, 1).$$

Row $1$ is unchanged: $(1, 1, 1, \ldots, 1)$.

**Step 2: The resulting matrix.**

After these row operations, the matrix becomes:

$$\begin{pmatrix}
1 & 1 & 1 & 1 & \cdots & 1 \\
0 & 1 & 1 & 1 & \cdots & 1 \\
0 & 0 & 1 & 1 & \cdots & 1 \\
\vdots & & & \ddots & & \vdots \\
0 & 0 & \cdots & 0 & 1 & 1 \\
0 & 0 & \cdots & 0 & 0 & 1
\end{pmatrix}.$$

This is upper triangular with all diagonal entries equal to $1$.

**Step 3: Read off the determinant.**

Since row operations of the form $R_k \leftarrow R_k - R_{k-1}$ do not change the determinant, and the resulting matrix is upper triangular with all $1$s on the diagonal:

$$\det(A) = 1.$$

**Sanity check for small $n$:**

For $n = 2$:
$$\det\begin{pmatrix}1 & 1 \\ 1 & 2\end{pmatrix} = 2 - 1 = 1. \checkmark$$

For $n = 3$:
$$\det\begin{pmatrix}1 & 1 & 1 \\ 1 & 2 & 2 \\ 1 & 2 & 3\end{pmatrix} = 1(6-4) - 1(3-2) + 1(2-2) = 2 - 1 + 0 = 1. \checkmark$$

**Conclusion:**

$$\boxed{\det(A) = 1}$$

for all $n \geq 1$.

**Bonus remark:** The matrix $A_{ij} = \min(i,j)$ is the covariance matrix of a standard Brownian motion $(B_1, B_2, \ldots, B_n)$ at integer times. The fact that its determinant is $1$ reflects a deep property of the increments: the Brownian increments $B_1, B_2 - B_1, \ldots, B_n - B_{n-1}$ are i.i.d. $N(0,1)$, so the transformation from $(B_k)$ to its increments is volume-preserving — exactly what determinant $1$ says!
