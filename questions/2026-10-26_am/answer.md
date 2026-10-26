# Answer: How Fast Does Iterated Sine Die?

## Key Idea / Intuition

Near $0$ we have $\sin x \approx x - x^3/6$. Each step therefore subtracts about $x^3/6$. Think of $n$ as continuous time. The iteration then looks like the ODE

$$
\frac{dx}{dn} = -\frac{x^3}{6}.
$$

This separates to $\frac{d}{dn}\left(x^{-2}\right) = \frac13$, so $1/x^2$ should grow linearly with slope $1/3$. That gives $x \approx \sqrt{3/n}$.

The rigorous proof follows the same idea in three steps:
- Show the increments $\frac{1}{x_{n+1}^2} - \frac{1}{x_n^2}$ tend to $\frac13$.
- Average them (Cesàro).
- Conclude that $\frac{1}{n x_n^2} \to \frac13$.

---

## Formal Proof / Solution

### Step 1: $x_n \downarrow 0$

Since $x_0 \in (0,\pi)$, we get $x_1 = \sin x_0 \in (0, 1]$.

For $x \in (0,1]$ we have $0 < \sin x < x$. By induction, $(x_n)_{n\ge1}$ is strictly decreasing and positive. It therefore converges to some limit $L \in [0,1]$.

By continuity of $\sin$, the limit satisfies $\sin L = L$. The only solution in $[0,1]$ is $L = 0$. So $x_n \to 0$, with $x_n > 0$ for all $n$.

### Step 2: The increments of $1/x_n^2$ tend to $1/3$

Let $y_n = 1/x_n^2$. Then

$$
y_{n+1} - y_n = \frac{1}{\sin^2 x_n} - \frac{1}{x_n^2} = \frac{x_n^2 - \sin^2 x_n}{x_n^2 \sin^2 x_n}.
$$

From $\sin x = x - \frac{x^3}{6} + O(x^5)$ we get

$$
\sin^2 x = x^2 - \frac{x^4}{3} + O(x^6).
$$

Hence, as $x \to 0$:

$$
\frac{x^2 - \sin^2 x}{x^2 \sin^2 x}
= \frac{\frac{x^4}{3} + O(x^6)}{x^4 + O(x^6)}
\longrightarrow \frac13.
$$

Since $x_n \to 0$, it follows that

$$
d_n := y_{n+1} - y_n \longrightarrow \frac13.
$$

### Step 3: Cesàro averaging (Stolz–Cesàro)

**Claim.** If $d_n \to c$, then $\dfrac{y_n}{n} \to c$.

*Proof.* Write $y_n = y_0 + \sum_{k=0}^{n-1} d_k$. Fix $\varepsilon > 0$ and choose $N$ with $|d_k - c| < \varepsilon$ for $k \ge N$. For $n > N$:

$$
\left| \frac{y_n}{n} - c \right|
\le \frac{|y_0| + \sum_{k<N} |d_k - c|}{n} + \frac{1}{n}\sum_{k=N}^{n-1} |d_k - c|
\le \frac{C_N}{n} + \varepsilon.
$$

Here $C_N$ does not depend on $n$. Taking $\limsup_{n\to\infty}$ gives $\limsup |y_n/n - c| \le \varepsilon$. Since $\varepsilon$ was arbitrary, the claim follows. $\square$

Apply the claim with $c = \frac13$:

$$
\frac{1}{n x_n^2} = \frac{y_n}{n} \longrightarrow \frac13
\quad\Longrightarrow\quad
n x_n^2 \to 3
\quad\Longrightarrow\quad
\sqrt{n}\, x_n \to \sqrt{3},
$$

using $x_n > 0$ in the last step. $\blacksquare$

---

## Remarks

- **Why $x_0$ disappears.** The starting point only affects finitely many early increments $d_k$. Cesàro averaging washes these out, since they contribute $O(1/n)$. This is why the limit is universal.
- **The general principle.** Suppose $x_{n+1} = x_n - a x_n^{p} + o(x_n^{p})$ with $p > 1$ and $a > 0$. The same argument applied to $y_n = x_n^{-(p-1)}$ gives

  $$
  x_n \sim \big((p-1)\,a\,n\big)^{-1/(p-1)}.
  $$

  For $\sin$, take $p = 3$ and $a = 1/6$. This gives $x_n \sim (n/3)^{-1/2}$.
- **Finer asymptotics.** Pushing the expansion one order further shows that the next correction to $\sqrt{3/n}$ has order $\frac{\ln n}{n^{3/2}}$. So the convergence to $\sqrt3$ is genuinely slow, which you can see numerically.
- **Calculator check.** Start from $x_0 = 1$ and take $n = 1000$. Then $\sqrt{3/1000} \approx 0.0548$, which is already close to the true $x_{1000}$.
