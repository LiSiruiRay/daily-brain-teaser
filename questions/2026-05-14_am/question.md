---
name: "Argument Principle: Zeros in an Annulus"
type: "Complex Analysis"
tags: ["argument principle", "Rouché's theorem", "winding number", "zeros of polynomials", "logarithmic derivative"]
date: "2026-05-14"
solved: false
comments: ""
related: []
redo: 0
difficulty: 3
source: "Complex Analysis, Stein & Shakarchi, Chapter 3"
---
# The Argument Principle: Counting Zeros by Winding

Let $f$ be a meromorphic function on a domain containing the closed disk $\overline{D}$, with no zeros or poles on the boundary circle $\gamma = \partial D$. Define the **logarithmic derivative integral**:

$$N - P = \frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)}\, dz,$$

where $N$ is the number of zeros of $f$ inside $D$ (counted with multiplicity) and $P$ is the number of poles (counted with multiplicity).

**Problem:** Use this principle to determine how many zeros the function

$$f(z) = z^4 - 5z + 1$$

has inside the annulus $1 < |z| < 2$.

*(Hint: Apply the argument principle on each boundary circle separately, using Rouché's theorem to count zeros on $|z|=1$ and $|z|=2$ separately.)*
