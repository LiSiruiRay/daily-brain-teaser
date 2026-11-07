# Answer: The Exponential That Hides a Product Rule

## Key Idea / Intuition

Any time you see $e^x$ times something awkward, ask whether the awkward factor has the form $f+f'$ for a nice $f$. If it does, the integrand is exactly $\frac{d}{dx}\big(e^x f\big)$, and the integral collapses to evaluating at the endpoints.

The denominator $(x+1)^2$ suggests where to look. Differentiating something over $(x+1)$ produces $(x+1)^2$ in the denominator. So guess $f(x)=\frac{\text{linear}}{x+1}$ and solve for the coefficients.

---

## Formal Proof / Solution

**Step 1: The reverse product rule.** For differentiable $f$,

$$
\frac{d}{dx}\big(e^x f(x)\big) = e^x f(x) + e^x f'(x) = e^x\big(f(x)+f'(x)\big).
$$

So it suffices to find $f$ with $f+f' = \dfrac{x^2+1}{(x+1)^2}$.

**Step 2: Ansatz.** Try $f(x)=\dfrac{ax+b}{x+1}$. Then

$$
f'(x)=\frac{a(x+1)-(ax+b)}{(x+1)^2}=\frac{a-b}{(x+1)^2}.
$$

Adding the two terms over the common denominator:

$$
f+f'=\frac{(ax+b)(x+1)+(a-b)}{(x+1)^2}=\frac{ax^2+(a+b)x+a}{(x+1)^2}.
$$

**Step 3: Match coefficients.** We need $ax^2+(a+b)x+a = x^2+0\cdot x+1$. This gives:

- $a=1$,
- $a+b=0$, so $b=-1$,
- the constant term is $a=1$, which agrees.

So $f(x)=\dfrac{x-1}{x+1}$.

Check directly: $f'(x)=\dfrac{2}{(x+1)^2}$, and

$$
f+f'=\frac{(x-1)(x+1)+2}{(x+1)^2}=\frac{x^2+1}{(x+1)^2}.
$$

**Step 4: Evaluate.**

$$
I=\Big[e^x\,\frac{x-1}{x+1}\Big]_0^1 = e\cdot\frac{0}{2}-1\cdot\frac{-1}{1}=0+1=1.
$$

$$
\boxed{I=1}
$$

---

## Remarks

- **Why the ansatz is the right one.** Solving $f+f'=g$ means inverting the operator $1+D$. All solutions differ by $Ce^{-x}$, which is not rational. So if a rational solution exists, it is unique, and a rational ansatz is the natural thing to try.
- **Formal series view.** Formally, $(1+D)^{-1}=1-D+D^2-D^3+\cdots$. For polynomial $g$ this series terminates, which explains why $\int x^n e^x\,dx$ always has a polynomial-times-$e^x$ antiderivative.
- **Same trick, other shapes.** The identity
$$\frac{d}{dx}\big(e^{g(x)}f(x)\big)=e^{g(x)}\big(f'+g'f\big)$$
covers more cases. For example, $\int e^x\big(\tfrac1x-\tfrac1{x^2}\big)dx=\tfrac{e^x}{x}+C$. Similarly, $\int_1^e e^x\big(\ln x+\tfrac1x\big)dx=e^e$.
