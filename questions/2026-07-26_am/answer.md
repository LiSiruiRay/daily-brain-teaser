# Answer: The Vanishing Gradient Plateau: Why Sigmoid Networks Saturate

## Key Idea / Intuition

The sigmoid function "squashes" its input into $(0,1)$, which is great for probability interpretation — but the price is that its derivative $\sigma'(z) = \sigma(z)(1-\sigma(z))$ is nearly **zero** whenever $|z|$ is large. So when a neuron is confidently wrong (output near 0 or 1), the gradient almost vanishes, and weights barely move. The network is stuck in a flat landscape of its own making.

---

## Formal Proof / Solution

### Part (a): Computing the gradient

By the chain rule:

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \sigma} \cdot \frac{\partial \sigma}{\partial z} \cdot \frac{\partial z}{\partial w}$$

Each factor:
- $\frac{\partial L}{\partial \sigma} = -\bigl(y - \sigma(z)\bigr)$
- $\frac{\partial \sigma}{\partial z} = \sigma(z)\bigl(1 - \sigma(z)\bigr)$ (standard sigmoid derivative)
- $\frac{\partial z}{\partial w} = x$

So:

$$\boxed{\frac{\partial L}{\partial w} = -\bigl(y - \sigma(z)\bigr)\,\sigma(z)\bigl(1-\sigma(z)\bigr)\,x}$$

The factor $\sigma(z)(1-\sigma(z))$ appears explicitly.

---

### Part (b): Large error yet slow learning

With $w \gg 1$, $x = 1$, $y = 0$: we have $z = w \gg 1$, so $\sigma(z) \approx 1$.

- **Error:** $L = \frac{1}{2}(0 - \sigma(z))^2 \approx \frac{1}{2}$. This is a large error (the neuron is outputting $\approx 1$ when the target is $0$).

- **Gradient factor:** $\sigma(z)(1-\sigma(z)) \approx 1 \cdot (1-1) \approx 0$.

So the gradient $\frac{\partial L}{\partial w} \approx -(0-1)(0)(1) = 0$. Learning is essentially **frozen** despite the large loss.

**Maximum of $\sigma(z)(1-\sigma(z))$:**

Let $s = \sigma(z) \in (0,1)$. We maximize $f(s) = s(1-s)$ by AM-GM or calculus:

$$f'(s) = 1 - 2s = 0 \implies s = \frac{1}{2}$$

$$f\!\left(\tfrac{1}{2}\right) = \tfrac{1}{4}$$

So the maximum gradient factor is $\frac{1}{4}$, achieved when $z = 0$ (the neuron is exactly at the decision boundary, outputting $\frac{1}{2}$).

This means even in the **best** case, back-propagating through a sigmoid layer multiplies the gradient by at most $\frac{1}{4}$. With many layers, this compounds: through $L$ layers, the gradient can shrink by up to $(1/4)^L$.

---

### Part (c): Intuition and fix

**Intuition:** The sigmoid flattens out at both ends of its S-curve; a neuron that has made up its mind (output near 0 or 1) sits in a flat region where infinitesimal changes to the weight produce infinitesimal changes in output, killing the learning signal.

**Fix:** Replace sigmoid with **ReLU** ($\max(0, z)$), whose derivative is either $0$ or $1$ — it doesn't saturate for positive inputs, so gradients flow through cleanly (at the cost of "dying ReLU" for negative inputs, addressed by Leaky ReLU or ELU).

---

## Summary Table

| Quantity | Value |
|---|---|
| Max of $\sigma(z)(1-\sigma(z))$ | $1/4$ at $z=0$ |
| Value when $z \gg 1$ | $\approx 0$ |
| Gradient at large $w$ | $\approx 0$ despite large loss |
| Per-layer gradient decay | up to factor $1/4$ |

Written to: [questions/2026-06-17_am.md](questions/2026-06-17_am.md)
