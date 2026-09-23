---
name: "The Collector Who Stops Too Early"
type: "Probability"
tags: ["stopping time", "symmetry", "exchangeability", "optional stopping", "uniform distribution"]
date: "2026-09-23"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore / probability puzzle classic"
---
# The Collector Who Stops Too Early

A deck of $n$ cards is shuffled uniformly at random. You flip cards one by one. At some point you decide to **stop** and you want the **last card you saw to be an Ace** (the card in position $n$ of the original deck is an Ace with probability $1/n$, but you don't know where the Ace is).

Here is a simpler version to focus on:

A box contains **3 red** and **1 green** ball. You draw balls one at a time **without replacement**, uniformly at random. You must **declare in advance** (before any draws) a position $k \in \{1,2,3,4\}$ at which to stop, and you win if the ball at position $k$ is green.

**Question:** Is there a stopping position $k$ that gives you a better than $1/4$ chance of winning? What if instead you are allowed to **peek at the previous balls** before deciding to stop (an adaptive strategy)?

More precisely: find an **adaptive stopping rule** (based on what you have seen) that gives you a **strictly better** chance of winning than any fixed $k$.

Or does no such adaptive rule exist?
