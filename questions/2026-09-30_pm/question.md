---
name: "The Gambler's Ruin on a Circle"
type: "Probability"
tags: ["random walk", "gambler's ruin", "absorbing barrier", "geometric series", "recurrence"]
date: "2026-09-30"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Classic probability folklore / Gambler's Ruin"
---
# The Gambler's Ruin on a Circle

Seven players sit at a round table, numbered $1$ through $7$. Each round, a "token" held by player $k$ moves clockwise (to player $k+1 \bmod 7$) with probability $\tfrac{2}{3}$, and counter-clockwise (to player $k-1 \bmod 7$) with probability $\tfrac{1}{3}$.

The game ends when the token reaches player $7$ (the "winner") or player $1$ (the "loser"). The token starts at player $4$.

What is the probability the token reaches player $7$ before player $1$?
