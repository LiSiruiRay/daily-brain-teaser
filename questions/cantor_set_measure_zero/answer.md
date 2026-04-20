# Answer: The Cantor Set — Measure Zero yet Uncountable

## Part 1: Measure Zero

At each stage $n$, we remove $2^{n-1}$ open intervals each of length $\tfrac{1}{3^n}$.

Total measure removed:

$$\sum_{n=1}^{\infty} 2^{n-1} \cdot \frac{1}{3^n} = \frac{1}{3} \sum_{n=1}^{\infty} \left(\frac{2}{3}\right)^{n-1} = \frac{1}{3} \cdot \frac{1}{1 - \frac{2}{3}} = 1$$

So **all of $[0,1]$ is removed**, and:

$$m(C) = m([0,1]) - 1 = 0 \qquad \blacksquare$$

---

## Part 2: Uncountable

**Key idea:** every point in $C$ has a base-3 (ternary) expansion using only the digits $\{0, 2\}$.

**Why:** At each stage, removing the middle third eliminates exactly those numbers whose ternary expansion has a $1$ in the $n$-th position (that is genuinely a $1$, not a tail of $2$'s). What remains are numbers expressible as:

$$x = \sum_{n=1}^{\infty} \frac{a_n}{3^n}, \qquad a_n \in \{0, 2\}$$

Now define the map $\varphi: C \to [0,1]$ by replacing each digit $2$ with $1$ and reading in base 2:

$$\varphi(x) = \sum_{n=1}^{\infty} \frac{a_n/2}{2^n}$$

This map is **surjective** onto $[0,1]$: every binary sequence $(b_n) \in \{0,1\}^{\mathbb{N}}$ lifts to a sequence $(2b_n) \in \{0,2\}^{\mathbb{N}}$, giving a point in $C$.

Since $[0,1]$ is uncountable and $\varphi: C \twoheadrightarrow [0,1]$, we conclude:

$$|C| \geq |[0,1]| = \mathfrak{c} \qquad \blacksquare$$

---

## The Punchline

The Cantor set has the same cardinality as $\mathbb{R}$, yet measure zero. The bijection works because $C$ has a **product structure**: each point is an independent binary choice at each stage, giving $\{0,2\}^{\mathbb{N}} \cong \{0,1\}^{\mathbb{N}}$, which has cardinality $2^{\aleph_0} = \mathfrak{c}$.

This is why "small in measure" and "small in cardinality" are completely orthogonal notions.
