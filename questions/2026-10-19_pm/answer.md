# Answer: The Derivative That Drags Its Function Along

## Key Idea / Intuition

Think of $f+f'=g$ as the ODE $y'=-y+g$. The term $-y$ pulls $y$ toward the "input" $g$, and $g$ is eventually close to $L$, so $y$ gets pulled to $L$. The function "forgets" its past exponentially fast.

Algebraically, the integrating factor $e^x$ turns the combination $f+f'$ into a single derivative: $(e^x f)'=e^x(f+f')$. So $f = \dfrac{e^x f}{e^x}$ is a quotient whose numerator and denominator have derivative ratio $f+f'\to L$. This is exactly the setting of L'Hôpital's rule.

---

## Formal Proof / Solution

### Step 1: The integrating factor

Set $g = f+f'$. Then

$$\frac{d}{dx}\big(e^x f(x)\big) = e^x\big(f(x)+f'(x)\big) = e^x g(x).$$

### Step 2: Fast route via L'Hôpital

Write $f(x)=\dfrac{e^x f(x)}{e^x}$. The denominator $e^x\to\infty$, and the ratio of derivatives is

$$\frac{(e^x f)'}{(e^x)'} = \frac{e^x g(x)}{e^x} = g(x)\to L.$$

We use the version of L'Hôpital's rule that requires **only the denominator** to tend to $\infty$, with no assumption on the numerator (Rudin, *PMA*, Thm 5.13). It gives $f(x)\to L$.

### Step 3: Self-contained $\varepsilon$-argument (no L'Hôpital)

Fix $\varepsilon>0$ and choose $M$ such that $|g(t)-L|<\varepsilon$ for all $t\ge M$. For $x> M$, integrate Step 1 from $M$ to $x$. The integrand $e^t g(t)$ is a derivative, so the fundamental theorem of calculus applies in the form needed here. Writing $e^t g = e^t L + e^t(g-L)$ gives

$$e^x f(x) - e^M f(M) = L\,(e^x-e^M) + \int_M^x e^t\big(g(t)-L\big)\,dt.$$

The last integral has absolute value at most $\varepsilon(e^x-e^M)$. Divide by $e^x$:

$$f(x) = e^{M-x}f(M) + L\,(1-e^{M-x}) + R(x),\qquad |R(x)|\le \varepsilon.$$

As $x\to\infty$, $e^{M-x}\to 0$. Hence

$$\limsup_{x\to\infty}|f(x)-L|\le\varepsilon.$$

Since $\varepsilon$ was arbitrary, $f(x)\to L$.

*(Technical remark: if one prefers to avoid integrating a derivative that might not be Riemann integrable, apply the mean value theorem to $h(x)=e^x f(x) - (L\pm\varepsilon)e^x$. Its derivative $e^x(g-L\mp\varepsilon)$ has a fixed sign on $[M,\infty)$, so $h$ is monotone there. This yields the same two-sided bound.)*

### Step 4: The derivative

We have $f'(x) = g(x) - f(x)$. Since $g\to L$ and $f\to L$, it follows that $f'(x)\to L-L=0$. $\blacksquare$

---

## Follow-ups

1. **$f+f''\to 0$: fails.** Take $f(x)=\sin x$. Then $f+f''\equiv 0$, but $f$ oscillates forever. The equation $y''+y=0$ is an *undamped* oscillator, so there is no forgetting mechanism.

2. **$f-f'\to 0$: fails.** Take $f(x)=e^x$. Then $f-f'\equiv 0$, but $f\to\infty$. The equation $y'=y-g$ is *unstable*: the term $+y$ pushes away from equilibrium instead of pulling toward it. In the proof, the integrating factor becomes $e^{-x}$, which tends to $0$ rather than $\infty$, and the argument collapses.

3. **$f+2f'\to L$: works.** Use the integrating factor $e^{x/2}$:
$$\frac{(e^{x/2}f)'}{(e^{x/2})'} = \frac{\tfrac12 e^{x/2}(f+2f')}{\tfrac12 e^{x/2}} = f+2f' \to L.$$
In general, $f+cf'\to L$ forces $f\to L$ exactly when $c>0$.

**Moral:** the hypothesis is about stability of a linear ODE. Whether $f$ converges depends on the sign of the characteristic root of $y + c\,y' = 0$. A negative root $-1/c$ (that is, $c>0$) gives decay and convergence. A positive root gives blow-up. A purely imaginary pair, as in $y''+y=0$, gives oscillation.
