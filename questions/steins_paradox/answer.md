# Stein's Paradox — Answer

## Setup

Let $X \sim \mathcal{N}(\mu, I_d)$. Write the James–Stein estimator as:
$$\hat{\mu}_{JS} = X + g(X), \qquad g(X) = -\frac{d-2}{\|X\|^2}\, X$$

The risk of any estimator $X + g(X)$ expands as:
$$E\|X + g(X) - \mu\|^2 = E\|X - \mu\|^2 + 2E\langle X - \mu,\, g(X)\rangle + E\|g(X)\|^2$$
$$= d + 2E\langle X - \mu,\, g(X)\rangle + E\|g(X)\|^2 \tag{1}$$

---

## Stein's Identity

**Lemma (Stein, 1981).** If $X \sim \mathcal{N}(\mu, I_d)$ and $g: \mathbb{R}^d \to \mathbb{R}^d$ is weakly differentiable with $E\|\nabla \cdot g\| < \infty$, then:
$$E\langle X - \mu,\, g(X)\rangle = E[\nabla \cdot g(X)]$$

*Proof sketch for $d=1$:* Integration by parts on the Gaussian density $\phi(x) = e^{-(x-\mu)^2/2}/\sqrt{2\pi}$:
$$E[(X-\mu)g(X)] = \int (x-\mu)g(x)\phi(x)\,dx = \int g(x)(-\phi'(x))\,(-1)\,dx$$
Wait — since $\phi'(x) = -(x-\mu)\phi(x)$, we get $(x-\mu)\phi(x) = -\phi'(x)$. Integrate by parts:
$$\int g(x)(x-\mu)\phi(x)\,dx = -\int g(x)\phi'(x)\,dx = \int g'(x)\phi(x)\,dx = E[g'(X)]$$

---

## Computing the Cross-Term

For $g(X) = -\frac{d-2}{\|X\|^2} X$, compute the divergence:

$$\nabla \cdot g(X) = \nabla \cdot \left(-\frac{d-2}{\|X\|^2} X\right) = -(d-2)\, \nabla \cdot \frac{X}{\|X\|^2}$$

Using $\frac{\partial}{\partial x_i}\frac{x_i}{\|x\|^2} = \frac{\|x\|^2 - 2x_i^2}{\|x\|^4}$ and summing over $i$:

$$\nabla \cdot \frac{X}{\|X\|^2} = \frac{d\|X\|^2 - 2\|X\|^2}{\|X\|^4} = \frac{d-2}{\|X\|^2}$$

So by Stein's identity:
$$E\langle X-\mu,\, g(X)\rangle = E\left[-(d-2)\cdot\frac{d-2}{\|X\|^2}\right] = -(d-2)^2\, E\frac{1}{\|X\|^2}$$

---

## Computing the Squared Norm Term

$$\|g(X)\|^2 = \frac{(d-2)^2}{\|X\|^4}\|X\|^2 = \frac{(d-2)^2}{\|X\|^2}$$

---

## Putting It Together

Substituting into $(1)$:
$$E\|\hat{\mu}_{JS} - \mu\|^2 = d - 2(d-2)^2 E\frac{1}{\|X\|^2} + (d-2)^2 E\frac{1}{\|X\|^2}$$
$$= d - (d-2)^2\, E\frac{1}{\|X\|^2}$$

Since $\|X\|^2 > 0$ a.s., we have $E[1/\|X\|^2] > 0$. Therefore, **when $d \geq 3$**:

$$\boxed{E\|\hat{\mu}_{JS} - \mu\|^2 = d - (d-2)^2\, E\frac{1}{\|X\|^2} < d}$$

for **all** $\mu$. The MLE is inadmissible. $\blacksquare$

---

## Why $d = 1, 2$ Fails

For $d = 1, 2$: $(d-2)^2 = 0$ or $1$, but $d - (d-2)^2 E[1/\|X\|^2]$ can become negative (worse than MLE) for some $\mu$ when $d < 3$ — the identity doesn't yield a uniform improvement. In fact for $d = 1, 2$ the MLE is admissible.

The phase transition at $d = 3$ is sharp and still not fully "intuitively explained" — it's one of those results that is mathematically clear but conceptually mysterious.

---

## Connection to Ridge Regression

Ridge regression estimates $\hat{\beta} = (X^TX + \lambda I)^{-1}X^Ty$, which **shrinks coefficients toward zero**. This is exactly Stein shrinkage in disguise — ridge is justified not just as regularization against overfitting, but as a provably better estimator in the MSE sense when the number of parameters $\geq 3$.
