# Answer: The Polynomial That Is Always Divisible by n!

## Key Idea / Intuition

The product $\prod_{i < j}(a_j - a_i)$ looks like a Vandermonde determinant — and the key insight is that when you evaluate a Vandermonde determinant at **integer** arguments, you can relate it to a product of binomial coefficients, each of which is an integer. The ratio of the Vandermonde determinant to $1! \cdot 2! \cdots (n-1)!$ is itself a product of integers (it counts something combinatorially), which forces the divisibility.

More concretely: sort the $a_i$ and compare the product to the "standard" Vandermonde at $\{0, 1, 2, \ldots, n-1\}$. The standard one equals $\prod_{k=0}^{n-1} k! = 1!\cdot 2!\cdots (n-1)!$, and for any integer inputs the ratio is an integer.

---

## Formal Proof / Solution

**Step 1: Reduction to distinct values.**

If any two $a_i$ are equal, the product is $0$, which is divisible by anything. So assume the $a_i$ are distinct integers.

**Step 2: The Vandermonde connection.**

Order the integers: let $b_1 < b_2 < \cdots < b_n$ be $a_1, \ldots, a_n$ in increasing order (the absolute value of the product is unchanged by permutation). Then

$$\prod_{1 \le i < j \le n}(b_j - b_i) > 0.$$

**Step 3: Express as a product of binomial coefficients.**

Define the falling-factorial / binomial counting as follows. We claim:

$$\frac{\prod_{i < j}(b_j - b_i)}{1!\cdot 2!\cdots (n-1)!} = \det\left[\binom{b_i}{j-1}\right]_{i,j=1}^{n}.$$

Here is why. The Vandermonde determinant satisfies

$$\det[b_i^{j-1}]_{i,j} = \prod_{i<j}(b_j - b_i).$$

Now consider the matrix $M$ with entries $M_{ij} = \binom{b_i}{j-1}$. Since $\binom{b}{k} = \frac{b^k}{k!} - \text{lower terms}$, the column operations converting $[b_i^{j-1}]$ to $[\binom{b_i}{j-1}]$ multiply column $j$ by $\frac{1}{(j-1)!}$. Hence

$$\det\left[\binom{b_i}{j-1}\right] = \frac{1}{0!\cdot 1!\cdots (n-1)!}\det[b_i^{j-1}] = \frac{\prod_{i<j}(b_j - b_i)}{1!\cdot 2!\cdots (n-1)!}.$$

**Step 4: The determinant is an integer.**

The matrix $\left[\binom{b_i}{j-1}\right]$ has integer entries (since each $b_i$ is an integer and $\binom{m}{k} \in \mathbb{Z}$ for all integers $m \ge 0$ and $k \ge 0$; for negative integers one checks $\binom{m}{k}$ is still an integer). Therefore its determinant is an integer.

**Conclusion.**

$$1!\cdot 2!\cdots(n-1)! \;\Big|\; \prod_{1\le i < j \le n}(a_j - a_i). \qquad \blacksquare$$

**Sanity check with $n=3$, $(a_1,a_2,a_3) = (0,1,3)$:**
$$\prod_{i<j}(a_j - a_i) = (1-0)(3-0)(3-1) = 6, \quad 1!\cdot 2! = 2. \quad 2\mid 6. \checkmark$$

**Why this is beautiful:** The quantity $\frac{\prod_{i<j}(b_j-b_i)}{1!\cdots(n-1)!}$ secretly counts the number of Standard Young Tableaux of staircase shape, or equivalently appears in the hook-length formula — the divisibility is not an accident but reflects deep combinatorial structure.
