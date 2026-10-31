# Answer: The Quartic That Folds onto Itself

## Key Idea / Intuition

The map $x\mapsto 1/x$ swaps $(0,1)$ and $(1,\infty)$. Under it, $\frac{1}{1+x^4}$ turns into its "twin" $\frac{x^2}{1+x^4}$, so both integrals are equal. Averaging them gives the more symmetric integrand $\frac{1+x^2}{1+x^4}$. Dividing numerator and denominator by $x^2$ makes it a function of $u=x-\frac1x$ times exactly $du$. The quartic denominator then collapses to the quadratic $u^2+2$.

---

## Formal Proof / Solution

**Step 1: The inversion twin.** Substitute $x=1/t$, so $dx=-dt/t^2$:

$$
I=\int_0^\infty \frac{dx}{1+x^4}=\int_0^\infty \frac{1}{1+t^{-4}}\cdot\frac{dt}{t^2}
=\int_0^\infty \frac{t^2}{1+t^4}\,dt .
$$

Call this second integral $J$. We have shown $I=J$.

**Step 2: Average the two forms.**

$$
2I = I+J=\int_0^\infty \frac{1+x^2}{1+x^4}\,dx
=\int_0^\infty \frac{1+\frac{1}{x^2}}{x^2+\frac{1}{x^2}}\,dx ,
$$

where we divided the numerator and denominator by $x^2$.

**Step 3: The substitution $u=x-\frac1x$.**
- On $(0,\infty)$, $u$ is strictly increasing and maps $(0,\infty)$ bijectively onto $(-\infty,\infty)$.
- Its derivative is $du=\left(1+\frac1{x^2}\right)dx$.
- The denominator becomes $x^2+\frac1{x^2}=\left(x-\frac1x\right)^2+2=u^2+2$.

Hence

$$
2I=\int_{-\infty}^{\infty}\frac{du}{u^2+2}=\frac{1}{\sqrt2}\Big[\arctan\tfrac{u}{\sqrt2}\Big]_{-\infty}^{\infty}=\frac{\pi}{\sqrt2}.
$$

$$
\boxed{\,I=\int_0^\infty\frac{dx}{1+x^4}=\frac{\pi}{2\sqrt2}\,}
$$

**Sanity check: the difference.** The same idea with $v=x+\frac1x$ handles $J-I$:

$$
J-I=\int_0^\infty\frac{1-\frac1{x^2}}{x^2+\frac1{x^2}}\,dx=\int \frac{dv}{v^2-2}.
$$

As $x$ runs from $0$ to $\infty$, $v$ runs from $\infty$ down to $2$ and back up to $\infty$. The two halves cancel, so $J-I=0$, consistent with Step 1.

**Bonus.** Divide by $x^2$ again:

$$
\int_0^\infty \frac{x^2+1}{x^4+x^2+1}\,dx=\int_0^\infty\frac{1+\frac1{x^2}}{x^2+1+\frac1{x^2}}\,dx .
$$

With $u=x-\frac1x$ we get $x^2+1+\frac1{x^2}=u^2+3$, so

$$
\int_{-\infty}^{\infty}\frac{du}{u^2+3}=\frac{\pi}{\sqrt3}.
$$

**Takeaway.** For an integrand built from a palindromic (reciprocal-symmetric) polynomial, dividing by the middle power of $x$ rewrites everything in terms of $x\pm\frac1x$. The degree is halved, and the integrand becomes elementary in one stroke.
