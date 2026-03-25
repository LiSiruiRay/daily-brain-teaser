# The Hat Check Problem — Answer

## Setup

A **derangement** is a permutation of $\{1, \dots, n\}$ with no fixed points. Let $D_n$ = number of derangements. We want $P_n = D_n / n!$.

---

## Solution via Inclusion-Exclusion

Let $A_i$ = "person $i$ gets their own hat." We want $P(\text{no } A_i \text{ occurs})$.

**Step 1.** For any set $S \subseteq \{1,\dots,n\}$ with $|S| = k$:
$$P\!\left(\bigcap_{i \in S} A_i\right) = \frac{(n-k)!}{n!}$$
since fixing $k$ people to their own hats leaves $(n-k)!$ arrangements for the rest.

$$P\!\left(\bigcap_{i \in S} A_i\right)$$ means the probability of $k$ people getting their own hats.

**Step 2.** By inclusion-exclusion:

The inclusion-exclusion principle expands $P(\bigcup A_i)$ as:
$$\sum_i P(A_i) - \sum_{i<j} P(A_i \cap A_j) + \sum_{i<j<k} P(A_i \cap A_j \cap A_k) - \cdots$$

Grouping by the size $k$ of the intersection: there are $\binom{n}{k}$ ways to choose which $k$ people all get their own hat, and from Step 1 each such event has probability $(n-k)!/n!$. So:

$$P\!\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^n (-1)^{k+1} \underbrace{\binom{n}{k}}_{\text{choose the }k\text{ people}} \cdot \underbrace{\frac{(n-k)!}{n!}}_{\text{prob all }k\text{ fixed}}$$

The $\binom{n}{k}$ and $(n-k)!/n!$ simplify neatly:
$$\binom{n}{k} \cdot \frac{(n-k)!}{n!} = \frac{n!}{k!\,(n-k)!} \cdot \frac{(n-k)!}{n!} = \frac{1}{k!}$$

So the sum collapses to:
$$P\!\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^n \frac{(-1)^{k+1}}{k!}$$

**Step 3.** The probability of a derangement is:
$$P_n = 1 - P\!\left(\bigcup A_i\right) = \sum_{k=0}^n \frac{(-1)^k}{k!}$$

This is the partial sum of the Taylor series for $e^x$ at $x = -1$:
$$P_n = \sum_{k=0}^n \frac{(-1)^k}{k!} \xrightarrow{n\to\infty} e^{-1}$$

---

## Closed Form for $D_n$

$$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!} = n! \left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!}\right)$$

Equivalently, $D_n = \lfloor n!/e + 1/2 \rfloor$ — the nearest integer to $n!/e$.

---

## Numerical Check

| $n$ | $P_n$ |
|-----|-------|
| 1 | 0 |
| 2 | 0.5 |
| 3 | 0.333... |
| 4 | 0.375 |
| 5 | 0.3667 |
| 10 | 0.36788... |
| $\infty$ | $1/e \approx 0.36788$ |

The convergence is shockingly fast — the alternating series error after $n$ terms is $\leq 1/(n+1)!$.

---

## Why This Gives $e$

The Taylor series $e^x = \sum_{k=0}^\infty x^k / k!$ evaluated at $x = -1$ gives exactly $e^{-1}$. The inclusion-exclusion formula naturally produces the partial sums of this series. The connection is not a coincidence: the Poisson distribution with parameter $\lambda = 1$ assigns probability $e^{-1} \cdot 1^k / k!$ to $k$ events — and a derangement corresponds to zero fixed points when fixed points are approximately Poisson(1).

---

## Bonus: Recursion

$D_n = (n-1)(D_{n-1} + D_{n-2})$ with $D_1 = 0$, $D_2 = 1$.

**Proof:** Person 1 goes to position $j \neq 1$ ($(n-1)$ choices). Either person $j$ goes to position 1 (giving a derangement of the remaining $n-2$, so $D_{n-2}$ ways), or person $j$ does not go to position 1 (equivalent to a derangement of $n-1$ objects, so $D_{n-1}$ ways).

# Related to Leetcode
This question appeared in the leetcode question [634.Find the Derangement-of-An-Array](https://leetcode.com/problems/find-the-derangement-of-an-array/description/)

See the solution here: [solution](https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/634.Find-the-Derangement-of-An-Array)