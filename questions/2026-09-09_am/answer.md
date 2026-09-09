# Answer: The Lazy Gambler's Last Dollar

## Key Idea / Intuition

For part (1), the gambler's ruin formula gives the win probability using the ratio $r = q/p$. Because the game is favorable ($p > q$), the gambler has a better-than-even chance despite starting with only half the money. 

For part (2), there is a slick martingale approach: the process $M_n = X_n - (p - q)n$ is a martingale (it tracks "corrected wealth"), and optional stopping gives a linear equation for the expected duration. Together the two martingales — $X_n$ and the quadratic one — pin down $\mathbb{E}[T]$ without any system of equations.

---

## Formal Proof / Solution

**Setup.** Let the gambler start at position $m = 3$, the total pot be $N = 6$, $p = 2/3$, $q = 1/3$, and $r = q/p = 1/2$.

---

### Part 1: Win Probability

The classic gambler's ruin formula: if the gambler starts at $m$ with total $N$,

$$P(\text{gambler wins}) = \frac{1 - r^m}{1 - r^N} = \frac{1 - (1/2)^3}{1 - (1/2)^6} = \frac{1 - 1/8}{1 - 1/64} = \frac{7/8}{63/64} = \frac{7}{8} \cdot \frac{64}{63} = \frac{8}{9}.$$

So the gambler wins with probability $\boxed{8/9}$.

*Derivation sketch:* Let $P_k$ be the win probability starting from $k$. The recurrence $P_k = p\,P_{k+1} + q\,P_{k-1}$ with $P_0 = 0$, $P_N = 1$ has the general solution $P_k = A + B\,r^k$ (for $r \neq 1$), giving the formula above.

---

### Part 2: Expected Duration via Two Martingales

**Martingale 1.** $X_n$ (the gambler's wealth) satisfies $\mathbb{E}[X_{n+1} \mid X_n] = p(X_n+1)+q(X_n-1) = X_n + (p-q) = X_n + 1/3$. So

$$M_n = X_n - \frac{n}{3}$$

is a martingale. By optional stopping (the game ends at finite time $T$ a.s.):

$$\mathbb{E}[X_T] - \frac{\mathbb{E}[T]}{3} = X_0 = 3.$$

Now $X_T \in \{0, 6\}$: the gambler ends with $\$6$ with prob $8/9$ and $\$0$ with prob $1/9$:

$$\mathbb{E}[X_T] = 6 \cdot \frac{8}{9} + 0 \cdot \frac{1}{9} = \frac{48}{9} = \frac{16}{3}.$$

So:

$$\frac{16}{3} - \frac{\mathbb{E}[T]}{3} = 3 \implies \mathbb{E}[T] = \frac{16}{3} - 3 = \frac{7}{3}.$$

Wait — let's recheck this against Martingale 2 for consistency.

**Martingale 2.** For the quadratic martingale, note $\mathbb{E}[X_{n+1}^2 \mid X_n] = p(X_n+1)^2 + q(X_n-1)^2 = X_n^2 + 2(p-q)X_n + 1 = X_n^2 + \frac{2}{3}X_n + 1$.

So $X_n^2 - \frac{2n}{3}X_n - n$ is **not** a martingale directly. Let's use the standard approach instead.

**Direct computation via the system.** Let $D_k = \mathbb{E}[T \mid X_0 = k]$. Then:

$$D_k = 1 + p\,D_{k+1} + q\,D_{k-1}, \quad D_0 = D_6 = 0.$$

This gives $D_k = \frac{k(N-k)}{p - q}$ when $p \neq q$... actually the formula for expected duration is:

$$D_k = \frac{k}{p-q} - \frac{N}{p-q} \cdot \frac{1 - r^k}{1 - r^N}.$$

With $p - q = 1/3$, $N = 6$, $k = 3$, $r = 1/2$:

$$D_3 = \frac{3}{1/3} - \frac{6}{1/3} \cdot \frac{1-(1/2)^3}{1-(1/2)^6} = 9 - 18 \cdot \frac{8}{9} = 9 - 16 = -7.$$

That's negative — let me restate the correct formula carefully.

The correct formula (from solving the recurrence $D_k = 1 + pD_{k+1} + qD_{k-1}$):

$$D_k = \frac{k}{q - p} + \frac{N}{p - q} \cdot \frac{1 - r^k}{1 - r^N}.$$

With $q - p = -1/3$ (so $1/(q-p) = -3$):

$$D_3 = -3 \cdot 3 + 3 \cdot 6 \cdot \frac{7/8}{63/64} = -9 + 18 \cdot \frac{8}{9} = -9 + 16 = 7.$$

So $\mathbb{E}[T] = \boxed{7}$ rounds.

**Verification via Martingale 1 (corrected):** $\mathbb{E}[X_T] - \frac{\mathbb{E}[T]}{3} = 3$ gives $\mathbb{E}[T] = 3(\mathbb{E}[X_T] - 3) = 3(16/3 - 3) = 16 - 9 = 7$. ✓

---

### Summary

| Quantity | Value |
|---|---|
| Win probability | $8/9 \approx 88.9\%$ |
| Expected duration | $7$ rounds |

The gambler is heavily favored despite equal starting wealth, and the game is expected to end quite quickly — a beautiful consequence of the favorable odds.
