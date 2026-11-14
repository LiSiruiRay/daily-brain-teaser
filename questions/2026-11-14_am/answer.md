# Answer: The Integral That Doesn't Notice x − 1/x

## Key Idea / Intuition

Dividing the numerator and the denominator by $x^2$ turns the integrand into $\dfrac{1}{(x-1/x)^2+1}$, which is a Lorentzian evaluated at $u = x - 1/x$.

The map $x\mapsto x-1/x$ covers the real line twice: once from $(-\infty,0)$ and once from $(0,\infty)$. Each value $u$ therefore has two preimages $x_-<0<x_+$. These preimages are the roots of $x^2 - ux - 1 = 0$, so Vieta's formulas give $x_+ + x_- = u$. Differentiating in $u$ shows that the two preimages move with speeds adding up to exactly $1$. Hence the two sheets together carry Lebesgue measure to Lebesgue measure, and the integral equals $\int \frac{du}{1+u^2} = \pi$.

---

## Formal Proof / Solution

### Step 1: Rewrite the integrand

For $x \neq 0$,

$$
\frac{x^2}{x^4 - x^2 + 1} \;=\; \frac{1}{x^2 - 1 + \frac{1}{x^2}} \;=\; \frac{1}{\left(x - \frac1x\right)^2 + 1}.
$$

So $I = \displaystyle\int_{\mathbb{R}} f\!\left(x - \tfrac1x\right)dx$ with $f(u) = \dfrac{1}{1+u^2}$. The single point $x=0$ does not affect the integral.

### Step 2: The map $\varphi(x) = x - 1/x$ has two increasing branches

Since $\varphi'(x) = 1 + 1/x^2 > 0$, the map $\varphi$ is strictly increasing on each half-line.

- On $(0,\infty)$: $\varphi \to -\infty$ as $x\to 0^+$ and $\varphi\to+\infty$ as $x\to\infty$. So $\varphi$ is a bijection $(0,\infty)\to\mathbb{R}$.
- On $(-\infty,0)$: $\varphi\to-\infty$ as $x\to-\infty$ and $\varphi\to+\infty$ as $x\to 0^-$. So $\varphi$ is a bijection $(-\infty,0)\to\mathbb{R}$.

For each $u\in\mathbb{R}$ there are therefore exactly two preimages, $x_+(u) > 0$ and $x_-(u) < 0$. Both are smooth and increasing in $u$.

### Step 3: The Vieta trick

The equation $x - 1/x = u$ is equivalent to $x^2 - ux - 1 = 0$, whose roots are exactly $x_+(u)$ and $x_-(u)$. By Vieta's formulas,

$$
x_+(u) + x_-(u) = u, \qquad x_+(u)\,x_-(u) = -1 .
$$

Differentiating the first identity gives

$$
x_+'(u) + x_-'(u) = 1 .
$$

### Step 4: Change variables on each branch

Substitute $x = x_\pm(u)$ on each half-line. Both branches are increasing bijections onto $\mathbb{R}$, so for $f\ge 0$ we get

$$
\int_{0}^{\infty} f(\varphi(x))\,dx = \int_{-\infty}^{\infty} f(u)\,x_+'(u)\,du,
\qquad
\int_{-\infty}^{0} f(\varphi(x))\,dx = \int_{-\infty}^{\infty} f(u)\,x_-'(u)\,du .
$$

Adding the two and using Step 3:

$$
\int_{-\infty}^{\infty} f\!\left(x-\tfrac1x\right)dx \;=\; \int_{-\infty}^{\infty} f(u)\,\big(x_+'(u)+x_-'(u)\big)\,du \;=\; \int_{-\infty}^{\infty} f(u)\,du .
$$

This holds for every measurable $f \ge 0$ by Tonelli. Splitting $f = f^+ - f^-$ extends it to every integrable $f$, which proves the follow-up.

**Explicit check.** The roots are $x_\pm = \frac{u\pm\sqrt{u^2+4}}{2}$, so

$$
x_\pm' = \tfrac12\left(1 \pm \tfrac{u}{\sqrt{u^2+4}}\right),
$$

and the two derivatives indeed sum to $1$.

### Step 5: Finish

$$
I = \int_{-\infty}^{\infty} \frac{du}{1+u^2} = \pi .
$$

Since the integrand is even, this also gives $\displaystyle\int_0^\infty \frac{x^2}{x^4-x^2+1}\,dx = \frac{\pi}{2}$.

---

### Remarks

- **Scaling.** The same argument with $x^2 - ux - a = 0$ shows that $x\mapsto x - a/x$ preserves Lebesgue measure for every $a>0$. For example,
$$
\int_{-\infty}^{\infty} e^{-(x - 1/x)^2}\,dx = \sqrt{\pi}.
$$
- **Glasser's Master Theorem.** More generally, the map
$$
\varphi(x) = x - \sum_{k=1}^n \frac{a_k}{x - b_k}, \qquad a_k>0,
$$
has $n+1$ increasing branches, each mapping onto $\mathbb{R}$. Clearing denominators in $\varphi(x)=u$ gives a monic polynomial equation of degree $n+1$ whose $x^n$-coefficient is $-u-\sum_k b_k$. By Vieta, the sum of all preimages is $u + \sum_k b_k$, so the preimage speeds again sum to $1$. Hence $\int f(\varphi(x))\,dx = \int f(u)\,du$.
- **Measure-theoretic view.** The pushforward of Lebesgue measure under $\varphi$ has density $\sum_{\varphi(x)=u} 1/|\varphi'(x)|$. The Vieta argument shows this density is identically $1$.
