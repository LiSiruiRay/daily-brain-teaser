# Answer: Rouché's Theorem: Zeros of z⁵+3z+1

## Key Idea / Intuition

The trick is to split $f(z) = z^5 + 3z + 1$ into a "dominant" piece and a "small" perturbation on the boundary circle $|z| = 1$. On the unit circle, the term $3z$ has modulus $3$, while $z^5 + 1$ has modulus at most $2$. Since the dominant part wins on the boundary, Rouché's theorem tells us $f$ has the **same number of zeros inside $|z|<1$ as the dominant part $3z$** — which has exactly one zero (at the origin).

---

## Formal Proof / Solution

**Rouché's Theorem (statement):** If $f$ and $g$ are holomorphic inside and on a simple closed contour $C$, and $|g(z)| < |f(z)|$ for all $z \in C$, then $f$ and $f + g$ have the same number of zeros (counted with multiplicity) inside $C$.

---

**Setup.** Write
$$f(z) = \underbrace{3z}_{=: f_0(z)} + \underbrace{z^5 + 1}_{=: g(z)}.$$

We apply Rouché's theorem with $C = \{|z| = 1\}$, comparing the "big" piece $f_0(z) = 3z$ against the "small" piece $g(z) = z^5 + 1$.

---

**Checking the Rouché condition on $|z| = 1$:**

- $|f_0(z)| = |3z| = 3$,
- $|g(z)| = |z^5 + 1| \leq |z^5| + 1 = 1 + 1 = 2$.

Since $|g(z)| \leq 2 < 3 = |f_0(z)|$ for all $z$ on $|z| = 1$, the condition $|g(z)| < |f_0(z)|$ holds everywhere on the contour.

---

**Applying Rouché's Theorem:**

The function $f_0(z) = 3z$ has exactly **one zero** inside $|z| < 1$ (namely $z = 0$, with multiplicity 1).

By Rouché's theorem, $f(z) = f_0(z) + g(z) = z^5 + 3z + 1$ also has exactly **one zero** inside $|z| < 1$.

---

**Conclusion.**

$$\boxed{f(z) = z^5 + 3z + 1 \text{ has exactly } 1 \text{ zero inside the unit disk.}}$$

The remaining four zeros (by the fundamental theorem of algebra) all lie outside the unit disk $|z| \geq 1$.

---

**Why this is beautiful:** Rouché's theorem lets you "transfer" zero-counting from a complicated function to a trivially simple one, purely by a modulus estimate on the boundary. No explicit root-finding required.
