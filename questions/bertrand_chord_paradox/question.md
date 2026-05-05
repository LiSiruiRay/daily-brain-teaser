---
name: "Bertrand's Chord Paradox"
type: "Probability"
tags: ["Geometric probability", "Measure", "Paradox", "Sample space"]
date: "2026-03-24"
solved: false
comments: ""
related: []
redo: 0
---
# Bertrand's Chord Paradox

## Problem

A chord of a unit circle is chosen **at random**. What is the probability that the chord is longer than the side of the inscribed equilateral triangle?

---

## Field
Probability / Foundations of Probability

## Why It's Beautiful

This is one of the most famous paradoxes in classical probability. The problem is perfectly well-posed geometrically, yet there are **three natural, defensible answers** — 1/2, 1/3, and 1/4. The paradox reveals that the phrase "chosen at random" is meaningless without specifying the underlying probability measure. This was a driving force behind the modern axiomatic foundations of probability (Kolmogorov, 1933).

It's not a trick question — all three answers are *correct* under their respective natural definitions of "random chord." The puzzle is recognizing that the question is subtly ill-posed.

## Key Idea / Trick

There is no canonical uniform distribution on the set of chords. Three natural parameterizations yield three different answers:

- **Method 1 (Random endpoints):** Pick two independent uniform points on the circle → P = **1/3**
- **Method 2 (Random midpoint):** Pick a uniform random point inside the disk as the chord's midpoint → P = **1/4**
- **Method 3 (Random radius + point):** Fix a radius, pick a uniform point on it as the midpoint of a perpendicular chord → P = **1/2**

Each method is "natural," yet they disagree. The lesson: specifying a probability space requires more than just symmetry.

## Difficulty
2 / 5

## Tags
Geometric probability, Measure theory, Paradox, Foundations of probability, Classical probability
