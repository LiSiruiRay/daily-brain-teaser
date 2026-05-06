# Answer: Coupon Collector Problem

## Key Idea / Intuition

Break the collection process into **phases**: after you have collected exactly $k$ distinct coupons, the probability that the next box gives a *new* coupon is $\frac{n-k}{n}$. So the waiting time in each phase is a geometric random variable, and the total expected time is just a sum of $n$ geometric expectations. This sum turns out to be $n$ times the $n$-th harmonic number, and for large $n$ the harmonic number grows like $\ln n$.

---

## Formal Proof / Solution

### Setting up phases

Define **Phase $k$** as the period during which you already have exactly $k-1$ distinct coupon types and are waiting to get the $k$-th new one, for $k = 1, 2, \ldots, n$.

In Phase $k$, the probability of drawing a *new* coupon on any given box is:
$$p_k = \frac{n - (k-1)}{n} = \frac{n - k + 1}{n}.$$

The number of boxes needed in Phase $k$ is **geometrically distributed** with success probability $p_k$, so its expectation is:
$$\mathbb{E}[\text{boxes in Phase } k] = \frac{1}{p_k} = \frac{n}{n - k + 1}.$$

### Total expected number of boxes

Let $T$ be the total number of boxes. By linearity of expectation:
$$\mathbb{E}[T] = \sum_{k=1}^{n} \frac{n}{n-k+1} = n \sum_{j=1}^{n} \frac{1}{j} = n \cdot H_n,$$

where $H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$ is the $n$-th **harmonic number**.

### Concrete answer for $n = 6$

$$\mathbb{E}[T] = 6 \left(1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6}\right) = 6 \cdot \frac{49}{20} = \frac{49}{10} = 14.7.$$

So on average you need about **14.7 rolls** of a fair die to see all 6 faces — perhaps more than you'd guess!

### Asymptotics for large $n$

Since $H_n = \ln n + \gamma + O(1/n)$ where $\gamma \approx 0.5772$ is the Euler–Mascheroni constant:
$$\mathbb{E}[T] = n H_n \approx n \ln n + \gamma n.$$

For large $n$, the dominant behavior is $\boxed{n \ln n}$.

### Why this is beautiful

The problem looks like it might require tracking a complex Markov chain, but the **phase decomposition** reduces everything to a sum of independent geometric waiting times. The harmonic series $H_n$ appears naturally — the same series that famously diverges, here telling us the coupon collector problem takes longer and longer (superlinearly) as $n$ grows.
