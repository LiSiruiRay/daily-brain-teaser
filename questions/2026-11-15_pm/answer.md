# Answer: Logistic Regression Secretly Balances Its Books

## Key Idea / Intuition

The logit is the **canonical link** of the Bernoulli family. With this link, the derivative of the log-likelihood with respect to the linear predictor is just the raw residual $y_i - p_i$.

Setting the gradient to zero therefore says the residuals are **orthogonal to every feature column**, exactly as in ordinary least squares. The intercept is a column of all ones, so the residuals sum to zero. An indicator column makes them sum to zero within each group.

Put differently, logistic regression is a moment-matching (maximum-entropy) fit: the model's expected sufficient statistics $X^T\hat p$ equal the observed ones $X^T y$. Other links, such as probit, insert non-constant weights into the score, so this exact balance is lost.

---

## Formal Proof / Solution

**Setup.** Absorb the intercept by prepending a $1$ to each $x_i$, write $\eta_i = x_i^T\beta$, and let $X$ be the $N\times(p+1)$ design matrix whose first column is $\mathbf 1$.

The log-likelihood is
$$
\ell(\beta) = \sum_{i=1}^N \big[y_i\log p_i + (1-y_i)\log(1-p_i)\big]
= \sum_{i=1}^N \big[y_i\eta_i - \log(1+e^{\eta_i})\big].
$$

**The score.** Since $\frac{d}{d\eta}\log(1+e^\eta) = \sigma(\eta) = p$,
$$
\frac{\partial \ell}{\partial \eta_i} = y_i - p_i
\quad\Longrightarrow\quad
\nabla_\beta \ell = \sum_{i=1}^N x_i\,(y_i - p_i) = X^T(y - p).
$$

The function $\ell$ is concave, so the MLE is characterized by the score equations
$$
X^T(y - \hat p) = 0 .
$$
These are equation (4.24) in ESL.

**(a)** The first column of $X$ is $\mathbf 1$, so the first score equation reads
$$
\mathbf 1^T(y-\hat p) = 0 \iff \sum_i \hat p_i = \sum_i y_i.
$$

**(b)** The column for the indicator $x_{\cdot 1}$ gives
$$
\sum_i x_{i1}(y_i - \hat p_i) = 0 \iff \sum_{i:\,\text{female}} \hat p_i = \sum_{i:\,\text{female}} y_i .
$$
Dividing by the number of women gives the claim for women. Subtracting this equation from the one in (a) gives the same identity for the men.

Note that this is **calibration within the groups defined by the features**. It is not calibration in bins of predicted probability. A model can satisfy every one of these identities and still be miscalibrated among, say, patients with $\hat p\in[0.8,0.9]$.

**(c) Probit.** With $p_i = \Phi(\eta_i)$,
$$
\frac{\partial \ell}{\partial \eta_i}
= y_i\frac{\phi(\eta_i)}{\Phi(\eta_i)} - (1-y_i)\frac{\phi(\eta_i)}{1-\Phi(\eta_i)}
= w_i\,(y_i - p_i),
\qquad
w_i = \frac{\phi(\eta_i)}{\Phi(\eta_i)\big(1-\Phi(\eta_i)\big)}.
$$

The score equations become
$$
X^T W (y - \hat p) = 0, \qquad W = \operatorname{diag}(w_i).
$$
The intercept equation now gives only a **weighted** balance, $\sum_i w_i(y_i - \hat p_i) = 0$.

The weight $w(\eta)$ is not constant: it is smallest at $\eta=0$ and grows with $|\eta|$. So $\sum_i(y_i - \hat p_i)=0$ holds only by coincidence. It does hold when the model is saturated, for example with intercept only, or a single binary feature, where $\hat p$ equals the group proportions. With a continuous predictor it generically fails. You can check this numerically, for instance in R with `glm(..., family = binomial(link = "probit"))` and comparing `mean(fitted)` to `mean(y)`.

**What is special about the logit.** For an exponential family $f(y)\propto \exp(y\theta - b(\theta))$ with mean $\mu = b'(\theta)$, the score with respect to $\theta$ is $y - \mu$. If the linear predictor *is* the natural parameter ($\eta=\theta$, the canonical link), the score is $X^T(y-\mu)$ with no weights. For Bernoulli, $\theta = \log\frac{p}{1-p}$ is exactly the logit.

The same phenomenon appears elsewhere:
- **OLS** (Gaussian, identity link): residuals sum to zero when an intercept is included.
- **Poisson regression** with log link: $\sum_i \hat\mu_i = \sum_i y_i$.

**(d) Lasso.** The penalized optimality (KKT) conditions are
$$
\mathbf 1^T(y-\hat p) = 0 \quad(\text{intercept, unpenalized}),
\qquad
x_j^T(y-\hat p) = \lambda\,\operatorname{sign}(\hat\beta_j)\ \ \text{if } \hat\beta_j\ne 0,
\qquad
|x_j^T(y-\hat p)|\le\lambda\ \ \text{if } \hat\beta_j=0 .
$$
These are ESL equation (4.32).

- Identity (a) **survives**, because the intercept is unpenalized.
- The group identity in (b) is **broken**. The residual correlation with the indicator is $\pm\lambda$ if the indicator is active, and at most $\lambda$ in absolute value if not. Shrinkage deliberately under-fits the gap between the groups.

Ridge behaves the same way: there $x_j^T(y-\hat p) = \lambda\hat\beta_j$.
