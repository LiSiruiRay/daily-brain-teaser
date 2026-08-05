# Answer: Gambler's Ruin: Martingale and Win Probability

## Key Idea / Intuition

The key insight is that **in a fair game, the probability of winning is exactly proportional to your starting wealth relative to the total pot**. There's a beautiful reason: the gambler's fortune is a martingale (its expected value never changes), and optional stopping forces the expectation at the end to equal the expectation at the start. This pins down the win probability with almost no computation.

So Alice wins with probability $a/(a+b)$. With $a=1$ and $b=99$, Alice wins with probability just $1/100 = 1\%$. The casino's deep pockets are overwhelmingly protective — even in a perfectly fair game.

---

## Formal Proof / Solution

**Setup.** Let $p_k$ = probability Alice wins when she currently has $k$ dollars (and Bob has $a+b-k$). The total pot is $N = a + b$.

**Martingale argument (slick).** Alice's fortune $X_t$ at time $t$ is a martingale: since the coin is fair,
$$E[X_{t+1} \mid X_t] = \frac{1}{2}(X_t + 1) + \frac{1}{2}(X_t - 1) = X_t.$$
The game ends at a random time $T$ when $X_T \in \{0, N\}$ (one player goes broke). By the Optional Stopping Theorem (applicable here since the game terminates with probability 1 and the fortune is bounded):
$$E[X_T] = E[X_0] = a.$$
But $X_T = N$ with probability $p_a$ (Alice wins) and $X_T = 0$ with probability $1 - p_a$ (Bob wins). So:
$$E[X_T] = p_a \cdot N + (1-p_a) \cdot 0 = p_a \cdot N.$$
Setting equal:
$$p_a \cdot N = a \implies \boxed{p_a = \frac{a}{a+b}.}$$

**The Surprising Answer.** With $a = 1$, $b = 99$:
$$p_1 = \frac{1}{100} = 1\%.$$

Alice has only a 1% chance of winning, despite the game being **perfectly fair** at every single step. The asymmetry comes entirely from starting positions, not from any bias in the coin.

**Why is this surprising?** People often conflate "fair game" (each flip is 50-50) with "fair competition" (both players have equal chances). A fair game only guarantees fairness in expectation — not in survival. The richer player benefits enormously from their "buffer" against the random fluctuations.

**Alternative derivation (recurrence).** For completeness, the same answer follows from solving the recurrence:
$$p_k = \frac{1}{2}p_{k-1} + \frac{1}{2}p_{k+1}, \quad p_0 = 0,\; p_N = 1.$$
The general solution is $p_k = Ak + B$, and boundary conditions give $p_k = k/N$.
