# Answer: Vanishing Integral on All Measurable Sets

## Key Idea / Intuition

The first part uses a classical bootstrapping trick: if $\int_a^b f = 0$ for all intervals, then by approximation the same holds for all open sets, then all measurable sets. Once $\int_E f = 0$ for every measurable $E$, you choose $E = \{f > 0\}$ and $E = \{f < 0\}$ separately — both integrals being zero forces $f = 0$ a.e.

The twist resolves itself: **no such non-zero $g$ can exist**. The argument for the first part already shows that "$\int_E g = 0$ for every measurable $E$" implies $g = 0$ a.e. So the two parts are actually one theorem, with the first part being the key engine.

---

## Formal Proof / Solution

### Step 1: From intervals to all measurable sets

Define $F(x) = \int_0^x f(t)\, dt$. The hypothesis says $F(b) - F(a) = 0$ for all $a \le b$, so $F \equiv 0$ on $[0,1]$.

By the **Lebesgue Differentiation Theorem**, $F'(x) = f(x)$ for almost every $x$. Since $F \equiv 0$, we have $F'(x) = 0$ a.e., so $f = 0$ a.e.

*Alternatively (without differentiating):* From $\int_a^b f = 0$ for all intervals, we extend to all measurable sets by approximation:

- Every open set $U \subseteq [0,1]$ is a countable union of disjoint open intervals, so $\int_U f = 0$.
- Every closed set $C$ satisfies $\int_C f = \int_{[0,1]} f - \int_{[0,1]\setminus C} f = 0 - 0 = 0$.
- A standard monotone class / $\pi$-$\lambda$ argument (or Carathéodory extension) gives $\int_E f = 0$ for **every** measurable $E \subseteq [0,1]$.

### Step 2: $\int_E f = 0$ for all measurable $E$ implies $f = 0$ a.e.

Let $E^+ = \{x \in [0,1] : f(x) > 0\}$. This is measurable, so:

$$\int_{E^+} f(x)\, dx = 0.$$

But on $E^+$, the integrand is strictly positive, so $\mu(E^+) = 0$.

Similarly, let $E^- = \{x : f(x) < 0\}$, giving $\int_{E^-} f = 0$, so $\mu(E^-) = 0$.

Hence $f = 0$ outside $E^+ \cup E^-$, which has measure zero. **$f = 0$ a.e.** $\blacksquare$

### Step 3: Resolution of the twist

The question asks: can there exist a *non-zero* $g$ with $\int_E g = 0$ for every measurable $E$?

**No.** Apply Step 2 directly: the hypothesis $\int_E g = 0$ for every measurable $E$ is strictly stronger than the hypothesis of Step 1 (it already includes all measurable sets, not just intervals). Step 2 alone gives $g = 0$ a.e.

So the "twist" is a trap — the condition for all measurable sets is self-defeating and forces $g = 0$ a.e. immediately. There is no exotic counterexample hiding here.

### Summary

$$\boxed{f = 0 \text{ a.e.}, \quad \text{and no non-zero } g \text{ can satisfy } \int_E g = 0 \text{ for all measurable } E.}$$

The beautiful point: **the measurable sets are "rich enough" that knowing all their integrals completely determines $f$ up to a null set.** This is the measure-theoretic content of the Lebesgue integral being determined by its values on all measurable sets.
