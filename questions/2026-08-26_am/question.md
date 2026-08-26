---
name: "Gambler's Duration via Martingale"
type: "Probability"
tags: ["martingale", "optional stopping", "random walk", "gambler's ruin", "expected hitting time"]
date: "2026-08-26"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore / Mosteller-adjacent classic"
---
# The Drunkard's Last Dollar: Gambler's Ruin with a Twist

A gambler starts with $\$1$ and plays a sequence of fair coin flips. On each flip, he wins $\$1$ with probability $1/2$ and loses $\$1$ with probability $1/2$. He stops when he is **ruined** (reaches $\$0$) or when he reaches $\$n$.

Now consider a **different** question: instead of asking for the probability of reaching $\$n$ before ruin, ask for the **expected number of steps until the game ends** (either ruin or reaching $\$n$), starting from $\$k$.

Show that the expected duration is $k(n-k)$.

In particular, starting from $\$1$ with target $\$n$, the expected duration is $n-1$.
