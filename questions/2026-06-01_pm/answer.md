# Answer: Two Integral Conditions Force Two Zeros

## Key Idea / Intuition

The two integral conditions force $f$ to "oscillate" enough that it cannot have just one sign-change. Think of it this way: if $f$ had only one zero, you could factor out a sign pattern $f = c \cdot (\text{one-sign piece})$, but then a clever linear combination of the two integrals would give a contradiction. The key move is to use the vanishing of both integrals to build a polynomial that "witnesses" a second zero must exist — essentially an intermediate-value + mean-value argument.

---

## Formal Proof / Solution

**Claim:** Yes, $f$ must have at least two zeros in $(0,1)$.

---

**Step 1: $f$ must change sign (at least one zero in $(0,1)$).**

Since $\int_0^1 f(x)\,dx = 0$ and $f$ is continuous, if $f$ were never zero on $(0,1)$, then $f$ has constant sign and the integral cannot vanish. So $f$ has at least one zero.

---

**Step 2: Suppose for contradiction that $f$ has exactly one zero in $(0,1)$, say at $c \in (0,1)$.**

Then $f$ changes sign exactly once: say $f > 0$ on $(0,c)$ and $f < 0$ on $(c,1)$ (or vice versa).

---

**Step 3: Derive a contradiction using a linear combination.**

Consider the linear combination

$$\int_0^1 (x - \alpha)\, f(x)\, dx = \int_0^1 x\,f(x)\,dx - \alpha \int_0^1 f(x)\,dx = 0 - \alpha \cdot 0 = 0$$

for **any** $\alpha \in \mathbb{R}$. Now choose $\alpha = c$, the unique zero. Then:

$$\int_0^1 (x - c)\, f(x)\, dx = 0.$$

But now observe the sign of $(x - c)f(x)$:
- On $(0, c)$: $x - c < 0$ and $f(x) > 0$, so $(x-c)f(x) < 0$.
- On $(c, 1)$: $x - c > 0$ and $f(x) < 0$, so $(x-c)f(x) < 0$.

Therefore $(x-c)f(x) \leq 0$ on all of $(0,1)$, with strict inequality on sets of positive measure. This gives

$$\int_0^1 (x-c)\,f(x)\,dx < 0,$$

which **contradicts** the fact that the integral equals zero.

---

**Step 4: Conclusion.**

The assumption that $f$ has exactly one zero in $(0,1)$ leads to a contradiction. Combined with Step 1, $f$ must have **at least two zeros** in $(0,1)$. $\blacksquare$

---

**Remark (the elegant structure):** The two conditions $\int f = 0$ and $\int xf = 0$ together say that $f$ is orthogonal (in $L^2[0,1]$) to the two-dimensional space spanned by $\{1, x\}$. In particular, $f$ is orthogonal to **every** linear polynomial $\alpha + \beta x$. Choosing the linear polynomial $x - c$ that vanishes at the only candidate zero is precisely what kills the sign argument. This is a shadow of the general principle: orthogonality to $n$ functions forces at least $n$ sign changes.
