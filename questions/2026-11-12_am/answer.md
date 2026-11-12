# Answer: A Univalent Map Cannot Shrink the Disk

## Key Idea / Intuition

A holomorphic map stretches infinitesimal area by the factor $|f'(z)|^2$, which is its real Jacobian. Because $f$ is injective, the area of the image is exactly $\int_{\mathbb D}|f'|^2\,dA$. Expand $f'$ in a power series. The functions $z^{n}$ are orthogonal on the disk, since rotating by $e^{i\theta}$ separates them. So $\int|f'|^2$ splits into a sum of non-negative contributions, one per coefficient. The linear term alone contributes exactly $\pi$, and every other term only adds area.

---

## Formal Proof / Solution

**Step 1: Area as an integral.**
Write $f=u+iv$. By the Cauchy–Riemann equations, the real Jacobian is

$$
\det\begin{pmatrix}u_x & u_y\\ v_x & v_y\end{pmatrix}=u_x^2+v_x^2=|f'(z)|^2 .
$$

Since $f$ is injective, the change-of-variables formula gives, for each $0<r<1$,

$$
\operatorname{Area}\big(f(\mathbb{D}_r)\big)=\int_{\mathbb{D}_r}|f'(z)|^2\,dA,\qquad \mathbb{D}_r=\{|z|<r\}.
$$

Injectivity is used exactly here. Without it, the integral counts area with multiplicity.

**Step 2: Expand and use orthogonality.**
Write $f(z)=\sum_{n\ge1}a_nz^n$ with $a_1=f'(0)=1$, so $f'(z)=\sum_{n\ge1}na_nz^{n-1}$. In polar coordinates $z=\rho e^{i\theta}$,

$$
\int_0^{2\pi} e^{i(n-1)\theta}\,\overline{e^{i(m-1)\theta}}\,d\theta = 2\pi\,\delta_{nm}.
$$

On the circle $|z|=\rho<r$ the series converges uniformly, so we may integrate term by term. All cross terms vanish:

$$
\int_{\mathbb{D}_r}|f'|^2\,dA=\sum_{n\ge1}n^2|a_n|^2\int_0^r \rho^{2n-2}\,2\pi\rho\,d\rho
=\pi\sum_{n\ge1}n|a_n|^2\,r^{2n}.
$$

**Step 3: Let $r\to1$.**
The sets $f(\mathbb{D}_r)$ increase to $f(\mathbb{D})$, and each term $n|a_n|^2r^{2n}$ increases in $r$. By monotone convergence on both sides,

$$
\operatorname{Area}\big(f(\mathbb{D})\big)=\pi\sum_{n\ge1}n|a_n|^2 \;\in[0,\infty].
$$

**Step 4: Conclude.**
Every term is non-negative and $a_1=1$, so

$$
\operatorname{Area}\big(f(\mathbb{D})\big)=\pi+\pi\sum_{n\ge2}n|a_n|^2\;\ge\;\pi.
$$

Equality holds iff $a_n=0$ for all $n\ge2$, that is, iff $f(z)=z$. $\blacksquare$

---

**Remarks.**
- More generally, for injective $f$ the same computation gives $\operatorname{Area}(f(\mathbb D))\ge \pi|f'(0)|^2$.
- **Gronwall's area theorem.** Apply the same idea to $g(z)=z+\sum_{n\ge0}b_nz^{-n}$, univalent on $|z|>1$. The complement of the image has non-negative area, which forces $\sum n|b_n|^2\le 1$. From this one gets Bieberbach's bound $|a_2|\le2$ for normalized univalent maps of the disk.
