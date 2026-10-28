# Answer: Doubling Your Accuracy

## Key Idea / Intuition

Measuring rods one at a time is wasteful, because each measurement tells you about only one rod. If every measurement involves **both** rods, then each rod is effectively measured twice. Adding the sum and the difference recovers each length. The two independent errors then get averaged, which halves the variance. This is the seed of **weighing designs** and Hadamard designs in the theory of experimental design. The best designs use measurements whose coefficient vectors are orthogonal and have entries $\pm1$.

---

## Formal Proof / Solution

### 1. The scheme

Assume without loss of generality that $a \ge b$. If not, swap the names; the side-by-side comparison shows which rod sticks out.

- **Measurement 1 (end to end):** $S = (a+b) + \varepsilon_1$.
- **Measurement 2 (side by side):** $D = (a-b) + \varepsilon_2$.

Define

$$
\hat a = \frac{S+D}{2}, \qquad \hat b = \frac{S-D}{2}.
$$

**Unbiasedness.** Since $\mathbb{E}[\varepsilon_i]=0$,

$$
\mathbb{E}[\hat a] = \frac{(a+b)+(a-b)}{2} = a, \qquad \mathbb{E}[\hat b] = \frac{(a+b)-(a-b)}{2} = b.
$$

**Variance.** We have $\hat a - a = \tfrac12(\varepsilon_1+\varepsilon_2)$ and $\hat b - b = \tfrac12(\varepsilon_1-\varepsilon_2)$. The errors are independent, so

$$
\operatorname{Var}(\hat a) = \operatorname{Var}(\hat b) = \frac{\sigma^2+\sigma^2}{4} = \frac{\sigma^2}{2}.
$$

The two estimates are also uncorrelated:

$$
\operatorname{Cov}(\hat a,\hat b) = \tfrac14\big(\operatorname{Var}\varepsilon_1 - \operatorname{Var}\varepsilon_2\big) = 0.
$$

So with the same two measurements, each length is estimated as precisely as if it had been measured twice on its own. The accuracy is "doubled" in the sense that the variance is halved.

### 2. Optimality (bonus)

Write a general two-measurement design as $Y = X\theta + \varepsilon$, where $\theta = (a,b)^\top$. Here $X$ is a $2\times 2$ matrix with entries in $\{-1,0,1\}$ and $\operatorname{Cov}(\varepsilon)=\sigma^2 I$.

**Reduction to the matrix $X^\top X$.** For both $a$ and $b$ to be estimable, $X$ must be invertible. The unique linear unbiased estimator is then $\hat\theta = X^{-1}Y$. This is the same as least squares, so

$$
\operatorname{Cov}(\hat\theta) = \sigma^2 (X^\top X)^{-1}.
$$

**A lower bound on the diagonal.** Let $M = X^\top X$, which is symmetric positive definite. For such a matrix,

$$
(M^{-1})_{ii} \;\ge\; \frac{1}{M_{ii}}.
$$

To see this, apply Cauchy–Schwarz to $e_i^\top e_i = (M^{1/2}e_i)^\top(M^{-1/2}e_i)$:

$$
1 = (e_i^\top e_i)^2 \le (e_i^\top M e_i)(e_i^\top M^{-1} e_i).
$$

**Bounding $M_{ii}$.** The entry $M_{ii} = \sum_k x_{ki}^2$ is a sum of two terms, each at most $1$. So $M_{ii} \le 2$, and therefore

$$
\operatorname{Var}(\hat\theta_i) = \sigma^2 (M^{-1})_{ii} \ge \frac{\sigma^2}{2}.
$$

**When equality holds.** Equality requires two things:

- every entry of $X$ is $\pm1$, so that $M_{ii}=2$;
- $M$ is diagonal, so that Cauchy–Schwarz is tight.

That is exactly the sum/difference design. $\blacksquare$

### 3. $n$ rods, $n$ measurements (bonus)

The same argument shows that $\operatorname{Var}(\hat\theta_i) \ge \sigma^2/n$. Equality holds if and only if $X$ has entries $\pm1$ and $X^\top X = nI$, which means $X$ is a **Hadamard matrix**. In that case

$$
\hat\theta = \tfrac1n X^\top Y, \qquad \operatorname{Var}(\hat\theta_i) = \frac{\sigma^2}{n}.
$$

So $n$ measurements give each of the $n$ objects the precision of $n$ separate measurements. That is an $n$-fold gain over measuring one at a time. This is possible whenever a Hadamard matrix of order $n$ exists (for example, $n = 2^k$).

In a physical setting, "$+$" means placing a rod on one side of a two-pan balance and "$-$" means placing it on the other side. This is Hotelling's and Yates' **chemical balance weighing problem**.

---

### Why it's interesting

- **Field:** Probability / statistics (design of experiments).
- **The surprise:** you cannot get more measurements, but you can make each measurement carry information about every unknown. The noise then averages out across the measurements.
- **Connections:** the same idea underlies Hadamard spectroscopy, orthogonal designs in experimental design, and the general principle that orthogonal regressors minimize OLS variance.
- **Difficulty:** 2/5.
- **Source:** Mosteller, *Fifty Challenging Problems in Probability with Solutions*, problem "Doubling Your Accuracy." The optimality argument and the Hadamard generalization are standard extensions.
