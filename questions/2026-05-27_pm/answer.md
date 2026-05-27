# Answer: The Collector's Last Coupon

## Key Idea / Intuition

The game ends the moment the *second color appears for the first time* — equivalently, it ends at the flip that breaks the initial "all one color" run. The first card is always some color. We then wait until the **first card of the opposite color** appears. By symmetry, what matters is only the position of the first card of the minority color among a deck of $2n$ cards. This turns into a clean question about the position of a specific card type in a random ordering.

---

## Formal Proof / Solution

**Setup.** After flipping the first card (say it's red, by symmetry the argument is identical for black), we need the first black card among the remaining $2n - 1$ cards, of which exactly $n$ are black.

**Key observation.** Consider the positions of the $n$ black cards among the remaining $2n-1$ slots. By symmetry, the first black card is equally likely to be in any of the $2n-1$ positions — but that's not quite right. We need the minimum order statistic of $n$ uniform draws without replacement from $\{1, 2, \ldots, 2n-1\}$.

**Expected position of the first black card.** If we pick $n$ items uniformly at random (without replacement) from $\{1, 2, \ldots, 2n-1\}$, the expected value of the *minimum* is:

$$\mathbb{E}[\min] = \frac{2n - 1 + 1}{n + 1} = \frac{2n}{n+1}.$$

This uses the standard result: for the minimum of $n$ items chosen without replacement from $\{1, \ldots, N\}$,

$$\mathbb{E}[\text{min}] = \frac{N+1}{n+1}.$$

Here $N = 2n-1$, so $\mathbb{E}[\text{min}] = \frac{2n}{n+1}$.

**Total expected flips.** We flip the first card (1 flip always), then wait $\mathbb{E}[\text{min}]$ more flips to see the first opposite-color card:

$$\mathbb{E}[\text{total}] = 1 + \frac{2n}{n+1} = \frac{n+1+2n}{n+1} = \frac{3n+1}{n+1}.$$

**Sanity checks:**
- $n=1$: deck has 1 red, 1 black. You always flip exactly 2 cards. Formula gives $\frac{4}{2} = 2$. ✓
- $n=2$: deck has 2 red, 2 black. Formula gives $\frac{7}{3} \approx 2.33$.

  Manual check: P(stop at flip 2) = P(second card differs from first) = $\frac{2}{3}$; P(stop at flip 3) = $\frac{1}{3}$ (second card same, third must differ). $\mathbb{E} = 2 \cdot \frac{2}{3} + 3 \cdot \frac{1}{3} = \frac{7}{3}$. ✓

**The elegant formula:**

$$\boxed{\mathbb{E}[\text{cards flipped}] = \frac{3n+1}{n+1}}$$

As $n \to \infty$, this approaches $3$ — a beautiful limit saying that in a very large balanced deck, you expect to flip only about **3 cards** before seeing both colors.

**Why the limit is 3:** In a huge deck, the probability the second card already differs from the first is $\approx 1/2$. If not, the third card differs with probability $\approx 1/2$, and so on. This geometric-like structure gives $\mathbb{E} \approx 1 + 2 = 3$ via a geometric series argument (expectation of a geometric with $p=1/2$, shifted).
