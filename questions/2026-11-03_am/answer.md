# Answer: Maps from RP² to the Circle (and Borsuk–Ulam)

## Key Idea / Intuition

A map into $S^1$ is null-homotopic exactly when it has a continuous "angle function", that is, when it lifts to the universal cover $\mathbb{R}$. The only obstruction to lifting is what the map does to loops. In $\mathbb{RP}^2$ the nontrivial loop becomes trivial when traversed twice. Its image in $\pi_1(S^1)=\mathbb{Z}$ is therefore an integer $n$ with $2n=0$, so $n=0$, and the lift exists.

For (b), an odd map $h$ would give a map $h^2$ that descends to $\mathbb{RP}^2$. Lifting that map produces a continuous **square root** of $h^2$ defined on $\mathbb{RP}^2$, which means it is *even* on $S^2$. On the connected space $S^2$, $h$ can differ from this even square root only by a constant sign. So $h$ would be even and odd at the same time, which is impossible.

---

## Formal Proof / Solution

### (a) Every map $\mathbb{RP}^2\to S^1$ is null-homotopic

Let $p:\mathbb{R}\to S^1$, $p(t)=e^{2\pi i t}$, be the universal covering.

**Step 1: The induced map on $\pi_1$ is trivial.** The map $f$ induces a homomorphism
$$f_*:\pi_1(\mathbb{RP}^2)\cong\mathbb{Z}/2\longrightarrow \pi_1(S^1)\cong\mathbb{Z}.$$
If $g$ generates $\mathbb{Z}/2$ and $f_*(g)=n$, then $2n=f_*(g^2)=f_*(1)=0$. So $n=0$, because $\mathbb{Z}$ is torsion-free. Hence $f_*$ is trivial.

**Step 2: Lift.** The space $\mathbb{RP}^2$ is path-connected and locally path-connected, and
$$f_*\big(\pi_1(\mathbb{RP}^2)\big)=\{1\}=p_*\big(\pi_1(\mathbb{R})\big).$$
By the lifting criterion there is a continuous $F:\mathbb{RP}^2\to\mathbb{R}$ with $p\circ F=f$.

**Step 3: Contract.** Since $\mathbb{R}$ is contractible, define
$$H_t(y)=p\big((1-t)F(y)\big),\qquad t\in[0,1].$$
This is continuous, with $H_0=f$ and $H_1\equiv p(0)=1$. So $f$ is null-homotopic. $\blacksquare$

### (b) No odd map $S^2\to S^1$

Suppose $h:S^2\to S^1$ is continuous with $h(-x)=-h(x)$.

**Step 1: Descend to $\mathbb{RP}^2$.** Define $g:\mathbb{RP}^2\to S^1$ by
$$g([x]) = h(x)^2 .$$
This is well defined because $h(-x)^2=(-h(x))^2=h(x)^2$. It is continuous because $S^2\to\mathbb{RP}^2$ is a quotient map.

**Step 2: Take a continuous square root.** By Step 2 of (a), $g$ lifts. There is a continuous $G:\mathbb{RP}^2\to\mathbb{R}$ with $g=e^{2\pi i G}$. Set
$$r(x)=e^{\pi i\,G([x])},\qquad x\in S^2 .$$
Then $r$ is continuous and **even**, since $r(-x)=r(x)$. It also satisfies $r(x)^2=g([x])=h(x)^2$.

**Step 3: Compare signs.** The function $s(x)=h(x)/r(x)$ is continuous on $S^2$ with $s(x)^2=1$, so $s$ takes values in $\{\pm1\}$. Since $S^2$ is connected, $s\equiv\varepsilon$ is constant. Therefore
$$h(-x)=\varepsilon\, r(-x)=\varepsilon\, r(x)=h(x).$$
Combined with $h(-x)=-h(x)$, this gives $h(x)=0$. That contradicts $h(x)\in S^1$. $\blacksquare$

### (c) Borsuk–Ulam in dimension 2

Suppose $\varphi(x)\neq\varphi(-x)$ for every $x$. Then
$$h(x)=\frac{\varphi(x)-\varphi(-x)}{\lVert\varphi(x)-\varphi(-x)\rVert}$$
is a continuous map $S^2\to S^1$ with $h(-x)=-h(x)$. This contradicts (b). Hence some $x$ has $\varphi(x)=\varphi(-x)$. $\blacksquare$

---

**Remark.** The same argument shows that any map from a space with finite fundamental group, such as $\mathbb{RP}^n$ or a lens space, into $S^1$ is null-homotopic. In particular $\mathbb{RP}^2$ does not retract onto any circle inside it. The deeper lesson: **torsion in $\pi_1$ cannot be detected by maps to the circle.** Maps $X\to S^1$ up to homotopy correspond to $H^1(X;\mathbb{Z})\cong\operatorname{Hom}(\pi_1X,\mathbb{Z})$, and that group ignores torsion.
