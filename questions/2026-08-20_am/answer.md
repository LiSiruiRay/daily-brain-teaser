# Answer: Weighted Argument Principle: Summing Zeros and Poles

## Key Idea / Intuition

The argument principle works because $\frac{f'}{f} = (\log f)'$, and $\log f$ has a simple pole of residue $+m$ at each zero of order $m$ and residue $-n$ at each pole of order $n$. Once you insert a weight $g(z)$ inside the integral, the residue theorem simply **evaluates $g$ at each zero and pole**—positive contribution from zeros, negative from poles. The result is a "weighted count" where the weight is the value of $g$ at each singularity.

---

## Formal Proof / Solution

**Step 1: Local structure of $\frac{f'}{f}$.**

Near a zero $a_k$ of order $m_k$, write $f(z) = (z - a_k)^{m_k} h(z)$ where $h$ is holomorphic and nonzero near $a_k$. Then:
$$\frac{f'(z)}{f(z)} = \frac{m_k}{z - a_k} + \frac{h'(z)}{h(z)}.$$
So $\frac{f'}{f}$ has a simple pole at $a_k$ with residue $+m_k$.

Near a pole $b_j$ of order $n_j$, write $f(z) = (z - b_j)^{-n_j} k(z)$ with $k$ holomorphic and nonzero. Then:
$$\frac{f'(z)}{f(z)} = \frac{-n_j}{z - b_j} + \frac{k'(z)}{k(z)}.$$
So $\frac{f'}{f}$ has a simple pole at $b_j$ with residue $-n_j$.

**Step 2: Compute the weighted integral.**

For $g$ holomorphic on $\overline{\mathbb{D}}$, the function $g(z)\frac{f'(z)}{f(z)}$ is meromorphic on $\overline{\mathbb{D}}$ with simple poles exactly at the zeros and poles of $f$ inside $\mathbb{D}$.

By the **residue theorem**:
$$\frac{1}{2\pi i} \oint_{|z|=1} g(z)\,\frac{f'(z)}{f(z)}\,dz = \sum_{\text{zeros } a_k} m_k \cdot g(a_k) - \sum_{\text{poles } b_j} n_j \cdot g(b_j).$$

**Step 3: Answer the specific question.**

Taking $g(z) = z$:

$$\boxed{\frac{1}{2\pi i} \oint_{|z|=1} z\,\frac{f'(z)}{f(z)}\,dz = \sum_{k=1}^{N} a_k - \sum_{j=1}^{P} b_j,}$$

where zeros and poles are listed with multiplicity.

**In words:** this integral computes the **sum of zeros minus the sum of poles** of $f$ inside $\mathbb{D}$.

**Step 4: The bonus result.**

For any $g$ holomorphic on $\overline{\mathbb{D}}$:
$$\frac{1}{2\pi i} \oint_{|z|=1} g(z)\,\frac{f'(z)}{f(z)}\,dz = \sum_{\text{zeros}} g(a_k) - \sum_{\text{poles}} g(b_j),$$
a beautiful **generalization of the argument principle**: ordinary argument principle uses $g \equiv 1$, the sum-of-zeros uses $g(z)=z$, and taking $g(z) = z^n$ one can reconstruct **all Newton power sums** of the zeros and poles — hence all elementary symmetric polynomials, hence even locate the zeros and poles (at least in principle) purely from contour integrals!

**Example sanity check.** Take $f(z) = z - a$ for $|a| < 1$. Then $\frac{f'}{f} = \frac{1}{z-a}$ and
$$\frac{1}{2\pi i}\oint_{|z|=1} z \cdot \frac{1}{z-a}\,dz = a. \checkmark$$
