---
name: "Pointwise Limits and Meagre Discontinuity Sets"
type: "analysis"
tags: ["Baire category", "pointwise convergence", "oscillation", "Baire-1 functions", "meagre sets"]
date: "2026-07-06"
solved: false
comments: ""
related: []
redo: 0
difficulty: 4
source: "Classical real analysis folklore; see Rudin Real & Complex Analysis, Baire category applications"
---
# The Pointwise Limit of Continuous Functions Can Be Very Wild — But How Wild?

We know a pointwise limit of continuous functions need not be continuous. But here is a sharper question:

Let $f_n : [0,1] \to \mathbb{R}$ be a sequence of continuous functions converging **pointwise** to a function $f : [0,1] \to \mathbb{R}$.

**Prove that the set of discontinuities of $f$ is a meagre set (a countable union of nowhere-dense sets), i.e., a set of first Baire category.**

In particular, $f$ cannot be discontinuous *everywhere* — its continuity points are dense.

*Hint: Think about what pointwise convergence tells you about oscillation, and how to write the discontinuity set as a countable union.*
