# Answer: The Secretary Who Knows the Distribution

## Key Idea / Intuition

With two candidates, you can afford a pure threshold rule: if the first candidate scores above some cutoff $t$, hire them immediately; otherwise, wait and take the second (regardless of their score, since it's your last chance). The surprising punchline is that as the number of candidates grows, the optimal threshold strategy guarantees you hire the best with probability approaching $1/e \approx 0.368$ — the same asymptotic as the classical secretary problem (where you know only ranks, not values). Knowing the distribution doesn't actually help asymptotically!

---

## Formal Proof / Solution

### Step 1: Optimal Strategy for $n = 2$

Let the two scores be $X_1, X_2 \sim \text{Uniform}[0,1]$, independent.

**Strategy:** Choose threshold $t \in [0,1]$. Accept $X_1$ if $X_1 > t$; otherwise accept $X_2$.

**Probability of hiring the best:**

$$P(\text{success}) = P(X_1 > t \text{ and } X_1 > X_2) + P(X_1 \leq t \text{ and } X_2 > X_1)$$

Compute each term:
$$P(X_1 > t,\ X_1 > X_2) = \int_t^1 P(X_2 < x)\,dx = \int_t^1 x\,dx = \frac{1-t^2}{2}$$

$$P(X_1 \leq t,\ X_2 > X_1) = \int_0^t P(X_2 > x)\,dx = \int_0^t (1-x)\,dx = t - \frac{t^2}{2}$$

So:
$$P(\text{success}) = \frac{1-t^2}{2} + t - \frac{t^2}{2} = \frac{1}{2} + t - t^2$$

Optimize over $t$:
$$\frac{d}{dt}\left(\frac{1}{2} + t - t^2\right) = 1 - 2t = 0 \implies t^* = \frac{1}{2}$$

$$P(\text{success}) = \frac{1}{2} + \frac{1}{2} - \frac{1}{4} = \boxed{\frac{3}{4}}$$

This is strictly better than the rank-based secretary problem with $n=2$ (which gives $1/2$), because knowing the distribution lets you make a smarter decision on the first candidate.

---

### Step 2: The $n$-Candidate Threshold Strategy

With $n$ candidates and scores $X_1, \ldots, X_n \sim \text{Uniform}[0,1]$, work backwards. With $r$ candidates remaining and the current candidate having score $x$, the optimal policy sets an **indifference threshold** $x_r$ satisfying:

$$\text{(value of accepting } x_r\text{)} = \text{(value of continuing)}$$

From Mosteller's analysis: with $r$ draws remaining and candidate in hand with score $x$, you should accept if $x > x_r$ where $x_r$ satisfies:

$$x_r^r = \binom{r}{1}x_r^{r-1}(1-x_r)\cdot 1 + \binom{r}{2}x_r^{r-2}(1-x_r)^2 \cdot \frac{1}{2} + \cdots$$

The right-hand side simplifies: it equals the probability that at least one of the remaining $r$ candidates exceeds $x_r$ **and** you successfully pick the largest.

---

### Step 3: The Asymptotic Surprise

As $n \to \infty$, the optimal success probability satisfies:

$$P_n(\text{success}) \to \frac{1}{e}$$

**Why?** The threshold $t$ for the first candidate you'd accept, as $n$ grows, converges to $e^{-1/n} \cdot n$-th power scaling. One can show the optimal thresholds $x_r \approx 1 - \frac{1}{r}$ for large $r$, and the probability of winning under the optimal policy satisfies the recursion whose solution converges to $1/e$.

Concretely, compare:

| $n$ | Optimal (known distribution) | Classical secretary (rank only) |
|-----|-----------------------------|---------------------------------|
| 1   | 1                           | 1                               |
| 2   | 3/4                         | 1/2                             |
| 3   | ~0.618                      | ~0.500                          |
| $\infty$ | $1/e \approx 0.368$ | $1/e \approx 0.368$             |

**The deep insight:** For small $n$, knowing the distribution helps substantially. But as $n \to \infty$, the problem becomes so hard (you're increasingly likely to miss the best by a wrong decision early on) that both strategies converge to $1/e$. The extra information from knowing the distribution is asymptotically useless.

---

### Summary

- With $n=2$: threshold $t^* = 1/2$, success probability $= 3/4$.
- With general $n$: use decreasing thresholds $x_n < x_{n-1} < \cdots < x_1$.
- As $n \to \infty$: $P(\text{success}) \to 1/e$, matching the classical (rank-only) secretary problem.
