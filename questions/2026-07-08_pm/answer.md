# Answer: The Ballot Box Surprise: Two Candidates, One Mystery

## Key Idea / Intuition

This is the **Ballot Problem** in disguise, but now applied to sampling without replacement from a finite urn rather than counting votes. The answer turns out to be strikingly clean: the probability depends only on the final margin $r - b$, not on the total number of balls. The key trick is the **reflection principle** (or cycle lemma), which counts "bad" sequences — those where blue ties or overtakes red at some point — by bijecting them with a shifted set of sequences.

---

## Formal Proof / Solution

### Setup

We have $n = r + b$ balls in total: $r$ red, $b$ blue, $r > b$. A random drawing without replacement corresponds to choosing a uniformly random permutation of these $r + b$ balls. We want:

$$P(\text{red strictly leads at every step}) = P(R_k > B_k \text{ for all } k = 1, \ldots, r+b).$$

### Reformulation as Lattice Paths

Encode each sequence as a lattice path from $(0,0)$ to $(r, b)$: a red ball is a step **right** $(+1, 0)$ and a blue ball is a step **up** $(0, +1)$. The condition $R_k > B_k$ for all $k$ means the path stays **strictly below the diagonal** $y = x$ (i.e., above the line $y = x - 1$ but below $y = x$, equivalently $R_k - B_k \geq 1$ always).

The total number of paths is $\binom{r+b}{b}$.

### The Ballot Problem Result

The **classical Ballot Theorem** (Bertrand, 1887) states:

> If candidate A receives $r$ votes and candidate B receives $b$ votes with $r > b$, the probability that A is strictly ahead of B throughout the counting is $\dfrac{r - b}{r + b}$.

### Proof via the Cycle Lemma

Consider all $(r+b)!/(r! \, b!)$ sequences. We want to count those where red is strictly ahead at every prefix.

**Cycle Lemma argument:** Take any sequence of $r$ R's and $b$ B's. Consider all $r + b$ **cyclic rotations** of this sequence. Exactly $r - b$ of these rotations have the property that every prefix has more R's than B's.

*Why $r - b$?* Define the **score** of a rotation as the minimum prefix sum (where R $= +1$, B $= -1$). The full sum is $r - b > 0$. Among the $r + b$ cyclic shifts, the number of "good" ones (every prefix positive) equals exactly the final sum $r - b$ — this is the Cycle Lemma (Dvoretzky & Motzkin, 1947).

Since exactly $r - b$ out of every $r + b$ rotations are "good," and the rotations of distinct sequences are evenly distributed, we conclude:

$$P(\text{red strictly leads throughout}) = \frac{r - b}{r + b}.$$

### Verification with Small Cases

- $r = 2, b = 1$: sequences are RRB, RBR, BRR. Only RRB and RBR keep red ahead at every step... actually check: RBR gives R,RB,RBR → leads 1,0,1 — fails at step 2. Only RRB works? Let's recount: $\frac{r-b}{r+b} = \frac{1}{3}$, so 1 out of 3. ✓ (Only RRB: after step 1: R>B ✓, step 2: 2R,0B ✓, step 3: 2R,1B ✓. RBR fails at step 2. BRR fails at step 1.)

- $r = 3, b = 1$: probability $= \frac{2}{4} = \frac{1}{2}$. Out of $\binom{4}{1} = 4$ sequences: RRRB ✓, RRBR ✓, RBRR ✗ (step 3: tied), BRRR ✗. So 2 out of 4. ✓

### Final Answer

$$\boxed{P = \dfrac{r - b}{r + b}}$$

The beautiful surprise: this probability depends **only on the margin** $r - b$ relative to the total $r + b$. Doubling both the red and blue count while keeping the same margin halves the probability — the lead becomes harder to maintain with more balls in play.
