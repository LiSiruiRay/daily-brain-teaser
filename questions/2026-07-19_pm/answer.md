# Answer: Temperature Scaling and Softmax Saturation

## Key Idea / Intuition

Temperature scaling is a way of "sharpening" or "flattening" a probability distribution. Low temperature amplifies score differences so the model becomes overconfident (winner-takes-all), while high temperature washes them out toward uniform. The cross-entropy loss thus perfectly detects whether the model "got it right" in raw scores (part 2), and tells us the maximum possible entropy of confusion at high temperature (part 3). This connects the geometric intuition of softmax to the information-theoretic meaning of cross-entropy.

---

## Formal Proof / Solution

### Part 1: Limits of the softmax probabilities

Replace $z_k$ with $z_k / T$. Then:

$$p_k(T) = \frac{e^{z_k/T}}{\sum_{j=1}^K e^{z_j/T}}.$$

**As $T \to 0^+$:** Divide numerator and denominator by $e^{z_{\max}/T}$ where $z_{\max} = \max_j z_j$:

$$p_k(T) = \frac{e^{(z_k - z_{\max})/T}}{\sum_{j} e^{(z_j - z_{\max})/T}}.$$

- If $z_k < z_{\max}$: the numerator $\to 0$ since $(z_k - z_{\max})/T \to -\infty$.
- If $z_k = z_{\max}$: the numerator $\to 1$.

So the probability concentrates equally on all classes achieving the maximum score. If there is a unique maximizer (say class 1), then $p_1(T) \to 1$ and all others $\to 0$: **winner-takes-all / argmax behavior**.

**As $T \to \infty$:** All exponents $z_k/T \to 0$, so $e^{z_k/T} \to 1$ for all $k$:

$$p_k(T) \to \frac{1}{K} \quad \text{for all } k.$$

The distribution **flattens to uniform** — the model becomes maximally uncertain.

---

### Part 2: $\mathcal{L}(T) \to 0$ iff class 1 has strictly highest score

The loss is:

$$\mathcal{L}(T) = -\log p_1(T) = \log\!\left(\sum_{j=1}^K e^{z_j/T}\right) - \frac{z_1}{T}.$$

Divide inside the log by $e^{z_1/T}$:

$$\mathcal{L}(T) = \log\!\left(\sum_{j=1}^K e^{(z_j - z_1)/T}\right).$$

Note the $j=1$ term contributes exactly $e^0 = 1$ to the sum.

**($\Rightarrow$ direction):** Suppose $z_1 > z_j$ for all $j \neq 1$. Then $(z_j - z_1) < 0$ for all $j \neq 1$, so:

$$e^{(z_j - z_1)/T} \to 0 \quad \text{as } T \to 0^+.$$

The entire sum $\to 1$, so:

$$\mathcal{L}(T) = \log(1 + \text{small positive}) \to \log 1 = 0. \checkmark$$

**($\Leftarrow$ direction):** Suppose some $j^* \neq 1$ satisfies $z_{j^*} \geq z_1$. Then $(z_{j^*} - z_1)/T \geq 0$ and since $T \to 0^+$, this term is at least 1 and does not vanish. The sum inside the log is $\geq 1 + 1 = 2$, so:

$$\mathcal{L}(T) \geq \log 2 > 0.$$

Hence $\mathcal{L}(T) \not\to 0$. $\checkmark$

**Conclusion:** $\mathcal{L}(T) \to 0$ as $T \to 0^+$ if and only if $z_1 = \arg\max_j z_j$ strictly.

---

### Part 3: The high-temperature limit of the loss

From Part 1, as $T \to \infty$, all $p_k \to 1/K$. Therefore:

$$\mathcal{L}(T) = -\log p_1(T) \to -\log \frac{1}{K} = \log K.$$

**Interpretation:** $\log K$ is the **entropy of the uniform distribution** over $K$ classes. At infinite temperature, the model is completely ignorant — it assigns equal probability to all classes — and pays the maximum possible cross-entropy loss of $\log K$. This is also the cross-entropy of any distribution against the uniform distribution when the truth is known.

In terms of **temperature scaling for calibration** (a practical ML technique): using $T > 1$ makes a model *less confident* and better calibrated when the raw logits are overconfident; the penalty is a higher but bounded loss approaching $\log K$.

---

### Summary Table

| Temperature | Probabilities | Cross-entropy loss |
|---|---|---|
| $T \to 0^+$ (if $z_1$ largest) | $p_1 \to 1$, rest $\to 0$ | $\mathcal{L} \to 0$ |
| $T \to 0^+$ (if $z_1$ not largest) | Mass on $\arg\max$ classes | $\mathcal{L} \geq \log 2 > 0$ |
| $T = 1$ | Standard softmax | $\mathcal{L} = -\log p_1$ |
| $T \to \infty$ | Uniform ($1/K$ each) | $\mathcal{L} \to \log K$ |
