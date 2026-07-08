# Answer: The Lazy Prisoner: A Probability Paradox

## Key Idea / Intuition

The warden's statement is **not symmetric information** about A and C. The warden was *forced* to name B if A is the one pardoned (since both B and C would be executed), but also *sometimes* names B when C is pardoned. Carefully tracking the warden's coin-flip behavior via Bayes' theorem reveals that A's probability stays at $\frac{1}{3}$, while C's probability jumps to $\frac{2}{3}$. The key insight: the information "B will not be pardoned" was almost *guaranteed* if C is the one pardoned (warden had no choice), but only had probability $\frac{1}{2}$ of being said if A is pardoned. So hearing "B" is stronger evidence for C than for A.

---

## Formal Proof / Solution

**Setup.** Let $P$ = event A is pardoned, $Q$ = event C is pardoned, $R$ = event B is pardoned. Each has prior probability $\frac{1}{3}$.

Let $W_B$ = event that warden names B (says "B will not be pardoned").

**Compute $P(W_B \mid \text{each case})$:**

- If **A is pardoned**: both B and C will be executed, so warden flips a fair coin.  
  $$P(W_B \mid P) = \frac{1}{2}$$

- If **B is pardoned**: warden cannot name B (B is being pardoned), so must name C.  
  $$P(W_B \mid R) = 0$$

- If **C is pardoned**: warden must name B (only non-pardoned candidate available, since A can't be named).  
  $$P(W_B \mid Q) = 1$$

**Apply Bayes' theorem:**

$$P(W_B) = P(W_B \mid P)\cdot\frac{1}{3} + P(W_B \mid R)\cdot\frac{1}{3} + P(W_B \mid Q)\cdot\frac{1}{3}$$

$$= \frac{1}{2}\cdot\frac{1}{3} + 0\cdot\frac{1}{3} + 1\cdot\frac{1}{3} = \frac{1}{6} + \frac{1}{3} = \frac{1}{2}$$

**Posterior for A:**

$$P(P \mid W_B) = \frac{P(W_B \mid P)\cdot P(P)}{P(W_B)} = \frac{\frac{1}{2}\cdot\frac{1}{3}}{\frac{1}{2}} = \boxed{\frac{1}{3}}$$

**Posterior for C:**

$$P(Q \mid W_B) = \frac{P(W_B \mid Q)\cdot P(Q)}{P(W_B)} = \frac{1\cdot\frac{1}{3}}{\frac{1}{2}} = \boxed{\frac{2}{3}}$$

**Conclusion:**

| Prisoner | Prior | Posterior (after warden names B) |
|----------|-------|----------------------------------|
| A        | $1/3$ | $1/3$ (unchanged!) |
| B        | $1/3$ | $0$ |
| C        | $1/3$ | $2/3$ |

**Why does A not gain?** A already *knew* that either B or C would be executed — hearing which one adds no information about A's own fate. But it *transfers* all of B's probability mass to C, since C's execution was guaranteed to produce the answer "B." This is a classic instance of the **Monty Hall phenomenon**: the agent who *had no choice* is the one whose posterior surges.

The intuition that "now it's 50-50 between A and C" is the famous fallacy: it ignores the asymmetry in how the warden was constrained.
