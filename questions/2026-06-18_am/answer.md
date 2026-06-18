# Answer: Argument of a Product Along a Circle

## Key Idea / Intuition

The key insight is that $\frac{f'}{f}$ is the *logarithmic derivative* of $f$. If $f$ factors as $\prod_{k=1}^n (z - z_k)$, then $\log f$ splits into a sum of $\log(z - z_k)$ terms — so the logarithmic derivative splits into a sum of simple fractions $\frac{1}{z-z_k}$, each contributing a residue of $1$. The total winding of the argument of $f$ around the origin is exactly the sum of these contributions, giving $n$.

---

## Formal Proof / Solution

**Step 1: Factor $f$ and compute the logarithmic derivative.**

Since $f$ is a monic degree-$n$ polynomial, it factors over $\mathbb{C}$ as
$$f(z) = \prod_{k=1}^{n}(z - z_k),$$
where $z_1, \dots, z_n$ are the zeros (counted with multiplicity). By assumption all $z_k$ satisfy $|z_k| < R$.

Taking the logarithmic derivative:
$$\frac{f'(z)}{f(z)} = \frac{d}{dz}\log f(z) = \sum_{k=1}^{n} \frac{1}{z - z_k}.$$

This follows directly from the product rule:
$$f'(z) = \sum_{k=1}^n \prod_{j \neq k}(z - z_j) \implies \frac{f'(z)}{f(z)} = \sum_{k=1}^n \frac{1}{z-z_k}.$$

**Step 2: Compute the integral by residues.**

$$I = \frac{1}{2\pi i}\int_{|z|=R} \frac{f'(z)}{f(z)}\,dz = \frac{1}{2\pi i}\int_{|z|=R}\sum_{k=1}^n \frac{1}{z-z_k}\,dz.$$

Since integration is linear and each $z_k$ is inside $|z|=R$, by the residue theorem:
$$\frac{1}{2\pi i}\int_{|z|=R}\frac{1}{z-z_k}\,dz = 1 \quad \text{for each } k.$$

Therefore,
$$\boxed{I = \sum_{k=1}^n 1 = n.}$$

**Step 3: Interpret as winding of the argument.**

Write $f(z) = |f(z)|\,e^{i\arg f(z)}$ along the contour $z = Re^{i\theta}$, $\theta \in [0, 2\pi]$. Then
$$\frac{d}{d\theta}\log f(z(\theta)) = \frac{d}{d\theta}\log|f| + i\frac{d}{d\theta}\arg f.$$

On the other hand,
$$\int_{|z|=R}\frac{f'(z)}{f(z)}\,dz = \int_0^{2\pi}\frac{f'(z(\theta))}{f(z(\theta))}\cdot iRe^{i\theta}\,d\theta = \int_0^{2\pi}\frac{d}{d\theta}\log f(z(\theta))\,d\theta.$$

Since $|f(z)|$ returns to its original value after one full loop ($\theta: 0\to 2\pi$), the real part contributes $0$. Thus:
$$\int_0^{2\pi}\frac{d}{d\theta}\arg f(z(\theta))\,d\theta = \operatorname{Im}\!\left(\int_{|z|=R}\frac{f'}{f}\,dz\right) = \operatorname{Im}(2\pi i \cdot n) = 2\pi n.$$

So the total increase in $\arg f(z)$ as $z$ winds once counterclockwise around $|z|=R$ is exactly $2\pi n$ — the argument winds around $n$ full times, consistent with $f$ having $n$ zeros inside the circle.
