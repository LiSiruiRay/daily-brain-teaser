# Answer: The Kernel Trick: Why Inner Products Are All You Need

## Key Idea / Intuition

The kernel trick is the observation that many algorithms only need pairwise inner products between data points — never the feature vectors themselves. So if we can compute $\langle \phi(x), \phi(x') \rangle$ cheaply via a kernel function $k(x,x')$, we get the power of working in a huge (or infinite) feature space at the cost of working in the original space. The puzzle here is to make this concrete: expand the polynomial kernel by the binomial theorem and read off $\phi$ directly.

---

## Formal Proof / Solution

### Part (a): Explicit feature map for $k(x,x') = (1 + x \cdot x')^2$, $x \in \mathbb{R}^2$

Let $x = (x_1, x_2)$ and $x' = (x_1', x_2')$. Expand:

$$k(x, x') = (1 + x_1 x_1' + x_2 x_2')^2$$

Apply the multinomial theorem:

$$= 1 + x_1^2 (x_1')^2 + x_2^2 (x_2')^2 + 2 x_1 x_1' + 2 x_2 x_2' + 2 x_1 x_2 x_1' x_2'$$

This is exactly $\langle \phi(x), \phi(x') \rangle$ with:

$$\phi(x) = \bigl(1,\ x_1^2,\ x_2^2,\ \sqrt{2}\, x_1,\ \sqrt{2}\, x_2,\ \sqrt{2}\, x_1 x_2\bigr) \in \mathbb{R}^6$$

**Verification:**
$$\langle \phi(x), \phi(x') \rangle = 1 \cdot 1 + x_1^2 (x_1')^2 + x_2^2(x_2')^2 + 2x_1 x_1' + 2x_2 x_2' + 2 x_1 x_2 x_1' x_2' = k(x,x') \checkmark$$

---

### Part (b): Dimension of the feature space

For $k(x,x') = (1 + x \cdot x')^p$ on $\mathbb{R}^d$:

The feature map $\phi(x)$ consists of all monomials in the components of $x$ of degree $0, 1, 2, \ldots, p$, each with appropriate $\sqrt{\binom{p}{|\alpha|}\binom{|\alpha|}{\alpha}}$ coefficients.

The number of monomials $x_1^{\alpha_1} \cdots x_d^{\alpha_d}$ with $|\alpha| = k$ is $\binom{d+k-1}{k}$, so the total dimension is:

$$m = \sum_{k=0}^{p} \binom{d+k-1}{k} = \binom{d+p}{p}$$

For fixed $p$, this grows as $O(d^p)$; for fixed $d$, as $O(p^d)$.

**Concretely:**
- $d = 2, p = 2$: $m = \binom{4}{2} = 6$ ✓ (matches part (a))  
- $d = 100, p = 5$: $m = \binom{105}{5} \approx 9.6 \times 10^9$ — nearly 10 billion dimensions!

---

### Part (c): The punch line

- **Computing $k(x, x') = (1 + x \cdot x')^p$:** costs $O(d)$ — just a dot product and a power.
- **Computing $\langle \phi(x), \phi(x') \rangle$ explicitly:** costs $O(m) = O(d^p)$, which is astronomically larger.

The kernel trick lets you implicitly operate in an $m$-dimensional feature space while paying only $O(d)$ per inner product. 

More strikingly: for the **RBF (Gaussian) kernel** $k(x,x') = e^{-\|x-x'\|^2/(2\sigma^2)}$, the induced feature space is **infinite-dimensional** — yet you still evaluate $k$ in $O(d)$ time. You are effectively running a linear classifier in $\infty$-dimensional space at finite cost.

**The key insight:** Any algorithm (SVM, kernel regression, PCA, etc.) that only accesses data through inner products can be "kernelized" for free — the feature map $\phi$ need never be constructed explicitly. The computational bottleneck becomes the $n \times n$ kernel matrix, not the dimension of the feature space.
