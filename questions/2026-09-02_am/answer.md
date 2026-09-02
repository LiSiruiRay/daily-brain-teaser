# Answer: Twin Knights: Meeting in the Tournament

## Key Idea / Intuition

The elegant trick is to **avoid tracking the bracket structure round by round**, and instead think about it from a symmetry/counting perspective. Among all $\binom{8}{2} = 28$ possible pairs of knights, the tournament will produce exactly **7 matches** in total (since each match eliminates one knight, and we need to eliminate 7). By symmetry, every pair of knights is equally likely to be the pair that meets in any given match slot. So the probability that Balin and Balan are **one of those 7 matched pairs** is simply $\frac{7}{28} = \frac{1}{4}$.

This "all pairs equally likely" symmetry argument is the beautiful shortcut — no need to case-split on quarterfinals, semifinals, and finals.

---

## Formal Proof / Solution

**Setup.** The bracket assigns 8 knights into 4 first-round pairs, then 2 semifinal pairs, then 1 final pair. The initial seeding is uniformly random.

**Total matches.** A single-elimination tournament with 8 players has exactly
$$8 - 1 = 7 \text{ matches total.}$$

**Symmetry argument.** Consider the following perspective: at the start, randomly order all 8 knights. The tournament bracket pairs them as:
- Round 1: positions $(1,2), (3,4), (5,6), (7,8)$
- Round 2 (semis): winners of those pairs meet
- Round 3 (final): last two meet

But here is the key insight. Since **all knights are evenly matched** (each match is 50-50), the 7 matches that actually occur correspond to 7 pairs of knights. By a symmetry argument, **every pair $\{i,j\}$ of the original 8 knights is equally likely to appear as one of these 7 matched pairs**.

*Why?* Think of it this way: label the 8 initial slots uniformly at random. The structure of who plays whom in later rounds is determined by earlier random coin flips, which (combined with the uniform initial seeding) treats all pairs symmetrically. No pair has any structural advantage over any other.

**Counting.** There are $\binom{8}{2} = 28$ possible pairs. Exactly 7 of them will actually meet in the tournament. By symmetry, the probability that $\{\text{Balin, Balan}\}$ is among those 7 pairs is:

$$P(\text{twins meet}) = \frac{7}{28} = \boxed{\frac{1}{4}}.$$

**Sanity check via direct calculation.** One can also compute round by round:
- **Quarter-final:** Balin is in some slot. Balan is equally likely to be in any of the 7 remaining slots, of which exactly **1** is Balin's quarter-final opponent.
$$P(\text{meet in QF}) = \frac{1}{7}.$$
- **Semi-final:** They must both win their QF (probability $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$), and their bracket must place them in the same semi (probability $\frac{2}{6}$ of the remaining 6 knights = Balan is among the 2 who face Balin's semi slot). Working this out carefully:
$$P(\text{meet in SF}) = \frac{2}{7} \cdot \frac{1}{4} = \frac{2}{28}.$$
- **Final:** Similarly, $P(\text{meet in Final}) = \frac{4}{7} \cdot \frac{1}{16} = \frac{4}{112}= \frac{1}{28}$.

Summing:
$$\frac{1}{7} + \frac{2}{28} + \frac{1}{28} = \frac{4}{28} + \frac{2}{28} + \frac{1}{28} = \frac{7}{28} = \frac{1}{4}. \checkmark$$

The symmetry argument gives the answer instantly; the round-by-round calculation confirms it.
