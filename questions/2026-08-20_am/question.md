---
name: "Weighted Argument Principle: Summing Zeros and Poles"
type: "Complex Analysis"
tags: ["argument principle", "residue theorem", "zeros and poles", "contour integral", "meromorphic functions"]
date: "2026-08-20"
solved: false
comments: ""
related: []
redo: 0
difficulty: 2
source: "Mathematical folklore / classical complex analysis"
---
# The Argument Principle Counts, But Can It Tell You More?

Let $f$ be meromorphic on an open set containing the closed unit disk $\overline{\mathbb{D}}$, with no zeros or poles on the unit circle $|z|=1$. Define

$$N = \text{(number of zeros of } f \text{ in } \mathbb{D}\text{, counted with multiplicity)}$$
$$P = \text{(number of poles of } f \text{ in } \mathbb{D}\text{, counted with multiplicity)}$$

The **argument principle** tells you:

$$\frac{1}{2\pi i} \oint_{|z|=1} \frac{f'(z)}{f(z)}\,dz = N - P.$$

Now here is the question: what does the integral

$$\frac{1}{2\pi i} \oint_{|z|=1} z\,\frac{f'(z)}{f(z)}\,dz$$

compute? Express your answer in terms of the zeros $a_1, \ldots, a_N$ and poles $b_1, \ldots, b_P$ of $f$ inside $\mathbb{D}$.

*Bonus:* What does the integral

$$\frac{1}{2\pi i} \oint_{|z|=1} g(z)\,\frac{f'(z)}{f(z)}\,dz$$

compute for any function $g$ holomorphic on $\overline{\mathbb{D}}$?
