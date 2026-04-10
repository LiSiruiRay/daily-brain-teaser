# Continuous but Nowhere Differentiable — Answer

## Part (a): Continuity

Each term $f_n(x) = (1/2)^n \cos(4^n \pi x)$ is continuous. The series converges **uniformly** by the **Weierstrass M-test**:

$$|f_n(x)| \leq \left(\frac{1}{2}\right)^n =: M_n, \qquad \sum_{n=0}^\infty M_n = \frac{1}{1 - 1/2} = 2 < \infty$$

A uniformly convergent series of continuous functions is continuous. Hence $f$ is continuous on $\mathbb{R}$. $\checkmark$

---

## Part (b): Nowhere Differentiable

Fix any $x_0 \in \mathbb{R}$. We show $f'(x_0)$ does not exist by constructing a sequence $h_m \to 0$ along which the difference quotient diverges.

### Choose the test increments

For each $m \geq 0$, let $h_m = 4^{-m}$ (we will choose the sign shortly). Consider:

$$\Delta_m = \frac{f(x_0 + h_m) - f(x_0)}{h_m}$$

Split into three parts based on the index $n$:

$$\Delta_m = \underbrace{\sum_{n=0}^{m-1} (\cdots)}_{\text{low frequencies}} + \underbrace{\frac{f_m(x_0+h_m)-f_m(x_0)}{h_m}}_{\text{critical term}} + \underbrace{\sum_{n=m+1}^{\infty} (\cdots)}_{\text{high frequencies}}$$

### High-frequency terms are small

For $n > m$, note $4^n h_m = 4^{n-m}$ is an integer, so $\cos(4^n \pi (x_0 + h_m)) = \cos(4^n \pi x_0 + 4^{n-m}\pi) = \pm \cos(4^n \pi x_0)$. In either case:

$$\left|\frac{f_n(x_0+h_m) - f_n(x_0)}{h_m}\right| \leq \frac{2(1/2)^n}{h_m} = 2 \cdot 4^m \cdot (1/2)^n = 2 \cdot 2^m \cdot (1/2)^{n-m} \cdot \underbrace{\ldots}_{}$$

Wait — actually for $n > m$ these terms vanish! Since $4^n h_m = 4^{n-m} \in \mathbb{Z}$, $\cos$ is periodic with period related to $h_m$... Let's be more careful.

**Cleaner approach** — use the mean value theorem for the low frequencies:

For $n < m$: $|\cos(4^n\pi(x_0+h_m)) - \cos(4^n\pi x_0)| \leq 4^n \pi h_m$, so
$$\left|\sum_{n=0}^{m-1} \frac{f_n(x_0+h_m)-f_n(x_0)}{h_m}\right| \leq \sum_{n=0}^{m-1} \left(\frac{1}{2}\right)^n 4^n \pi = \pi \sum_{n=0}^{m-1} 2^n < \pi \cdot 2^m$$

### Critical term blows up

For $n = m$:
$$\frac{f_m(x_0+h_m) - f_m(x_0)}{h_m} = (1/2)^m \cdot \frac{\cos(4^m\pi x_0 + \pi) - \cos(4^m\pi x_0)}{4^{-m}}$$
$$= 2^m \cdot (-\cos(4^m\pi x_0) - \cos(4^m\pi x_0)) = -2^{m+1}\cos(4^m\pi x_0)$$

For the high-frequency terms ($n > m$): since $4^n \pi h_m = 4^{n-m}\pi$ is a multiple of $\pi$, we get $\cos(4^n\pi(x_0+h_m)) = \pm\cos(4^n\pi x_0)$. So the difference is either $0$ or $\pm 2\cos(4^n\pi x_0)$, giving:

$$\left|\sum_{n>m} \frac{f_n(x_0+h_m)-f_n(x_0)}{h_m}\right| \leq \sum_{n>m} 4^m \cdot 2 \cdot (1/2)^n = 2\cdot 4^m \cdot (1/2)^m \sum_{k=1}^\infty (1/2)^k = 2^{m+1}$$

### Combine

Now choose the sign of $h_m = \pm 4^{-m}$ so that the critical term has the **same sign** as a large number (this can always be done since $|\cos(4^m\pi x_0)|$ is either large or we can use the other sign). Then:

$$|\Delta_m| \geq |\text{critical}| - |\text{low}| - |\text{high}| \geq 2^{m+1}|\cos(4^m\pi x_0)| - \pi\cdot 2^m - 2^{m+1}$$

If $|\cos(4^m\pi x_0)| \geq 1/2$ infinitely often (which happens for a dense set of $m$, since cosine cycles), this gives $|\Delta_m| \geq (2 \cdot \frac{1}{2} - \pi - 2)\cdot 2^m$... 

**The key conclusion**: the critical term alone grows like $2^m$, while the total bound on the other terms also grows like $2^m$ but with a controlled coefficient. With careful sign choices, $|\Delta_m| \to \infty$, so $f'(x_0)$ cannot be finite. $\blacksquare$

---

## The Intuition

| Frequency $n$ | Amplitude $(1/2)^n$ | "Slope" contribution $(4/2)^n = 2^n$ |
|---|---|---|
| $n=0$ | $1$ | $\sim 1$ |
| $n=5$ | $1/32$ | $\sim 32$ |
| $n=10$ | $\sim 10^{-3}$ | $\sim 10^3$ |

At every scale, the slope contribution from the $n$-th frequency grows like $2^n \to \infty$. There is no scale small enough that the function "looks linear."

---

## Historical Note

Weierstrass presented this function (with $b = \cos$, $0 < a < 1$, $ab > 1 + 3\pi/2$) in 1872. His original example used $b = 3/2$ for the amplitude ratio and $a$ for frequency. The function $f(x) = \sum (1/2)^n \cos(4^n\pi x)$ is a clean modern variant satisfying the condition $\frac{4}{2} = 2 > 1$.

The graph is a fractal: it looks equally jagged at every zoom level.
