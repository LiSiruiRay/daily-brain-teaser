# Answer: Zeros Hidden Before the Beginning

## Key Idea / Intuition

Modulo $N$, a recursion that depends on finitely many previous terms is eventually periodic, because there are only finitely many possible "windows" of consecutive residues. If the recursion can also be **run backwards** with integer coefficients, the step map is a bijection on a finite set. Then the sequence is *purely* periodic mod $N$, so its past repeats in its future. Running this recursion backwards from the start produces exactly $2005$ zeros. Periodicity then carries that block of zeros into the positive indices.

Instead of searching forward for zeros, look backward: the forward-looking sequence hides the zeros "before time $1$."

---

## Formal Proof / Solution

**Step 1: Extend the sequence to all integers.**
The recursion $x_{k+1} = x_k + x_{k-2005}$ can be rewritten as

$$x_{j} = x_{j+2006} - x_{j+2005}.$$

This defines $x_j$ uniquely for all $j \le 0$. The result is a doubly infinite integer sequence $(x_k)_{k\in\mathbb Z}$ satisfying $x_{k+1} = x_k + x_{k-2005}$ for **every** $k \in \mathbb Z$.

**Step 2: Compute backwards.**

- For $j = 0, -1, \dots, -2004$, the indices $j+2006$ and $j+2005$ range over consecutive values in $\{1,\dots,2006\}$, where $x_m = m$. So
$$x_j = (j+2006) - (j+2005) = 1 \qquad (-2004 \le j \le 0).$$
- For $j = -2005, \dots, -4009$, the indices $j+2006$ and $j+2005$ are consecutive values in $\{-2003, \dots, 1\}$. Every such value of $x$ equals $1$: we have $x_1 = 1$, and $x_m = 1$ for $-2004 \le m \le 0$. Hence
$$x_j = 1 - 1 = 0 \qquad (-4009 \le j \le -2005).$$

That gives $4009 - 2005 + 1 = 2005$ consecutive zeros: $x_{-4009} = \cdots = x_{-2005} = 0$.

**Step 3: Pure periodicity modulo $N = 2006$.**
Consider the "window" vectors

$$S_k = (x_{k-2005}, x_{k-2004}, \dots, x_k) \bmod N \in (\mathbb Z/N)^{2006}.$$

The recursion gives a map $T: S_k \mapsto S_{k+1}$. It shifts the window left and appends $x_k + x_{k-2005}$.

$T$ is invertible: from $S_{k+1}$ we recover the dropped entry as $x_{k-2005} = x_{k+1} - x_k$.

So $T$ is a permutation of the finite set $(\mathbb Z/N)^{2006}$. Some power is the identity: $T^p = \mathrm{id}$ for some $p \ge 1$, for instance the order of $T$ in the symmetric group. Therefore

$$x_{k+p} \equiv x_k \pmod{N} \qquad \text{for all } k \in \mathbb Z.$$

**Step 4: Transport the zeros forward.**
Choose $m$ with $mp > 4009$. Then for $-4009 \le j \le -2005$,

$$x_{j+mp} \equiv x_j = 0 \pmod{2006}.$$

The indices $j + mp$ are positive. They are $2005$ consecutive terms of the original sequence, each divisible by $2006$. $\blacksquare$

---

**Remarks.**
- The same argument shows that this sequence has arbitrarily long runs of terms divisible by **any** $N$ (here, up to $2005$ consecutive terms). Nothing about $2006$ was used except in setting up the recursion.
- The general principle is reusable: an invertible recursion over a finite ring is purely periodic. It is the same reason the Fibonacci sequence mod $N$ returns to $0, 1$, so every $N$ divides some Fibonacci number.
