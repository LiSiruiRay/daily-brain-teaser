# Answer: $L^p$ Norm $\to$ $L^\infty$

## Key Idea

Use the **Squeeze Theorem**: find upper and lower bounds for $\|f\|_p$ that both converge to $\|f\|_\infty$ as $p \to \infty$.

---

## Proof

Let $M = \|f\|_\infty$.

### Upper Bound

Since $|f(x)| \leq M$ a.e., we have:

$$\|f\|_p = \left(\int_X |f|^p \, d\mu\right)^{1/p} \leq \left(\int_X M^p \, d\mu\right)^{1/p} = M \cdot \mu(X)^{1/p}$$

Since $\mu(X) < \infty$, as $p \to \infty$:

$$\mu(X)^{1/p} = e^{\frac{1}{p}\ln \mu(X)} \to e^0 = 1$$

Therefore $\displaystyle\limsup_{p \to \infty} \|f\|_p \leq M$.

---

### Lower Bound

For any $\varepsilon > 0$, define:

$$E_\varepsilon = \{x \in X : |f(x)| > M - \varepsilon\}$$

By definition of essential supremum, $\mu(E_\varepsilon) > 0$. Then:

$$\|f\|_p \geq \left(\int_{E_\varepsilon} |f|^p \, d\mu\right)^{1/p} \geq (M - \varepsilon) \cdot \mu(E_\varepsilon)^{1/p}$$

As $p \to \infty$, again $\mu(E_\varepsilon)^{1/p} \to 1$, so:

$$\liminf_{p \to \infty} \|f\|_p \geq M - \varepsilon$$

Since $\varepsilon > 0$ was arbitrary:

$$\liminf_{p \to \infty} \|f\|_p \geq M$$

---

### Conclusion

Combining both bounds:

$$M \leq \liminf_{p \to \infty} \|f\|_p \leq \limsup_{p \to \infty} \|f\|_p \leq M$$

Therefore:

$$\lim_{p \to \infty} \|f\|_p = M = \|f\|_\infty \qquad \blacksquare$$

---

## Why $\mu(X) < \infty$ is needed

If $\mu(X) = \infty$, the upper bound step fails — $\mu(X)^{1/p} \to \infty$ and the argument breaks. (Counterexample: $f \equiv 1$ on $\mathbb{R}$ with Lebesgue measure gives $\|f\|_p = \infty$ for all $p < \infty$ but $\|f\|_\infty = 1$.)
