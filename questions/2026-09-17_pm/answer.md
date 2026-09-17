# Answer: The Entire Function That Grows Too Slowly

## Key Idea / Intuition

The Taylor series of an entire function is its power series centered at zero, and the coefficients are controlled by Cauchy's integral formula. If the function grows slower than $|z|^1$, it grows slower than any linear function, which means all coefficients of degree $\geq 1$ must vanish. This is a souped-up version of Liouville's theorem: not just boundedness, but any sub-polynomial growth kills all higher-order terms.

---

## Formal Proof / Solution

**Step 1: Cauchy's estimate.**

Since $f$ is entire, it has a Taylor expansion $f(z) = \sum_{n=0}^\infty a_n z^n$. The $n$-th coefficient satisfies Cauchy's estimate:

$$|a_n| \leq \frac{\max_{|z|=R} |f(z)|}{R^n}$$

for any $R > 0$.

**Step 2: Apply the growth bound.**

On the circle $|z| = R$, we have $|f(z)| \leq C R^{1/2}$, so:

$$|a_n| \leq \frac{C R^{1/2}}{R^n} = C R^{1/2 - n}.$$

**Step 3: Take $R \to \infty$.**

- For $n \geq 1$: the exponent $\frac{1}{2} - n \leq -\frac{1}{2} < 0$, so $R^{1/2 - n} \to 0$ as $R \to \infty$. Therefore $a_n = 0$ for all $n \geq 1$.

- For $n = 0$: the estimate gives $|a_0| \leq C R^{1/2} \to \infty$, which is no constraint.

**Step 4: Conclusion.**

All Taylor coefficients $a_n$ vanish for $n \geq 1$, so $f(z) = a_0$ is a **constant function**.

---

**Remark (general principle):** If $f$ is entire and $|f(z)| \leq C|z|^\alpha$ for all large $|z|$, where $\alpha \geq 0$, then $f$ is a **polynomial of degree at most $\lfloor \alpha \rfloor$**. The classic Liouville theorem is the case $\alpha = 0$. Here $\alpha = 1/2$, so $\lfloor 1/2 \rfloor = 0$ and $f$ must be constant.
