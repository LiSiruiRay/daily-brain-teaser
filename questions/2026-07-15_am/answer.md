# Answer: The Pepys–Newton Problem

## Key Idea / Intuition

Each scenario has the same **expected number of sixes** (1, 2, and 3 respectively, since the expected number of sixes in $n$ dice is $n/6$). So at first glance, all three might seem equally likely. But expectation and probability are not the same thing! The key is that in each case, you need to *meet or exceed* the mean — and the probability of doing so depends on the **skewness and spread** of the binomial distribution. With fewer dice, the distribution is more spread and asymmetric, so the probability of hitting at least the mean is higher. As $n$ grows, the distribution becomes more symmetric and the probability of reaching the mean from below approaches $1/2$. So **(A) > (B) > (C)**.

---

## Formal Proof / Solution

Each scenario follows a **Binomial** distribution with success probability $p = 1/6$.

### Option (A): At least one 6 in 6 dice

$$P(A) = 1 - P(\text{no 6s in 6 dice}) = 1 - \left(\frac{5}{6}\right)^6$$

$$= 1 - \frac{5^6}{6^6} = 1 - \frac{15625}{46656} = \frac{31031}{46656} \approx \mathbf{0.6651}$$

### Option (B): At least two 6s in 12 dice

$$P(B) = 1 - P(0 \text{ sixes}) - P(1 \text{ six})$$

$$P(0) = \left(\frac{5}{6}\right)^{12} \approx 0.1122$$

$$P(1) = \binom{12}{1}\left(\frac{1}{6}\right)^1\left(\frac{5}{6}\right)^{11} = 12 \cdot \frac{1}{6} \cdot \left(\frac{5}{6}\right)^{11} \approx 12 \cdot \frac{1}{6} \cdot 0.1346 \approx 0.2692$$

$$P(B) = 1 - 0.1122 - 0.2692 \approx \mathbf{0.6187}$$

### Option (C): At least three 6s in 18 dice

$$P(C) = 1 - P(0) - P(1) - P(2)$$

$$P(0) = \left(\frac{5}{6}\right)^{18} \approx 0.0376$$

$$P(1) = \binom{18}{1}\frac{1}{6}\left(\frac{5}{6}\right)^{17} \approx 18 \cdot \frac{1}{6} \cdot 0.0451 \approx 0.1353$$

$$P(2) = \binom{18}{2}\frac{1}{36}\left(\frac{5}{6}\right)^{16} \approx 153 \cdot \frac{1}{36} \cdot 0.0541 \approx 0.2299$$

$$P(C) = 1 - 0.0376 - 0.1353 - 0.2299 \approx \mathbf{0.5973}$$

### Summary

| Option | Dice | Mean sixes | Probability |
|--------|------|-----------|-------------|
| A | 6 | 1 | ≈ 0.6651 |
| B | 12 | 2 | ≈ 0.6187 |
| C | 18 | 3 | ≈ 0.5973 |

**Option (A) wins**, despite all having the same expected number of sixes.

### Why does this happen?

The binomial distribution $\text{Bin}(n, 1/6)$ is **right-skewed** for small $n$: the median lies *below* the mean. As $n \to \infty$, by the CLT the distribution becomes symmetric and $P(\text{at least mean}) \to 1/2$. For small $n$, the probability of meeting the mean is significantly above $1/2$, and this effect is strongest for $n = 6$. Newton correctly identified (A) as the best bet.
