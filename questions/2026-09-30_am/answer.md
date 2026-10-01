# Answer: The Flippant Juror's Cousin: Four Jurors and a Coin

## Key Idea / Intuition

The coin-flipper is adding pure noise to a 4-person panel. Surprisingly, the 4-person jury with a coin-flipper does **worse** than the clean 3-person jury — but only by a small and elegant amount. The key insight is to condition on what the three serious jurors do: when they all agree (unanimously), the coin-flipper is irrelevant; when they split 2-1, the coin-flipper becomes a kingmaker whose random vote hurts you exactly half the time. Tracking these cases carefully reveals a clean formula.

---

## Formal Proof / Solution

**Setup.** Label the three serious jurors $A, B, C$, each correct with probability $p$ independently. The coin-flipper $D$ votes correctly with probability $\frac{1}{2}$.

**Three-person panel (benchmark):** Majority of 3, so correct iff at least 2 of $\{A, B, C\}$ vote correctly:
$$P_3 = \binom{3}{2}p^2(1-p) + \binom{3}{3}p^3 = 3p^2(1-p) + p^3 = 3p^2 - 2p^3.$$

**Four-person jury with coin-flipper:** Correct iff at least 3 of $\{A,B,C,D\}$ vote correctly. Condition on the votes of the three serious jurors:

**Case 1: All three serious jurors agree correctly** (probability $p^3$).
The result is correct regardless of $D$. This case contributes $p^3$.

**Case 2: All three serious jurors agree incorrectly** (probability $(1-p)^3$).
The result is incorrect regardless of $D$. Contributes $0$.

**Case 3: Exactly 2 serious jurors vote correctly, 1 incorrectly** (probability $3p^2(1-p)$).
Score among $A,B,C$ is 2–1 correct. The four-person jury is correct iff $D$ also votes correctly, which happens with probability $\frac{1}{2}$.
Contributes $3p^2(1-p) \cdot \frac{1}{2}$.

**Case 4: Exactly 1 serious juror votes correctly, 2 incorrectly** (probability $3p(1-p)^2$).
Score among $A,B,C$ is 1–2 correct. The four-person jury is correct iff $D$ votes correctly, giving a score of 2–2 — but wait, we need **at least 3** of 4 to be correct. With 1 correct serious juror and $D$ correct, we get only 2 correct, which is a tie — **not** a majority of 4. So this case **never** contributes a correct verdict.
Contributes $0$.

**Total probability for the 4-person jury:**
$$P_4 = p^3 + \frac{3}{2}p^2(1-p) = p^3 + \frac{3}{2}p^2 - \frac{3}{2}p^3 = \frac{3}{2}p^2 - \frac{1}{2}p^3 = \frac{p^2}{2}(3 - p).$$

**Comparison:**
$$P_3 - P_4 = \left(3p^2 - 2p^3\right) - \left(\frac{3}{2}p^2 - \frac{1}{2}p^3\right) = \frac{3}{2}p^2 - \frac{3}{2}p^3 = \frac{3}{2}p^2(1-p).$$

For any $p \in (0,1)$, we have $P_3 - P_4 > 0$.

**Conclusion:** The clean three-person panel is strictly better than the four-person jury with a coin-flipper (for $0 < p < 1$). The margin $\frac{3}{2}p^2(1-p)$ is largest around $p = \frac{2}{3}$, where the damage from the coin-flipper is greatest.

**Why?** In the clean 3-person jury, a 2-1 split always goes the right way (the majority is correct). In the 4-person jury, a 2-1 split among the serious jurors gets decided by a coin — and the coin only helps half the time.
