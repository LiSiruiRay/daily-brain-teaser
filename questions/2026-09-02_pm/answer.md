# Answer: The Three-Door Switcheroo: Generalized Monty Hall

## Key Idea / Intuition

The crucial insight: your original door was chosen before any information arrived, so it always holds the car with probability $1/n$. The host's action of opening goat-doors concentrates all the remaining $1 - 1/n = (n-1)/n$ probability among the other doors. When the host opens $k$ of those $n-1$ doors (guaranteed goats), the surviving $n-1-k$ doors share that $(n-1)/n$ mass equally. So switching is always better, and the advantage grows as the host opens more doors — in the extreme, if $k = n-2$, switching wins with probability $(n-1)/n$.

---

## Formal Proof / Solution

### Setup

Label the doors $1, \ldots, n$. The car is equally likely to be behind any door. You pick door 1. The host opens $k$ doors from $\{2, \ldots, n\}$, all goats. You may now stay or switch to one of the remaining $n-1-k$ doors in $\{2, \ldots, n\}$.

---

### Part 1: Probability of winning by staying

Your initial choice captures the car with probability

$$P(\text{win} \mid \text{stay}) = \frac{1}{n}.$$

The host's action reveals no information about whether *your* door has the car (he always opens only goat doors regardless), so this probability is unchanged.

---

### Part 2: Probability of winning by switching

The car is **not** behind your door with probability

$$P(\text{car is elsewhere}) = \frac{n-1}{n}.$$

Conditional on this event, the car is equally likely to be behind any one of the $n-1$ other doors. The host opens $k$ of these $n-1$ doors (all goats), leaving $n-1-k$ doors. By symmetry, the car is equally likely to be behind any of these $n-1-k$ surviving doors. So if you switch to one uniformly at random:

$$P(\text{win} \mid \text{switch}) = \frac{n-1}{n} \cdot \frac{1}{n-1-k} = \frac{n-1}{n(n-1-k)}.$$

---

### Part 3: Advantage of switching grows with $k$

Define the **switching advantage**:

$$\text{Advantage} = P(\text{win} \mid \text{switch}) - P(\text{win} \mid \text{stay}) = \frac{n-1}{n(n-1-k)} - \frac{1}{n}.$$

Simplifying:

$$= \frac{1}{n}\left(\frac{n-1}{n-1-k} - 1\right) = \frac{1}{n} \cdot \frac{k}{n-1-k}.$$

This is **strictly increasing in $k$**. As $k \to n-2$ (the maximum, leaving only 1 other door):

$$P(\text{win} \mid \text{switch}) \to \frac{n-1}{n}, \qquad \text{Advantage} \to \frac{n-1}{n} - \frac{1}{n} = \frac{n-2}{n}.$$

---

### Sanity Check: Classic Monty Hall

Set $n = 3$, $k = 1$:

$$P(\text{stay}) = \frac{1}{3}, \quad P(\text{switch}) = \frac{2}{3 \cdot 1} = \frac{2}{3}. \checkmark$$

---

### Summary Table

| $n$ | $k$ | $P(\text{stay})$ | $P(\text{switch})$ |
|-----|-----|------|---------|
| 3 | 1 | 1/3 | 2/3 |
| 4 | 1 | 1/4 | 3/8 |
| 4 | 2 | 1/4 | 3/4 |
| 100 | 98 | 1/100 | 99/100 |

The host is essentially a teacher: the more goats they eliminate, the louder they scream "the car is probably over there!"
