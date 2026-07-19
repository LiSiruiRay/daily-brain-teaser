# Answer: Curse of Dimensionality: Nearest Neighbor Becomes Global

## Key Idea / Intuition

In low dimensions, "nearby" means genuinely local. But in high dimensions, to find even a tiny fraction of your data, you must look almost everywhere in the cube — the neighborhood that captures 1% of the data has edge length close to 1. This is the geometric heart of the curse of dimensionality: local methods become global, losing their ability to exploit local structure. The EPE ratio of 2 arises because 1-NN has irreducible variance equal to $\sigma^2$ (from the label noise of the nearest neighbor itself), whereas OLS (under a correct linear model) has near-zero variance, so the 1-NN error is at least $\sigma^2_{\text{bias}} + \sigma^2 \geq \sigma^2$, giving a ratio $\geq 2$ against OLS's EPE $\approx \sigma^2$.

---

## Formal Proof / Solution

### Part 1: Edge Length Computation

To capture fraction $r$ of uniformly distributed points, the hypercubic neighborhood of edge length $\ell$ satisfies:

$$\ell^p = r \implies \ell = r^{1/p}$$

For $r = 0.01$:

| $p$ | $\ell = (0.01)^{1/p}$ | Interpretation |
|-----|----------------------|----------------|
| $p=1$ | $(0.01)^1 = 0.01$ | 1% of the unit interval — truly local |
| $p=2$ | $(0.01)^{1/2} = 0.1$ | 10% of each side — already a large square |
| $p=10$ | $(0.01)^{1/10} = 10^{-2/10} = 10^{-0.2} \approx 0.63$ | 63% of each side! |

As $p \to \infty$:
$$\ell = r^{1/p} = e^{\frac{\ln r}{p}} \to e^0 = 1$$

**No matter how small $r > 0$ is**, the required edge length $\to 1$ as $p \to \infty$.

### Part 2: Why 1-NN Becomes Global

A neighborhood capturing only 1% of the data already spans **63% of each coordinate axis** in $p=10$ dimensions. The "nearest neighbor" is no longer near — it could be almost anywhere in the cube. The implicit smoothness assumption ("nearby points have similar labels") completely breaks down. The method is forced to interpolate across the entire feature space, making it no more "local" than a global method.

### Part 3: EPE Ratio ≥ 2 Even at $p=1$

For the model $Y = f(X) + \varepsilon$ with $\varepsilon \sim (0, \sigma^2)$, the EPE of any predictor $\hat{f}(x_0)$ decomposes as:

$$\text{EPE} = \text{Bias}^2(\hat{f}(x_0)) + \text{Var}(\hat{f}(x_0)) + \sigma^2$$

**For OLS** (correct linear model): bias $= 0$, variance $\approx 0$ for large $n$, so:
$$\text{EPE}_{\text{OLS}} \approx \sigma^2$$

**For 1-NN**: The prediction is $\hat{f}(x_0) = Y_{(1)} = f(x_{(1)}) + \varepsilon_{(1)}$, where $x_{(1)}$ is the nearest training point. There are **two sources of noise**:

1. **Noise in the label**: $\varepsilon_{(1)} \sim (0, \sigma^2)$ — irreducible, contributes $+\sigma^2$
2. **Distance bias**: $f(x_{(1)}) \neq f(x_0)$ because $x_{(1)} \neq x_0$ — contributes additional error

Thus:
$$\text{EPE}_{\text{1-NN}} = \underbrace{\mathbb{E}[(f(x_{(1)}) - f(x_0))^2]}_{\geq 0} + \sigma^2 \geq \sigma^2$$

The ratio is:
$$\frac{\text{EPE}_{\text{1-NN}}}{\text{EPE}_{\text{OLS}}} \geq \frac{\sigma^2}{\sigma^2} = 1$$

But more precisely, even in $p=1$ with $n$ points uniform on $[0,1]$, the expected distance to the nearest neighbor is $\sim 1/(n+1)$, giving a nonzero bias term. For the **linear** $f(x) = x_1$, the distance contribution is small but positive, and the **variance alone** is already $\sigma^2$. Since 1-NN uses a single noisy observation (variance $= \sigma^2$) while OLS averages over $n$ points (variance $\to 0$), we get:

$$\frac{\text{EPE}_{\text{1-NN}}}{\text{EPE}_{\text{OLS}}} \approx \frac{0 + \sigma^2 + \sigma^2}{\sigma^2} = 2$$

The **key insight**: 1-NN's irreducible $\sigma^2$ variance (from the training label noise) is an extra cost OLS doesn't pay, because OLS borrows strength from **all** $n$ observations, while 1-NN only uses one.

As $p$ increases, the bias term $\mathbb{E}[(f(x_{(1)}) - f(x_0))^2]$ grows (nearest neighbor drifts away), so the ratio **exceeds 2 and keeps growing** — exactly as shown in Figure 2.9 of ESL.
