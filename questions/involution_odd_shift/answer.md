# No Function with $f(f(n)) = n + 2025$ — Answer

Let $c = 2025$ for convenience. Suppose for contradiction that $f: \mathbb{Z} \to \mathbb{Z}$ satisfies $f(f(n)) = n + c$ for all $n$.

---

## Step 1: Periodicity — $f(n + c) = f(n) + c$

Apply $f$ to both sides of $f(f(n)) = n + c$:
$$f(f(f(n))) = f(n + c)$$

But also, applying the functional equation to $f(n)$ in place of $n$:
$$f(f(f(n))) = f(n) + c$$

Combining: $f(n + c) = f(n) + c$ for all $n \in \mathbb{Z}$.

---

## Step 2: $f$ descends to a map $\bar{f}$ on $\mathbb{Z}/c\mathbb{Z}$

Since $f(n+c) = f(n) + c$, the residue $f(n) \bmod c$ depends only on $n \bmod c$. So define:
$$\bar{f}: \mathbb{Z}/c\mathbb{Z} \to \mathbb{Z}/c\mathbb{Z}, \qquad \bar{f}(n \bmod c) = f(n) \bmod c$$

This is well-defined. From $f(f(n)) = n + c \equiv n \pmod{c}$, we get:
$$\bar{f}(\bar{f}(n)) = n \quad \text{in } \mathbb{Z}/c\mathbb{Z}$$

So $\bar{f}$ is an **involution** ($\bar{f}^2 = \mathrm{id}$), hence a bijection.

---

## Step 3: $\bar{f}$ has no fixed points

Suppose $\bar{f}(k) = k$ for some $k \in \mathbb{Z}/c\mathbb{Z}$, i.e., $f(n) \equiv n \pmod{c}$ for some $n$ with $n \equiv k$.

Then $f(n) = n + mc$ for some integer $m$. Applying $f$ again using Step 1:
$$f(f(n)) = f(n + mc) = f(n) + mc = n + 2mc$$

But $f(f(n)) = n + c$, so $2mc = c$, giving $m = \tfrac{1}{2}$ — not an integer. Contradiction.

So $\bar{f}$ is a **fixed-point-free involution** on $\mathbb{Z}/c\mathbb{Z}$.

---

## Step 4: Contradiction

A fixed-point-free involution partitions every element into a 2-element orbit $\{k,\, \bar{f}(k)\}$ (since $\bar{f}(k) \neq k$ and $\bar{f}(\bar{f}(k)) = k$). So the orbits partition $\mathbb{Z}/c\mathbb{Z}$ into pairs, requiring $|\mathbb{Z}/c\mathbb{Z}| = c$ to be **even**.

But $c = 2025 = 45^2$ is **odd**. Contradiction. $\blacksquare$

---

## Why 2025 specifically?

The proof works for any odd $c$. For even $c$, no contradiction arises — and indeed $f(f(n)) = n + 2$ has a solution: $f(n) = n + 1$.

The key is not any special property of 2025 beyond its being odd.

---

## Summary of the argument chain

$$f(f(n)) = n + c \implies f(n+c) = f(n)+c \implies \bar{f} \text{ is a fixed-point-free involution on } \mathbb{Z}/c\mathbb{Z} \implies c \text{ is even}$$
