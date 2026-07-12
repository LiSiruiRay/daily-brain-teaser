# Answer: AdaBoost Exponential Training Error Bound

## Key Idea / Intuition

The insight is that training error is **upper bounded by an exponential loss**, and each round of AdaBoost multiplies that exponential loss by a factor strictly less than 1. The weights $\alpha_t$ are chosen *precisely* to make this multiplicative factor as small as possible — in fact, minimizing the per-round factor is what uniquely determines $\alpha_t$. Once you see the bound as a telescoping product, exponential decay in $T$ is immediate.

---

## Formal Proof / Solution

**Step 1: Training error is bounded by exponential loss.**

For any margin $y_i F_T(x_i)$: if $H(x_i) \neq y_i$, then $y_i F_T(x_i) \leq 0$, so $e^{-y_i F_T(x_i)} \geq 1$. Therefore,

$$\text{TrainingError}(H) = \frac{1}{n}\sum_{i=1}^n \mathbf{1}[y_i F_T(x_i) \leq 0] \leq \frac{1}{n}\sum_{i=1}^n e^{-y_i F_T(x_i)}.$$

**Step 2: Track how the exponential loss evolves each round.**

AdaBoost maintains sample weights $w_i^{(t)}$, initialized to $w_i^{(1)} = 1/n$, and updated as

$$w_i^{(t+1)} = w_i^{(t)} \cdot e^{-\alpha_t y_i h_t(x_i)}.$$

Unrolling the recursion gives $w_i^{(T+1)} = \frac{1}{n} e^{-y_i F_T(x_i)}$, so

$$\frac{1}{n}\sum_{i=1}^n e^{-y_i F_T(x_i)} = \sum_{i=1}^n w_i^{(T+1)}.$$

It suffices to show $\sum_i w_i^{(T+1)} \leq e^{-2\gamma^2 T}$.

**Step 3: Per-round multiplicative factor.**

Define $Z_t = \sum_i w_i^{(t+1)} / \sum_i w_i^{(t)}$ (the normalization constant at round $t$). Then

$$\sum_i w_i^{(T+1)} = \prod_{t=1}^T Z_t.$$

Expanding $Z_t$:

$$Z_t = \sum_i w_i^{(t)} e^{-\alpha_t y_i h_t(x_i)} = \epsilon_t e^{\alpha_t} + (1-\epsilon_t)e^{-\alpha_t},$$

where $\epsilon_t$ is the weighted error of $h_t$ and we split into misclassified ($y_i h_t(x_i) = -1$) and correct ($y_i h_t(x_i) = +1$) examples.

**Step 4: Minimize $Z_t$ over $\alpha_t$.**

Setting $\frac{d}{d\alpha_t} Z_t = 0$ gives the optimal

$$\alpha_t = \frac{1}{2}\ln\!\left(\frac{1-\epsilon_t}{\epsilon_t}\right),$$

which is exactly what AdaBoost uses! Substituting back:

$$Z_t = \epsilon_t \sqrt{\frac{1-\epsilon_t}{\epsilon_t}} + (1-\epsilon_t)\sqrt{\frac{\epsilon_t}{1-\epsilon_t}} = 2\sqrt{\epsilon_t(1-\epsilon_t)}.$$

**Step 5: Apply the weak learning assumption.**

Since $\epsilon_t \leq \frac{1}{2} - \gamma$, we have $\epsilon_t(1-\epsilon_t) \leq \frac{1}{4} - \gamma^2$, so

$$Z_t = 2\sqrt{\epsilon_t(1-\epsilon_t)} \leq 2\sqrt{\tfrac{1}{4}-\gamma^2} = \sqrt{1-4\gamma^2} \leq e^{-2\gamma^2},$$

where the last step uses $\sqrt{1-x} \leq e^{-x/2}$ for $x \in [0,1]$.

**Step 6: Conclude.**

$$\text{TrainingError}(H) \leq \prod_{t=1}^T Z_t \leq \left(e^{-2\gamma^2}\right)^T = e^{-2\gamma^2 T}.$$

**Conceptual punchline:** The weight $\alpha_t$ is not chosen by guesswork — it is the unique value that *minimizes the per-round multiplicative factor* $Z_t$. The entire algorithm can be derived by asking: "what assignment of $\alpha_t$ makes the exponential loss shrink fastest?" This reveals AdaBoost as **coordinate descent on the exponential loss**, a beautiful unification of a seemingly heuristic procedure with proper optimization.
