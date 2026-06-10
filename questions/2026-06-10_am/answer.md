# Answer: HH vs HT: Waiting Times for Coin Patterns

## Key Idea / Intuition

At first glance, HH and HT seem symmetric — each is a sequence of two fair-coin outcomes. But they behave very differently because of what happens when a "near-miss" occurs. If you're waiting for HH and you see HT, you've wasted both flips. But if you're waiting for HT and you see HH, the second H can still serve as the start of a future HT. This asymmetry in "overlap structure" makes HH harder to achieve, giving it a longer expected waiting time.

---

## Formal Proof / Solution

### Expected time to HH

Let $E$ = expected number of flips to see HH from a fresh start.  
Let $E_H$ = expected additional flips to see HH, given the last flip was H.

**Setting up equations:**

From a fresh start, flip once:
- With prob $\tfrac{1}{2}$, get T → back to fresh start. Cost: 1 flip.
- With prob $\tfrac{1}{2}$, get H → now in state $E_H$. Cost: 1 flip.

$$E = 1 + \tfrac{1}{2} E + \tfrac{1}{2} E_H$$

From state $E_H$ (last flip was H), flip again:
- With prob $\tfrac{1}{2}$, get H → **done!** Cost: 1 flip.
- With prob $\tfrac{1}{2}$, get T → back to fresh start. Cost: 1 flip.

$$E_H = 1 + \tfrac{1}{2}(0) + \tfrac{1}{2} E = 1 + \tfrac{1}{2} E$$

Substituting into the first equation:

$$E = 1 + \tfrac{1}{2}E + \tfrac{1}{2}\!\left(1 + \tfrac{1}{2}E\right) = 2 + \tfrac{3}{4}E$$

$$\tfrac{1}{4}E = 2 \implies \boxed{E_{HH} = 6}$$

---

### Expected time to HT

Let $F$ = expected flips to HT from fresh start.  
Let $F_H$ = expected additional flips, given last flip was H.

From a fresh start:
- With prob $\tfrac{1}{2}$, get T → back to fresh start. Cost: 1 flip.
- With prob $\tfrac{1}{2}$, get H → state $F_H$. Cost: 1 flip.

$$F = 1 + \tfrac{1}{2}F + \tfrac{1}{2}F_H$$

From state $F_H$ (last flip was H), flip again:
- With prob $\tfrac{1}{2}$, get T → **done!** Cost: 1 flip.
- With prob $\tfrac{1}{2}$, get H → **stay in $F_H$** (the new H can still start HT). Cost: 1 flip.

$$F_H = 1 + \tfrac{1}{2}(0) + \tfrac{1}{2}F_H$$

$$\tfrac{1}{2}F_H = 1 \implies F_H = 2$$

Substituting back:

$$F = 1 + \tfrac{1}{2}F + \tfrac{1}{2}(2) = 2 + \tfrac{1}{2}F$$

$$\tfrac{1}{2}F = 2 \implies \boxed{E_{HT} = 4}$$

---

### Why the difference? (Intuition recap)

| Pattern | Near-miss behavior | Expected time |
|---------|-------------------|---------------|
| **HH** | Getting HT resets you completely | **6** |
| **HT** | Getting HH keeps you in a "H seen" state | **4** |

For **HH**: a failure (getting T after H) wastes everything.  
For **HT**: a "false start" (getting HH) is not fully wasted — the second H still counts as a potential head toward HT.

This is an instance of the general theory of **pattern waiting times**, where the overlap structure of the pattern determines how quickly it appears. HH has a self-overlap (its first H is also a valid start of HH), which paradoxically *hurts* it, because each near-miss costs more.
