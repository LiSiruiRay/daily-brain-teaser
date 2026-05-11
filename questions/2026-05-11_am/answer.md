# Answer: Dirichlet Function and Lebesgue Measure Zero

## Key Idea / Intuition

The Dirichlet function is the poster child for why the Lebesgue integral was invented. Riemann integration "sees" oscillation at every scale and fails, but Lebesgue integration "doesn't care" about individual points or countable sets — a countable set has measure zero, so it contributes nothing to the integral. The sequence $f_n$ then gives a concrete, hands-on illustration that integrating through pointwise limits is valid here, exactly as the Monotone Convergence Theorem promises.

---

## Formal Proof / Solution

### Part 1: $f$ is not Riemann integrable

Recall: $f$ is Riemann integrable iff for every $\varepsilon > 0$ there exists a partition $P$ such that $U(f,P) - L(f,P) < \varepsilon$.

For **any** partition $P = \{x_0, x_1, \ldots, x_n\}$ of $[0,1]$, every subinterval $[x_{i-1}, x_i]$ contains both a rational and an irrational number (by density of $\mathbb{Q}$ and $\mathbb{R} \setminus \mathbb{Q}$ in $\mathbb{R}$). Therefore:

$$M_i = \sup_{[x_{i-1},x_i]} f = 1, \qquad m_i = \inf_{[x_{i-1},x_i]} f = 0.$$

So for every partition $P$:
$$U(f,P) = \sum_{i=1}^n M_i \Delta x_i = 1, \qquad L(f,P) = \sum_{i=1}^n m_i \Delta x_i = 0.$$

Hence $U(f,P) - L(f,P) = 1$ for all $P$, so $f$ is **not Riemann integrable**.

---

### Part 2: Lebesgue integral of $f$

The set of rationals $\mathbb{Q} \cap [0,1]$ is countable, hence has Lebesgue measure zero:

$$\mu(\mathbb{Q} \cap [0,1]) = 0.$$

We can write $f = \mathbf{1}_{\mathbb{Q} \cap [0,1]}$, the indicator of a null set. For any non-negative measurable simple function $\phi = \sum_i a_i \mathbf{1}_{A_i}$, the Lebesgue integral is $\sum_i a_i \mu(A_i)$. Here $f$ itself is a simple function (two values, two measurable sets):

$$\int_{[0,1]} f \, d\mu = 1 \cdot \mu(\mathbb{Q} \cap [0,1]) + 0 \cdot \mu((\mathbb{R}\setminus\mathbb{Q}) \cap [0,1]) = 1 \cdot 0 + 0 \cdot 1 = \boxed{0}.$$

Alternatively: $f = 0$ **almost everywhere** (a.e.), so its Lebesgue integral equals $\int 0 \, d\mu = 0$. This is the key philosophy: **sets of measure zero are invisible to Lebesgue integration**.

---

### Part 3: The sequence $f_n$ and MCT

**Pointwise convergence to $f$:** Fix any $x \in [0,1]$.
- If $x \notin \mathbb{Q}$: $f_n(x) = 0$ for all $n$, so $f_n(x) \to 0 = f(x)$. ✓
- If $x \in \mathbb{Q}$: then $x = q_k$ for some $k$. For all $n \geq k$, $f_n(x) = 1$, so $f_n(x) \to 1 = f(x)$. ✓

So $f_n \to f$ pointwise on all of $[0,1]$.

**Integral of $f_n$:** Each $f_n = \mathbf{1}_{\{q_1,\ldots,q_n\}}$ is the indicator of a finite set. Finite sets have measure zero, so:

$$\int_{[0,1]} f_n \, d\mu = 1 \cdot \mu(\{q_1, \ldots, q_n\}) = 1 \cdot 0 = 0 \quad \text{for every } n.$$

**Verification of MCT:** The Monotone Convergence Theorem states: if $0 \leq f_n \nearrow f$ a.e. and each $f_n$ is measurable, then

$$\lim_{n \to \infty} \int f_n \, d\mu = \int f \, d\mu.$$

Here:
- $f_n \geq 0$ ✓
- $f_n \leq f_{n+1}$ since $\{q_1,\ldots,q_n\} \subseteq \{q_1,\ldots,q_{n+1}\}$ ✓
- $f_n \to f$ pointwise ✓

And indeed:
$$\lim_{n\to\infty} \int f_n \, d\mu = \lim_{n\to\infty} 0 = 0 = \int f \, d\mu. \checkmark$$

The example is slightly degenerate (all integrals are $0$) but perfectly illustrates that the passage of the limit through the integral is valid — and shows how Lebesgue theory handles functions that are wildly discontinuous yet perfectly integrable.
