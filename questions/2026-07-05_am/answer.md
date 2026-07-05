# Answer: Curse of Dimensionality: Nearest Neighbor Bias

## Key Idea / Intuition

In low dimensions, "local" truly means local — you can find nearby neighbors in a small region. But as dimension grows, the volume of a hypercube scales as $\ell^d$, so to contain any fixed fraction of points, you must reach out to a large neighborhood. The curse of dimensionality means that "nearest neighbors" are not really near at all, and local methods silently become global — introducing massive bias without anyone noticing.

---

## Formal Proof / Solution

### Setup

To capture a fraction $r$ of uniformly distributed points in $[0,1]^d$, we need a sub-cube with side length $\ell$ satisfying:

$$\ell^d = r \implies \ell = r^{1/d}.$$

This is because the volume of a $d$-dimensional sub-cube of side $\ell$ is $\ell^d$, and the fraction of uniform points it contains is exactly $\ell^d$.

### Computation

Set $r = 0.01$:

| Dimension $d$ | Required side length $\ell = (0.01)^{1/d}$ |
|:---:|:---:|
| $d = 1$ | $\ell = 0.01$ |
| $d = 2$ | $\ell = (0.01)^{1/2} = 0.10$ |
| $d = 10$ | $\ell = (0.01)^{1/10} = 10^{-2/10} \approx 0.63$ |

### What This Reveals

- In $d=1$: to capture 1% of the data, you only need to reach out $1\%$ of the way across the space. Truly local.

- In $d=2$: you must reach out $10\%$ of the way. Still manageable.

- In $d=10$: you must reach $63\%$ of the way across the entire input space just to find 1% of the data. Your "local" neighborhood is most of the space.

### Implication for Bias

The 1-NN classifier predicts using the label of the single nearest training point. Its bias comes from the fact that the nearest neighbor is not at the query point itself — it lies at some distance $\delta$ away. The prediction is:

$$\hat{f}(\mathbf{x}) = f(\mathbf{x}_{\text{NN}}) \approx f(\mathbf{x}) + \nabla f \cdot (\mathbf{x}_{\text{NN}} - \mathbf{x}) + \cdots$$

In low dimensions $\delta$ is small, so the bias is small. In high dimensions, the nearest neighbor can be far from the query point — even with a large dataset. The **bias of 1-NN does not vanish** as $d \to \infty$ for fixed $n$, because the neighbor is essentially drawn from across the whole space.

### The Paradox

This is subtle: we have $n$ training points, yet every one of them is far from the query. The data is not "sparse" in the sense of being few — it's sparse because high-dimensional volume is overwhelmingly concentrated away from any fixed point. Local neighborhoods must be global to contain anything.

**Summary punchline:** The formula $\ell = r^{1/d}$ makes the curse of dimensionality completely explicit and quantitative. With $d=10$ and $r=0.01$, you need $\ell \approx 0.63$ — more than half the input range — just to find 1% of your data.
