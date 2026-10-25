# Answer: Nearest Neighbor Is Never More Than Twice as Bad as Bayes

## Key Idea / Intuition

With infinite data, your nearest neighbor sits essentially on top of you. Its label is therefore an independent draw from the same coin $\eta(x)$ as your own label. So 1-NN errs exactly when two independent flips of the same biased coin disagree, which happens with probability $2\eta(1-\eta)$.

Bayes, by contrast, errs with probability $m = \min(\eta, 1-\eta)$. Since $2\eta(1-\eta) = 2m(1-m)$ lies between $m$ and $2m$, we get the pointwise bounds. The function $m \mapsto 2m(1-m)$ is concave, so Jensen's inequality averages the pointwise bound into the sharper global bound $2R^*(1-R^*)$.

---

## Formal Proof / Solution

### (a) The asymptotic error

Fix a query point $x$. Let $Y$ be its true label and $Y'$ the label of its nearest neighbor $X_{(1)}$.

Given the feature values, the labels are drawn independently:
- $Y \sim \text{Bernoulli}(\eta(x))$,
- $Y' \sim \text{Bernoulli}(\eta(X_{(1)}))$.

As $N \to \infty$, we have $X_{(1)} \to x$. By continuity, $\eta(X_{(1)}) \to \eta(x)$.

The classifier errs exactly when $Y \neq Y'$. So the conditional error converges to
$$P(Y \ne Y') = \eta(x)\,(1-\eta(x)) + (1-\eta(x))\,\eta(x) = 2\eta(x)(1-\eta(x)).$$

The conditional error is bounded by $1$, so dominated convergence lets us take expectations over $X$:
$$R_{NN} = \mathbb{E}\big[2\eta(X)(1-\eta(X))\big].$$

### (b) The Cover–Hart bounds

Let $m(x) = \min(\eta(x), 1-\eta(x)) \in [0, \tfrac12]$. By symmetry,
$$2\eta(1-\eta) = 2m(1-m).$$

**Lower bound.** Since $m \le \tfrac12$, we have $1-m \ge \tfrac12$. Hence
$$2m(1-m) \ge m.$$
Taking expectations gives $R_{NN} \ge \mathbb{E}[m] = R^*$.

This is also clear without calculation: no rule beats Bayes.

**Upper bound.** The function $\varphi(m) = 2m(1-m)$ is concave. By Jensen's inequality,
$$R_{NN} = \mathbb{E}[\varphi(m(X))] \le \varphi(\mathbb{E}[m(X)]) = 2R^*(1-R^*).$$

Finally, $2R^*(1-R^*) \le 2R^*$ is trivial.

**Remarks.**
- The pointwise bound alone, $2m(1-m) \le 2m$, already gives the factor 2.
- Jensen sharpens it to $2R^*(1-R^*)$. Equality holds when $m(X)$ is almost surely constant, for example when noise is uniform across feature space.
- When $R^* = 0$ (separable classes), 1-NN is asymptotically perfect.
- When $R^* = \tfrac12$ (pure noise), both rules have error $\tfrac12$.

### (c) $K$ classes

At a point $x$, let the posteriors be $p_1, \dots, p_K$. Let $k^*$ be the index of the largest posterior, and set $r = 1 - p_{k^*}$. Then $r$ is the Bayes error at $x$.

**The NN error at $x$.** By the same argument as in (a), the true label and the neighbor's label are independent draws from $(p_k)$. Hence
$$\text{err}_{NN}(x) = 1 - \sum_k p_k^2.$$

**Bounding the sum of squares.** The other $K-1$ probabilities sum to $r$. By Cauchy–Schwarz,
$$\sum_{k \ne k^*} p_k^2 \ge \frac{r^2}{K-1}.$$
Therefore
$$1 - \sum_k p_k^2 \;\le\; 1 - (1-r)^2 - \frac{r^2}{K-1} \;=\; 2r - \frac{K}{K-1}\,r^2 \;=:\; \psi(r).$$

**Averaging.** The function $\psi$ is concave in $r$, and $\mathbb{E}[r(X)] = R^*$. By Jensen,
$$R_{NN} \le \mathbb{E}[\psi(r(X))] \le \psi(R^*) = R^*\left(2 - \frac{K}{K-1}R^*\right).$$

For $K = 2$ this reduces exactly to $2R^*(1-R^*)$.

**Moral.** The whole proof rests on two observations. First, an asymptotic nearest neighbor is an independent copy of your own label. Second, the map from Bayes error to NN error is concave, so averaging over feature space can only help the bound.

**Caveat.** The result is asymptotic. In high dimensions, $X_{(1)} \to x$ happens extremely slowly (the curse of dimensionality), so finite-$N$ performance can be far worse than this bound suggests.
