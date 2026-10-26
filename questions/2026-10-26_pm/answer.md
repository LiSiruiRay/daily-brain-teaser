# Answer: Olivier's Theorem: Decreasing Terms Are o(1/n)

## Key Idea / Intuition

If the terms decrease, then $a_n$ is the *smallest* of the terms $a_{n/2+1},\dots,a_n$. So the "block" of the last $n/2$ terms is at least $\tfrac n2 a_n$. Since the series converges, its tails are small (Cauchy criterion), so every such block tends to $0$. That forces $\tfrac n2 a_n \to 0$.

Monotonicity is what lets one term "speak for" a whole block. Without it, a sparse set of large spikes can hide inside a convergent series.

---

## Formal Proof / Solution

### (a)

**Step 1: the terms are non-negative.** Since $\sum a_n$ converges, $a_n \to 0$. A non-increasing sequence converging to $0$ satisfies $a_n \ge \lim_k a_k = 0$ for all $n$.

**Step 2: the block estimate.** Fix $n \ge 2$ and let $m = \lfloor n/2 \rfloor$. The block $a_{m+1}, \dots, a_n$ has $n - m \ge n/2$ terms. Since the sequence is non-increasing, each term is $\ge a_n \ge 0$. Hence
$$
0 \le \frac{n}{2}\, a_n \;\le\; (n-m)\,a_n \;\le\; \sum_{k=m+1}^{n} a_k .
$$

**Step 3: the Cauchy criterion.** Since $\sum a_k$ converges, for every $\varepsilon>0$ there is $N$ such that $\sum_{k=p+1}^{q} a_k < \varepsilon$ whenever $q > p \ge N$. Take $n \ge 2N+2$, so that $m = \lfloor n/2\rfloor \ge N$. Then
$$
0 \le \frac n2 a_n < \varepsilon .
$$
Therefore $n a_n < 2\varepsilon$ for all large $n$, which shows $n a_n \to 0$. $\blacksquare$

*(Equivalently, write $S_n$ for the partial sums and $S$ for the sum. Then $\tfrac n2 a_n \le S_n - S_{\lfloor n/2\rfloor} \to S - S = 0$.)*

### (b) Monotonicity is essential

Define
$$
a_n = \begin{cases} \dfrac{1}{n}, & n \text{ a perfect square},\\[2mm] \dfrac{1}{n^2}, & \text{otherwise}. \end{cases}
$$

- The terms are positive.
- The series converges: $\displaystyle \sum_n a_n \le \sum_{k\ge1} \frac{1}{k^2} + \sum_{n\ge1}\frac1{n^2} < \infty$, because the squares $n=k^2$ contribute $\sum_k 1/k^2$.
- Yet $n a_n = 1$ for every perfect square $n$, so $n a_n \not\to 0$.

The spikes are too sparse to affect convergence, but each one individually is as large as $1/n$.

### (c) The converse fails

Take $a_n = \dfrac{1}{n\ln n}$ for $n\ge 2$.

- The sequence is positive and decreasing.
- $n a_n = \dfrac{1}{\ln n} \to 0$.
- The series diverges. By the integral test, $\displaystyle\int_2^X \frac{dx}{x\ln x} = \ln\ln X - \ln\ln 2 \to \infty$. Alternatively, Cauchy condensation turns it into $\sum 2^k \cdot \frac{1}{2^k k\ln 2} = \frac{1}{\ln 2}\sum \frac1k = \infty$.

So $a_n = o(1/n)$ is necessary for convergence of a monotone series, but not sufficient.

### Remark

The block trick in (a) is exactly the "lower half" of Cauchy's condensation test. Grouping terms into dyadic blocks $[2^k, 2^{k+1})$ and bounding each block above and below by its endpoint terms gives
$$
\sum a_n < \infty \iff \sum 2^k a_{2^k} < \infty .
$$
Olivier's theorem is the observation that the dyadic terms $2^k a_{2^k}$ of a convergent series must tend to $0$.
