# The Hat Check Problem (Derangements)

## Problem

At a party, $n$ people each check in their hat. The hats are returned in a completely random order. What is the probability that **no one receives their own hat**?

Find a closed form, and determine what happens as $n \to \infty$.

---

## Field
Probability / Combinatorics

## Why It's Beautiful

The answer converges to $1/e \approx 36.8\%$ incredibly fast — for $n \geq 5$ it's already within $0.3\%$ of $1/e$. So whether you have 5 people or 5 million, the probability is essentially the same. It's remarkable that a purely combinatorial counting problem produces $e$ so naturally.

The key technique — **inclusion-exclusion** — is one of the most versatile tools in combinatorics and probability, and this is its most elegant showcase.

## Key Idea / Trick

Let $A_i$ = event that person $i$ gets their own hat. You want $P(\text{none of } A_1, \dots, A_n)$.

By inclusion-exclusion:

$$P\!\left(\bigcup A_i\right) = \sum_k (-1)^{k+1} \binom{n}{k} \frac{(n-k)!}{n!} = \sum_{k=1}^n \frac{(-1)^{k+1}}{k!}$$

So $P(\text{derangement}) = 1 - \sum_{k=1}^n \frac{(-1)^{k+1}}{k!} = \sum_{k=0}^n \frac{(-1)^k}{k!} \to e^{-1}$.

## Difficulty
2 / 5

## Tags
Probability, Combinatorics, Inclusion-exclusion, Derangements, $e$, Permutations
