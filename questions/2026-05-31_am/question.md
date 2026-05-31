---
name: "Curse of Dimensionality: Shell Concentration"
type: "ML/Stats"
tags: ["curse of dimensionality", "high dimensions", "k-NN", "volume concentration", "statistical learning"]
date: "2026-05-31"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "The Elements of Statistical Learning, Hastie, Tibshirani, Friedman, 2nd ed., Chapter 2"
---
# The Curse of Dimensionality: Where Does the Data Hide?

You draw $n$ points uniformly at random from the $d$-dimensional unit hypercube $[0,1]^d$.

**Part (a):** Show that the expected distance from a query point to its nearest neighbor grows as $d \to \infty$ (for fixed $n$).

**Part (b) [The real puzzle]:** Consider instead the unit hypersphere in $\mathbb{R}^d$. Show that for large $d$, almost all of the volume of the ball $B^d(r) = \{x : \|x\| \le r\}$ is concentrated in a thin shell near the surface. Specifically, show:

$$\frac{\text{Vol}(B^d(1)) - \text{Vol}(B^d(1-\varepsilon))}{\text{Vol}(B^d(1))} \to 1 \quad \text{as } d \to \infty,$$

for any fixed $\varepsilon \in (0,1)$.

**Part (c) [Punchline]:** What does this imply about $k$-nearest neighbor classifiers in high dimensions?
