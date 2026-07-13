# Answer: Frullani Integral: (e^{-x}-e^{-2x})/x

## Key Idea / Intuition

The integrand looks like a single ugly fraction, but hidden inside it is a **Frullani integral**: the formula that says $\int_0^\infty \frac{f(ax)-f(bx)}{x}\,dx = (f(0)-f(\infty))\ln(b/a)$ whenever $f$ is continuous and the limits at $0$ and $\infty$ exist. Here $f(x)=e^{-x}$, so $f(0)=1$, $f(\infty)=0$, and the ratio of the two "speeds" is $2/1$. The answer pops out in one line.

Alternatively, one can **differentiate under the integral sign**: introduce a parameter, swap differentiation and integration, then integrate back. Both routes lead to the same beautiful answer $\ln 2$.

---

## Formal Proof / Solution

### Method 1: Frullani's Integral

**Frullani's theorem.** If $f:[0,\infty)\to\mathbb{R}$ is continuous and $f(0)$, $f(\infty):=\lim_{x\to\infty}f(x)$ both exist, then for $0 < a < b$,

$$\int_0^\infty \frac{f(ax)-f(bx)}{x}\,dx = \bigl(f(0)-f(\infty)\bigr)\ln\!\frac{b}{a}.$$

Write our integral as

$$I = \int_0^\infty \frac{e^{-x} - e^{-2x}}{x}\,dx = \int_0^\infty \frac{f(1\cdot x)-f(2\cdot x)}{x}\,dx,\quad f(t)=e^{-t}.$$

Then $f(0)=1$, $f(\infty)=0$, $a=1$, $b=2$, so Frullani gives

$$\boxed{I = (1-0)\ln\!\frac{2}{1} = \ln 2.}$$

---

### Method 2: Differentiation Under the Integral Sign (Feynman)

Define

$$I(t) = \int_0^\infty \frac{e^{-x} - e^{-tx}}{x}\,dx, \quad t > 0.$$

Differentiate with respect to $t$ (justified by dominated convergence, since $|{-xe^{-tx}}/{x}| = e^{-tx}$ is integrable):

$$I'(t) = \int_0^\infty \frac{\partial}{\partial t}\!\left(\frac{e^{-x}-e^{-tx}}{x}\right)dx = \int_0^\infty e^{-tx}\,dx = \frac{1}{t}.$$

Integrate back: $I(t) = \ln t + C$.

Boundary condition: $I(1) = \int_0^\infty \frac{e^{-x}-e^{-x}}{x}\,dx = 0$, so $0 = \ln 1 + C = C$.

Therefore $I(t) = \ln t$, and

$$I = I(2) = \ln 2.$$

---

### Quick sanity check

For large $x$ the integrand decays like $e^{-x}$ (absolutely integrable). Near $x=0$, $e^{-x}-e^{-2x} \approx x - (2x - \cdots) = x(1-2)\cdot (-1)+\cdots \sim x$, so $(e^{-x}-e^{-2x})/x\to 1$: no singularity. The integral is well-defined. ✓
