# Answer: The Duelist's Dilemma: Who Wins When A Shoots First?

## Key Idea / Intuition

Going first sounds like an advantage — but it only helps if you actually hit. Each round, A shoots first; if A misses (probability $1-p$), then B gets a shot. The game is memoryless, so the probability of A winning satisfies a clean geometric series. The surprise: A wins more than half the time **if and only if** $p > q(1-p)$, i.e., $p > q/(1+q)$. Going first is not always enough to overcome a skill disadvantage.

---

## Formal Proof / Solution

**Setup.** Each round proceeds:
1. A shoots and hits B with probability $p$. → A wins.
2. If A misses (probability $1-p$), B shoots and hits A with probability $q$. → B wins.
3. If both miss (probability $(1-p)(1-q)$), the round resets.

**Computing $P(A \text{ wins})$.**

Let $W$ = event A wins. Within one round:
- A wins with probability $p$.
- B wins with probability $(1-p)q$.
- Round resets with probability $(1-p)(1-q)$.

Since the game resets to the same state, we get the equation:

$$P(A \text{ wins}) = p + (1-p)(1-q) \cdot P(A \text{ wins})$$

Let $\alpha = P(A \text{ wins})$. Then:

$$\alpha = p + (1-p)(1-q)\,\alpha$$

$$\alpha \left[1 - (1-p)(1-q)\right] = p$$

$$\boxed{\alpha = \frac{p}{1 - (1-p)(1-q)} = \frac{p}{p + q - pq}}$$

**Sanity check:** If $p = q = 1/2$:
$$\alpha = \frac{1/2}{1/2 + 1/2 - 1/4} = \frac{1/2}{3/4} = \frac{2}{3}$$

So A wins with probability $2/3$ when both are equally skilled — going first is a big advantage when you have a 50% hit rate!

---

**When does A win with probability less than $1/2$?**

We need $\alpha < 1/2$:
$$\frac{p}{p + q - pq} < \frac{1}{2}$$
$$2p < p + q - pq$$
$$p < q - pq = q(1-p)$$
$$\frac{p}{1-p} < q$$

So **A is the underdog** (despite going first) exactly when:

$$q > \frac{p}{1-p}$$

For example, if $p = 1/3$, then A is an underdog whenever $q > (1/3)/(2/3) = 1/2$.

**Interpretation.** Going first gives A a guaranteed first shot, but if A's hit probability is low, the advantage is small. A skilled B can overcome the order disadvantage as long as B's skill $q$ exceeds the threshold $p/(1-p)$.

---

**Summary Table for $p = q = 1/2$:**

| Event | Probability |
|-------|-------------|
| A wins in round 1 | $1/2$ |
| B wins in round 1 | $1/4$ |
| Game continues | $1/4$ |
| **A wins overall** | $\mathbf{2/3}$ |

The clean formula $\alpha = \dfrac{p}{p + q - pq}$ is the heart of the problem.

Written to [question file](questions/2026-09-20_pm.md) and answer included below.
