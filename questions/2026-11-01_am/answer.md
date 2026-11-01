# Answer: The Bootstrap That Fools Itself: 1-NN on Pure Noise

## Key Idea / Intuition

A bootstrap sample is a noisy copy of the training set. About 63% of the original points reappear in it, and 37% are left out.

1-NN memorizes perfectly. When a point is in the bootstrap sample, the model finds the point itself at distance $0$ and predicts its label correctly, for free. Only the left-out points actually test the model, and on those it is a coin flip.

So the naive bootstrap reports an error of about $0.368 \times 0.5 \approx 0.18$, which is badly optimistic. The .632 correction blends in the training error, which is also $0$ for 1-NN. That blend is itself fooled, giving $0.316$.

The moral: these estimators are fooled exactly when the model overfits as hard as possible. This failure is what motivates Efron's .632+ correction.

---

## Formal Proof / Solution

### (a) The 0.632 probability

A single draw misses observation $i$ with probability $1 - \tfrac1N$. The $N$ draws are independent, so
$$
\Pr(i \notin \text{sample } b) = \left(1-\frac1N\right)^N \xrightarrow{N\to\infty} e^{-1} \approx 0.368.
$$
Hence
$$
\Pr(i \in \text{sample } b) \to 1 - e^{-1} \approx 0.632.
$$
Equivalently, a bootstrap sample contains only about $0.632N$ *distinct* points.

### (b) The naive bootstrap is badly optimistic

Fix a pair $(b, i)$ and split into two cases.

**Case 1: $i \in$ sample $b$.** The point $x_i$ is in the bootstrap training set at distance $0$ from itself. The $x$'s are distinct, so it is the unique nearest neighbor, and therefore $\hat f^{*b}(x_i) = y_i$. The loss is $0$.

**Case 2: $i \notin$ sample $b$.** The prediction $\hat f^{*b}(x_i)$ is the label of some other training point $j \neq i$. Labels are independent fair coins, so $y_j$ is independent of $y_i$. Therefore
$$
\Pr\big(\hat f^{*b}(x_i) \neq y_i\big) = \tfrac12.
$$

Combining the two cases:
$$
\mathbb E\big[\widehat{\mathrm{Err}}_{\text{boot}}\big]
= 0\cdot \Pr(i\in b) + \tfrac12 \Pr(i\notin b)
= \tfrac12\left(1-\tfrac1N\right)^N \;\longrightarrow\; \tfrac12 e^{-1} \approx 0.184.
$$

This is far below the true error of $0.5$. The cause is that the bootstrap "training" and "test" sets overlap by about 63%, exactly as in ordinary training error.

### (c) The .632 estimator is still fooled

**Leave-one-out bootstrap.** For each $i$ we use only the models with $i \notin b$. That is always Case 2 above, so each term has expected loss $1/2$:
$$
\widehat{\mathrm{Err}}^{(1)} \approx 0.5.
$$
This estimator is honest here. In general it is slightly *pessimistic*, because each model effectively trains on only about $0.632N$ distinct points.

**Training error.** 1-NN fit on the full data predicts each training point from itself, so
$$
\overline{\mathrm{err}} = 0.
$$

**The .632 blend.** The weights $0.368$ and $0.632$ are meant to pull the pessimistic $\widehat{\mathrm{Err}}^{(1)}$ toward the optimistic $\overline{\mathrm{err}}$. Here they give
$$
\widehat{\mathrm{Err}}^{(.632)} = 0.368\cdot 0 + 0.632\cdot 0.5 = 0.316 \neq 0.5.
$$

**Interpretation.** The .632 rule implicitly assumes a moderate amount of overfitting. When the model memorizes completely ($\overline{\mathrm{err}} = 0$ regardless of signal), the blend drags the estimate down by a factor of $0.632$.

**Remark: the .632+ repair.** Efron and Tibshirani measure overfitting explicitly. Let $\hat\gamma$ be the *no-information error rate*, the error when $x$ and $y$ are independent. Here $\hat\gamma = 0.5$. Define the relative overfitting rate
$$
\hat R = \frac{\widehat{\mathrm{Err}}^{(1)} - \overline{\mathrm{err}}}{\hat\gamma - \overline{\mathrm{err}}} = \frac{0.5 - 0}{0.5 - 0} = 1.
$$
The adaptive weight is then
$$
\hat w = \frac{0.632}{1 - 0.368\,\hat R} = 1.
$$
So the .632+ estimator puts all its weight on $\widehat{\mathrm{Err}}^{(1)}$. It returns $0.5$, which is correct.
