# Answer: Naive Bayes Independence Violation: Wrong Probabilities, Right Decisions

## Key Idea / Intuition

Naive Bayes corrupts the **magnitude** of the posterior probabilities because it double-counts correlated evidence — seeing "free" and "prize" together gets counted as two independent pieces of evidence when they really carry only one. But the decision boundary only cares about which side of the posterior ratio $\frac{P(Y=1 \mid x)}{P(Y=0 \mid x)}$ equals 1 — i.e., whether the log-odds is positive or negative. As long as the corruption pushes in the **same direction** for both classes, the sign of the log-odds is preserved, and the classification is correct.

---

## Formal Proof / Solution

### Part 1: Why Probability Estimates Are Wrong

The Naive Bayes posterior is

$$\hat{P}(Y=1 \mid x) = \frac{P(Y=1)\prod_j P(x_j \mid Y=1)}{P(Y=1)\prod_j P(x_j \mid Y=1) + P(Y=0)\prod_j P(x_j \mid Y=0)}.$$

When $X_1$ and $X_2$ are **positively correlated** given $Y=1$, the true joint satisfies

$$P(X_1=1, X_2=1 \mid Y=1) > P(X_1=1 \mid Y=1) \cdot P(X_2=1 \mid Y=1).$$

So the Naive Bayes model **underestimates** the true joint likelihood for spam. Similarly it underestimates for $Y=0$. The two underestimates do not cancel, so the resulting posterior $\hat{P}(Y=1 \mid x)$ is not calibrated — it can be systematically too extreme or too conservative.

### Part 2: Why the Decision Is Often Still Correct

The Naive Bayes classifier predicts $\hat{Y} = 1$ if and only if the **log-odds** is positive:

$$\log \frac{\hat{P}(Y=1 \mid x)}{\hat{P}(Y=0 \mid x)} = \log \frac{P(Y=1)}{P(Y=0)} + \sum_j \log \frac{P(x_j \mid Y=1)}{P(x_j \mid Y=0)} > 0.$$

Each term $\log \frac{P(x_j \mid Y=1)}{P(x_j \mid Y=0)}$ is individually a valid **signal** pointing in the right direction. The problem is that correlated features add **redundant** signals — but redundant signals that all point the same way only make the log-odds **more extreme**, not wrong in sign.

### Concrete Example

Using the numbers in the problem, the **true** likelihood ratio is

$$\frac{P(X_1=1, X_2=1 \mid Y=1)}{P(X_1=1, X_2=1 \mid Y=0)} = \frac{0.8}{0.05} = 16.$$

The **Naive Bayes** likelihood ratio is

$$\frac{\hat{P}(X_1=1 \mid Y=1)^2}{\hat{P}(X_1=1 \mid Y=0)^2} = \frac{0.64}{0.0025} = 256.$$

Both are much greater than 1. The naive version wildly over-inflates the ratio (because it double-counts), but the sign — and hence the decision — is still correct: classify as spam.

### Summary Table

| Quantity | True model | Naive Bayes |
|---|---|---|
| Likelihood ratio | 16 | 256 |
| Decision ($Y=1$?) | ✓ | ✓ |
| Probability estimate | Correct | Overconfident |

### The Punchline

Naive Bayes is a **bad density estimator** but can be a **good classifier**. The independence assumption inflates or deflates posterior probabilities, but as long as it inflates the correct class's score more than the wrong class's, the decision boundary is unchanged. This is why Naive Bayes famously works well in practice (e.g., spam filters) even when its independence assumption is obviously false — it is solving a simpler problem (sign of log-odds) than full probability calibration.

This insight is sometimes called the **"optimism of Naive Bayes"**: the model is overconfident but directionally correct.
