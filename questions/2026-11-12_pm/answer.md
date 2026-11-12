# Answer: How Many Zeros Can a Bounded Function Afford?

## Key Idea / Intuition

Every zero of a bounded holomorphic function has a cost. Dividing out a zero at $a$ by the disk automorphism $\varphi_a(z)=\frac{z-a}{1-\bar a z}$ does not change the size of $f$ on the boundary circle, because $|\varphi_a|=1$ there. It does inflate the value at the origin by the factor $1/|a|$. A zero close to the origin therefore forces $|f(0)|$ to be small relative to $\sup|f|$. With a "budget" of $\sup|f|/|f(0)| = 2$, the function can pay for one zero of modulus $\le \tfrac12$, but two such zeros would cost a factor of at least $4$. This is the zero-counting content of Jensen's formula, obtained here with nothing more than the maximum modulus principle.

---

## Formal Proof / Solution

**Blaschke factors.** For $|a|<1$ let
$$\varphi_a(z)=\frac{z-a}{1-\bar a z}.$$
This function is holomorphic on a neighborhood of $\overline{\mathbb{D}}$ and vanishes only at $a$, where the zero is simple. Its value at the origin satisfies $|\varphi_a(0)|=|a|$. A direct computation gives
$$1-|\varphi_a(z)|^2=\frac{(1-|a|^2)(1-|z|^2)}{|1-\bar a z|^2}.$$
Since $|1-\bar a z|\ge 1-|a|>0$, the right-hand side tends to $0$ uniformly as $|z|\to 1$. Hence
$$\min_{|z|=\rho}|\varphi_a(z)|\xrightarrow[\rho\to1^-]{}1. \tag{$*$}$$

**(a)** Suppose, for contradiction, that $f$ has two zeros $a,b$ (possibly $a=b$ for a double zero) with $|a|,|b|\le\tfrac12$. Because $f(0)=1$, neither $a$ nor $b$ is zero. Define
$$g(z)=\frac{f(z)}{\varphi_a(z)\,\varphi_b(z)}.$$
The zeros of the denominator are cancelled by zeros of $f$ of at least the same multiplicity. So $g$ has only removable singularities and extends to a holomorphic function on $\mathbb{D}$.

Fix $\rho\in(\tfrac12,1)$. By the maximum modulus principle on $\{|z|\le\rho\}$,
$$|g(0)|\le\max_{|z|=\rho}|g(z)|\le\frac{2}{\min_{|z|=\rho}|\varphi_a|\cdot\min_{|z|=\rho}|\varphi_b|}.$$
Let $\rho\to1^-$. By $(*)$ the right-hand side tends to $2$, so $|g(0)|\le 2$.

On the other hand,
$$|g(0)|=\frac{|f(0)|}{|\varphi_a(0)||\varphi_b(0)|}=\frac{1}{|a|\,|b|}\ge\frac{1}{(1/2)(1/2)}=4.$$
This contradicts $|g(0)|\le 2$. Hence $f$ has at most one zero in $\{|z|\le\tfrac12\}$. $\blacksquare$

**(b) Sharpness.** Take
$$f(z)=-2\,\varphi_{1/2}(z)=-2\,\frac{z-\tfrac12}{1-\tfrac z2}.$$
- It is holomorphic on $\mathbb{D}$.
- Since $|\varphi_{1/2}|<1$ on $\mathbb{D}$, we get $|f|<2$.
- At the origin, $f(0)=-2\cdot(-\tfrac12)=1$.
- It vanishes at $z=\tfrac12$, which lies on the boundary of the disk $\{|z|\le \tfrac12\}$.

So exactly one zero is attained.

**(c) General version.** Let $a_1,\dots,a_n$ be zeros in $\{|z|\le r\}$, counted with multiplicity. Divide by all $n$ Blaschke factors:
$$g=\frac{f}{\prod_{k=1}^n\varphi_{a_k}}.$$
The same argument as in (a) gives $|g(0)|\le M$, and also
$$|g(0)|=\frac{1}{\prod_k |a_k|}\ge r^{-n}.$$
Therefore $r^{-n}\le M$, which rearranges to
$$n\le\frac{\log M}{\log(1/r)}.$$

**Remark (Jensen's formula).** The inequality is a shadow of Jensen's formula. If $f$ is holomorphic near $\{|z|\le R\}$ with $f(0)\ne0$, then
$$\log|f(0)|=\sum_{|a_k|<R}\log\frac{|a_k|}{R}+\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|\,d\theta.$$
Each zero contributes a negative term $\log(|a_k|/R)$. The boundary average, here at most $\log M$, must pay for all of these terms. This is the same "zeros cost growth" principle that underlies Hadamard's factorization theorem.
