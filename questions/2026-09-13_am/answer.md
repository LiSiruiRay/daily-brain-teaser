# Answer: Naive Bayes Beats Its Own Assumptions

## Key Idea / Intuition

Naive Bayes makes a decision by comparing $P(\text{spam}|x)$ vs $P(\text{not-spam}|x)$, which is equivalent to asking whether the **log-odds ratio** crosses zero. Even if each individual probability is wildly wrong due to the false independence assumption, the log-odds ratio only needs to have the **correct sign** to make the correct classification. The threshold is zero, not the actual probability value — so calibration errors can cancel out or simply not affect the sign of the decision.

---

## Formal Proof / Solution

**Setup.** Let $Y \in \{0,1\}$ and features $X = (X_1, \ldots, X_p)$. Naive Bayes predicts class 1 if:

$$\log \frac{P_{\text{NB}}(Y=1 \mid X)}{P_{\text{NB}}(Y=0 \mid X)} > 0$$

Under the independence assumption, this becomes:

$$\log \frac{\pi_1}{\pi_0} + \sum_{j=1}^{p} \log \frac{P(X_j \mid Y=1)}{P(X_j \mid Y=0)} > 0$$

where $\pi_k = P(Y=k)$.

**The wrong model, the right boundary.** Even if the true joint is

$$P(X_1, \ldots, X_p \mid Y=k) \neq \prod_j P(X_j \mid Y=k)$$

the **predicted probabilities** $P_{\text{NB}}(Y=1|x)$ are miscalibrated. However, the decision boundary is:

$$\hat{Y} = \mathbf{1}\!\left[\log P_{\text{NB}}(Y=1 \mid x) - \log P_{\text{NB}}(Y=0 \mid x) > 0\right]$$

This coincides with the Bayes-optimal decision if and only if:

$$\text{sign}\!\left[\log \frac{P_{\text{NB}}(Y=1\mid x)}{P_{\text{NB}}(Y=0\mid x)}\right] = \text{sign}\!\left[\log \frac{P(Y=1\mid x)}{P(Y=0\mid x)}\right]$$

**A concrete example.** Suppose $p=2$ with features $X_1, X_2 \in \{0,1\}$ that are perfectly correlated: $X_1 = X_2$ always. The true log-odds is:

$$\log \frac{P(X_1=1, X_2=1 \mid Y=1)}{P(X_1=1, X_2=1 \mid Y=0)} \cdot \frac{\pi_1}{\pi_0}$$

Naive Bayes computes instead:

$$\log \frac{\pi_1}{\pi_0} + \log \frac{P(X_1=1\mid Y=1)}{P(X_1=1\mid Y=0)} + \log \frac{X_2=1\mid Y=1)}{P(X_2=1\mid Y=0)}$$

$$= \log \frac{\pi_1}{\pi_0} + 2\log \frac{P(X_1=1\mid Y=1)}{P(X_1=1\mid Y=0)}$$

This double-counts the evidence, but if the per-feature log-odds is positive (resp. negative), doubling it preserves the sign. So the decision is still correct — only the **magnitude** of the score is wrong, not its direction.

**The structural reason.** The Naive Bayes log-odds is a monotone function of the true log-odds in many symmetric situations. More generally, if the Naive Bayes score is a strictly increasing transformation of the true posterior log-odds (even a nonlinear one), then the zero-crossing (decision boundary) is preserved.

**Formal statement (Domingos & Pazzani, 1997).** Naive Bayes can be optimal even when the independence assumption is severely violated, because optimality of classification only requires the **ranking** of posteriors to be correct for most inputs, not the actual probability values.

**Takeaway.** There is a strict separation between:
- **Calibration** (do the predicted probabilities match true probabilities?) — Naive Bayes often fails here.
- **Decision accuracy** (does the argmax give the right class?) — Naive Bayes can succeed here even under gross model misspecification.

This is why Naive Bayes is surprisingly competitive in practice despite its obviously wrong assumptions.
