# Answer: Devil's Staircase: FTC Fails Without Absolute Continuity

## Key Idea / Intuition

The Cantor function does all of its "climbing" on the Cantor set $C$, which has **Lebesgue measure zero**. Off $C$, the function is locally constant, so its derivative is zero — yet the total rise is 1. The FTC in its standard Lebesgue form holds if and only if $f$ is **absolutely continuous**, and the Cantor function is the canonical example of a continuous, monotone function that is **not** absolutely continuous. Absolute continuity is exactly the extra condition that bridges "derivative zero a.e." with "function is constant."

---

## Formal Proof / Solution

### Part (a): $f' = 0$ a.e.

The complement of the Cantor set in $[0,1]$ is the open set

$$[0,1] \setminus C = \bigcup_{k} I_k,$$

a countable union of open intervals (the removed middle thirds). By construction, $f$ is **constant on each $I_k$** (e.g., $f \equiv \frac{1}{2}$ on $(\frac{1}{3}, \frac{2}{3})$, etc.).

Therefore:

$$x \in [0,1] \setminus C \implies f'(x) = 0.$$

Since $\lambda(C) = 0$ (the Cantor set has Lebesgue measure zero), the set $[0,1] \setminus C$ has measure **1**. Hence $f' = 0$ almost everywhere. $\checkmark$

### Part (b): Why FTC fails

**Computing the integral:**

$$\int_0^1 f'(x)\, dx = \int_0^1 0 \, dx = 0,$$

yet $f(1) - f(0) = 1 - 0 = 1$.

So indeed $\int_0^1 f'(x)\,dx \neq f(1) - f(0)$.

**Why is this not a contradiction?**

The version of FTC that says

$$f(b) - f(a) = \int_a^b f'(x)\,dx$$

requires $f$ to be **absolutely continuous** on $[a,b]$. Recall:

> $f$ is **absolutely continuous** on $[a,b]$ if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for any finite collection of disjoint subintervals $(a_k, b_k)$ with $\sum (b_k - a_k) < \delta$, we have $\sum |f(b_k) - f(a_k)| < \varepsilon$.

The Cantor function **fails** absolute continuity. Here is the intuition: you can cover $C$ by intervals of arbitrarily small **total length** (since $\lambda(C)=0$), yet the total variation of $f$ over those intervals is **1** — all of $f$'s increase happens there, no matter how small the cover.

More precisely, after $n$ stages of constructing $C$, the remaining $2^n$ intervals each have length $3^{-n}$ and together carry total oscillation $1$. Taking $n \to \infty$: total length $\to 0$ but total variation $= 1 \not\to 0$, violating absolute continuity.

**The correct FTC for monotone functions** (Lebesgue's theorem):

> If $f$ is monotone on $[a,b]$, then $f'$ exists a.e., $f'$ is integrable, and
> $$\int_a^b f'(x)\,dx \leq f(b) - f(a),$$
> with **equality** if and only if $f$ is absolutely continuous.

The Cantor function saturates the **inequality** with a strict gap of $1 - 0 = 1$.

### Summary

| Property | Cantor function |
|---|---|
| Continuous? | ✅ Yes |
| Monotone? | ✅ Yes (non-decreasing) |
| $f'=0$ a.e.? | ✅ Yes |
| Absolutely continuous? | ❌ No |
| FTC holds? | ❌ No ($\int f' = 0 \neq 1$) |

The Devil's Staircase is the canonical example that **continuity + monotonicity + a.e. differentiability** is strictly weaker than **absolute continuity**, and that the FTC genuinely requires absolute continuity as a hypothesis.
