---
name: "Furstenberg's Topological Proof of Infinitely Many Primes"
type: "topology"
tags: ["point-set topology", "arithmetic progressions", "clopen sets", "number theory", "proofs from THE BOOK"]
date: "2026-10-20"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Aigner & Ziegler, Proofs from THE BOOK, Ch. 1 (Sixth proof, Furstenberg 1955)"
---
# Furstenberg's Topological Proof of the Infinitude of Primes

For integers $a, b$ with $b \ge 1$, define the two-sided arithmetic progression
$$N_{a,b} = \{\, a + nb : n \in \mathbb{Z} \,\}.$$
Call a set $U \subseteq \mathbb{Z}$ **open** if $U = \varnothing$, or if for every $a \in U$ there is some $b \ge 1$ with $N_{a,b} \subseteq U$.

1. Show that this defines a topology on $\mathbb{Z}$.
2. Show that every nonempty open set is infinite, and that every $N_{a,b}$ is **closed** as well as open.
3. Using only (1) and (2) and the fact that every integer other than $\pm 1$ has a prime divisor, prove that **there are infinitely many primes**.

*Bonus thought:* Where exactly is "infinitely many" smuggled in? Which topological property of finite unions is used?
