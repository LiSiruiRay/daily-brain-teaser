# Answer: The Integral That Only Sees the Tangent

## Key Idea / Intuition

The denominator is homogeneous. Scaling $(\sin x,\cos x)$ by $\lambda$ scales $(\sqrt{\sin x}+\sqrt{\cos x})^4$ by $\lambda^2$. So the denominator equals $\cos^2 x$ times a function of the ratio $\tan x$. On $[0,\pi/2)$ the ratio $\tan x$ runs over $[0,\infty)$, and the leftover $1/\cos^2 x$ is precisely the Jacobian $d(\tan x)/dx$. The trigonometric integral therefore becomes a rational-type integral on $[0,\infty)$. After one more substitution $u = t^2$ it is a one-line computation.

---

## Formal Proof / Solution

**Step 1 — Pull out $\cos^2 x$.** For $0 \le x < \pi/2$ we have $\cos x>0$, so

$$
\sqrt{\sin x}+\sqrt{\cos x} = \sqrt{\cos x}\,\bigl(1+\sqrt{\tan x}\bigr),
$$

and raising this to the fourth power gives

$$
\left(\sqrt{\sin x}+\sqrt{\cos x}\right)^4 = \cos^2 x\,\bigl(1+\sqrt{\tan x}\bigr)^4 .
$$

Hence

$$
I = \int_0^{\pi/2} \frac{\sec^2 x}{\bigl(1+\sqrt{\tan x}\bigr)^4}\,dx .
$$

**Step 2 — Substitute $u=\tan x$.** Then $du=\sec^2 x\,dx$, and $u$ runs from $0$ to $\infty$:

$$
I = \int_0^\infty \frac{du}{(1+\sqrt u)^4}.
$$

**Step 3 — Substitute $u=t^2$.** Then $du = 2t\,dt$:

$$
I = \int_0^\infty \frac{2t}{(1+t)^4}\,dt .
$$

**Step 4 — Write $t=(1+t)-1$.** This splits the integrand into two simple powers:

$$
I = 2\int_0^\infty \left[\frac{1}{(1+t)^3}-\frac{1}{(1+t)^4}\right]dt
= 2\left[\frac12-\frac13\right] = \frac13 .
$$

$$
\boxed{\,I=\tfrac13\,}
$$

**Sanity check.** The integrand equals $1$ at the endpoints and $1/8$ at $x=\pi/4$. Its average over an interval of length $\pi/2\approx1.57$ should therefore be around $0.2$, which gives roughly $0.33$. ✓

**Beta-function viewpoint.** The integral in Step 3 is $2\,B(2,2)$, since

$$
\int_0^\infty \frac{t^{p-1}}{(1+t)^{p+q}}\,dt = B(p,q),
$$

and $B(2,2)=\frac{1!\,1!}{3!}=\frac16$. This again gives $2\cdot\tfrac16=\tfrac13$.

**Warm-up variant.** Apply the same trick:

$$
\int_0^{\pi/2}\frac{dx}{(a\sin x+b\cos x)^2}
=\int_0^{\pi/2}\frac{\sec^2 x\,dx}{(a\tan x+b)^2}
=\int_0^\infty\frac{du}{(au+b)^2}
=\left[-\frac{1}{a(au+b)}\right]_0^\infty=\frac{1}{ab}.
$$

**General principle.** Let $R(s,c)$ be homogeneous of degree $-2$ in $(s,c)$. Then

$$
\int_0^{\pi/2} R(\sin x,\cos x)\,dx = \int_0^\infty R(u,1)\,du .
$$

Both computations above are instances of this identity.
