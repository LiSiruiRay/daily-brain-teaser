# Answer: Pointwise Limits and Meagre Discontinuity Sets

## Key Idea / Intuition

The key insight is to quantify "how bad" a discontinuity is using the **oscillation** of $f$ at a point: $f$ is discontinuous at $x$ if and only if its oscillation is positive. The oscillation can be expressed via the functions $f_n$, which are continuous, and this lets us write the discontinuity set as a countable union of **closed** sets, each of which turns out to be **nowhere dense** by a Baire-category argument. The punchline: pointwise limits of continuous functions are exactly the **Baire class 1** functions, and their discontinuity sets are meagre.

---

## Formal Proof / Solution

### Step 1: Define the oscillation

For a bounded function $f$ on $[0,1]$, define the **oscillation of $f$ at $x$**:
$$\omega_f(x) = \lim_{\delta \to 0^+} \sup_{|x-y|<\delta} |f(y) - f(z)|.$$

The function $f$ is continuous at $x$ if and only if $\omega_f(x) = 0$. So the discontinuity set is:
$$D = \{x \in [0,1] : \omega_f(x) > 0\} = \bigcup_{k=1}^\infty \left\{x : \omega_f(x) \geq \frac{1}{k}\right\}.$$

It suffices to show each set $F_k = \{x : \omega_f(x) \geq \frac{1}{k}\}$ is **nowhere dense**.

### Step 2: Each $F_k$ is closed

If $\omega_f(x_n) \geq \frac{1}{k}$ and $x_n \to x$, then for any $\delta > 0$, points near $x_n$ (for large $n$) are near $x$, so the oscillation of $f$ in a $\delta$-ball around $x$ is also $\geq \frac{1}{k}$. Hence $x \in F_k$, so $F_k$ is closed.

### Step 3: Each $F_k$ has empty interior (i.e., is nowhere dense)

Suppose for contradiction that $F_k$ contains an open interval $I$. We derive a contradiction using the **Baire Category Theorem** applied to $I$ (which is a complete metric space).

Define, for each $m, n$:
$$E_{m,n} = \left\{x \in I : |f_j(x) - f_l(x)| \leq \frac{1}{3k} \text{ for all } j, l \geq m\right\}.$$

Since the $f_n$ are continuous, each $E_{m,n}$ is **closed**. By pointwise convergence, for every $x \in I$ there exists $m$ such that $|f_j(x) - f_l(x)| \leq \frac{1}{3k}$ for all $j, l \geq m$; so $I = \bigcup_{m=1}^\infty E_{m,m}$.

By the **Baire Category Theorem**, some $E_{m_0, m_0}$ contains a nonempty open subinterval $J \subset I$.

### Step 4: On $J$, the oscillation of $f$ is small

For $x \in J$, since $f_n \to f$ pointwise:
$$|f(x) - f_{m_0}(x)| = \lim_{n\to\infty} |f_n(x) - f_{m_0}(x)| \leq \frac{1}{3k}.$$

For any $x \in J$, since $f_{m_0}$ is continuous at $x$, there exists $\delta > 0$ such that $|f_{m_0}(x) - f_{m_0}(y)| \leq \frac{1}{3k}$ for all $y$ with $|y - x| < \delta$ and $y \in J$.

Then for such $y$:
$$|f(x) - f(y)| \leq |f(x) - f_{m_0}(x)| + |f_{m_0}(x) - f_{m_0}(y)| + |f_{m_0}(y) - f(y)| \leq \frac{1}{3k} + \frac{1}{3k} + \frac{1}{3k} = \frac{1}{k}.$$

So $\omega_f(x) \leq \frac{1}{k}$ for all $x \in J$. But $J \subset I \subset F_k$ means $\omega_f(x) \geq \frac{1}{k}$ for all $x \in J$. 

### Step 5: Contradiction

This forces $\omega_f(x) = \frac{1}{k}$ exactly on $J$, but actually the inequality $\leq \frac{1}{k}$ and $\geq \frac{1}{k}$ give $\omega_f \equiv \frac{1}{k}$ on $J$ — while $f$ would actually be **continuous** at interior points of $J$ by the argument above (oscillation $< \frac{1}{k}$ for any $\frac{1}{k}$-bound). More carefully: repeating the argument with $\frac{1}{k}$ replaced by $\epsilon < \frac{1}{k}$ gives a contradiction. Hence $F_k$ has empty interior.

### Conclusion

The discontinuity set $D = \bigcup_{k=1}^\infty F_k$ is a countable union of nowhere-dense closed sets — a **meagre (first-category) set**. By the Baire Category Theorem on $[0,1]$, meagre sets have **dense complement**, so the continuity points of $f$ are dense. $\blacksquare$

**Upshot:** A pointwise limit of continuous functions (a Baire-1 function) can be very wild — e.g., the characteristic function of $\mathbb{Q}$ is Baire-1 — but it can never be discontinuous on a "thick" set in the Baire sense.
