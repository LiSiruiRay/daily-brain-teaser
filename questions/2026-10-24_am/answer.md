# Answer: The Integral That Only Cares About the Ratio

## Key Idea / Intuition

Scale both $\sin x$ and $\cos x$ by the same factor $\lambda$. Then $(\sqrt{\sin x}+\sqrt{\cos x})^4$ scales by $\lambda^2$, so the integrand has degree $-2$. The measure $\frac{dx}{\cos^2 x}=d(\tan x)$ also has degree $-2$. This means the integrand is really $(\text{a function of } \tan x)\cdot d(\tan x)$: only the *ratio* $\sin x/\cos x$ matters.

Substituting $t=\tan x$ sends the quarter-circle $[0,\pi/2]$ to the half-line $[0,\infty)$. One more substitution, $u=\sqrt t$, removes the square roots and leaves an elementary rational integral.

---

## Formal Proof / Solution

**Step 1: Factor out $\cos^2 x$.**

On $(0,\pi/2)$ we have $\sin x=\cos x\tan x$. Therefore

$$
\left(\sqrt{\sin x}+\sqrt{\cos x}\right)^4=\cos^2 x\,\left(1+\sqrt{\tan x}\right)^4 .
$$

This gives

$$
I=\int_0^{\pi/2}\frac{1}{(1+\sqrt{\tan x})^4}\cdot\frac{dx}{\cos^2 x}.
$$

**Step 2: Substitute $t=\tan x$.**

We have $dt=\sec^2x\,dx$, and $t$ runs from $0$ to $\infty$:

$$
I=\int_0^{\infty}\frac{dt}{(1+\sqrt t)^4}.
$$

The integrand decays like $t^{-2}$, so the integral converges.

**Step 3: Substitute $u=\sqrt t$.**

With $t=u^2$ and $dt=2u\,du$:

$$
I=\int_0^\infty\frac{2u\,du}{(1+u)^4}.
$$

**Step 4: Evaluate.**

Write $u=(1+u)-1$:

$$
I=2\int_0^\infty\left[\frac{1}{(1+u)^3}-\frac{1}{(1+u)^4}\right]du
=2\left(\frac12-\frac13\right)=\frac13 .
$$

$$
\boxed{I=\tfrac13}
$$

---

### Bonus: the general family

The same argument works because $(\sin^p x+\cos^p x)^{2/p}=\cos^2x\,(1+\tan^p x)^{2/p}$. So

$$
J_p:=\int_0^{\pi/2}\frac{dx}{(\sin^p x+\cos^p x)^{2/p}}=\int_0^\infty\frac{dt}{(1+t^p)^{2/p}}.
$$

Now substitute $v=t^p$, so that $dt=\frac1p v^{1/p-1}\,dv$:

$$
J_p=\frac1p\int_0^\infty\frac{v^{1/p-1}}{(1+v)^{2/p}}\,dv=\frac1p\,B\!\left(\tfrac1p,\tfrac1p\right).
$$

This uses $\int_0^\infty \frac{v^{a-1}}{(1+v)^{a+b}}dv=B(a,b)$ with $a=b=\frac1p$.

**Sanity checks:**

| $p$ | Integrand | $\frac1p B(\frac1p,\frac1p)$ |
|---|---|---|
| $2$ | $\dfrac{1}{\sin^2x+\cos^2x}=1$, integral $=\pi/2$ | $\tfrac12 B(\tfrac12,\tfrac12)=\tfrac12\cdot\pi=\tfrac{\pi}{2}$ ✓ |
| $1$ | $\dfrac{1}{(\sin x+\cos x)^2}$, integral $=\int_0^\infty\frac{dt}{(1+t)^2}=1$ | $B(1,1)=1$ ✓ |
| $\tfrac12$ | our problem | $2B(2,2)=2\cdot\frac{1!\,1!}{3!}=\tfrac13$ ✓ |

**Takeaway:** Suppose an integrand in $(\sin x,\cos x)$ is homogeneous of degree $-2$. Then dividing by $\cos^2 x$ and substituting $t=\tan x$ always turns the integral over $[0,\pi/2]$ into a one-variable integral over $[0,\infty)$. The geometry of the quarter-circle drops out, and only the slope remains.
