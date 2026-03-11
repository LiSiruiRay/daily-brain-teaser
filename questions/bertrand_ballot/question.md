# Bertrand's Ballot Problem

**Type:** Probability / Combinatorics
**Tags:** Ballot problem, Reflection principle, Counting paths, Combinatorics
**Date:** 2026-03-11
**Difficulty:** 3/5

**Why it's beautiful:**
The answer is shockingly clean — just $(a - b)/(a + b)$ — and the proof uses a gorgeous geometric trick called the **reflection principle**: you count "bad" paths by reflecting them into "good" paths, creating a perfect bijection.

---

## Problem

In an election, candidate A receives $a$ votes and candidate B receives $b$ votes, where $a > b$.

The $a + b$ ballots are counted one by one in a uniformly random order.

**What is the probability that A is strictly ahead of B throughout the entire counting process (i.e., at every point during the count, A has strictly more votes than B)?**

---

*Hint: Think about counting paths on a grid. Each vote for A is a step right (+1), each vote for B is a step left (-1). You want paths from 0 to $a - b$ that never touch 0 after the start.*
