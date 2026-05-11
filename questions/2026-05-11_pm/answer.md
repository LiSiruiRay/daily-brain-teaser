# Answer: Nowhere-Zero Derivative Paradox

## Key Idea / Intuition

Your first instinct might be: "If $f'$ is never zero, it can't switch sign, because by the Intermediate Value Theorem it would have to pass through zero." And this is **exactly right** — but the key insight is subtle: the derivative $f'$ need not be continuous, yet it still satisfies the **Intermediate Value Property** (Darboux's theorem). So even though $f'$ might be discontinuous, it cannot skip over zero. Therefore yes: $f'$ must have constant sign.

---

## Formal Proof / Solution

**Claim:** If $f: \mathbb{R} \to \mathbb{R}$ is differentiable everywhere and $f'(x) \neq 0$ for all $x$, then $f'$ has constant sign.

**Step 1: State Darboux's Theorem.**

> *Darboux's Theorem:* If $f$ is differentiable on $[a, b]$, then $f'$ satisfies the **Intermediate Value Property**: for any $a < b$ and any value $k$ strictly between $f'(a)$ and $f'(b)$, there exists $c \in (a, b)$ with $f'(c) = k$.

This is remarkable because $f'$ need not be continuous — yet it cannot "jump" over any value. (The proof uses that $g(x) = f(x) - kx$ achieves its extremum at an interior point where $g' = 0$.)

**Step 2: Apply Darboux to conclude constant sign.**

Suppose for contradiction that $f'$ takes both positive and negative values. Then there exist $a, b \in \mathbb{R}$ with $f'(a) > 0$ and $f'(b) < 0$.

By Darboux's theorem applied on the interval $[\min(a,b),\, \max(a,b)]$, since $0$ lies strictly between $f'(a)$ and $f'(b)$, there exists $c$ between $a$ and $b$ such that:
$$f'(c) = 0.$$

This contradicts the assumption that $f'(x) \neq 0$ for all $x$.

**Conclusion:** $f'$ cannot change sign. Since $f'$ is never zero, we must have either $f'(x) > 0$ for all $x \in \mathbb{R}$, or $f'(x) < 0$ for all $x \in \mathbb{R}$. $\blacksquare$

---

**Why this is surprising:**

One might think: "Maybe $f'$ oscillates wildly enough to avoid zero while still changing sign — like $\sin(1/x)$." But Darboux blocks this entirely. The IVP for derivatives is a hidden rigidity that survives even in the absence of continuity.

A classic example of a discontinuous derivative: $f(x) = x^2 \sin(1/x)$ (with $f(0) = 0$) has $f'(0) = 0$ but $f'$ oscillates near $0$. This shows derivatives can be wild — but Darboux guarantees they can never skip a value.
