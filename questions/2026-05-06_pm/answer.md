# Answer: Gambler's Ruin: Probability and Expected Duration

## Key Idea / Intuition

For part (a), since the game is fair, the gambler's fortune is a martingale — its expected value never changes. So the probability of reaching $N$ before $0$ must be exactly $k/N$, the only linear interpolation consistent with boundary values $0$ and $1$.

For part (b), the surprise: the expected duration is $k(N - k)$. This is the product of the two "distances to the walls." Intuitively, the gambler wanders diffusively, and diffusion takes time proportional to (distance)². The quantity $X_t^2 - t$ is also a martingale, and applying optional stopping to it gives the answer without solving a recursion directly.

---

## Formal Proof / Solution

### Part (a): Probability of Reaching $N$

Let $p_k = P(\text{reach } N \mid \text{start at } k)$, with $p_0 = 0$, $p_N = 1$.

The balance equation is:
$$p_k = \frac{1}{2} p_{k+1} + \frac{1}{2} p_{k-1}$$

This says $p_{k+1} - p_k = p_k - p_{k-1}$, so $p_k$ is **linear** in $k$. With boundary conditions:

$$\boxed{p_k = \frac{k}{N}}$$

**Martingale view:** $X_t$ (the fortune at time $t$) is a martingale. By the Optional Stopping Theorem (the game ends in finite time a.s., and $|X_t|$ is bounded by $N$):
$$E[X_T] = X_0 = k$$
$$N \cdot p_k + 0 \cdot (1 - p_k) = k \implies p_k = \frac{k}{N}. \checkmark$$

---

### Part (b): Expected Duration

Let $\tau$ = stopping time. We use the second martingale:

**Claim:** $M_t = X_t^2 - t$ is a martingale.

**Proof of claim:** 
$$E[X_{t+1}^2 \mid X_t] = \frac{1}{2}(X_t + 1)^2 + \frac{1}{2}(X_t - 1)^2 = X_t^2 + 1$$

So $E[M_{t+1} \mid \mathcal{F}_t] = X_t^2 + 1 - (t+1) = X_t^2 - t = M_t$. ✓

**Apply Optional Stopping** to $M_t = X_t^2 - t$:
$$E[X_\tau^2 - \tau] = E[X_0^2 - 0] = k^2$$

Therefore:
$$E[\tau] = E[X_\tau^2] - k^2$$

Now compute $E[X_\tau^2]$: at stopping, $X_\tau = N$ with probability $k/N$ and $X_\tau = 0$ with probability $1 - k/N$:
$$E[X_\tau^2] = N^2 \cdot \frac{k}{N} + 0^2 \cdot \left(1 - \frac{k}{N}\right) = Nk$$

Therefore:
$$\boxed{E[\tau] = Nk - k^2 = k(N - k)}$$

---

### Why This Is Surprising

- The expected duration depends on **both** the starting point and the target.
- Starting at $k = N/2$ (the middle) gives the **longest** expected game: $E[\tau] = N^2/4$.
- A gambler starting with $\$1$ facing a casino with $\$999$ (so $N = 1000$, $k = 1$) has an expected game of only $999$ steps — but wins with probability only $1/1000$. A very short doomed journey!
- The shape $k(N-k)$ is a discrete parabola, symmetric in $k$ and $N-k$, reflecting the symmetry between the two absorbing barriers.
