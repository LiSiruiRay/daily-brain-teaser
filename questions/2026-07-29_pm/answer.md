# Answer: The Lazy Drunk: Random Walk Returns in 2D vs 3D

## Key Idea / Intuition

The 2D walk is **recurrent**: the drunk always comes home. The 3D walk is **transient**: the particle drifts away forever with positive probability. The reason is fundamentally about how quickly the probability of being at the origin decays with time — in 2D it decays like $1/n$, whose sum diverges (so infinitely many returns), while in 3D it decays like $1/n^{3/2}$, whose sum converges (so only finitely many returns on average, meaning escape is possible).

The key tool is a beautiful connection between **return probabilities** and **expected number of returns**, combined with a generating-function / Fourier analysis of the walk.

---

## Formal Proof / Solution

### Step 1: Expected number of returns as a convergence criterion

Let $p_n$ = probability of being at origin after $n$ steps. The **expected total number of visits to the origin** (including time 0) is:

$$E[\text{visits}] = \sum_{n=0}^{\infty} p_n.$$

Let $P$ = probability of **ever** returning to the origin. After each return, the particle starts fresh, so the number of returns follows a geometric distribution with success parameter $Q = 1-P$. Hence:

$$E[\text{returns after time 0}] = \frac{P}{Q} = \frac{P}{1-P}.$$

- If $P = 1$ (recurrent): the expected number of returns is **infinite**, so $\sum_{n=1}^\infty p_n = \infty$.
- If $P < 1$ (transient): the sum **converges**, and $P = 1 - \frac{1}{\sum_{n=0}^\infty p_n}$.

So **recurrence $\iff$ $\sum_n p_n$ diverges**.

---

### Step 2: Asymptotics of $p_n$

**In 2D:** By the local central limit theorem, after $2n$ steps,

$$p_{2n} \sim \frac{1}{\pi n} \quad \text{as } n \to \infty.$$

(Odd steps give $p_{2n+1} = 0$ by parity.) So $\sum_{n=1}^\infty p_n \sim \sum_{n} \frac{1}{\pi n} = \infty$. **Recurrent.**

**In 3D:** After $2n$ steps,

$$p_{2n} \sim \frac{1}{(4\pi n/3)^{3/2}} \cdot C = \frac{C}{n^{3/2}}.$$

More precisely, $p_{2n} \sim \left(\frac{3}{2\pi n}\right)^{3/2}$. Since $\sum_n n^{-3/2} < \infty$ (a convergent $p$-series with $p = 3/2 > 1$), **the walk is transient**.

---

### Step 3: Why the dimension matters

The key is dimension $d$:
- After $n$ steps, the particle is spread over a ball of radius $\sim \sqrt{n}$, so volume $\sim n^{d/2}$.
- The probability of being at the origin $\sim n^{-d/2}$.
- Recurrence requires $\sum n^{-d/2} = \infty$, i.e., $d/2 \leq 1$, i.e., $\mathbf{d \leq 2}$.

This is **Pólya's theorem** (1921): The simple random walk on $\mathbb{Z}^d$ is recurrent for $d \leq 2$ and transient for $d \geq 3$.

---

### Step 4: The escape probability in 3D

Since $\sum_{n=0}^\infty p_n$ converges, we can compute:

$$\sum_{n=0}^{\infty} p_{2n} = \frac{1}{(2\pi)^3} \int_{[-\pi,\pi]^3} \frac{d^3\mathbf{k}}{1 - \frac{1}{3}(\cos k_x + \cos k_y + \cos k_z)}.$$

This is **Watson's triple integral** (1939), which evaluates to:

$$\sum_{n=0}^{\infty} p_{2n} = \frac{\sqrt{6}}{96\pi^3}\,\Gamma\!\left(\tfrac{1}{4}\right)^4 \approx 1.5164\ldots$$

Therefore:

$$P(\text{return}) = 1 - \frac{1}{\sum p_n} \approx 1 - \frac{1}{1.5164} \approx 0.3405 \quad \text{(escape probability)} $$

$$\Rightarrow P(\text{ever return}) \approx 1 - 0.3405 = 0.6595.$$

---

### Summary

| Dimension | $p_n$ decay | $\sum p_n$ | Walk type | Return prob |
|-----------|-------------|------------|-----------|-------------|
| $d = 1$ | $n^{-1/2}$ | $\infty$ | Recurrent | 1 |
| $d = 2$ | $n^{-1}$ | $\infty$ | Recurrent | 1 |
| $d = 3$ | $n^{-3/2}$ | $< \infty$ | Transient | $\approx 0.34$ |

The drunk in 2D will always find his way home. In 3D, he has about a **34% chance of wandering off forever** — the extra dimension gives him too much room to escape.
