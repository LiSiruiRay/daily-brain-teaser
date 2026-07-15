---
name: "The Shared Birthday Secretary"
type: "Probability"
tags: ["birthday paradox", "expected value", "tail sum", "coupon collector", "collision"]
date: "2026-07-15"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Fifty Challenging Problems in Probability with Solutions (Mosteller) — inspired by birthday-type problems; classical folklore"
---
# The Shared Birthday Secretary

There are $n$ people in a room. Each person independently and uniformly selects a birthday from $\{1, 2, \ldots, 365\}$. You interview them one by one, learning each person's birthday as you go.

**Question:** What is the expected number of people you must interview until you find the *first* person who shares a birthday with someone you've already interviewed (i.e., the first "collision")?

For concreteness, find a clean closed form in terms of $n = 365$ and compare to your intuition from the birthday paradox.
