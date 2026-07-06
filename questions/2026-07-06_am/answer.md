# Answer: Generic Continuous Function Is Nowhere Differentiable

## Key Idea / Intuition

The space $C([0,1])$ is a complete metric space, so Baire's theorem says it cannot be written as a countable union of nowhere-dense closed sets. The "bad" functions — those that are differentiable at even one point — can be expressed as exactly such a countable union. So "most" continuous functions (in the Baire category sense) are nowhere differentiable. Differentiability is the exception, not the rule.

---

## Formal Proof / Solution

### Step 1: Write the "differentiable somewhere" set as a countable union

A function $f \in C([0,1])$ has a **finite right-derivative** at some point $x$ if and only if there exist integers $n, k \geq 1$ such that $f \in A_{n,k}$, where

$$A_{n,k} = \left\{ f \in C([0,1]) : \exists\, x \in \left[0, 1 - \tfrac{1}{k}\right] \text{ such that } \forall\, 0 < h < \tfrac{1}{k},\ \frac{|f(x+h)-f(x)|}{h} \leq n \right\}.$$

Informally: $A_{n,k}$ is the set of functions that have a bounded difference quotient of size $\leq n$ for all small steps $h < 1/k$ at some point $x$. Any function differentiable at some point belongs to $\bigcup_{n,k} A_{n,k}$.

### Step 2: Each $A_{n,k}$ is **closed** in $C([0,1])$

Suppose $f_m \to f$ uniformly and each $f_m \in A_{n,k}$, witnessed at points $x_m$. By compactness, $x_m \to x$ along a subsequence. Then for any $0 < h < 1/k$:

$$\frac{|f(x+h)-f(x)|}{h} = \lim_{m\to\infty} \frac{|f_m(x_m+h)-f_m(x_m)|}{h} \leq n$$

(using uniform convergence to swap limit and evaluation). So $f \in A_{n,k}$. Hence $A_{n,k}$ is closed.

### Step 3: Each $A_{n,k}$ is **nowhere dense**

We show: every open ball in $C([0,1])$ contains a function outside $A_{n,k}$.

Given any $f \in C([0,1])$ and $\varepsilon > 0$, we construct $g$ with $\|f - g\|_\infty < \varepsilon$ and $g \notin A_{n,k}$.

Take a piecewise-linear "sawtooth" perturbation $s$ with amplitude $< \varepsilon$ and slope $\pm M$ for $M \gg n$ on intervals of width $< 1/k$. Set $g = f + s$. Then $g$ is close to $f$, but at every point $x$, there exists a small $h < 1/k$ where the difference quotient of $g$ exceeds $n$ (the sawtooth spike dominates). So $g \notin A_{n,k}$.

This shows $A_{n,k}$ has **empty interior**, i.e., is nowhere dense.

### Step 4: Apply Baire Category

Since $C([0,1])$ is complete, the Baire Category Theorem says:

$$\bigcup_{n,k=1}^\infty A_{n,k} \text{ is meager (first category)}.$$

Therefore its complement

$$\mathcal{ND} = C([0,1]) \setminus \bigcup_{n,k} A_{n,k}$$

is **residual (comeager)**, a dense $G_\delta$. Every $f \in \mathcal{ND}$ is nowhere differentiable.

### Conclusion

$$\boxed{\mathcal{ND} \text{ is residual in } C([0,1]).}$$

The nowhere-differentiable functions are not a curiosity — they form the **vast majority** of all continuous functions in the Baire category sense. Weierstrass's explicit example (1872) was just the first proof that such functions exist; Baire category tells us they're typical.
