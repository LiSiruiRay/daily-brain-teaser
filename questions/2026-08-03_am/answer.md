# Answer: The Function That Equalizes Its Own Averages

## Key Idea / Intuition

Define $F(t) = \int_0^t f(x)\,dx$. We want to show $F$ has a zero in $(0,1)$. The hypothesis links $F(1)$ to a weighted integral of $F$ via integration by parts — and the two conditions together force $F$ to change sign (or vanish) somewhere strictly inside $(0,1)$.

---

## Formal Proof / Solution

**Step 1: Set up $F$ and integrate by parts.**

Let $F(t) = \int_0^t f(x)\,dx$. Then $F(0) = 0$, $F$ is continuous, and $F'(t) = f(t)$.

Integrate $\int_0^1 x\,f(x)\,dx$ by parts with $u = x$, $dv = f(x)\,dx$:

$$\int_0^1 x\,f(x)\,dx = \bigl[x\,F(x)\bigr]_0^1 - \int_0^1 F(x)\,dx = F(1) - \int_0^1 F(x)\,dx.$$

**Step 2: Use the hypothesis.**

The hypothesis says $\int_0^1 f(x)\,dx = \int_0^1 x\,f(x)\,dx$, i.e.,

$$F(1) = F(1) - \int_0^1 F(x)\,dx.$$

This immediately gives

$$\int_0^1 F(x)\,dx = 0.$$

**Step 3: Conclude $F$ has a zero in $(0,1)$.**

Since $\int_0^1 F(x)\,dx = 0$ and $F$ is continuous, either:

- $F \equiv 0$ on $[0,1]$, in which case every point of $(0,1)$ works, or  
- $F$ is not identically zero, so it takes both positive and negative values (otherwise $F \geq 0$ or $F \leq 0$ everywhere with $\int F = 0$ would force $F \equiv 0$).

In the latter case, by the Intermediate Value Theorem, $F$ must cross zero at some $c \in (0,1)$. $\blacksquare$

**Summary of the chain:**
$$\text{hypothesis} \xRightarrow{\text{IBP}} \int_0^1 F(x)\,dx = 0 \xRightarrow{\text{IVT}} F(c) = 0 \text{ for some } c \in (0,1).$$
