---
name: "The Tournament Bracket Paradox"
type: "Putnam"
tags: ["probabilistic method", "combinatorics", "tournaments", "quadratic residues", "existence proof"]
date: "2026-07-10"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "putnam/2008s.pdf (probabilistic method flavor); Paley tournament construction is classical combinatorics folklore"
---
# The Tournament Bracket Paradox

In a round-robin tournament with $n$ players, each pair of players plays exactly once, and every game has a winner (no ties). Call a tournament **transitive** if the players can be ranked $1, 2, \ldots, n$ so that player $i$ beats player $j$ whenever $i < j$ (a "perfect ordering").

Show that for every $n \geq 3$, there exists a tournament on $n$ players that is **not** transitive, yet has the property that for every player $p$, there exists another player who beats $p$.

Actually, prove the stronger and more surprising fact:

> **For every $n \geq 3$, there exists a tournament on $n$ players such that for every subset $S$ of players with $|S| \leq n-1$, there is some player outside $S$ who beats every player in $S$.**

Wait — is this even possible? For $n = 3$: find a tournament on 3 players where for every single player $p$, some other player beats $p$. (That's easy: a 3-cycle.) Now for $n = 7$: prove that there exists a tournament on 7 players such that for every pair of players $\{p, q\}$, there is a third player who beats **both** $p$ and $q$.
