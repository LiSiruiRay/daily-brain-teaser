# Answer: The Closed Subgroup of ℝ

## Key Idea / Intuition

A subgroup of $\mathbb{R}$ has only two possibilities: either it is **dense** (in which case closedness forces it to be all of $\mathbb{R}$), or it has a **smallest positive element** (in which case it must be an integer multiple of that element). The trichotomy comes entirely from whether the infimum of positive elements in $H$ is zero or positive — topology forces the two cases to be clean.

---

## Formal Proof / Solution

Let $H \leq (\mathbb{R}, +)$ be a closed subgroup.

**Case 1: $H = \{0\}$.**

This is $0 \cdot \mathbb{Z}$, so we're done.

**Case 2: $H \neq \{0\}$.**

Let $a = \inf\{h \in H : h > 0\}$, which exists since $H$ contains positive elements (if $x \in H$ with $x < 0$, then $-x \in H$ with $-x > 0$).

**Sub-case 2a: $a = 0$.**

Then there exist elements of $H$ arbitrarily close to $0$. For any $x \in \mathbb{R}$ and $\varepsilon > 0$, pick $h \in H$ with $0 < h < \varepsilon$. Then for some $n \in \mathbb{Z}$, $nh \in H$ and
$$|nh - x| < h < \varepsilon.$$
(Just take $n = \lfloor x/h \rfloor$.) So $H$ is **dense** in $\mathbb{R}$. Since $H$ is also closed, $H = \mathbb{R}$.

**Sub-case 2b: $a > 0$.**

We claim $H = a\mathbb{Z}$.

First, $a \in H$: by definition of infimum, there exist $h_n \in H$ with $h_n \searrow a$. But actually, we need to be more careful — the infimum might not be achieved by this sequence argument alone. Instead:

Suppose $a \notin H$. Then there exist $h_n \in H$ with $h_n > a$ and $h_n \to a$. Consider $h_n - h_m \in H$ for $n \neq m$; these can be made arbitrarily small and positive, contradicting $a = \inf\{h \in H : h > 0\} > 0$. So actually the infimum **is** achieved: $a \in H$.

More precisely: if no element equals $a$, pick $h_1, h_2 \in H$ with $a < h_2 < h_1 < 2a$. Then $0 < h_1 - h_2 < a$, contradicting the definition of $a$. So $a \in H$.

Now clearly $a\mathbb{Z} \subseteq H$ (since $H$ is a subgroup and $a \in H$).

Conversely, suppose $x \in H$. Write $x = na + r$ with $n \in \mathbb{Z}$ and $0 \leq r < a$. Then
$$r = x - na \in H.$$
By minimality of $a$, we must have $r = 0$. So $x = na \in a\mathbb{Z}$.

**Conclusion.** Every closed subgroup of $\mathbb{R}$ is one of:
$$\{0\},\quad a\mathbb{Z} \text{ for some } a > 0, \quad \mathbb{R}.$$

**Why this is beautiful:** The argument is purely topological + algebraic — no measure theory needed. The infimum of the positive part of $H$ acts as a "generator," and closedness is used exactly once, to rule out density implying anything other than $\mathbb{R}$. The same argument classifies closed subgroups of any locally compact abelian group, and is the key step in showing $\mathbb{R}/\mathbb{Z} \cong S^1$ is the "only" compact quotient.
