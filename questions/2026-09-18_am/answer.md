# Answer: Expected Fixed Points of a Random Permutation

## Key Idea / Intuition

Instead of thinking about each permutation as a whole, **swap the order of summation**: count, for each position $i$, how many permutations fix $i$. This linearity trick turns a complicated global count into $n$ identical easy counts. The surprise is that the expected number of fixed points is exactly $1$, regardless of $n$ — even as $n \to \infty$.

---

## Formal Proof / Solution

**Step 1: Swap the sum.**

$$\sum_{\sigma \in S_n} (\text{# fixed points of } \sigma) = \sum_{\sigma \in S_n} \sum_{i=1}^n \mathbf{1}[\sigma(i) = i] = \sum_{i=1}^n \sum_{\sigma \in S_n} \mathbf{1}[\sigma(i) = i].$$

**Step 2: Count permutations fixing a given $i$.**

For a fixed $i$, the number of $\sigma \in S_n$ with $\sigma(i) = i$ is $(n-1)!$, since the remaining $n-1$ elements can be arranged freely.

**Step 3: Compute the total.**

$$\sum_{\sigma \in S_n} (\text{# fixed points of } \sigma) = \sum_{i=1}^n (n-1)! = n \cdot (n-1)! = n!.$$

**Step 4: Expected value.**

Since there are $n!$ permutations total, the expected number of fixed points of a uniformly random permutation is:

$$\mathbb{E}[\text{# fixed points}] = \frac{n!}{n!} = \boxed{1}.$$

**Why is this beautiful?**

The same argument via **linearity of expectation** is even slicker: let $X_i = \mathbf{1}[\sigma(i) = i]$. Then $\mathbb{P}(X_i = 1) = \frac{(n-1)!}{n!} = \frac{1}{n}$, and

$$\mathbb{E}\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n \frac{1}{n} = 1.$$

The $X_i$ are **not independent** — if $\sigma$ fixes 1 and 2, it cannot fix $n$ if it must be a derangement of the rest — yet their **expectations add linearly anyway**, giving exactly 1 for all $n$. The answer is independent of $n$: whether you shuffle 3 cards or 3 million, on average exactly one card lands in its original position.

This is also the starting point for the derangement formula: the probability of **no** fixed points approaches $1/e \approx 0.368$ as $n \to \infty$, yet the mean never moves from 1.
