# Answer: The Universal Chord Theorem

## Key Idea / Intuition

**Part (a).** Steps of length $1/n$ tile $[0,1]$ exactly, so the $n$ increments of $f$ over consecutive steps telescope to $f(1)-f(0)=0$. Numbers that sum to zero cannot all be positive or all be negative. The Intermediate Value Theorem then forces an increment of exactly zero somewhere.

**Part (b).** When $a$ does not tile $[0,1]$, there is no telescoping. We can build a function that is periodic with period $a$ (so every $a$-step changes it by $0$) and then add a linear drift, which shifts every $a$-step by the same nonzero amount. The drift is tuned so that $f(0)=f(1)$. This tuning is possible precisely because $1$ is not a multiple of the period $a$.

---

## Formal Proof / Solution

### (a) Chords of length $1/n$ always exist

Fix $n\ge 1$. If $n=1$, the pair $x=0$, $x+1=1$ works, so assume $n\ge2$. Define the continuous function
$$g(x) = f\!\left(x+\tfrac1n\right) - f(x), \qquad x\in\left[0,\,1-\tfrac1n\right].$$
Evaluate $g$ at the points $0,\tfrac1n,\dots,\tfrac{n-1}{n}$ and sum. The sum telescopes:
$$\sum_{k=0}^{n-1} g\!\left(\tfrac kn\right) = \sum_{k=0}^{n-1}\left[f\!\left(\tfrac{k+1}{n}\right)-f\!\left(\tfrac kn\right)\right] = f(1)-f(0) = 0.$$

There are two cases.

- If some $g(k/n)=0$, then $x=k/n$ gives the desired chord.
- Otherwise, the terms sum to zero and none is zero, so some term is positive and some term is negative. Say $g(k_1/n)>0>g(k_2/n)$. By the Intermediate Value Theorem, $g$ has a zero $x^*$ between $k_1/n$ and $k_2/n$.

In both cases there is an $x$ with $f(x+\tfrac1n)=f(x)$. $\blacksquare$

### (b) Other lengths can fail

Let $a\in(0,1)$ with $1/a\notin\mathbb{Z}$. Define
$$f(x) = \sin^2\!\left(\frac{\pi x}{a}\right) - x\,\sin^2\!\left(\frac{\pi}{a}\right).$$

The first term is periodic with period $a$, and the second term is a linear drift.

**Endpoints agree.** We have $f(0)=0-0=0$ and
$$f(1)=\sin^2\!\left(\tfrac{\pi}{a}\right)-\sin^2\!\left(\tfrac{\pi}{a}\right)=0.$$

**No chord of length $a$.** Take any $x\in[0,1-a]$. Since $\sin^2$ has period $\pi$, we have $\sin^2\!\left(\tfrac{\pi x}{a}+\pi\right)=\sin^2\!\left(\tfrac{\pi x}{a}\right)$. Therefore
$$f(x+a)-f(x) = \underbrace{\sin^2\!\left(\tfrac{\pi x}{a}+\pi\right)-\sin^2\!\left(\tfrac{\pi x}{a}\right)}_{=\,0} \;-\; a\,\sin^2\!\left(\tfrac{\pi}{a}\right) = -a\sin^2\!\left(\tfrac{\pi}{a}\right).$$

This value is nonzero. Indeed, $\sin(\pi/a)=0$ exactly when $1/a\in\mathbb{Z}$, which we excluded.

So $f(x+a)\neq f(x)$ for every $x$, and $f$ has no horizontal chord of length $a$. $\blacksquare$

### Remarks

- **Why the drift is not arbitrary.** The drift slope is forced by the condition $f(1)=f(0)$. It vanishes exactly when $1$ is a multiple of the period $a$. This is the same arithmetic fact that drives the telescoping in part (a), seen from the other side.
- **The $2/5$ example.** Taking $a=\tfrac25$ gives a continuous loop-like profile with chords of lengths $\tfrac12,\tfrac13,\tfrac14,\tfrac15,\dots$ but none of length $\tfrac25$. In particular, the set of chord lengths of a given $f$ need not be closed under addition.
- **A general fact behind (a).** For a continuous $g$, if the values at some points sum to zero, then $g$ vanishes somewhere. This "averaging plus IVT" trick appears repeatedly in analysis.
