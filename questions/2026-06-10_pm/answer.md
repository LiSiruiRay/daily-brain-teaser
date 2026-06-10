# Answer: Second-Best Runner-Up

## Key Idea / Intuition

The second-best player wins the runner-up cup if and only if they **never meet the best player until the final**. This happens precisely when they are placed in the **opposite half** of the bracket from the best player. Since the bracket has two halves of equal size, and the best player occupies one slot in one half, the question reduces to: what fraction of the remaining slots are in the **other half**?

---

## Formal Proof / Solution

**Setup.** Fix the best player's position (by symmetry, it doesn't matter where they are). There are $8 - 1 = 7$ remaining slots for the second-best player to occupy.

**When does the second-best win the runner-up cup?**

The second-best player can only lose (and thus get the runner-up cup) by facing the best player — but to receive the runner-up cup, this loss must happen **in the final**.

Since the best player **always wins**, the best player will reach the final regardless. The second-best player reaches the final if and only if they **never meet the best player before the final**, which happens if and only if they are in the **opposite half of the bracket**.

**Counting.** With 8 players, each half of the bracket has 4 slots. The best player occupies 1 slot in their half. The remaining 7 slots are distributed as:
- 3 slots in the **same half** as the best player
- 4 slots in the **opposite half**

So the probability is:

$$P(\text{runner-up cup}) = \frac{4}{7}$$

**General case with $2^n$ players.**

Each half has $2^{n-1}$ slots. One slot is taken by the best player in their half. Remaining slots:
- $2^{n-1} - 1$ in the same half
- $2^{n-1}$ in the opposite half
- Total remaining: $2^n - 1$

$$\boxed{P = \frac{2^{n-1}}{2^n - 1}}$$

For $n = 3$ (8 players): $P = \frac{4}{7} \approx 0.571$.

**Sanity check as $n \to \infty$:**
$$\frac{2^{n-1}}{2^n - 1} \to \frac{1}{2}$$
which makes sense: in a huge tournament, the two halves are nearly equally likely, so the second-best ends up in the opposite half roughly half the time.

**What's beautiful here:** The problem looks like it requires tracking all possible bracket matchups, but the key insight collapses everything to a single observation — the second-best player's fate is entirely determined by which half of the bracket they land in. All the internal randomness within each half is irrelevant, because both the best and second-best players are guaranteed to win every match except against each other.
