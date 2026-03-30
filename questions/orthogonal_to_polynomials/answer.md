# Orthogonality to All Monomials Forces Zero — Answer

## Step 1: Extend to all polynomials

By hypothesis, $\int_0^1 f(x) x^n dx = 0$ for each $n \geq 0$.

For any polynomial $p(x) = \sum_{k=0}^N a_k x^k$, linearity of the integral gives:
$$\int_0^1 f(x)\, p(x)\, dx = \sum_{k=0}^N a_k \int_0^1 f(x)\, x^k\, dx = \sum_{k=0}^N a_k \cdot 0 = 0$$

So $f$ is orthogonal to **every** polynomial.

---

## Step 2: Approximate $f$ by polynomials (Weierstrass)

By the **Weierstrass Approximation Theorem**, since $f$ is continuous on the compact interval $[0,1]$, there exists a sequence of polynomials $p_k$ such that:
$$\|p_k - f\|_\infty = \sup_{x \in [0,1]} |p_k(x) - f(x)| \to 0$$

---

## Step 3: Force $\int_0^1 f^2 = 0$

$$\int_0^1 f(x)^2\, dx = \int_0^1 f(x)\bigl(f(x) - p_k(x)\bigr)\, dx + \underbrace{\int_0^1 f(x)\, p_k(x)\, dx}_{=\, 0}$$

The remaining term is bounded by:
$$\left|\int_0^1 f(x)(f(x) - p_k(x))\, dx\right| \leq \|f\|_\infty \cdot \|f - p_k\|_\infty \cdot 1 \to 0$$

Since $\int_0^1 f^2$ is a fixed non-negative number bounded above by something going to 0:
$$\int_0^1 f(x)^2\, dx = 0$$

---

## Step 4: Conclude $f \equiv 0$

Since $f$ is continuous and $f(x)^2 \geq 0$ everywhere, and $\int_0^1 f^2 = 0$, we must have $f(x)^2 = 0$ for all $x \in [0,1]$.

(If $f(x_0)^2 > 0$ for some $x_0$, by continuity $f^2 > \epsilon$ on some interval, making the integral positive — contradiction.)

Therefore $f(x) = 0$ for all $x \in [0,1]$. $\blacksquare$

---

## The Key Move

The trick is choosing the polynomial to approximate $f$ **itself**, and then splitting:
$$\int f^2 = \int f(f - p_k) + \int f \cdot p_k = \text{small} + 0$$

Using $f$ as its own "test function" is what extracts the information from the orthogonality condition.

---

## Generalizations

- The same result holds with $\{x^n\}$ replaced by any set of functions whose linear span is **dense** in $C[0,1]$ (e.g., $\{\sin(nx)\}$, $\{\cos(nx)\}$ by Fourier theory).
- In $L^2[0,1]$: if $f \in L^2$ is orthogonal to all polynomials, then $f = 0$ a.e.
- This is the principle behind **moments determining distributions**: if two distributions have the same moments $\int x^n d\mu = \int x^n d\nu$ for all $n$, and the moment problem has a unique solution, then $\mu = \nu$.
