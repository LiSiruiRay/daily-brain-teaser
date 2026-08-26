# Answer: Gambler's Duration via Martingale

## Key Idea / Intuition

The key is to find a **martingale whose optional stopping gives the answer directly**. For a simple symmetric random walk $S_t$, both $S_t$ and $S_t^2 - t$ are martingales. The first gives the win probability (linear in starting position); the second, when stopped at the exit time $T$, gives $\mathbb{E}[T]$ in terms of the starting position. This is a beautiful example of how martingales convert a seemingly hard expectation problem into simple algebra.

---

## Formal Proof / Solution

**Setup.** Let $S_0 = k$, and let $T = \min\{t : S_t = 0 \text{ or } S_t = n\}$. We want $\mathbb{E}_k[T]$.

**Step 1: $S_t$ is a martingale.**

Since each step has mean zero, $\mathbb{E}[S_{t+1} \mid S_t] = S_t$, so $S_t$ is a martingale.

By Optional Stopping (the game ends in finite time a.s.):
$$\mathbb{E}[S_T] = S_0 = k.$$

Also $S_T \in \{0, n\}$, so if $p$ is the probability of reaching $n$:
$$p \cdot n + (1-p) \cdot 0 = k \implies p = \frac{k}{n}.$$

(This recovers the classical gambler's ruin formula.)

**Step 2: $M_t = S_t^2 - t$ is a martingale.**

Compute:
$$\mathbb{E}[S_{t+1}^2 \mid S_t] = \frac{1}{2}(S_t+1)^2 + \frac{1}{2}(S_t-1)^2 = S_t^2 + 1.$$

Therefore:
$$\mathbb{E}[M_{t+1} \mid \mathcal{F}_t] = S_t^2 + 1 - (t+1) = S_t^2 - t = M_t. \checkmark$$

**Step 3: Apply Optional Stopping to $M_t$.**

By Optional Stopping (justified since $T$ has finite expectation and bounded increments):
$$\mathbb{E}[M_T] = M_0 = k^2 - 0 = k^2.$$

But also:
$$\mathbb{E}[M_T] = \mathbb{E}[S_T^2] - \mathbb{E}[T].$$

We already know $S_T \in \{0, n\}$ with probabilities $1 - k/n$ and $k/n$, so:
$$\mathbb{E}[S_T^2] = \frac{k}{n} \cdot n^2 + \left(1 - \frac{k}{n}\right) \cdot 0 = kn.$$

Therefore:
$$k^2 = kn - \mathbb{E}[T]$$
$$\boxed{\mathbb{E}_k[T] = kn - k^2 = k(n-k).}$$

**Step 4: The special case.**

Starting from $k = 1$ with target $n$:
$$\mathbb{E}_1[T] = 1 \cdot (n - 1) = n - 1.$$

**Why this is beautiful.** The answer $k(n-k)$ is symmetric in $k$ and $n-k$: the game lasts longest when you start in the middle ($k = n/2$), which makes perfect intuitive sense. The martingale $S_t^2 - t$ does all the work, turning a recursive system of equations into a one-line calculation.

Written to [question file](questions/2026-08-17_am.md) and answer below.
