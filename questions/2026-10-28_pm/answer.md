# Answer: Curing the Compulsive Gambler

## Key Idea / Intuition

Roulette has a negative **mean**, but its payoff distribution is extremely skewed. Brown loses a little almost every spin, and occasionally wins a lot. So "Brown is behind" is *not* the same event as "Brown's expected gain is negative."

With 36 plays, a single win brings Brown back to exactly even. He is behind only if he never wins, which happens less than half the time. Friend's even-money bet is therefore a gift to Brown, and it outweighs the small house edge.

Add one more spin and the threshold flips. One win in 37 plays now leaves Brown \$1 down, so "behind" becomes very likely. The lesson is that mean and median can lie on opposite sides of zero, and for discrete payoffs the exact boundary matters enormously.

---

## Formal Proof / Solution

### Setup

Let $W$ be the number of wins in $n$ plays, so $W \sim \text{Bin}(n, 1/38)$.

Each win gives $+35$ and each loss gives $-1$. Brown's casino profit is therefore
$$
P_n = 35W - (n - W) = 36W - n.
$$

### (a) Horizon $n = 36$

**Casino expectation.** Per spin, the expected gain is
$$
35\cdot\tfrac{1}{38} - 1\cdot\tfrac{37}{38} = -\tfrac{2}{38} = -\tfrac{1}{19}.
$$
Over 36 spins this totals $-\tfrac{36}{19} \approx -1.89$ dollars.

**When is Brown behind?** We have $P_{36} = 36(W-1)$.
- If $W \ge 1$, then $P_{36} \ge 0$, so Brown is even or ahead.
- Brown is strictly behind only if $W = 0$.

The probability of that is
$$
\Pr(W=0) = \left(\tfrac{37}{38}\right)^{36} = \exp\!\left(36\ln\tfrac{37}{38}\right) \approx e^{-0.960} \approx 0.383.
$$

**Side bet expectation.** Brown wins the side bet with probability $0.617$ and loses it with probability $0.383$:
$$
20(0.617) - 20(0.383) = 20(0.234) \approx +4.68.
$$

**Total:**
$$
\mathbb{E}[\text{net}] \approx 4.68 - 1.89 = +2.79 \text{ dollars per 36 plays.}
$$

Brown is now *making* money at roulette. As Mosteller remarks, Kind Friend may be cured first. Brown does lose $36 + 20 = \$56$ whenever he goes 0-for-36, which happens about 38% of the time.

**Why this happens:** $P_{36}$ has negative mean, but its median is $\ge 0$. The even-money side bet is judged by the median-like event $\{P_{36}<0\}$, not by the mean.

### (b) Horizon $n = 37$

Now $P_{37} = 36W - 37$.
- If $W = 1$, then $P_{37} = -1$, so Brown is behind.
- If $W \ge 2$, then $P_{37} > 0$.

So Brown is behind if and only if $W \le 1$.

The two cases have the same probability:
$$
\Pr(W=0) = \left(\tfrac{37}{38}\right)^{37},
\qquad
\Pr(W=1) = 37\cdot\tfrac{1}{38}\left(\tfrac{37}{38}\right)^{36} = \left(\tfrac{37}{38}\right)^{37}.
$$
Hence
$$
\Pr(\text{behind}) = 2\left(\tfrac{37}{38}\right)^{37} \approx 2(0.383)(0.974) \approx 0.746.
$$

**Side bet expectation for Brown:**
$$
20(0.254) - 20(0.746) \approx -9.83.
$$

**Casino expectation:** $-\tfrac{37}{19} \approx -1.95$.

**Total:**
$$
\mathbb{E}[\text{net}] \approx -9.83 - 1.95 \approx -11.78 \text{ dollars per 37 plays.}
$$

One extra spin turns a cure that pays Brown \$2.79 into one that costs him almost \$12. The only change is that a single win is no longer enough to break even.

### Takeaway

- For a skewed payoff, $\Pr(X<0)$ can be well below $1/2$ even when $\mathbb{E}[X]<0$.
- Bets on *events*, such as "behind or not," and bets on *means* can disagree sharply.
- For lattice-valued outcomes, whether the boundary case counts as "behind" or "even" can swing the answer dramatically.
