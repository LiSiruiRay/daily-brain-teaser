# Answer: The Gaussian Mixture Whose Likelihood Explodes

## Key Idea / Intuition

A Gaussian with variance $\sigma\to 0$ placed exactly on a data point gives that point density $\sim 1/\sigma\to\infty$.

- **Single Gaussian:** the same spike must also explain every other point. Their densities decay like $e^{-c/\sigma^2}$, which overwhelms the gain, so the likelihood stays bounded.
- **Mixture:** the work can be split. One component degenerates into a spike on $x_1$. The second, ordinary component gives every other point a fixed positive density. Nothing pays for the spike, so the likelihood blows up.
- **Tied variance:** the spike can no longer be "private". With $n\ge 3$ points and only two means, some point is always far from both means and gets killed by $e^{-c/\sigma^2}$.

The moral is that maximum likelihood for mixtures is fundamentally ill-posed. EM is useful because it finds good *local* maxima. Regularization removes the degenerate spikes: variance floors, tied covariances, or priors (MAP).

---

## Formal Proof / Solution

**(a) Single Gaussian.**

Since the $x_i$ are distinct and $n\ge2$, the sample variance $s^2=\frac1n\sum_i (x_i-\bar x)^2$ is strictly positive. For every $\mu$,
$$\sum_i (x_i-\mu)^2 = n s^2 + n(\bar x-\mu)^2 \ \ge\ n s^2 .$$
Hence
$$L(\mu,\sigma)\le (2\pi\sigma^2)^{-n/2}\exp\!\Big(-\frac{n s^2}{2\sigma^2}\Big)=:g(\sigma).$$

Now examine $g$ at both ends:
- As $\sigma\to 0$, $g(\sigma)\to 0$, because $e^{-ns^2/2\sigma^2}$ beats any power $\sigma^{-n}$.
- As $\sigma\to\infty$, $g(\sigma)\to 0$ as well.

$g$ is continuous on $(0,\infty)$ and vanishes at both ends, so it is bounded. Hence $L$ is bounded.

(Indeed $g$ is maximized at $\sigma^2=s^2$, which recovers the usual MLE.)

**(b) Two Gaussians: the likelihood is unbounded.**

Fix the following parameter values:
- $\pi=\tfrac12$,
- $\mu_1=x_1$,
- $\mu_2=0$, $\sigma_2=1$.

Let $\sigma_1=\varepsilon\to 0$. Bound each factor from below:

- **The spiked point.** Since $\mu_1=x_1$,
$$f(x_1)\ \ge\ \tfrac12\,\varphi_\varepsilon(0)=\frac{1}{2\sqrt{2\pi}\,\varepsilon}.$$
- **Every other point** ($i\ge 2$). Dropping the first, nonnegative component,
$$f(x_i)\ \ge\ \tfrac12\,\varphi_1(x_i)=:c_i>0.$$
The constant $c_i$ does not depend on $\varepsilon$.

Therefore
$$L\ \ge\ \frac{1}{2\sqrt{2\pi}\,\varepsilon}\prod_{i\ge2}c_i\ \xrightarrow[\varepsilon\to0]{}\ +\infty .$$

The second component acts as a "life support" for the remaining data. That is exactly what the single Gaussian in (a) lacked.

**(c) Tied variance, $n\ge3$: bounded again.**

Let $\delta=\min_{i\ne j}|x_i-x_j|>0$.

*Claim:* for any $\mu_1,\mu_2$, some data point $x_{i^*}$ satisfies $\min_k |x_{i^*}-\mu_k|\ge \delta/2$.

*Proof of claim:* suppose instead every point is within distance $<\delta/2$ of $\mu_1$ or $\mu_2$. With $n\ge 3$ points and $2$ means, pigeonhole puts two points $x_i,x_j$ within $<\delta/2$ of the same mean. Then $|x_i-x_j|<\delta$, a contradiction.

Now bound the factors of $L$:

- **For every $i$**, each component density is at most $\frac{1}{\sqrt{2\pi}\sigma}$, and the weights sum to $1$. Hence
$$f(x_i)\le \frac{1}{\sqrt{2\pi}\,\sigma}.$$
- **For the far point $i^*$**, both components are evaluated at distance at least $\delta/2$. Hence
$$f(x_{i^*})\le \frac{1}{\sqrt{2\pi}\,\sigma}\,e^{-\delta^2/(8\sigma^2)}.$$

Multiplying the bounds over all $n$ points,
$$L\ \le\ (2\pi\sigma^2)^{-n/2}\,e^{-\delta^2/(8\sigma^2)}=:h(\sigma).$$

As in (a), $h(\sigma)\to0$ both as $\sigma\to0$ and as $\sigma\to\infty$. Since $h$ is continuous, it is bounded on $(0,\infty)$, and the bound is uniform in $\pi,\mu_1,\mu_2$. Hence $L$ is bounded. $\blacksquare$

**Remark.** The condition $n\ge3$ is sharp. With $n=2$ and tied variance, put $\mu_1=x_1$ and $\mu_2=x_2$. Then $L\ge\big(\tfrac{\min(\pi,1-\pi)}{\sqrt{2\pi}\,\sigma}\big)^2\to\infty$.

The same phenomenon makes EM for Gaussian mixtures occasionally "collapse" a component onto a single point. ESL (§8.5.1) notes exactly this degenerate maximum: a spike of infinite height at one observation. It also explains that EM is instead used to find a good local maximum.
