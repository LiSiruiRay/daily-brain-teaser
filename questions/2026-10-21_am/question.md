---
name: "The Cliff-Hanger"
type: "Probability"
tags: ["random walk", "first-step analysis", "self-similarity", "smallest fixed point", "strong Markov property"]
date: "2026-10-21"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mosteller, Fifty Challenging Problems in Probability with Solutions, Problem 35 (The Cliff-Hanger)"
---
# The Cliff-Hanger

A drunk man stands **one step** from the edge of a cliff. Each step is independent of all the others. With probability $p$ he steps **toward** the cliff, and with probability $q = 1-p$ he steps **away** from it. His position is an integer distance $k \ge 0$ from the edge, and he falls as soon as he reaches $k = 0$.

1. Take $p = \tfrac13$. What is the probability that he eventually falls off the cliff?
2. More generally, find the probability of falling as a function of $p$.

You can probably write down a quadratic equation that the answer must satisfy. That equation has **two** roots, and one of them is always $1$. The real content of the problem is to explain rigorously **which root is the correct one**.

---

**Field:** Probability (random walks, first-passage problems)

**Why it's interesting:** The man is twice as likely to walk away from the cliff as toward it. Even so, he falls with probability exactly $\tfrac12$. The solution uses a self-similarity trick that reduces an infinite-state problem to one quadratic equation. It then raises a subtle question that is easy to skip: the equation alone cannot tell you the answer. This "smallest fixed point" phenomenon shows up again in branching processes (extinction probabilities) and in Catalan-number generating functions.

**Difficulty:** 2 / 5

**Source:** Mosteller, *Fifty Challenging Problems in Probability with Solutions*, Problem 35 ("The Cliff-Hanger").
