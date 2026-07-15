# Answer: The Shared Birthday Secretary

## Key Idea / Intuition

The birthday paradox tells us there's about a 50% chance of a collision among just 23 people — far fewer than the 183 one might naively expect. The expected number of interviews until the first collision captures the same phenomenon algebraically. At step $k$, the probability that the $k$-th person is *new* (no collision yet) is $\frac{365-(k-1)}{365}$, so we can compute the expected stopping time by summing the probability of "no collision in the first $k$ people" over all $k$.

The key trick is: $E[\text{stopping time}] = \sum_{k=0}^{\infty} P(\text{first } k \text{ people all have distinct birthdays})$, which is a standard tail-sum formula for expectations.

---

## Formal Proof / Solution

Let $N$ be the number of people interviewed until the first collision (including the person who causes the collision). We want $E[N]$.

**Tail-sum formula.** For any non-negative integer-valued random variable,
$$E[N] = \sum_{k=0}^{\infty} P(N > k).$$

Now $P(N > k)$ is the probability that the first $k$ people all have *distinct* birthdays (so no collision has happened yet after $k$ interviews):

$$P(N > k) = \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{365 - k + 1}{365} = \prod_{j=0}^{k-1} \frac{365 - j}{365}.$$

Setting $n = 365$ for brevity:

$$E[N] = \sum_{k=0}^{n} \prod_{j=0}^{k-1} \left(1 - \frac{j}{n}\right).$$

(The sum terminates at $k = n$ because after interviewing $n+1$ people a collision is guaranteed by pigeonhole.)

**Numerical value.** Computing this sum for $n = 365$:

$$E[N] \approx 24.6.$$

**Approximate closed form.** Since $\prod_{j=0}^{k-1}(1 - j/n) \approx e^{-k(k-1)/(2n)}$ for large $n$, we approximate the sum by an integral:

$$E[N] \approx \int_0^{\infty} e^{-k^2/(2n)} \, dk = \sqrt{\frac{\pi n}{2}}.$$

For $n = 365$:

$$\sqrt{\frac{\pi \cdot 365}{2}} \approx \sqrt{573} \approx 23.9.$$

**The surprise.** You only need to interview about $\sqrt{\pi n / 2} \approx 24$ people on average — roughly $\sqrt{n}$ rather than $n$. This is the birthday paradox in quantitative form: collisions happen shockingly early because the number of *pairs* grows as $k^2/2$, and a collision becomes likely once $k^2/2 \approx n$, i.e., $k \approx \sqrt{2n}$.

**Summary table:**

| Quantity | Value ($n=365$) |
|---|---|
| Naive guess | $183$ |
| Expected interviews to first collision | $\approx 24.6$ |
| Approximation $\sqrt{\pi n/2}$ | $\approx 23.9$ |

Written to: [questions/2026-06-17_pm.md](questions/2026-06-17_pm.md)
Answer: [questions/2026-06-17_pm_answer.md](questions/2026-06-17_pm_answer.md)
