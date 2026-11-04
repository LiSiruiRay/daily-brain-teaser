# Answer: Random Quadratic Equations: Real Roots Almost Surely?

## Key Idea / Intuition

The roots are real exactly when $b^2 \ge c$ in (a), or $b^2 \ge ac$ in (b).

In (a) the two sides scale differently. A typical $b$ is of size $B$, so $b^2$ is of size $B^2$, while $c$ is only of size $B$. The quadratic term wins, and the "complex" region under the parabola becomes a vanishing sliver of the square.

In (b) the discriminant is homogeneous of degree 2 in $(a,b,c)$. Scaling the cube does not change the answer, so we get a fixed number strictly less than 1.

Dividing by $a$ does not rescue the analogy. The new coefficients $b/a$ and $c/a$ are neither uniform nor independent: they are heavy-tailed ratios.

---

## Formal Proof / Solution

**(a)** The roots are complex iff $c > b^2$.

Assume $B \ge 1$, so the parabola $c=b^2$ leaves the square through its top edge $c = B$, at $b = \pm\sqrt B$. The complex region is the area between the parabola and the top edge:

$$\text{Area} = \int_{-\sqrt B}^{\sqrt B} (B - b^2)\,db = 2B^{3/2} - \tfrac{2}{3}B^{3/2} = \tfrac43 B^{3/2}.$$

The square has area $4B^2$, so

$$P(\text{complex}) = \frac{\tfrac43 B^{3/2}}{4B^2} = \frac{1}{3\sqrt B}, \qquad p(B) = 1 - \frac{1}{3\sqrt B} \xrightarrow{B\to\infty} 1.$$

For example, $B=4$ gives $p = 5/6$. "Random" monic quadratics of this kind have real roots with probability tending to $1$.

**(b)** The roots are real iff $b^2 \ge ac$. This condition is invariant under $(a,b,c)\mapsto(\lambda a,\lambda b,\lambda c)$, so we may take $B=1$. The answer does not depend on $B$.

- **Case $ac \le 0$** (probability $1/2$). Then $b^2 \ge 0 \ge ac$, so the roots are always real.
- **Case $ac > 0$** (probability $1/2$). By symmetry we may take $a, c$ independent and uniform on $(0,1)$, and $|b|$ uniform on $(0,1)$, independent of them. The roots are complex iff $|b| < \sqrt{ac}$. Since $\sqrt{ac} \le 1$, conditioning on $(a,c)$ gives
$$P(\text{complex}\mid a,c) = \sqrt{ac}.$$
Averaging and using independence,
$$P(\text{complex}\mid ac>0) = \mathbb E[\sqrt a]\,\mathbb E[\sqrt c] = \left(\int_0^1 \sqrt t\,dt\right)^2 = \left(\tfrac23\right)^2 = \tfrac49.$$

Combining the two cases,

$$P(\text{real}) = 1 - \tfrac12\cdot\tfrac49 = \frac{7}{9}.$$

**(c)** Write $b' = b/a$ and $c' = c/a$. The equation becomes $x^2 + 2b'x + c' = 0$, but $(b',c')$ is not uniform on a large square.

- **Not uniform.** Each ratio has a heavy-tailed, sharply peaked distribution. Its density is constant on $[-1,1]$ and decays like $1/t^2$ outside. Most of the mass sits near the origin, which is exactly where the parabola region $c' > b'^2$ is not negligible.
- **Not independent.** $b'$ and $c'$ share the denominator $a$, so they are dependent.

The heart of the matter is that "uniform on a huge square" is not a scale-free notion. Part (a)'s answer is driven by the mismatch between the degree-2 term $b^2$ and the degree-1 term $c$ at large scale. Part (b) is homogeneous and therefore has a genuine scale-free answer, $7/9$.

The moral is a Bertrand-paradox-style lesson: "pick a random equation" has no meaning until the distribution is specified, and natural-looking reductions can silently change it.

*Reference:* Part (a) is Problem 50, "Random Quadratic Equations," in F. Mosteller, *Fifty Challenging Problems in Probability with Solutions*. The book warns that the three-coefficient case differs; part (b) works that case out.
