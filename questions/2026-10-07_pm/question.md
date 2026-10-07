---
name: "The Duelist's Dilemma: Who Wins When A Shoots First?"
type: "Probability"
tags: ["geometric series", "first-mover advantage", "duel", "probability", "classic"]
date: "2026-10-07"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Fifty Challenging Problems in Probability with Solutions, Frederick Mosteller, Problem 20"
---
# The Lazy Duelist: Optimal Shooting Distance

Two duelists, A and B, walk toward each other. At each step, each can choose to shoot. Duelist A hits with probability $p_A = 1/2$ if they shoot at the current moment, and duelist B hits with probability $p_B = 1/3$. They take turns stepping closer (A shoots first on each round, then B if A misses).

But here is the puzzle, stripped to its probabilistic core:

**A and B simultaneously decide (without knowing the other's choice) whether to shoot NOW or wait one more round. If they wait, both hit probabilities double (up to certainty). A shoots first. Should A shoot now or wait?**

Actually, let's pose the clean classic version:

---

**Problem (Mosteller, Problem 20 — The Duel):**

> Two men, $A$ and $B$, take turns shooting at each other. $A$ shoots first. At each turn, each man has probability $\frac{1}{2}$ of hitting the other. What is the probability that $A$ wins (i.e., hits $B$ before $B$ hits $A$)?

Now the **twist**: what if A is a *worse* shot — A hits with probability $p$ and B hits with probability $q$, with $p < q$? Surprisingly, there is a clean closed form. Find it, and determine: **for what values of $p$ is it better to go second** (i.e., $P(A \text{ wins}) < 1/2$)?
