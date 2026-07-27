# Answer: The Integrable Function Whose Integral Vanishes on Every Interval

## Key Idea / Intuition

The key insight is that integrals over all intervals (or all measurable sets) is an extremely rigid condition — it forces $f = 0$ a.e. In each case, the tool is the **Lebesgue Differentiation Theorem**: the integral function $F(x) = \int_0^x f(t)\,dt$ is differentiable a.e. with $F'(x) = f(x)$. If $F \equiv 0$, then $F' = 0$ a.e., so $f = 0$ a.e. The measurable-set version is the strongest and follows from choosing $E = \{f > 0\}$ and $E = \{f < 0\}$ separately.

---

## Formal Proof / Solution

### Case 1: $\int_a^b f(x)\,dx = 0$ for all $a < b$

Define $F(x) = \int_0^x f(t)\,dt$. The hypothesis (with $a = 0, b = x$) gives $F(x) = 0$ for all $x \geq 0$, and similarly for $x < 0$. So $F \equiv 0$.

By the **Lebesgue Differentiation Theorem**, for locally integrable $f$,

$$f(x) = F'(x) \quad \text{for a.e. } x.$$

Since $F \equiv 0$, we get $f = 0$ a.e. $\checkmark$

---

### Case 2: $\int_0^x f(t)\,dt = 0$ for all $x \geq 0$

This is identical to Case 1 on $[0, \infty)$: set $F(x) = \int_0^x f(t)\,dt \equiv 0$, apply the Lebesgue Differentiation Theorem to get $f = 0$ a.e. on $[0,\infty)$. $\checkmark$

**Remark:** One might worry that "only knowing $F$ vanishes at every $x$, not at every $a < b$" is weaker — but it is not, since $\int_a^b f = F(b) - F(a) = 0 - 0 = 0$ anyway.

---

### Case 3: $\int_E f\,d\mu = 0$ for every measurable $E \subseteq [0,1]$

This is the strongest condition. Let:

$$E^+ = \{x \in [0,1] : f(x) > 0\}, \quad E^- = \{x \in [0,1] : f(x) < 0\}.$$

Both sets are measurable (since $f$ is measurable). Apply the hypothesis to $E = E^+$:

$$0 = \int_{E^+} f\,d\mu.$$

But on $E^+$, we have $f > 0$, so the integrand is strictly positive on a set of positive measure — unless $\mu(E^+) = 0$. Therefore $\mu(E^+) = 0$.

Similarly, applying the hypothesis to $E = E^-$:

$$0 = \int_{E^-} f\,d\mu,$$

and since $f < 0$ on $E^-$, we get $\mu(E^-) = 0$.

Therefore $f = 0$ a.e. on $[0,1]$. $\checkmark$

---

### Summary Table

| Condition | Conclusion |
|---|---|
| $\int_a^b f = 0$ for all $a < b$ | $f = 0$ a.e. (Lebesgue Diff. Thm) |
| $\int_0^x f = 0$ for all $x$ | $f = 0$ a.e. (same) |
| $\int_E f = 0$ for all meas. $E$ | $f = 0$ a.e. (direct sign argument) |

The three cases are progressively "different looking" but all force the same conclusion. The cleanest proof is Case 3's direct argument: just plug in the set where $f$ has a sign.
