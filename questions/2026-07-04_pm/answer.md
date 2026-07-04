# Answer: Integral of 1/(1+tan^n x)

## Key Idea / Intuition

The substitution $x \mapsto \frac{\pi}{2} - x$ swaps $\tan x$ with $\cot x = 1/\tan x$. When you add the original integral to the substituted version, the two integrands sum to exactly $1$ everywhere on $[0, \pi/2]$. So $2I_n = \pi/2$, regardless of $n$.

---

## Formal Proof / Solution

**Step 1: Apply the King's substitution $x = \frac{\pi}{2} - t$.**

Under this substitution, $dx = -dt$, and when $x=0$, $t=\pi/2$; when $x=\pi/2$, $t=0$. Also:
$$\tan\!\left(\tfrac{\pi}{2} - t\right) = \cot t = \frac{1}{\tan t}$$

So:
$$I_n = \int_{\pi/2}^{0} \frac{1}{1 + \cot^n t}\,(-dt) = \int_0^{\pi/2} \frac{1}{1 + \cot^n t}\,dt$$

**Step 2: Simplify the new integrand.**

$$\frac{1}{1 + \cot^n t} = \frac{1}{1 + \dfrac{1}{\tan^n t}} = \frac{\tan^n t}{1 + \tan^n t}$$

**Step 3: Add the two expressions.**

$$2I_n = \int_0^{\pi/2} \frac{1}{1+\tan^n x}\,dx + \int_0^{\pi/2} \frac{\tan^n x}{1+\tan^n x}\,dx = \int_0^{\pi/2} \frac{1 + \tan^n x}{1 + \tan^n x}\,dx = \int_0^{\pi/2} 1\,dx = \frac{\pi}{2}$$

**Step 4: Conclude.**

$$\boxed{I_n = \frac{\pi}{4}}$$

for **every** $n > 0$, independently of $n$. The result is the same whether $n = 1, 2, 1000$, or $\pi$.

---

**Why this is surprising:** The integrand $\frac{1}{1+\tan^n x}$ changes its shape dramatically as $n$ varies — for large $n$ it becomes nearly a step function jumping at $x = \pi/4$ — yet the area is always exactly $\pi/4$. The symmetry of the interval $[0, \pi/2]$ about its midpoint $\pi/4$ is the hidden reason.
