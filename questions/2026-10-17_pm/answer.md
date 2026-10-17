# Answer: Two Integrals, One Curve

## Key Idea / Intuition

Each of the two terms in (a) looks impossible to integrate in elementary terms. But both describe the **same curve** $x^7+y^3=1$ in the unit square. One integral measures the area under it with vertical strips, and the other measures the same area with horizontal strips. So the two integrals are equal and $I=0$.

Part (b) uses the same idea: the graph of $f^{-1}$ is the graph of $f$ reflected across $y=x$. The area under $f^{-1}$ is a rectangle minus the area under $f$, and $f$ is easy to integrate.

---

## Formal Proof / Solution

### Part (a)

**Step 1: The two integrands are inverse functions.** Let $g(x)=(1-x^7)^{1/3}$ on $[0,1]$. For $x,y\in[0,1]$,
$$y=(1-x^7)^{1/3}\iff y^3=1-x^7 \iff x^7=1-y^3 \iff x=(1-y^3)^{1/7}.$$
So $g^{-1}(y)=(1-y^3)^{1/7}$, which is exactly the second integrand. Both are decreasing bijections of $[0,1]$ with $0\mapsto 1$ and $1\mapsto 0$.

**Step 2: Count one region in two ways.** Define
$$R=\{(x,y)\in[0,1]^2 : x^7+y^3\le 1\}.$$
Integrate the indicator $\mathbf 1_R$ over $[0,1]^2$, which is legitimate by Tonelli since it is nonnegative and measurable.

- **Vertical slices:** for fixed $x$, the condition is $0\le y\le (1-x^7)^{1/3}$, so
$$\operatorname{Area}(R)=\int_0^1 (1-x^7)^{1/3}\,dx.$$
- **Horizontal slices:** for fixed $y$, the condition is $0\le x\le (1-y^3)^{1/7}$, so
$$\operatorname{Area}(R)=\int_0^1 (1-y^3)^{1/7}\,dy.$$

**Step 3: Conclude.** The two integrals are equal, hence
$$\boxed{I=0}.$$

**Generalization.** The same argument gives, for all $p,q>0$,
$$\int_0^1 (1-x^p)^{1/q}\,dx=\int_0^1 (1-x^q)^{1/p}\,dx.$$

**Remark (Beta function check).** Substituting $t=x^7$ gives
$$\int_0^1 (1-x^7)^{1/3}dx=\tfrac17 B\!\left(\tfrac17,\tfrac43\right)=\frac{\Gamma(8/7)\,\Gamma(4/3)}{\Gamma(31/21)}.$$
This expression is symmetric in $3\leftrightarrow 7$, which confirms the result. The geometric argument needs none of this machinery.

### Part (b)

**Step 1: Locate the endpoints.** We have $f(0)=0$ and $f(1)=2$, so $f^{-1}$ maps $[0,2]$ onto $[0,1]$.

**Step 2: Substitute $y=f(x)$.** Then $dy=f'(x)\,dx$, and $y:0\to 2$ corresponds to $x:0\to1$. This gives
$$J=\int_0^1 x\,f'(x)\,dx.$$

**Step 3: Integrate by parts.**
$$J=\big[x f(x)\big]_0^1-\int_0^1 f(x)\,dx = 1\cdot 2-\int_0^1 (x^5+x)\,dx = 2-\left(\tfrac16+\tfrac12\right).$$
Therefore
$$\boxed{J=\tfrac43}.$$

**Geometric reading.** In general,
$$\int_a^b f+\int_{f(a)}^{f(b)} f^{-1} = b\,f(b)-a\,f(a).$$
The area under $f$ on $[0,1]$ and the area under $f^{-1}$ on $[0,2]$ together tile the $1\times 2$ rectangle. Part (a) is the special case where the curve is its own reflection, so the two pieces must have equal area.
