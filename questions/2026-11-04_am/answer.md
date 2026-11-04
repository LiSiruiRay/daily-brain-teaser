# Answer: Winning an Unfair Game

## Key Idea / Intuition

Two forces compete. The law of large numbers pulls long matches toward a loss, because $p < \tfrac12$. But with an even number of games, ties count as losses, and ties are very likely in short matches. In a 2-game match you need *both* wins, which is harsh. Lengthening the match makes ties rarer, roughly like $1/\sqrt{N}$. When $p$ is close to $\tfrac12$, this effect beats the slow drift against you for a while.

To find the balance point, compare a $2n$-game match with a $(2n+2)$-game match by **appending two games**. The outcome can only change in the two "boundary" situations, so all the binomial sums cancel except two terms.

---

## Formal Proof / Solution

Let $q = 1-p$, and let $P_{2n}$ be the probability of winning a $2n$-game match, i.e. of winning at least $n+1$ games.

**Step 1: Append two games.** Think of a $(2n+2)$-game match as the first $2n$ games followed by two more. After $2n$ games, your status (winner or loser) can change after the extra two games in only two cases:

- **You had exactly $n+1$ wins (a narrow win) and lose both extra games.** You end with $n+1$ wins out of $2n+2$, which is a tie and therefore a loss. This case has probability
$$\binom{2n}{n+1}p^{n+1}q^{n-1}\cdot q^2.$$
- **You had exactly $n$ wins (a tie) and win both extra games.** You end with $n+2$ wins out of $2n+2$, which is a win. This case has probability
$$\binom{2n}{n}p^{n}q^{n}\cdot p^2.$$

In every other case, your status is unchanged.

**Step 2: The difference.** Use $\binom{2n}{n+1} = \frac{n}{n+1}\binom{2n}{n}$. Then
$$P_{2n+2}-P_{2n} = \binom{2n}{n}p^{n+1}q^{n}\Big(p - \tfrac{n}{n+1}\,q\Big).$$
So
$$P_{2n+2} > P_{2n} \iff (n+1)p > nq \iff n(1-2p) < p \iff n < \frac{p}{1-2p}.$$
(This also holds for $n=0$, with $P_0 = 0$ and $P_2 = p^2$.)

**Step 3: Unimodality.** The sequence $P_2, P_4, P_6, \dots$ increases as long as $n < \frac{p}{1-2p}$ and decreases afterwards. If $\frac{p}{1-2p}$ is an integer $n$, then $P_{2n} = P_{2n+2}$. Hence the optimal number of games is
$$N^* = 2\left\lceil \frac{p}{1-2p}\right\rceil.$$

To restate this, note that $\frac{p}{1-2p} = \frac12\!\left(\frac{1}{1-2p}-1\right)$. So $N^*$ is the smallest even integer that is at least $\frac{1}{1-2p}-1$. Equivalently:

$$\boxed{N^* = \text{the even integer nearest to } \dfrac{1}{1-2p}}$$

When $\frac{1}{1-2p}$ is an odd integer, the two neighboring even integers tie.

In particular, $N^* = 2$ exactly when $p \le \tfrac13$.

**Step 4: The example $p = 0.45$.** Here $\frac{1}{1-2p} = \frac{1}{0.1} = 10$, so the optimal match has **10 games**. Numerically:
$$P_2 = 0.45^2 = 0.2025, \qquad P_{10} = \Pr[\mathrm{Bin}(10,0.45)\ge 6] \approx 0.2616.$$
That is about 30% better than the "obvious" choice of 2 games.

**Bonus: odd $N$.** Do the same two-extra-games comparison between $2n+1$ and $2n+3$ games. Now there are no ties. The status changes only if you had $n+1$ wins and lose both extra games, or had $n$ wins and win both. Since $\binom{2n+1}{n+1} = \binom{2n+1}{n}$,
$$P_{2n+3}-P_{2n+1} = \binom{2n+1}{n}p^{n+1}q^{n+1}(p-q) < 0.$$
So odd-length matches get steadily worse, and the best odd choice is $N = 1$, with winning probability $p$. For $p = 0.45$, this gives $0.45$, which beats $P_{10}$.

The surprise in part (a) therefore comes entirely from the **tie penalty**. Forcing $N$ to be even makes short matches unexpectedly costly, and a longer match is the best way to dilute the ties.

*Source: F. Mosteller, *Fifty Challenging Problems in Probability with Solutions*, Problem 44 ("Winning an Unfair Game"). Mosteller abridges it from "Optimal length of play for a binomial game," *Mathematics Teacher* 54 (1961), 411–412.*
