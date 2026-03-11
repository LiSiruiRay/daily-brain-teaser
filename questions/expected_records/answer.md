# Answer: Expected Number of Records

**Key Idea:** Linearity of expectation + symmetry
**Difficulty:** 2/5

---

## Step-by-Step Solution

### Step 1: Reframe using indicator variables

Instead of thinking about the total count directly, define:

$$X_k = \begin{cases} 1 & \text{if position } k \text{ is a record} \\ 0 & \text{otherwise} \end{cases}$$

Then the total number of records is:

$$X = X_1 + X_2 + \cdots + X_n$$

By **linearity of expectation**:

$$E[X] = E[X_1] + E[X_2] + \cdots + E[X_n] = \sum_{k=1}^n P(\text{position } k \text{ is a record})$$

This is the trick — we reduced the problem to computing one simple probability at each position.

---

### Step 2: Compute the probability at position k

Position $k$ is a record if $\sigma(k)$ is **larger than everything before it** — i.e., $\sigma(k)$ is the maximum of $\{\sigma(1), \sigma(2), \ldots, \sigma(k)\}$.

**Key symmetry argument:** Among the first $k$ elements, all $k!$ orderings are equally likely. So each of the $k$ elements is equally likely to be the largest.

Therefore:

$$P(\text{position } k \text{ is a record}) = \frac{1}{k}$$

- Position 1 is always a record (trivially the max of itself): $P = 1$
- Position 2 is a record if $\sigma(2) > \sigma(1)$: $P = 1/2$
- Position 3 is a record if $\sigma(3)$ is the max of the first 3: $P = 1/3$
- ... and so on.

---

### Step 3: Sum up

$$E[X] = \sum_{k=1}^n \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} = H_n$$

This is the **harmonic number** $H_n$.

---

## What does this mean concretely?

For $n = 52$ (a deck of cards), the expected number of records is $H_{52} \approx 4.5$.

As $n$ grows large, $H_n \approx \ln n$, so even in a permutation of a million elements, you only expect about $\ln(1{,}000{,}000) \approx 14$ records.

---

## Why linearity of expectation is so powerful here

The events "$X_1 = 1$", "$X_2 = 1$", etc. are **not independent** — whether position 3 is a record depends on positions 1 and 2. Normally this would make computing $E[X]$ complicated.

But linearity of expectation holds **regardless of independence**. You never need to worry about how the $X_k$'s interact — just compute each $E[X_k]$ on its own.
