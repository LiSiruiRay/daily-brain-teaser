# Answer: The Absent-Minded Secretary

## Key Idea / Intuition

This is the classic **derangement** problem. The clever approach uses inclusion-exclusion: instead of counting directly, we subtract out all the "bad" permutations where at least one letter is correctly placed. The magical punchline is that the answer converges — rapidly and exactly — to $1/e$, no matter how large $n$ gets. The series truncates at a familiar friend.

---

## Formal Proof / Solution

**Setup.** Let $A_i$ be the event that letter $i$ goes into the correct envelope. We want:
$$P(\text{no letter correct}) = P\!\left(\bigcap_{i=1}^n A_i^c\right) = 1 - P\!\left(\bigcup_{i=1}^n A_i\right).$$

**Inclusion-Exclusion.** By inclusion-exclusion:
$$P\!\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^n (-1)^{k+1} \binom{n}{k} \frac{(n-k)!}{n!}.$$

The term $\binom{n}{k}(n-k)!/n!$ counts the probability that $k$ specific letters are all correct (the remaining $n-k$ are free): there are $(n-k)!$ completions out of $n!$ total.

This simplifies beautifully:
$$\binom{n}{k} \frac{(n-k)!}{n!} = \frac{n!}{k!\,(n-k)!} \cdot \frac{(n-k)!}{n!} = \frac{1}{k!}.$$

So:
$$P(\text{no letter correct}) = 1 - \sum_{k=1}^n \frac{(-1)^{k+1}}{k!} = \sum_{k=0}^n \frac{(-1)^k}{k!}.$$

**The Answer:**
$$D_n = \sum_{k=0}^n \frac{(-1)^k}{k!} = 1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!}.$$

**As $n \to \infty$:** Recall $e^{-1} = \sum_{k=0}^\infty \frac{(-1)^k}{k!}$, so:
$$D_n \to \frac{1}{e} \approx 0.3679.$$

**How fast?** The error $|D_n - e^{-1}|$ is less than $\frac{1}{(n+1)!}$, which is already tiny for $n = 3$ or $4$. In fact, the integer number of derangements $D_n \cdot n!$ equals the nearest integer to $n!/e$ for all $n \geq 1$.

**Sanity check for small $n$:**

| $n$ | Derangements | Probability |
|-----|-------------|-------------|
| 1   | 0           | 0           |
| 2   | 1           | 1/2         |
| 3   | 2           | 1/3         |
| 4   | 9           | 3/8         |

All converging quickly to $1/e \approx 0.368$.

**The beautiful surprise:** no matter how many letters there are, you always have roughly a $36.8\%$ chance that *nobody* gets their own letter back — a fact that astonishes people every time.
