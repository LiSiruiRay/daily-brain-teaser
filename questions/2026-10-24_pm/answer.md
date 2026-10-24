# Answer: Lobachevsky's Folding Trick

## Key Idea / Intuition

The factor $f(x)$ repeats every $\pi$. The only non-periodic part is $\dfrac{\sin x}{x}$, and $\sin x$ itself just flips sign on each period.

So cut $[0,\infty)$ into intervals of length $\pi$ and stack them all on top of $[0,\pi]$. Then use the mirror symmetry $f(\pi-x)=f(x)$ to fold $[0,\pi]$ onto $[0,\pi/2]$.

After stacking and folding, the factor $\dfrac1x$ becomes an alternating sum over all its shifted copies $\dfrac{1}{u+m\pi}$. By Euler's partial fractions, that sum is exactly $\dfrac{1}{\sin u}$. It cancels the $\sin u$, and what remains is simply $\int_0^{\pi/2} f$.

The infinite oscillatory integral collapses to a finite, elementary one.

---

## Formal Proof / Solution

**Step 1 (Convergence).** The function $g(x)=\sin x\, f(x)$ satisfies $g(x+\pi)=-g(x)$. So $g$ has period $2\pi$ and zero mean over a period, which means its antiderivative is bounded. Since $1/x\downarrow 0$, Dirichlet's test shows that $\int_1^\infty g(x)/x\,dx$ converges. Near $0$ the integrand is bounded. Hence

$$
I=\lim_{N\to\infty}\int_0^{N\pi}\frac{\sin x}{x}f(x)\,dx .
$$

**Step 2 (Stack the periods).** On $[k\pi,(k+1)\pi]$, substitute $x=t+k\pi$. This uses $\sin(t+k\pi)=(-1)^k\sin t$ and $f(t+k\pi)=f(t)$:

$$
\int_{k\pi}^{(k+1)\pi}\frac{\sin x}{x}f(x)\,dx=(-1)^k\int_0^{\pi}\frac{\sin t\, f(t)}{t+k\pi}\,dt .
$$

**Step 3 (Fold the period in half).** Split $[0,\pi]$ into $[0,\pi/2]\cup[\pi/2,\pi]$. On the second half put $t=\pi-u$, which uses $\sin(\pi-u)=\sin u$ and $f(\pi-u)=f(u)$. The $k$-th piece becomes

$$
(-1)^k\int_0^{\pi/2}\sin u\, f(u)\left[\frac{1}{u+k\pi}+\frac{1}{(k+1)\pi-u}\right]du .
$$

**Step 4 (Sum over $k$).** Set $a_k(u)=\dfrac{1}{u+k\pi}+\dfrac{1}{(k+1)\pi-u}$. For $u\in(0,\pi/2]$ we have $a_k(u)>0$, $a_k(u)$ decreasing in $k$, and $a_k(u)\to0$.

So $\sum_k(-1)^k a_k(u)$ is a Leibniz series. Its partial sums lie between $0$ and $a_0(u)=\frac1u+\frac1{\pi-u}$. Therefore

$$
\Big|\sin u\, f(u)\sum_{k=0}^{N-1}(-1)^k a_k(u)\Big|\le \|f\|_\infty\,\sin u\left(\frac1u+\frac{1}{\pi-u}\right)\le C .
$$

This bound is integrable on $[0,\pi/2]$, so dominated convergence lets us swap the sum and the integral:

$$
I=\int_0^{\pi/2}\sin u\, f(u)\,S(u)\,du,\qquad S(u)=\sum_{k\ge0}(-1)^k\left[\frac{1}{u+k\pi}+\frac{1}{(k+1)\pi-u}\right].
$$

**Step 5 (Recognize the cosecant).** In the second sum, reindex with $m=-(k+1)$, so $m\le -1$. Then

$$
\frac{(-1)^k}{(k+1)\pi-u}=\frac{-(-1)^m}{-(u+m\pi)}=\frac{(-1)^m}{u+m\pi}.
$$

The terms with $k\ge0$ (that is, $m\ge0$) and with $m\le-1$ combine into the symmetric full sum. By Euler's expansion $\dfrac{\pi}{\sin \pi z}=\sum_m\dfrac{(-1)^m}{z-m}$ with $z=u/\pi$,

$$
S(u)=\sum_{m\in\mathbb Z}\frac{(-1)^m}{u+m\pi}=\frac{1}{\sin u}.
$$

So the $\sin u$ cancels, and we obtain **Lobachevsky's formula**:

$$
\int_0^\infty\frac{\sin x}{x}f(x)\,dx=\int_0^{\pi/2}f(u)\,du .
$$

**Step 6 (Apply to our $f$).** The function $f(x)=\dfrac{1}{1+\cos^2x}$ is continuous and $\pi$-periodic, and $\cos^2(\pi-x)=\cos^2x$, so the formula applies. With $v=\tan u$, $dv=\sec^2u\,du$, and $1+\cos^2u=\dfrac{\sec^2u+1}{\sec^2 u}=\dfrac{v^2+2}{\sec^2 u}$:

$$
\int_0^{\pi/2}\frac{du}{1+\cos^2u}=\int_0^{\infty}\frac{dv}{v^2+2}=\frac{1}{\sqrt2}\cdot\frac{\pi}{2}.
$$

$$
\boxed{\,I=\dfrac{\pi}{2\sqrt2}\,}
$$

**Remarks.**
- With $f\equiv1$ this recovers $\int_0^\infty \frac{\sin x}{x}\,dx=\frac{\pi}{2}$.
- With $f(x)=\dfrac{\sin^2x}{x^2}\cdot\dfrac{x^2}{\sin^2 x}$ the formula does not apply directly. However, a variant of the same folding gives $\int_0^\infty\frac{\sin^2x}{x^2}f(x)\,dx=\int_0^{\pi/2}f$ as well. This variant uses $\sum_m\frac{1}{(u+m\pi)^2}=\csc^2u$.
- The structural lesson: *periodic times $1/x$* can be summed by folding, and the fold turns $1/x$ into a Mittag-Leffler series.
