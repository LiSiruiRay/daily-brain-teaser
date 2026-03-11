# Answer: Bertrand's Ballot Problem

**Answer:** $\dfrac{a - b}{a + b}$

---

## Step 1: Think of votes as a path

Imagine drawing a graph as you count votes one by one:
- Vote for A → move **up** (+1)
- Vote for B → move **down** (−1)

You start at height 0 and end at height $a - b$ (since A wins by $a - b$ votes).

**We want:** the path **never touches or goes below 0** after the very first step.

---

## Step 2: Count the bad paths using the Cycle Lemma

Here is the key trick — the **Cycle Lemma**.

Take any fixed ordering of the $a + b$ ballots (a specific sequence of A's and B's). Now consider all **$a + b$ cyclic rotations** of this sequence — i.e., start the count from ballot 2, 3, 4, ... instead of ballot 1.

**Claim:** Among all $a + b$ rotations of any given sequence, **exactly $a - b$ of them** have A strictly ahead at every point.

This is a non-obvious but provable combinatorial fact. It follows because the path visits each "height level" in a regular pattern, and a simple counting argument shows exactly $a - b$ starting positions yield a "good" path.

---

## Step 3: Compute the probability

Since every sequence has $a + b$ rotations, and exactly $a - b$ of those rotations are "good":

$$P(\text{A always strictly ahead}) = \frac{a - b}{a + b}$$

---

## Example: $a = 3$, $b = 1$

$$P = \frac{3 - 1}{3 + 1} = \frac{1}{2}$$

List all 4 orderings of (A, A, A, B):

| Sequence | Running tallies (A − B) | A always ahead? |
|----------|------------------------|-----------------|
| A A A B  | 1, 2, 3, 2             | ✓               |
| A A B A  | 1, 2, 1, 2             | ✓               |
| A B A A  | 1, 0, 1, 2             | ✗ (ties at step 2) |
| B A A A  | −1, 0, 1, 2            | ✗ (B ahead at step 1) |

2 out of 4 = **1/2** ✓

---

## Intuition for the answer

- If $a \gg b$: probability $\approx 1$ — A is so far ahead, they're almost certainly always leading.
- If $a = b + 1$: probability $= \frac{1}{2b+1}$ — surprisingly small! A barely wins overall, so there are many ways the lead could flip.
- If $a = b$: probability $= 0$ — A must tie at the very end, so A cannot be *strictly* ahead throughout.

---

## Why it's beautiful

The answer $\dfrac{a-b}{a+b}$ is shockingly simple given how complex the question sounds. The proof uses pure **rotational symmetry** — no heavy computation, just the insight that every cyclic rotation of a ballot sequence is equally likely, and exactly $a - b$ of them are "good."
