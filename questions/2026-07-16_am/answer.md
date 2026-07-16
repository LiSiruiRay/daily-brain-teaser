# Answer: The Holomorphic Function Determined by Its Real Part

## Key Idea / Intuition

The Cauchy–Riemann equations are the bridge between real and complex information: they link partial derivatives of $u$ and $v$ so tightly that knowing $u \equiv 0$ forces all partial derivatives of $v$ to vanish too, making $v$ (and hence $f$) locally constant, and by connectedness, globally constant.

For the modulus case, if $|f|^2 = u^2 + v^2 = c$, differentiating this real constraint twice (once in $x$, once in $y$) and invoking Cauchy–Riemann creates a system of equations for $u$ and $v$ that forces their gradients to vanish — unless $c = 0$, which forces $f \equiv 0$ directly.

---

## Formal Proof / Solution

### Part 1: $u \equiv 0$ implies $f$ is constant

Since $f = u + iv$ is holomorphic on $\Omega$, the Cauchy–Riemann equations hold:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.$$

If $u \equiv 0$ on $\Omega$, then $\frac{\partial u}{\partial x} = \frac{\partial u}{\partial y} = 0$ everywhere. By Cauchy–Riemann:
$$\frac{\partial v}{\partial y} = \frac{\partial u}{\partial x} = 0, \qquad \frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y} = 0.$$

So $\nabla v \equiv 0$ on $\Omega$. Since $\Omega$ is connected, $v$ is constant, say $v \equiv c$. Therefore $f = 0 + ic$ is constant. $\blacksquare$

---

### Part 2: $|f|$ constant implies $f$ is constant

Suppose $|f(z)|^2 = u^2 + v^2 \equiv c^2$ for some $c \geq 0$ on $\Omega$.

**Case 1:** $c = 0$. Then $u^2 + v^2 = 0$, so $u = v = 0$ everywhere, and $f \equiv 0$.

**Case 2:** $c > 0$. Differentiate $u^2 + v^2 = c^2$ with respect to $x$ and $y$:
$$u\,u_x + v\,v_x = 0, \qquad u\,u_y + v\,v_y = 0.$$

Apply Cauchy–Riemann ($u_x = v_y$, $u_y = -v_x$):
$$u\,u_x + v\,v_x = 0 \quad \Rightarrow \quad u\,v_y - v\,u_y = 0 \quad \text{(using CR on the first)}$$

More directly, substitute CR into the two equations:
$$u\,u_x + v\,v_x = 0 \tag{i}$$
$$u\,u_y + v\,v_y = 0 \quad \Rightarrow \quad -u\,v_x + v\,u_x = 0 \tag{ii}$$

This is a linear system in $(u_x, v_x)$:
$$\begin{pmatrix} u & v \\ v & -u \end{pmatrix} \begin{pmatrix} u_x \\ v_x \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}.$$

The determinant of the coefficient matrix is $-(u^2 + v^2) = -c^2 \neq 0$. So the only solution is $u_x = v_x = 0$. By Cauchy–Riemann, $u_y = v_y = 0$ as well.

Thus $\nabla u = \nabla v = 0$ on $\Omega$, and by connectedness, $u$ and $v$ are both constant. So $f$ is constant. $\blacksquare$

---

### Summary

| Condition | Forces |
|-----------|--------|
| $\text{Re}(f) = 0$ | $f \equiv \text{const}$ via CR + connectedness |
| $|f| = \text{const}$ | $f \equiv \text{const}$ via CR + linear algebra |

Both results highlight the same theme: **holomorphic functions are rigid** — real data plus the Cauchy–Riemann constraint pins down the complex function completely.
