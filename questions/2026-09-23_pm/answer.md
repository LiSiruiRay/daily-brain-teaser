# Answer: The Ballot Box Twist: Runs of the Same Color

## Key Idea / Intuition

This is a beautiful disguised version of the **Ballot Problem**. The Ballot Problem says: if candidate A gets $a$ votes and candidate B gets $b$ votes with $a > b$, then the probability that A leads B **strictly throughout the entire counting** is $(a - b)/(a + b)$. Here the "votes" are the drawn balls, with red playing the role of the winning candidate. The answer drops out immediately once you see this connection.

The magic of the ballot problem is that it reduces a complex path-counting question to a single elegant formula, proved by a beautiful **reflection/cycle argument**.

---

## Formal Proof / Solution

**Setting up the correspondence.**

Label the $r$ red balls as $+1$ and the $b$ blue balls as $-1$. We draw all $n = r + b$ balls. Let $S_k$ be the running sum after $k$ draws. We want:

$$P(S_k > 0 \text{ for all } k = 1, 2, \ldots, r+b)$$

Since $S_{r+b} = r - b > 0$, we are in exactly the setting of the **Ballot Problem**.

**The Ballot Problem (Bertrand, 1887).**

> In an election, candidate A receives $a$ votes and candidate B receives $b < a$ votes. If ballots are counted in a uniformly random order, the probability that A is **strictly ahead** of B throughout the entire count is:
> $$\frac{a - b}{a + b}.$$

**Applying to our problem.**

With $a = r$ red balls and $b$ blue balls:

$$\boxed{P = \frac{r - b}{r + b}}$$

**Sketch of proof via the Cycle Lemma.**

Consider all $(r+b)!$ orderings of the balls, or equivalently all $\binom{r+b}{r}$ sequences of $+1$s and $-1$s with $r$ of $+1$ and $b$ of $-1$.

For any such sequence $(x_1, \ldots, x_n)$ with $n = r+b$, consider its $n$ **cyclic rotations**:
$$(x_1,\ldots,x_n),\; (x_2,\ldots,x_n,x_1),\; \ldots,\; (x_n, x_1, \ldots, x_{n-1}).$$

**Key fact (Cycle Lemma):** Among these $n$ cyclic rotations, exactly $r - b$ of them have all partial sums strictly positive.

*Why?* The partial sums of a rotation starting at position $i$ are all positive iff we start at a "record high" position of the cumulative sum. A careful counting argument shows there are exactly $r - b$ such starting positions (since the total sum is $r - b > 0$ and the sequence is generic).

Since each of the $n$ rotations is equally likely as a random arrangement, the probability that the original (random) sequence has all partial sums $> 0$ is:

$$\frac{r - b}{r + b}.$$

**Example.** With $r = 3$ red and $b = 1$ blue ball:
$$P = \frac{3-1}{3+1} = \frac{2}{4} = \frac{1}{2}.$$

You can verify by listing all $\binom{4}{1} = 4$ equally likely positions for the blue ball:
- Blue in position 1: ❌ (immediately tied or behind)
- Blue in position 2: RBRR — after draw 2: $1$ red, $1$ blue ❌
- Blue in position 3: RRBR — after draw 3: $2$ red, $1$ blue ✓
- Blue in position 4: RRRB — all prefixes ✓

Favorable outcomes: 2 out of 4 ✓ — matches $\frac{1}{2}$.
