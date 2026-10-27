---
name: "Exactly Twice Is Impossible"
type: "topology"
tags: ["connectedness", "intermediate value theorem", "compactness", "counting preimages", "folklore"]
date: "2026-10-27"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
---
# Exactly Twice Is Impossible

Prove that there is **no** continuous function $f:\mathbb{R}\to\mathbb{R}$ that takes every real value **exactly twice**. That is, there is no continuous $f$ with
$$
\#\{x\in\mathbb{R} : f(x)=y\} = 2 \quad\text{for every } y\in\mathbb{R}.
$$

*Bonus (think, don't prove):* Is there a continuous $f:\mathbb{R}\to\mathbb{R}$ taking every value exactly **three** times? What about exactly $n$ times?

---

**Field:** Topology / Real analysis (connectedness, Intermediate Value Theorem)

**Why it's interesting:** This is a folklore classic. "Every value exactly twice" sounds harmless, since a parabola nearly does it. But the condition cannot hold everywhere, and the obstruction is purely about the order and connectedness of $\mathbb{R}$. The answer also has a surprising parity twist: exactly $n$ times is possible if and only if $n$ is odd.

**Key technique:** Look at the maximum of $f$ between two points with the same value, then count preimages of values just below that maximum using the IVT.

**Difficulty:** 3/5
