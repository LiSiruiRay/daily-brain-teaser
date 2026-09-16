# Answer: Expected Number of Matches

## Key Idea / Intuition

The trick is **linearity of expectation** — you don't need to worry about dependencies between positions at all. Each of the $n$ positions contributes independently to the expected count. For position $i$, the probability that the card from deck 1 matches the card from deck 2 is exactly $1/n$, since the second deck is a uniformly random permutation. Summing over all $n$ positions gives an expected number of matches equal to **exactly 1, regardless of $n$**.

---

## Formal Proof / Solution

**Setup.** Let $X_i$ be the indicator random variable for the event that the card at position $i$ in the first deck matches the card at position $i$ in the second deck, for $i = 1, 2, \ldots, n$.

The total number of matches is

$$M = X_1 + X_2 + \cdots + X_n.$$

**Key computation.** By linearity of expectation,

$$\mathbb{E}[M] = \sum_{i=1}^{n} \mathbb{E}[X_i] = \sum_{i=1}^{n} P(\text{position } i \text{ matches}).$$

Now fix position $i$. The card at position $i$ in deck 1 is some fixed card (say, the 7 of hearts). The card at position $i$ in deck 2 is a uniformly random card from a fresh random permutation of $n$ cards — so it equals any particular card with probability $\frac{1}{n}$.

Therefore,

$$P(\text{position } i \text{ matches}) = \frac{1}{n}.$$

**Result.** Summing:

$$\mathbb{E}[M] = n \cdot \frac{1}{n} = \boxed{1}.$$

**The surprise:** The expected number of matches is always **1**, regardless of $n$. Whether you use a 2-card deck or a 52-card deck or a 1000-card deck, you expect exactly one match on average.

**Comparison with the derangement problem.** This is the same structure as the hat-check problem (derangements), but now we ask for the *expected* number of fixed points of a random permutation. The answer is 1 by the same argument — and this holds for any $n \geq 1$. The variance also simplifies beautifully: $\text{Var}(M) = 1$ for all $n$ (also by indicator calculations), so the distribution of $M$ converges to Poisson(1) as $n \to \infty$.
