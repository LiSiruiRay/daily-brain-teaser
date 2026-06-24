# Answer: The Matching Birthdays: Expected Collisions

## Key Idea / Intuition

The trick is **linearity of expectation**: instead of tracking the complicated event "at least one pair matches," just assign each pair an indicator and sum. The expectation is clean and exact. The paradox in part (3) is resolved by recognizing that $E[X] \geq 1$ and $P(X \geq 1) \geq \frac{1}{2}$ are *very different* thresholds — expectation can be dragged above 1 by rare but large values, while probability of at least one event can exceed $\frac{1}{2}$ much earlier.

---

## Formal Proof / Solution

### Part 1: Computing $E[X]$

There are $\binom{n}{2}$ pairs of people. For any pair $(i,j)$, define the indicator

$$I_{ij} = \mathbf{1}[\text{person } i \text{ and person } j \text{ share a birthday}].$$

The probability that two specific people share a birthday is

$$P(I_{ij} = 1) = \frac{365}{365^2} = \frac{1}{365},$$

since person $j$'s birthday must match person $i$'s (any of the 365 days), and there are $365^2$ equally likely pairs.

By linearity of expectation:

$$E[X] = \sum_{1 \leq i < j \leq n} E[I_{ij}] = \binom{n}{2} \cdot \frac{1}{365} = \frac{n(n-1)}{2 \cdot 365}.$$

### Part 2: When does $E[X] \geq 1$?

$$\frac{n(n-1)}{730} \geq 1 \iff n(n-1) \geq 730.$$

Check: $27 \times 26 = 702 < 730$ and $28 \times 27 = 756 \geq 730$.

So $E[X] \geq 1$ first holds at $n = 28$.

### Part 3: Reconciling with $n = 23$

The confusion is between two different statements:

| Quantity | Threshold |
|---|---|
| $P(\text{at least one shared pair}) \geq \frac{1}{2}$ | $n \approx 23$ |
| $E[\text{number of shared pairs}] \geq 1$ | $n \approx 28$ |

These are **not** the same. In general, for a non-negative integer-valued random variable $X$:

$$P(X \geq 1) \leq E[X] \quad \text{(by Markov's inequality)},$$

but also $P(X \geq 1)$ can be *large* even when $E[X]$ is *small*, if $X$ is concentrated near 1.

The key: when $n = 23$, the expected number of matching pairs is

$$E[X] = \frac{23 \times 22}{730} \approx 0.693 < 1,$$

yet $P(X \geq 1) \approx 0.507 > \frac{1}{2}$.

This is perfectly consistent! When $E[X] < 1$, the event $\{X \geq 1\}$ can still have probability close to $E[X]$ (since if $X$ is approximately Bernoulli or Poisson$(0.693)$, then $P(X \geq 1) = 1 - e^{-0.693} \approx 0.5$, which matches the birthday calculation beautifully).

**Intuitive summary:** At $n=23$, matching pairs are rare but not impossible — the distribution of $X$ is approximately Poisson with mean $\approx 0.693$, so the chance of *zero* collisions is $\approx e^{-0.693} \approx \frac{1}{2}$. Expectation exceeding 1 requires the mean to grow to 1, which needs more people.
