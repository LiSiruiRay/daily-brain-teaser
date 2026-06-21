# Answer: KDE Bandwidth Bias-Variance Tradeoff

## Key Idea / Intuition

KDE with bandwidth $h$ is essentially a local average of the data over a window of size $h$. A large window forces the estimate to look like a flattened version of the truth (high bias, low variance), while a tiny window uses almost no data per point (low bias, high variance). The optimal $h$ balances these two forces, and the optimal rate reveals a fundamental limit on how fast you can learn a density nonparametrically.

---

## Formal Proof / Solution

### Part (a): Bias Computation

The expected value of the estimator at $x$ is:

$$\mathbb{E}[\hat{f}_h(x)] = \frac{1}{h} \int K\!\left(\frac{x-t}{h}\right) f(t)\, dt$$

Substitute $u = (t - x)/h$, so $t = x + hu$, $dt = h\,du$:

$$\mathbb{E}[\hat{f}_h(x)] = \int K(u)\, f(x + hu)\, du$$

Now expand $f(x + hu)$ via Taylor series around $x$:

$$f(x + hu) = f(x) + hu f'(x) + \frac{h^2 u^2}{2} f''(x) + O(h^3)$$

Integrate term by term against $K(u)$:

$$\mathbb{E}[\hat{f}_h(x)] = f(x)\underbrace{\int K(u)\,du}_{=1} + h f'(x)\underbrace{\int u K(u)\,du}_{=0} + \frac{h^2}{2}f''(x)\underbrace{\int u^2 K(u)\,du}_{=\sigma_K^2} + O(h^3)$$

Therefore:

$$\boxed{\text{Bias}[\hat{f}_h(x)] = \mathbb{E}[\hat{f}_h(x)] - f(x) \approx \frac{h^2 \sigma_K^2}{2} f''(x)}$$

The bias is $O(h^2)$: wider bandwidth $\Rightarrow$ more smoothing $\Rightarrow$ larger bias.

---

### Part (b): Why Variance $\sim \frac{1}{nh}$?

The estimator $\hat{f}_h(x)$ is an average of $n$ i.i.d. terms $\frac{1}{h}K\!\left(\frac{x-X_i}{h}\right)$. By independence:

$$\text{Var}[\hat{f}_h(x)] = \frac{1}{n}\text{Var}\!\left[\frac{1}{h}K\!\left(\frac{x - X_1}{h}\right)\right]$$

The term $\frac{1}{h}K\!\left(\frac{x-X_1}{h}\right)$ has variance of order $\frac{1}{h^2} \cdot h = \frac{1}{h}$ (since the second moment of $\frac{1}{h}K((x-t)/h)$ scales as $\frac{1}{h}$ by a change of variables). Thus:

$$\text{Var}[\hat{f}_h(x)] \sim \frac{f(x)\|K\|_2^2}{nh}$$

**Intuition:** Each kernel window of width $h$ effectively uses only about $nh$ of the $n$ data points. Averaging $nh$ observations gives variance $\sim \frac{1}{nh}$.

Smaller $h$ $\Rightarrow$ fewer neighbors used $\Rightarrow$ higher variance. This is the direct opposite of the bias behavior.

---

### Part (c): Optimal Bandwidth and MSE Rate

The pointwise MSE decomposes as:

$$\text{MSE}[\hat{f}_h(x)] = \text{Bias}^2 + \text{Variance} \approx \underbrace{\frac{h^4 \sigma_K^4}{4}[f''(x)]^2}_{\sim h^4} + \underbrace{\frac{C}{nh}}_{\sim (nh)^{-1}}$$

Minimize over $h$ by differentiating:

$$\frac{d}{dh}\!\left[A h^4 + \frac{B}{nh}\right] = 4Ah^3 - \frac{B}{nh^2} = 0$$

$$\Rightarrow h^* \propto n^{-1/5}$$

Substituting back, the optimal MSE rate is:

$$\text{MSE}^* \sim n^{-4/5}$$

**Comparison with parametric rates:** In a parametric model, MSE decays as $n^{-1}$. KDE only achieves $n^{-4/5}$, which is strictly slower — this is the **price of not knowing** the functional form of $f$.

---

### The Punchline: The Bias–Variance Trade-off

You cannot take $h \to 0$ because:
- As $h \to 0$: bias $\to 0$ ✓ but variance $\to \infty$ ✗ (each point uses essentially no data).
- As $h \to \infty$: variance $\to 0$ ✓ but bias $\to \infty$ ✗ (you're estimating a flat function regardless of $f$).

The optimal $h^* \sim n^{-1/5}$ is a delicate balance. This trade-off is **universal** in nonparametric estimation: you pay a $n^{-4/5}$ rate rather than $n^{-1}$ because you must simultaneously reduce both bias and variance, and they pull in opposite directions.

This is the nonparametric analogue of bias–variance decomposition, and it is one of the most fundamental ideas in statistical learning theory.
