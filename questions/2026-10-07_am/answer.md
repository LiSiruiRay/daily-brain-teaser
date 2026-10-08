# Answer: The Flippant Juror: Three Jurors and a Coin

## Key Idea / Intuition

Your first instinct might be: adding a random coin-flipper to the jury should hurt performance — she's completely uninformative! But remarkably, the majority-of-three rule (with two competent jurors and one random one) gives **exactly the same probability of a correct verdict** as a single competent juror alone. The coin-flipper is perfectly harmless under majority rule. The reason: the flippant juror only changes the outcome when the two competent jurors already disagree — and in that case, a fair coin is exactly as good as a third competent voter would be, in the sense that the overall probability works out to the same number.

---

## Formal Proof / Solution

**Setup.** Let $p$ be the probability each competent juror is correct. Let jurors be $J_1$ (competent), $J_2$ (competent), $J_3$ (coin flipper, correct with probability $\frac{1}{2}$). All decisions are independent.

**Single competent juror.** The probability of a correct verdict is simply $p$.

**Jury majority rule.** The jury is correct if at least 2 of the 3 are correct. Let's compute $P(\text{correct})$.

Condition on the two competent jurors:

| $J_1$ correct | $J_2$ correct | Probability | Jury correct iff... |
|---|---|---|---|
| Yes | Yes | $p^2$ | Always (2 already correct) |
| Yes | No | $p(1-p)$ | $J_3$ correct (prob $\frac{1}{2}$) |
| No | Yes | $(1-p)p$ | $J_3$ correct (prob $\frac{1}{2}$) |
| No | No | $(1-p)^2$ | Never (at most 1 correct) |

So:

$$P(\text{jury correct}) = p^2 \cdot 1 + p(1-p) \cdot \frac{1}{2} + (1-p)p \cdot \frac{1}{2} + (1-p)^2 \cdot 0$$

$$= p^2 + 2p(1-p) \cdot \frac{1}{2}$$

$$= p^2 + p(1-p)$$

$$= p^2 + p - p^2$$

$$= p.$$

**Conclusion.** The jury of three (two competent, one coin-flipper) under majority rule has **exactly** the same probability $p$ of reaching the correct verdict as a single competent juror. The useless juror contributes nothing — but she also **takes nothing away**.

**Why this is beautiful.** The key insight is that the flippant juror only gets a "casting vote" when the two competent jurors disagree, which happens with probability $2p(1-p)$. In that tie-breaking role, her fair coin contributes $\frac{1}{2}$, giving the term $2p(1-p) \cdot \frac{1}{2} = p(1-p)$. And $p^2 + p(1-p) = p$ — it telescopes perfectly. The useless juror is perfectly neutral, not harmful.

This also shows: replacing a competent juror with a coin-flipper doesn't hurt majority rule! The "loss" from downgrading one juror is exactly compensated by the majority structure.
