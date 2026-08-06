# Answer: Weierstrass Product Convergence and Logarithmic Derivative

## Key Idea / Intuition

The bare product $\prod(1 - z/n)$ diverges because $\sum 1/n$ diverges. The fix is to insert the **convergence-producing factor** $e^{z/n}$, which exactly cancels the linear divergence: $\log(1-z/n) + z/n = O(z^2/n^2)$, and $\sum 1/n^2$ converges. The logarithmic derivative then inherits a beautiful partial-fraction form — each zero at $n$ contributes a pole with residue $1$, and the $e^{z/n}$ factors contribute the compensating $+1/n$ terms.

---

## Formal Proof / Solution

### Step 1: Reduce convergence to a series estimate

Define the partial product
$$P_N(z) = \prod_{n=1}^{N}\left(1-\frac{z}{n}\right)e^{z/n}.$$

Taking logarithms (on a simply connected region avoiding the zeros),

$$\log P_N(z) = \sum_{n=1}^{N}\left[\log\!\left(1-\frac{z}{n}\right) + \frac{z}{n}\right].$$

We need to show this sum converges absolutely and uniformly on $|z| \leq R$.

### Step 2: Uniform bound on each term

Use the standard power series: for $|w| < 1$,

$$\log(1-w) + w = -\frac{w^2}{2} - \frac{w^3}{3} - \cdots = -\sum_{k=2}^{\infty}\frac{w^k}{k}.$$

So

$$\left|\log\!\left(1-\frac{z}{n}\right) + \frac{z}{n}\right| \leq \sum_{k=2}^{\infty}\frac{|z|^k}{k \cdot n^k} \leq \frac{|z|^2}{n^2} \cdot \frac{1}{1 - |z|/n},$$

valid when $|z| < n$, i.e., for $n > R$ when $|z| \leq R$.

For $n > 2R$ (say), $|z|/n < 1/2$, so $\frac{1}{1-|z|/n} \leq 2$, giving

$$\left|\log\!\left(1-\frac{z}{n}\right) + \frac{z}{n}\right| \leq \frac{2R^2}{n^2}.$$

### Step 3: Absolute and uniform convergence

Split the sum: handle finitely many terms $n = 1, \ldots, \lfloor 2R \rfloor$ individually (they give entire contributions on any compact set that avoids the integers), and for $n > 2R$:

$$\sum_{n > 2R}\left|\log\!\left(1-\frac{z}{n}\right) + \frac{z}{n}\right| \leq 2R^2 \sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2 R^2}{3} < \infty.$$

This bound is **uniform** in $|z| \leq R$, so the series converges uniformly and absolutely. Therefore

$$f(z) = \prod_{n=1}^{\infty}\left(1-\frac{z}{n}\right)e^{z/n}$$

converges uniformly on compact sets to an entire function.

### Step 4: The logarithmic derivative

On a compact set avoiding the integers, differentiate the convergent series term by term (justified by uniform convergence):

$$\frac{f'(z)}{f(z)} = \frac{d}{dz}\sum_{n=1}^{\infty}\left[\log\!\left(1-\frac{z}{n}\right)+\frac{z}{n}\right] = \sum_{n=1}^{\infty}\left[\frac{-1/n}{1-z/n}+\frac{1}{n}\right].$$

Simplify each term:

$$\frac{-1/n}{1 - z/n} = \frac{-1}{n - z} = \frac{1}{z - n},$$

so

$$\boxed{\frac{f'(z)}{f(z)} = \sum_{n=1}^{\infty}\left(\frac{1}{z-n} + \frac{1}{n}\right).}$$

**Interpretation:** Each zero at $z = n$ contributes a simple pole with residue $+1$ (as expected), and the $+1/n$ terms are exactly the "Weierstrass tails" needed to make the sum converge — a partial-fraction expansion that recognizes the digamma function $\psi(z) = -\gamma + \sum_{n=0}^\infty\left(\frac{1}{n+1} - \frac{1}{z+n}\right)$ in disguise.

### Summary of key insight

| Layer | Content |
|-------|---------|
| Divergence of bare product | $\sum 1/n = \infty$ |
| Fix | Insert $e^{z/n}$, so each log term becomes $O(1/n^2)$ |
| Convergence engine | $\sum 1/n^2 < \infty$ |
| Logarithmic derivative | Partial fractions with compensating $+1/n$ |
