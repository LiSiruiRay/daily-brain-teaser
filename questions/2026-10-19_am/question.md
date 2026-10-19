---
name: "The Universal Chord Theorem"
type: "analysis"
tags: ["intermediate value theorem", "telescoping", "counterexample", "continuity", "Lévy"]
date: "2026-10-19"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "P. Lévy (1934), Universal Chord Theorem (mathematical folklore)"
---
# The Universal Chord Theorem

Let $f:[0,1]\to\mathbb{R}$ be continuous with $f(0)=f(1)$. Call a **horizontal chord of length $a$** a pair of points $x$ and $x+a$ in $[0,1]$ with $f(x)=f(x+a)$.

**(a)** Prove that for every positive integer $n$, the graph of $f$ has a horizontal chord of length $\dfrac1n$.

**(b)** Prove the surprising converse. If $a\in(0,1)$ is **not** of the form $1/n$, then there exists a continuous $f$ with $f(0)=f(1)$ that has **no** horizontal chord of length $a$.

So the set of chord lengths guaranteed for *every* such $f$ is exactly $\{1, \tfrac12, \tfrac13, \dots\}$. For instance, length $\tfrac25$ is not guaranteed, even though length $\tfrac15$ is.

*Interpretation:* A hiker walks for one hour and ends at the same altitude where he started. Then for every $n$, there is a time window of exactly $60/n$ minutes during which his start and end altitudes agree. This guarantee holds for 30 or 20 minutes, but not for 40 minutes.

**Why it is interesting.** This is the Universal Chord Theorem of Paul Lévy (1934). It is a classic of real analysis because the positive part takes three lines while the negative part is genuinely surprising. Intuition suggests that if chords of length $1/5$ always exist, then chords of length $2/5$ should exist too. They do not. The counterexample is a single clean formula.

**Field:** Real analysis (continuity, Intermediate Value Theorem)

**Difficulty:** 2 / 5
