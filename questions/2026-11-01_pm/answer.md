# Answer: The Cross-Validation That Peeked: Screening Before the Folds

## Key Idea / Intuition

Cross-validation is honest only if the held-out labels play **no role** in building the model that predicts them. In Procedure W, the screening step already looked at every label, including the ones later "held out." It chose features that happen to line up with those labels. So the held-out points are not fresh: their labels are partly encoded in the selected features themselves. With 5000 candidate features, there are always 100 that line up remarkably well by chance, and averaging over 100 such weak alignments produces a strong fake signal. Screening that never looks at the labels, such as screening by variance, is harmless.

---

## Formal Proof / Solution

### (a) True error is $1/2$

Since $X$ is independent of $Y$ and $P(Y=1)=1/2$, any classifier $g$ satisfies
$$P(g(X)\neq Y) = \mathbb E\big[P(Y\neq g(X)\mid X)\big] = \mathbb E[1/2] = 1/2 .$$
No method can beat a coin flip, so the Bayes error is $1/2$.

### (b) Procedure R is exactly unbiased

Fix a fold $F$ and a held-out index $i\in F$. In Procedure R, the prediction $\hat y_i$ is a deterministic function of:

- the training data $\{(x_k,y_k): k\notin F\}$, which drives both the screening and the 1-NN fit, and
- the held-out feature vector $x_i$.

By assumption, $y_i$ is independent of all of these. Write $Z$ for the collection of these inputs. Then
$$P(\hat y_i \neq y_i) = \mathbb E\big[P(y_i \neq \hat y_i(Z)\mid Z)\big] = \mathbb E[1/2] = \tfrac12 .$$
The CV estimate is the average of the indicators $\mathbf 1\{\hat y_i\neq y_i\}$ over all $i$. By linearity of expectation, its expectation is exactly $1/2$. $\blacksquare$

The argument uses nothing about 1-NN, the number of features, or the number of folds. It needs only one thing: the held-out label was never touched.

### (c) Why Procedure W reports a tiny error

**Where the logic breaks.** In W, the selected feature set $S$ depends on all of $y_1,\dots,y_{50}$. So the prediction $\hat y_i$ depends on $y_i$ through $S$, and the argument in (b) collapses.

**How big the effect is.** Under the null, the sample correlation $r_j$ of a feature with the labels is approximately $\mathcal N(0,1/N)$. Keeping the top 100 of 5000 means keeping the top $2\%$ in absolute value. That corresponds to $|z|\gtrsim 2.33$, so
$$|r_j| \gtrsim \frac{2.33}{\sqrt{50}} \approx 0.33 .$$
The average over the selected features is a bit larger. A typical value is $r_j^2\approx 0.13$.

**What this means for the data.** Let $\tilde y$ be the standardized label vector. For each selected feature, decompose the 50-vector $x_{\cdot j}$ as
$$x_{\cdot j} = r_j\,\tilde y + \text{residual}, \qquad \text{residual variance} \approx 1-r_j^2 .$$
This decomposition holds on all 50 coordinates, including the samples later held out, because the correlation was computed on all of them. Each selected coordinate therefore carries a shift of about $\pm r_j$ that depends on the class.

**Effect on nearest-neighbour distances.** In the 100-dimensional selected space:

- Same-class pairs have squared distance $\approx 2\cdot 100\,(1-\bar{r^2}) \approx 174$.
- Opposite-class pairs have an extra $\approx 4\sum_j r_j^2 \approx 52$, giving about $226$.
- The fluctuation of a squared distance is roughly $\sqrt{100\cdot 8(1-\bar{r^2})^2}\approx 25$.

So opposite-class points sit about two standard deviations farther away. Taking the minimum over about 20 candidates of each class makes the nearest neighbour usually same-class.

The result is a reported error of a few percent. Hastie–Tibshirani–Friedman's simulation of exactly this setup gives an average CV error of about $3\%$, while the truth is $50\%$.

**The moral.** Each selected feature is only a weak, chance alignment with the labels, about $0.33$ correlation. But the selection picked 100 of them out of 5000, and they all point at the same label vector. Summing 100 weak alignments yields a strong fake signal, and the fake signal includes the "test" points.

### (d) Variance screening is fine

Sample variances $\hat\sigma_j^2$ are functions of the features only. Let $Z_i$ denote everything used to produce $\hat y_i$: all 50 feature vectors (used for screening), plus the training labels. Then $y_i$ is still independent of $Z_i$, and the argument of (b) applies verbatim, giving expectation $1/2$.

**General rule:** unsupervised preprocessing (variance filters, PCA on $X$, standardization) may be done before CV. Any step that uses the labels must be repeated inside every fold.
