# Answer: Positive Real Part of the Derivative Forces Injectivity

## Key Idea / Intuition

In one real variable, $g' > 0$ forces $g(b) - g(a) > 0$ because $g(b) - g(a)$ is the integral of $g'$, which is positive. Here, $f(b) - f(a)$ is $(b-a)$ times the *average* of $f'$ along the segment from $a$ to $b$. Each value of $f'$ lies in the open right half-plane. That half-plane is convex, so the average also lies in it, and in particular the average is not $0$. Convexity is used twice: once in the domain, so the segment stays inside $D$, and once in the target, since the right half-plane is closed under averaging.

---

## Formal Proof / Solution

### (a) Injectivity

Take $a \neq b$ in $D$. Because $D$ is convex, the segment $\gamma(t) = a + t(b-a)$, $t \in [0,1]$, lies in $D$. By the fundamental theorem of calculus along $\gamma$:
$$
f(b) - f(a) = \int_0^1 \frac{d}{dt} f(\gamma(t))\,dt = (b-a)\int_0^1 f'\big(a + t(b-a)\big)\,dt.
$$
Call the last integral $I$. Then
$$
\operatorname{Re} I = \int_0^1 \operatorname{Re} f'\big(a + t(b-a)\big)\,dt > 0,
$$
because the integrand is continuous and strictly positive on $[0,1]$. So $I \neq 0$. Since also $b - a \neq 0$, we get
$$
f(b) - f(a) = (b-a)\, I \neq 0.
$$
Hence $f$ is injective. $\blacksquare$

*Remark.* The same argument works if $\operatorname{Re}\big(e^{i\alpha} f'\big) > 0$ for some fixed angle $\alpha$. In words: it suffices that $f'(D)$ lies in some open half-plane whose boundary passes through $0$.

### (b) The example $f(z) = z + z^2/2$

**Injectivity on $\mathbb{D}$.** We have $f'(z) = 1 + z$. Writing $z = x + iy$ with $|z| < 1$ gives $x > -1$, so
$$
\operatorname{Re} f'(z) = 1 + x > 0.
$$
The disk is convex, so part (a) shows $f$ is injective on $\mathbb{D}$.

*Sanity check by direct algebra:*
$$
f(a) - f(b) = (a-b)\left(1 + \frac{a+b}{2}\right).
$$
For $a, b \in \mathbb{D}$ we have $|a+b| < 2$, so the second factor cannot vanish. This confirms the result.

**Sharpness.** Let $r > 1$. The point $-1$ lies in $\{|z| < r\}$, and $f'(-1) = 0$. Expanding $f$ around $-1$:
$$
f(-1 + w) = (-1 + w) + \frac{(-1+w)^2}{2} = -\frac12 + \frac{w^2}{2}.
$$
For small $w \neq 0$, both $-1 + w$ and $-1 - w$ lie in $\{|z| < r\}$, and they have the same image $-\tfrac12 + \tfrac{w^2}{2}$. So $f$ is not injective on any disk of radius $r > 1$.

More conceptually: a holomorphic function is never injective near a critical point, since there it behaves locally like $w \mapsto w^k$ with $k \ge 2$. The critical point $-1$ sits exactly on the unit circle, so $\mathbb{D}$ is the largest disk centered at $0$ on which $f$ is injective. $\blacksquare$
