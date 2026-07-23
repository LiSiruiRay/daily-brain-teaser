# Answer: Infinite Product Telescoping to 2

## Key Idea / Intuition

Each factor $\frac{n^2}{n^2-1}$ splits as $\frac{n}{n-1} \cdot \frac{n}{n+1}$. When you write out the partial product, two separate telescoping products emerge — one marching upward, one marching downward — and their product collapses beautifully to $2$. No $\pi$ is needed in the end; the answer is a clean integer!

(The title was a small misdirection: $\pi$ appears in Wallis's product $\frac{\pi}{2} = \prod \frac{(2n)(2n)}{(2n-1)(2n+1)}$, which superficially resembles this, but here the answer turns out to be $2$.)

---

## Formal Proof / Solution

**Step 1: Factor each term.**

$$\frac{n^2}{n^2-1} = \frac{n^2}{(n-1)(n+1)} = \frac{n}{n-1} \cdot \frac{n}{n+1}.$$

**Step 2: Write the partial product.**

$$P_N = \prod_{n=2}^{N} \frac{n}{n-1} \cdot \prod_{n=2}^{N} \frac{n}{n+1}.$$

**Telescoping the first product:**

$$\prod_{n=2}^{N} \frac{n}{n-1} = \frac{2}{1}\cdot\frac{3}{2}\cdot\frac{4}{3}\cdots\frac{N}{N-1} = N.$$

**Telescoping the second product:**

$$\prod_{n=2}^{N} \frac{n}{n+1} = \frac{2}{3}\cdot\frac{3}{4}\cdot\frac{4}{5}\cdots\frac{N}{N+1} = \frac{2}{N+1}.$$

**Step 3: Combine.**

$$P_N = N \cdot \frac{2}{N+1} = \frac{2N}{N+1}.$$

**Step 4: Take the limit.**

$$P = \lim_{N\to\infty} \frac{2N}{N+1} = \boxed{2}.$$

**Sanity check:** Each factor $\frac{n^2}{n^2-1} > 1$, so the product should exceed $1$ — check. The factors approach $1$ fast enough (like $1 + 1/n^2$) for convergence — check. And indeed the closed form $2$ is surprisingly clean.

**Conceptual remark:** This is the "harmonic telescope" trick in its purest form. The same splitting idea — writing a ratio as a product of two ratios that telescope in opposite directions — reappears in partial fractions, in evaluating $\sum 1/n(n+1)$, and in verifying Wallis's product. Recognizing when a product or sum has a hidden telescoping structure is one of the most versatile tools in elementary analysis.
