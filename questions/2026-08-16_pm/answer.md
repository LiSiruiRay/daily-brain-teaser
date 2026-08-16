# Answer: LDA Is Secretly Logistic Regression

## Key Idea / Intuition

The stunning fact is that when the class-conditional distributions are Gaussian with equal covariances, the posterior $P(y=1 \mid x)$ is **exactly a logistic sigmoid of a linear function of $x$** — the same functional form as logistic regression. So LDA is a *special case* of logistic regression in terms of the decision boundary shape. The difference lies in how the parameters are estimated: LDA uses a generative model (more assumptions, more parameters to estimate), while logistic regression fits the boundary directly (fewer assumptions, estimates only $\beta$). This tradeoff reveals a classical bias-variance story.

---

## Formal Proof / Solution

**Step 1: Apply Bayes' theorem.**

$$P(y=1 \mid x) = \frac{P(x \mid y=1)\, \pi_1}{P(x \mid y=1)\, \pi_1 + P(x \mid y=0)\, \pi_0}.$$

Dividing numerator and denominator by the numerator:

$$P(y=1 \mid x) = \frac{1}{1 + \dfrac{P(x \mid y=0)\, \pi_0}{P(x \mid y=1)\, \pi_1}} = \sigma\!\left(\log \frac{P(x \mid y=1)\, \pi_1}{P(x \mid y=0)\, \pi_0}\right).$$

**Step 2: Plug in the Gaussian densities.**

With $x \mid y=k \sim \mathcal{N}(\mu_k, \Sigma)$:

$$\log \frac{P(x \mid y=1)}{P(x \mid y=0)} = -\tfrac{1}{2}(x-\mu_1)^T\Sigma^{-1}(x-\mu_1) + \tfrac{1}{2}(x-\mu_0)^T\Sigma^{-1}(x-\mu_0).$$

Expanding (the $x^T \Sigma^{-1} x$ terms cancel because $\Sigma$ is **shared**):

$$= x^T \Sigma^{-1}(\mu_1 - \mu_0) - \tfrac{1}{2}(\mu_1^T\Sigma^{-1}\mu_1 - \mu_0^T\Sigma^{-1}\mu_0).$$

**Step 3: Collect into a linear form.**

Define:

$$\beta = \Sigma^{-1}(\mu_1 - \mu_0), \qquad \beta_0 = -\tfrac{1}{2}(\mu_1^T\Sigma^{-1}\mu_1 - \mu_0^T\Sigma^{-1}\mu_0) + \log\frac{\pi_1}{\pi_0}.$$

Then:

$$\boxed{P(y=1 \mid x) = \sigma(\beta_0 + \beta^T x).}$$

This is **exactly** the logistic regression form.

---

**Step 4: The punchline — what's different?**

| | Logistic Regression | LDA |
|---|---|---|
| Model | $P(y \mid x)$ directly | $P(x \mid y)$, then invert |
| Parameters estimated | $\beta \in \mathbb{R}^{p+1}$ | $\mu_0, \mu_1, \Sigma, \pi$ (many more) |
| Assumes Gaussian $x$? | No | Yes |
| Decision boundary | Linear in $x$ | Linear in $x$ (same form!) |

**Step 5: When does each win?**

- **LDA wins** when the Gaussian equal-covariance assumption is *actually true*: it uses the extra information from modeling $P(x \mid y)$, giving a lower-variance estimator of $\beta$. LDA is more **statistically efficient** in this regime.

- **Logistic regression wins** when the Gaussian assumption is wrong (e.g., binary features, skewed distributions): it makes no assumption on $P(x)$, so its estimates are not biased by a false generative model. It is more **robust**.

This is the canonical **efficiency vs. robustness** tradeoff in statistics: parametric generative models win when correct, semiparametric discriminative models win when the generative assumptions fail. ESL (Section 4.3) calls this the "Analysis of the Difference Between LDA and Logistic Regression."

---

**Bonus insight:** If instead the covariances differ ($\Sigma_0 \neq \Sigma_1$), the $x^T \Sigma^{-1} x$ terms do *not* cancel, and the posterior becomes **quadratic** in $x$ — this is Quadratic Discriminant Analysis (QDA), which gives curved decision boundaries.
