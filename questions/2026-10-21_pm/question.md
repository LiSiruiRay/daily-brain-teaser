---
name: "Buffon's Needle and the Noodle Trick"
type: "Probability"
tags: ["geometric probability", "linearity of expectation", "Buffon's needle", "Barbier", "Cauchy functional equation", "pi"]
date: "2026-10-21"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mosteller, Fifty Challenging Problems in Probability with Solutions, Problem 53 (Buffon's Needle); noodle argument due to Barbier (1860)"
---
# Buffon's Needle and the Noodle Trick

A floor is ruled with parallel lines spaced $d$ apart. A needle of length $\ell \le d$ is dropped at random. "At random" means two things. The distance from the needle's midpoint to the nearest line is uniform. The needle's angle is uniform and independent of that distance.

**(a)** Show that the probability that the needle crosses a line is
$$P = \frac{2\ell}{\pi d}.$$

**(b)** Prove this without evaluating any integral. Use only linearity of expectation and one cleverly chosen shape.

**(c)** Suppose the needle is long, with $\ell > d$, or is bent into an arbitrary rigid wire ("noodle") of total length $L$. What is the expected number of crossings?

---

**Field:** Probability / Geometric probability

**Why it's interesting:** Buffon's needle (1777) is the founding problem of geometric probability, and $\pi$ appears from dropping sticks. The standard proof is a two-line double integral. Barbier's 1860 "noodle" argument goes further. It shows that the answer is essentially forced by linearity of expectation together with the fact that a circle always crosses the lines exactly twice. As a bonus, it shows that the shape of the noodle does not matter at all.

**Difficulty:** 2 / 5

**Source:** Mosteller, *Fifty Challenging Problems in Probability*, Problem 53 ("Buffon's Needle"), with related Problems 54–55. The noodle proof is due to J.-É. Barbier (1860).
