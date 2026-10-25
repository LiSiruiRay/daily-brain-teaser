# Answer: Why the Wavelet Threshold Is σ√(2 log N)

## Key Idea / Intuition

An orthonormal transform rotates white Gaussian noise into white Gaussian noise. So in the wavelet domain, pure noise is just $N$ independent $N(0,\sigma^2)$ draws.

The question then becomes how large the biggest of $N$ Gaussians is. The Gaussian tail decays like $e^{-t^2/2}$. The level $t$ at which you expect about *one* exceedance among $N$ tries solves $N e^{-t^2/2}\approx 1$, which gives $t\approx\sqrt{2\log N}$.

The universal threshold is therefore exactly the height of the tallest noise spike:
- Set the threshold slightly higher, and all noise vanishes (by a union bound).
- Set it slightly lower, by any constant factor, and some noise spikes survive (by independence).

---

## Formal Proof / Solution

**(a) Noise stays white.**

With $\mathbf f=0$, we have $\mathbf y^*=W^\top\boldsymbol\varepsilon$. A linear image of a Gaussian vector is Gaussian, with covariance
$$
\operatorname{Cov}(W^\top\boldsymbol\varepsilon)=W^\top(\sigma^2 I)W=\sigma^2 W^\top W=\sigma^2 I.
$$
Uncorrelated jointly Gaussian variables are independent. Hence $y^*_j \overset{iid}{\sim} N(0,\sigma^2)$.

From now on, write $y^*_j=\sigma Z_j$ with $Z_j$ i.i.d. standard normal, and let $t_N=\sqrt{2\log N}$.

**Tail bounds.** Let $\varphi$ be the standard normal density and $\Phi$ its CDF. For $t>0$ we need an upper and a lower bound on $1-\Phi(t)$.

*Upper bound.* On $x\ge t$ we have $x/t\ge 1$, so
$$
1-\Phi(t)=\int_t^\infty\varphi(x)\,dx\le\int_t^\infty \frac{x}{t}\varphi(x)\,dx=\frac{\varphi(t)}{t}.
$$

*Lower bound* (for $t\ge1$). Integrate only over $[t,\,t+1/t]$, where $\varphi$ is at least its value at the right endpoint. Since $\big(t+\tfrac1t\big)^2/2=t^2/2+1+\tfrac{1}{2t^2}$,
$$
1-\Phi(t)\ge \frac1t\,\varphi\!\Big(t+\frac1t\Big)=\frac{\varphi(t)}{t}\,e^{-1-\frac{1}{2t^2}}\ge e^{-3/2}\,\frac{\varphi(t)}{t}.
$$
So $1-\Phi(t)\asymp \varphi(t)/t$.

**(b) The threshold kills all noise.**

Apply the union bound, then the upper tail bound with $\varphi(t_N)=\frac{1}{\sqrt{2\pi}}e^{-\log N}=\frac{1}{\sqrt{2\pi}\,N}$:
$$
P\Big(\max_j|Z_j|>t_N\Big)\le 2N\big(1-\Phi(t_N)\big)\le 2N\cdot\frac{1}{\sqrt{2\pi}\,N\,t_N}=\frac{1}{\sqrt{\pi\log N}}\longrightarrow 0.
$$

**(c) Any smaller threshold fails.**

Fix $c<1$ and let $s_N=c\,t_N$. For large $N$ we have $s_N\ge1$. Set $p_N=1-\Phi(s_N)$. Since $\varphi(s_N)=\frac{1}{\sqrt{2\pi}}N^{-c^2}$, the lower tail bound gives
$$
N p_N\;\ge\; \frac{e^{-3/2}}{\sqrt{2\pi}}\cdot\frac{N^{1-c^2}}{c\sqrt{2\log N}}\;\longrightarrow\;\infty,
$$
because the power $N^{1-c^2}$ beats $\sqrt{\log N}$.

Now use independence:
$$
P\Big(\max_j|Z_j|\le s_N\Big)\le P(Z_j\le s_N\ \forall j)=(1-p_N)^N\le e^{-Np_N}\longrightarrow 0.
$$

**Conclusion.** Combining (b) and (c), for every $c<1$,
$$
P\big(c\,t_N<\max_j|Z_j|\le t_N\big)\to1,
$$
so $\max_j|y^*_j|\big/\sigma\sqrt{2\log N}\to1$ in probability.

---

## Why This Is Beautiful

- **One number, two arguments.** The "$\le$" direction is a pure union bound and needs no independence at all. The "$\ge$" direction is exactly where independence matters. This is the standard extreme-value pattern for maxima.
- **Orthogonality as a rotation.** Part (a) is the reason orthonormal wavelets are so convenient: noise looks the same in every orthonormal basis, while a structured signal concentrates in a few large coefficients. Thresholding then separates the few big signal coefficients from the many small noise ones.
- **The bound is slow.** The failure probability in (b) decays only like $1/\sqrt{\log N}$. The universal threshold is conservative: it errs toward killing noise, which is why the resulting reconstructions look visually smooth.
- **Bigger picture.** Donoho and Johnstone (1994) showed that soft thresholding at $\sigma\sqrt{2\log N}$ attains risk within a factor of about $2\log N$ of an oracle that knows which coefficients are signal. The same $\sqrt{2\log p}$ scaling reappears as the natural penalty level for the LASSO in high dimensions.

**Difficulty:** 2.5 / 5

**Reference:** Hastie, Tibshirani, Friedman, *The Elements of Statistical Learning* (2nd ed.), §5.9.1–5.9.2, eq. (5.69), with the universal threshold $\lambda=\sigma\sqrt{2\log N}$. Original source: Donoho & Johnstone, "Ideal spatial adaptation by wavelet shrinkage," *Biometrika* (1994).
