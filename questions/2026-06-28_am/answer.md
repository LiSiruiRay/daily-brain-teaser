# Answer: The Wisdom of Crowds: When Does Averaging Hurt?

## Key Idea / Intuition

When classifiers are **truly independent**, their errors cancel out under majority vote — the law of large numbers drives ensemble error to zero. But when there is a **shared failure mode** (a correlated error component), adding more classifiers only averages out the *independent* noise; the **correlated part never cancels**. The ensemble hits a wall at exactly the probability of the shared failure event. This is the core message of **error correlation in ensembles**: diversity, not just quantity, is what matters.

---

## Formal Proof / Solution

### Part (a): Independent classifiers, $p > 1/2$

Let each classifier $h_i$ be correct independently with probability $p > 1/2$. The majority vote is correct when more than $B/2$ classifiers are correct. Let $S = \sum_{i=1}^B \mathbf{1}[h_i \text{ correct}]$, so $S \sim \text{Binomial}(B, p)$.

$$P(\text{ensemble correct}) = P\!\left(S > \frac{B}{2}\right).$$

By the Law of Large Numbers, $S/B \to p > 1/2$ almost surely. Thus for large $B$:

$$P\!\left(\frac{S}{B} > \frac{1}{2}\right) \to 1.$$

More precisely, by Hoeffding's inequality:

$$P\!\left(S \leq \frac{B}{2}\right) \leq \exp\!\left(-2B\!\left(p - \tfrac{1}{2}\right)^2\right) \to 0.$$

So ensemble accuracy $\to 1$ exponentially fast. $\checkmark$

---

### Part (b): Correlated failure core — the hard ceiling

**Model:** For each test point, with probability $\rho$ all $B$ classifiers are simultaneously wrong (the "shared error event" $E$). With probability $1 - \rho$, the shared error does not occur and each classifier errs independently with probability $q$.

Taking $q \to 0$ (independent errors outside the core vanish), the majority vote fails **if and only if** the shared error event $E$ occurs.

Why? 
- If $E$ occurs (prob $\rho$): all $B$ classifiers are wrong $\Rightarrow$ majority vote is wrong.
- If $E$ does not occur (prob $1-\rho$): as $B \to \infty$ with $q \to 0$, essentially all classifiers are correct $\Rightarrow$ majority vote is correct.

Therefore:

$$P(\text{ensemble wrong}) \;\xrightarrow{B\to\infty,\, q\to 0}\; \rho.$$

$$\boxed{P(\text{ensemble correct}) \to 1 - \rho.}$$

**The hard ceiling is $1 - \rho$**: no matter how many classifiers you add, you can never exceed accuracy $1 - \rho$ because the correlated failure mode is **irreducible** — majority vote is powerless against errors that all classifiers share simultaneously.

---

### Takeaway

The decomposition of ensemble error is:

$$\text{Ensemble error} \approx \underbrace{\rho}_{\text{irreducible correlated component}} + \underbrace{(1-\rho) \cdot f(B, q)}_{\to\, 0 \text{ as } B \to \infty}.$$

This is why in practice (random forests, boosting), the critical design principle is **encouraging diversity** — reducing $\rho$ — rather than simply increasing $B$. The formula also connects to the bias-variance decomposition for ensembles studied in ESL Chapter 8: variance (independent noise) is reduced by averaging, but **bias and correlated errors are not**.
