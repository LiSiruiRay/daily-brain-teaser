# Answer: The Calibration Trap: Perfect Accuracy vs Probability Estimation

## Key Idea / Intuition

Classification accuracy and probability calibration are **fundamentally different objectives**. A classifier only needs to get the *ordering* right — it must put $P(Y=1|X) > 0.5$ for positive examples and $< 0.5$ for negative ones. Any monotone transformation of the true posterior preserves classification accuracy, but wildly distorts probability estimates. Naive Bayes specifically **double-counts correlated evidence**, inflating its confidence far beyond what is warranted.

---

## Formal Proof / Solution

### Step 1: Accuracy vs. Calibration Are Different Things

A binary classifier is **perfectly accurate** if, for every input $x$:

$$\hat{y}(x) = \mathbf{1}[\hat{p}(Y=1|x) > 0.5] = y_{\text{true}}$$

This only requires the **sign** of $\hat{p} - 0.5$ to be correct. The actual value of $\hat{p}$ is irrelevant to accuracy.

A classifier is **calibrated** if, among all inputs where the model outputs score $s$:

$$P(Y=1 \mid \hat{p}(Y=1|X) = s) = s$$

These are independent properties. A perfectly accurate classifier can be completely miscalibrated.

### Step 2: The Concrete Sanity Check

Suppose the true posterior is $P(Y=1|X) = 0.6$ for some input $x$.

- The true label is 1 (since $0.6 > 0.5$).
- A classifier outputting score $\hat{p} = 0.99$ for this input is still **perfectly accurate** — it correctly predicts class 1.
- But the probability estimate $0.99$ is wildly wrong: the true chance is only $60\%$.

So yes, a perfectly accurate classifier can output $0.99$ when the truth is $0.6$. **No contradiction with accuracy; total failure of calibration.**

### Step 3: Why Naive Bayes Specifically Overcounts

Naive Bayes assumes conditional independence of features given the class:

$$\hat{P}(Y=1 \mid X_1, X_2) \propto P(Y=1) \cdot P(X_1|Y=1) \cdot P(X_2|Y=1)$$

When $X_1$ and $X_2$ are strongly correlated (say, $\rho = 0.95$), knowing $X_1$ already tells you almost everything about $X_2$. But naive Bayes multiplies both likelihoods as if they were **independent pieces of evidence**.

This is equivalent to counting the same evidence twice (or nearly twice). The log-odds get inflated:

$$\log \frac{\hat{P}(Y=1|X)}{\hat{P}(Y=0|X)} = \log \frac{P(Y=1)}{P(Y=0)} + \log \frac{P(X_1|Y=1)}{P(X_1|Y=0)} + \log \frac{P(X_2|Y=1)}{P(X_2|Y=0)}$$

Each term pushes in the same direction (since $X_1, X_2$ are correlated), so the sum is roughly **twice** what it should be. The resulting posterior gets pushed toward 0 or 1 much more aggressively than the truth warrants.

**Example:** Suppose the true log-odds should be $\log(3) \approx 1.1$ (corresponding to $P = 0.75$). Naive Bayes with two correlated features might produce log-odds $\approx 2.2$, giving $\hat{P} \approx 0.90$. Classification is still correct ($> 0.5$), but the probability is inflated.

### Step 4: The General Principle

| Property | What It Requires |
|---|---|
| Perfect accuracy | Correct sign of $(\hat{p} - 0.5)$ |
| Calibration | $\hat{p}$ equals true conditional probability |

Any strictly **monotone transformation** $f: [0,1] \to [0,1]$ with $f(p) > 0.5 \iff p > 0.5$ preserves accuracy while destroying calibration. This is why:

- **Naive Bayes** is often a strong classifier but a poor probability estimator (overconfident).
- **SVMs** with hinge loss optimize a margin, not likelihood — their scores need Platt scaling to become probabilities.
- **Boosting** also tends to produce overconfident scores.

The fix is **calibration post-processing**: Platt scaling (logistic regression on scores), isotonic regression, or temperature scaling — all of which adjust the scores to match empirical frequencies without changing the ranking.

### Summary

$$\text{Accuracy} \iff \text{correct ordering} \quad \not\!\!\!\!\implies \quad \text{calibration}$$

Naive Bayes violates calibration by treating correlated features as independent, double-counting evidence and systematically pushing posteriors toward 0 and 1. A score of 0.99 from a naive Bayes model might correspond to a true probability of 0.6 — and the model is still "perfectly accurate."
