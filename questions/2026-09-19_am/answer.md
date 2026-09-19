# Answer: The Integral That Knows Euler's Constant

## Key Idea / Intuition

The substitution $x = e^{-t}$ converts this into a classical integral over $[0,\infty)$ involving $e^{-t}\ln t$. That integral is exactly the definition of $-\gamma$ (the negative of the Euler–Mascheroni constant), which emerges from differentiating the Gamma function at $s=1$. So the answer is $-\gamma$ — a beautifully clean connection between a seemingly innocuous log-log integral and one of the most mysterious constants in mathematics.

---

## Formal Proof / Solution

**Step 1: Substitution.**

Let $x = e^{-t}$, so $t = -\ln x$ and $dx = -e^{-t}\,dt$. When $x=0$, $t=\infty$; when $x=1$, $t=0$. Then

$$I = \int_{\infty}^{0} \ln(t)\cdot e^{-t}\cdot(-dt) = \int_0^{\infty} e^{-t}\ln t\, dt.$$

**Step 2: Recognize the Gamma derivative.**

Recall the Gamma function:

$$\Gamma(s) = \int_0^{\infty} t^{s-1} e^{-t}\, dt.$$

Differentiating under the integral sign with respect to $s$:

$$\Gamma'(s) = \int_0^{\infty} t^{s-1} e^{-t} \ln t\, dt.$$

Setting $s = 1$ (so $t^{s-1} = 1$):

$$\Gamma'(1) = \int_0^{\infty} e^{-t} \ln t\, dt = I.$$

**Step 3: Evaluate $\Gamma'(1)$.**

The digamma function is $\psi(s) = \Gamma'(s)/\Gamma(s)$, so

$$\Gamma'(1) = \Gamma(1)\cdot\psi(1) = 1\cdot(-\gamma) = -\gamma,$$

where $\gamma \approx 0.5772\ldots$ is the Euler–Mascheroni constant, defined by $\psi(1) = -\gamma$.

**Conclusion.**

$$\boxed{I = -\gamma}.$$

This is a beautiful result: the integral $\int_0^1 \ln(-\ln x)\,dx$ distills the Euler–Mascheroni constant, which normally appears as the limit $\gamma = \lim_{n\to\infty}(H_n - \ln n)$, into a single clean definite integral.
