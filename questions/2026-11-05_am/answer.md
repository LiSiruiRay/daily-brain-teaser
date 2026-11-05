# Answer: Injective Entire Functions Are Linear

## Key Idea / Intuition

Every entire function has a singularity at $\infty$ of exactly one type: removable, pole, or essential. A removable singularity makes $f$ bounded, hence constant. An essential singularity makes $f$ wildly non-injective: near $\infty$, $f$ comes arbitrarily close to every value. In particular it lands in the open set $f(\text{unit disk})$, which is already "used up." So $\infty$ must be a pole, which forces $f$ to be a polynomial. A polynomial of degree $n$ is generically $n$-to-$1$, so injectivity forces $n=1$.

---

## Formal Proof / Solution

Since $f$ is injective, it is nonconstant. Define
$$
g(w) = f(1/w), \qquad w\neq 0.
$$
Then $g$ is holomorphic on $\mathbb{C}\setminus\{0\}$, and $w=0$ is an isolated singularity of $g$. We examine the three possible cases.

**Case 1: removable singularity.** Then $g$ is bounded near $0$, so $f$ is bounded on $\{|z|>R\}$ for some $R$. It is also bounded on the compact set $\{|z|\le R\}$. Hence $f$ is a bounded entire function, so it is constant by Liouville's theorem. This contradicts injectivity.

**Case 2: essential singularity.** Let $D=\{|z|<1\}$.

- By the open mapping theorem, $U := f(D)$ is a nonempty open set.
- By Casorati–Weierstrass, the image of the punctured disk under $g$ is dense in $\mathbb{C}$:
$$
g(\{0<|w|<1\}) = f(\{|z|>1\}).
$$
- A dense set meets every nonempty open set, so it meets $U$.

Therefore there exist $z_1$ with $|z_1|<1$ and $z_2$ with $|z_2|>1$ such that $f(z_1)=f(z_2)$. Since $z_1\neq z_2$, this contradicts injectivity.

**Case 3: pole.** This is the only remaining possibility. Write $f(z)=\sum_{k\ge 0} a_k z^k$, valid on all of $\mathbb{C}$. Then
$$
g(w) = \sum_{k\ge 0} a_k w^{-k}, \qquad w \neq 0,
$$
which is the Laurent expansion of $g$ at $0$. A pole of order $n$ at $0$ means $a_k=0$ for all $k>n$ and $a_n\ne 0$. Hence $f$ is a polynomial of degree $n\ge 1$.

**Finishing: an injective polynomial has degree 1.** Consider $p(z)=f(z)-f(0)$, a polynomial of degree $n$.

- By the Fundamental Theorem of Algebra, $p$ has $n$ roots counted with multiplicity.
- By injectivity, $f(z)=f(0)$ only at $z=0$, so $z=0$ is the only root.
- Therefore $p(z)=a_n z^n$, that is, $f(z)=a_n z^n + f(0)$.

If $n\ge 2$, let $\omega=e^{2\pi i/n}\neq 1$. Then $f(\omega)=a_n+f(0)=f(1)$, which contradicts injectivity. Hence $n=1$ and
$$
f(z)=az+b,\qquad a\neq 0. \qquad\blacksquare
$$

---

## Remarks

- **Alternative ending.** An injective holomorphic function has $f'\neq 0$ everywhere, since near a zero of $f'$ of order $m$ the map is $(m+1)$-to-$1$. A polynomial with nowhere-vanishing derivative must have constant derivative, so its degree is 1.
- **The bigger picture.** Combined with the analogous fact on the Riemann sphere, this shows $\operatorname{Aut}(\hat{\mathbb{C}})$ is the Möbius group. Also, $\operatorname{Aut}(\mathbb{C})$ is the subgroup of Möbius maps fixing $\infty$. This is one leg of the classical trichotomy $\hat{\mathbb{C}}$, $\mathbb{C}$, $\mathbb{D}$ in uniformization.
- **The general lesson.** "Analyze the singularity at $\infty$" is a powerful technique. Liouville's theorem, the fact that entire functions of polynomial growth are polynomials, and this result are all instances of it.
