# Answer: The Unfair Coin That Becomes Fair

## Key Idea / Intuition

The beautiful insight is due to John von Neumann: flip the coin **twice**. The outcomes HT and TH are not equally likely individually, but by symmetry they are equally likely *relative to each other* — both have probability $p(1-p)$. So declare HT = "heads" and TH = "tails", and simply repeat if you get HH or TT. This extracts perfect fairness from an unknown bias, with no knowledge of $p$ required whatsoever.

---

## Formal Proof / Solution

### The Procedure (Von Neumann's trick)

1. Flip the biased coin **twice**.
2. If the result is **HT**, output **Heads**.
3. If the result is **TH**, output **Tails**.
4. If the result is **HH** or **TT**, **discard and repeat** from step 1.

### Why It's Fair

Each pair of flips has the following probabilities:

$$P(HH) = p^2, \quad P(HT) = p(1-p), \quad P(TH) = (1-p)p, \quad P(TT) = (1-p)^2.$$

The key observation:

$$P(HT) = p(1-p) = (1-p)p = P(TH).$$

So conditioned on the event that we do **not** discard (i.e., we got HT or TH), both outcomes are equally likely:

$$P(\text{output Heads}) = P(\text{output Tails}) = \frac{p(1-p)}{p(1-p) + (1-p)p} = \frac{1}{2}.$$

This holds for **any** $p \in (0,1)$, with no knowledge of $p$ needed.

### Expected Number of Flips

Each round (2 flips) succeeds with probability:

$$q = P(HT \text{ or } TH) = 2p(1-p).$$

The number of rounds until success is geometric with mean $\frac{1}{q}$, so the expected number of **coin flips** is:

$$\mathbb{E}[\text{flips}] = \frac{2}{2p(1-p)} = \frac{1}{p(1-p)}.$$

Since $p(1-p) \leq \frac{1}{4}$ (maximized at $p = 1/2$), we have:

$$\mathbb{E}[\text{flips}] \geq 4,$$

with equality when $p = 1/2$ (the fair coin case), and the expected number grows to $\infty$ as $p \to 0$ or $p \to 1$ (very biased coins are very wasteful).

### Summary Table

| $p$ | $\mathbb{E}[\text{flips}]$ |
|------|---------------------------|
| $0.5$ | $4$ |
| $0.3$ | $\approx 4.76$ |
| $0.1$ | $\approx 11.1$ |
| $0.01$ | $\approx 101$ |

The elegance: **perfect fairness from unknown bias**, at the cost of only expected efficiency.

---

**Reference:** Von Neumann, J. (1951). "Various techniques used in connection with random digits." *Applied Math Series*, 12, 36–38.
