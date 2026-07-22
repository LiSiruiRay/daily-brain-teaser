# Answer: Evening Sales: Poisson Parity via e^m + e^{-m}

## Key Idea / Intuition

The trick is to use two Taylor series simultaneously: $e^m$ and $e^{-m}$. Their **sum** cancels all odd-powered terms and doubles the even-powered terms, directly extracting the even-indexed probabilities of the Poisson distribution. The result $\frac{1+e^{-2m}}{2}$ is always strictly above $\frac{1}{2}$ because the correction term $e^{-2m}$ is always positive — zero is an even number and the Poisson distribution places a non-trivial mass there, biasing things ever so slightly toward even counts.

---

## Formal Proof / Solution

**Setup.** Let $X \sim \text{Poisson}(m)$. The probability of exactly $r$ cakes is:

$$P(X = r) = e^{-m} \frac{m^r}{r!}$$

We want:

$$P(\text{even}) = \sum_{k=0}^{\infty} P(X = 2k) = \sum_{k=0}^{\infty} e^{-m} \frac{m^{2k}}{(2k)!}$$

**The key trick: add two exponential series.**

Recall the Taylor expansions:

$$e^m = \sum_{r=0}^{\infty} \frac{m^r}{r!} = 1 + m + \frac{m^2}{2!} + \frac{m^3}{3!} + \cdots$$

$$e^{-m} = \sum_{r=0}^{\infty} \frac{(-m)^r}{r!} = 1 - m + \frac{m^2}{2!} - \frac{m^3}{3!} + \cdots$$

Adding them:

$$e^m + e^{-m} = 2\sum_{k=0}^{\infty} \frac{m^{2k}}{(2k)!}$$

because all **odd** powers cancel perfectly. Therefore:

$$\sum_{k=0}^{\infty} \frac{m^{2k}}{(2k)!} = \frac{e^m + e^{-m}}{2}$$

**Computing the probability:**

$$P(\text{even}) = e^{-m} \cdot \frac{e^m + e^{-m}}{2} = \frac{1 + e^{-2m}}{2}$$

**Why is this always $> \frac{1}{2}$?**

For any finite $m > 0$:

$$e^{-2m} > 0 \implies \frac{1 + e^{-2m}}{2} > \frac{1}{2}$$

The intuitive reason: zero is an even number, and $P(X=0) = e^{-m} > 0$ always. This extra weight on even counts (especially 0) tips the balance ever so slightly in favor of even outcomes. As $m \to \infty$, the bias vanishes and $P(\text{even}) \to \frac{1}{2}$, but it never actually reaches $\frac{1}{2}$.

**Answer to the first part:** $P(\text{even}) = \frac{1}{2}$ only in the limit $m \to \infty$. For any finite Poisson mean, it is strictly impossible — zero is always favored.

**Example check:** For $m = 20$ (as in Mosteller's original problem):

$$P(\text{even}) = \frac{1 + e^{-40}}{2} \approx \frac{1}{2} + 10^{-18}$$

Essentially $\frac{1}{2}$, but never exactly.
