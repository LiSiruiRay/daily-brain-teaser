# Answer: The Square-Root Sandwich

## Key Idea / Intuition

Count degrees. The denominator $(\sqrt{\sin x}+\sqrt{\cos x})^4$ is homogeneous of degree $2$ in the pair $(\sin x, \cos x)$. So you can factor out $\cos^2 x$, and what remains depends only on the ratio $\tan x$. The factored-out $1/\cos^2 x = \sec^2 x$ is exactly the derivative of $\tan x$. The substitution $t=\tan x$ therefore turns the trigonometric integral into a rational one, with nothing left over. A second substitution, $u=\sqrt t$, removes the square root, and the result is a Beta integral.

The general principle is that any integrand $F(\sin x,\cos x)$ that is homogeneous of degree $-2$ becomes $\int_0^\infty F(t,1)\,dt$ under $t=\tan x$.

---

## Formal Proof / Solution

**Step 1: Factor out $\cos^2 x$.** For $x\in(0,\pi/2)$,
$$
\sqrt{\sin x}+\sqrt{\cos x} \;=\; \sqrt{\cos x}\,\bigl(1+\sqrt{\tan x}\bigr),
$$
so
$$
\left(\sqrt{\sin x}+\sqrt{\cos x}\right)^4 = \cos^2 x\,\bigl(1+\sqrt{\tan x}\bigr)^4 .
$$
Hence
$$
I = \int_0^{\pi/2} \frac{\sec^2 x\,dx}{\bigl(1+\sqrt{\tan x}\bigr)^4}.
$$

**Step 2: Substitute $t=\tan x$.** Then $dt=\sec^2 x\,dx$, and $t$ runs from $0$ to $\infty$:
$$
I = \int_0^\infty \frac{dt}{(1+\sqrt t)^4}.
$$
This converges, since the integrand behaves like $t^{-2}$ at infinity.

**Step 3: Substitute $t=u^2$.** Then $dt = 2u\,du$:
$$
I = \int_0^\infty \frac{2u\,du}{(1+u)^4}.
$$
Write $u=(1+u)-1$:
$$
I = 2\int_0^\infty \Bigl[(1+u)^{-3}-(1+u)^{-4}\Bigr]du
= 2\left(\frac12-\frac13\right) = \boxed{\frac13}.
$$

**Sanity check.** The integrand equals $1$ at both endpoints and $1/8$ at $x=\pi/4$. A function that drops quickly from $1$ to small values over an interval of length $\pi/2\approx 1.57$ plausibly has integral $\approx 0.33$.

**Bonus (general $n$).** The same factorization gives
$$
\left(\sin^{1/n}x+\cos^{1/n}x\right)^{2n} = \cos^2 x\,\bigl(1+\tan^{1/n}x\bigr)^{2n}.
$$
With $t=\tan x$ and then $t=u^n$ (so $dt = n u^{n-1}\,du$):
$$
I_n = \int_0^\infty \frac{dt}{(1+t^{1/n})^{2n}} = n\int_0^\infty \frac{u^{n-1}}{(1+u)^{2n}}\,du = n\,B(n,n) = \frac{n\,\bigl((n-1)!\bigr)^2}{(2n-1)!}.
$$
Here we used $\int_0^\infty \frac{u^{a-1}}{(1+u)^{a+b}}du = B(a,b)$. Checks:
- $n=1$: $\int_0^{\pi/2}\frac{dx}{(\sin x+\cos x)^2}=1$.
- $n=2$: $2B(2,2)=2\cdot\frac16=\frac13$, matching the main problem.
