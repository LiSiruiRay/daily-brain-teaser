# Answer: The Nowhere-Monotone Continuous Function

## Key Idea / Intuition

The answer is **yes** — such functions exist, and in fact the "generic" continuous function (in the Baire category sense) is nowhere monotone. The key insight is that continuity does *not* force any local monotone behavior: you can construct a function that oscillates infinitely on every interval, never settling into any increasing or decreasing trend. The Weierstrass nowhere-differentiable function is the canonical example, and we explain why nowhere differentiability (with unbounded variation) forces nowhere monotonicity.

---

## Formal Proof / Solution

### Step 1: The Weierstrass Function Is Continuous

Define the classical Weierstrass function:
$$f(x) = \sum_{n=0}^{\infty} a^n \cos(b^n \pi x),$$
where $0 < a < 1$, $b$ is a positive odd integer, and $ab > 1 + \frac{3\pi}{2}$.

This converges uniformly (by Weierstrass $M$-test, since $\sum a^n < \infty$), so $f$ is **continuous**.

### Step 2: Nowhere Differentiability Implies Nowhere Monotone

**Claim:** If $f$ is monotone on some interval $(c, d)$, then $f$ is differentiable almost everywhere on $(c, d)$.

**Proof of claim:** This is Lebesgue's monotone differentiation theorem — any monotone function on an interval is differentiable almost everywhere.

Therefore: if $f$ were monotone on *any* open interval $(c, d)$, it would have to be differentiable at almost every point of $(c, d)$.

But the Weierstrass function is **differentiable nowhere**. This is a contradiction.

Hence $f$ is **nowhere monotone**.

### Step 3: Why Is Nowhere Monotone Surprising?

One might think: "Surely on some tiny interval, the function must go up or down overall." But continuity alone does not prevent infinite oscillation. The Weierstrass function oscillates on every scale — zooming into any interval reveals the same chaotic structure. There is no interval where the function "trends" in any direction.

### Step 4: Baire Category Perspective (Bonus)

Define the set:
$$M_n = \left\{ f \in C([0,1]) : \exists\, x \in [0, 1-1/n] \text{ such that } f \text{ is increasing on } [x, x+1/n] \right\}.$$

Each $M_n$ is **closed and nowhere dense** in $C([0,1])$ with the sup-norm. By the **Baire Category Theorem**, $C([0,1]) \setminus \bigcup_n M_n$ is a dense $G_\delta$ — meaning **most** continuous functions (in the topological sense) are nowhere monotone.

### Summary

$$\boxed{\text{Yes. The Weierstrass function is continuous and nowhere monotone.}}$$

The logical chain is:
$$\text{nowhere differentiable} \xRightarrow{\text{Lebesgue}} \text{differentiable a.e. on no interval} \Rightarrow \text{monotone on no interval.}$$
