# Answer: Sum of Squares Under a Linear Constraint

## Key Idea / Intuition

The sum of squares can be made arbitrarily small by spreading the total weight $A$ over many terms (like equal slices), but it can **never reach zero** since all $x_j > 0$. On the upper end, concentrating nearly all weight in a single term pushes $\sum x_j^2$ close to $A^2$, but strict positivity prevents it from actually reaching $A^2$. So the answer is the open interval $(0, A^2)$.

---

## Formal Proof / Solution

**Step 1: Upper bound — $\sum x_j^2 < A^2$.**

By the Cauchy–Schwarz inequality (or simply because all $x_j > 0$ and their sum is $A$):
$$\sum_{j=0}^{\infty} x_j^2 \leq \left(\sum_{j=0}^{\infty} x_j\right)^2 = A^2$$
is **not** the right bound here. Let's think more carefully.

Since all $x_j > 0$ and $\sum x_j = A$, we have $x_j < A$ for every $j$. Therefore:
$$\sum_{j=0}^{\infty} x_j^2 = \sum_{j=0}^{\infty} x_j \cdot x_j < \sum_{j=0}^{\infty} x_j \cdot A = A \cdot A = A^2.$$

So $\sum x_j^2 < A^2$.

**Step 2: Approaching $A^2$ — the upper bound is tight.**

Let $x_0 = A - \epsilon \cdot \sum_{j=1}^\infty r^j$ and distribute the remaining weight $\epsilon$-small pieces geometrically. More directly: take
$$x_0 = A(1-\epsilon), \quad x_j = A\epsilon \cdot 2^{-j} \text{ for } j \geq 1,$$
so that $\sum x_j = A(1-\epsilon) + A\epsilon = A$. Then:
$$\sum x_j^2 = A^2(1-\epsilon)^2 + A^2\epsilon^2\sum_{j=1}^\infty 4^{-j} = A^2(1-\epsilon)^2 + \frac{A^2\epsilon^2}{3}.$$
As $\epsilon \to 0^+$, this approaches $A^2$. So $A^2$ is a supremum but is **not achieved**.

**Step 3: Lower bound — $\sum x_j^2 > 0$.**

Since each $x_j > 0$, clearly $\sum x_j^2 > 0$.

**Step 4: Approaching $0$ — the lower bound is tight.**

Take $x_j = \frac{A}{n} \cdot \mathbf{1}_{j < n}$ for large $n$ (i.e., equal weights on the first $n$ terms, tiny positive values for the rest — but we need all $x_j > 0$).

More carefully: take $x_j = c \cdot r^j$ for $0 < r < 1$, so $\sum x_j = \frac{c}{1-r} = A$, meaning $c = A(1-r)$. Then:
$$\sum x_j^2 = c^2 \sum r^{2j} = \frac{c^2}{1-r^2} = \frac{A^2(1-r)^2}{1-r^2} = \frac{A^2(1-r)}{1+r}.$$
As $r \to 1^-$, this approaches $0$. So $0$ is an infimum but is **not achieved**.

**Step 5: All values in $(0, A^2)$ are achieved.**

The function $r \mapsto \frac{A^2(1-r)}{1+r}$ is continuous and maps $(0,1)$ onto $(0, A^2)$ (it equals $A^2/3$ at $r=1/2$, etc.). By the intermediate value theorem, every value in $(0, A^2)$ is achieved.

**Conclusion:**

The set of possible values of $\displaystyle\sum_{j=0}^{\infty} x_j^2$ is exactly the open interval
$$\boxed{(0,\, A^2)}.$$
