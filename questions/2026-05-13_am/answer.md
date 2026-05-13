# Answer: The Prisoner's Dilemma

## Key Idea / Intuition

The mistake is subtle: $A$ forgets that the warder's *choice of words* is itself random data. When $A$ and $B$ are both to be released, the warder **must** say "$B$" (he can't name $A$). But when $B$ and $C$ are both to be released, the warder only says "$B$" with probability $\tfrac{1}{2}$. So hearing "$B$" is **more likely** under the scenario $\{A,B\}$ than under $\{B,C\}$, which tilts the posterior back in $A$'s favor. The answer is: $A$'s probability of release is still $\tfrac{2}{3}$ — asking changes nothing!

---

## Formal Proof / Solution

**Step 1 — Prior sample space.**

The three equally likely release pairs are:

$$\{A,B\},\quad \{A,C\},\quad \{B,C\}, \qquad \text{each with probability } \tfrac{1}{3}.$$

**Step 2 — Warder's behavior (the key modeling step).**

The warder must name someone other than $A$ who will be released.

| Event | Probability of event | Prob. warder says "$B$" given event |
|---|---|---|
| $\{A,B\}$ released | $\tfrac{1}{3}$ | $1$ (only $B$ is available) |
| $\{A,C\}$ released | $\tfrac{1}{3}$ | $0$ (must say "$C$") |
| $\{B,C\}$ released | $\tfrac{1}{3}$ | $\tfrac{1}{2}$ (names $B$ or $C$ equally) |

**Step 3 — Joint probabilities.**

$$P(\{A,B\} \text{ and warder says } B) = \tfrac{1}{3}\cdot 1 = \tfrac{1}{3}$$

$$P(\{A,C\} \text{ and warder says } B) = \tfrac{1}{3}\cdot 0 = 0$$

$$P(\{B,C\} \text{ and warder says } B) = \tfrac{1}{3}\cdot \tfrac{1}{2} = \tfrac{1}{6}$$

**Step 4 — Bayes' theorem.**

$$P(\text{warder says } B) = \tfrac{1}{3} + 0 + \tfrac{1}{6} = \tfrac{1}{2}.$$

$$P(A \text{ released} \mid \text{warder says } B) = \frac{P(\{A,B\} \text{ and warder says }B)}{P(\text{warder says }B)} = \frac{\tfrac{1}{3}}{\tfrac{1}{2}} = \boxed{\tfrac{2}{3}}.$$

**Conclusion.** $A$'s probability of release is still $\tfrac{2}{3}$, exactly as before asking. The information "$B$ will be released" tells $A$ nothing new about his own fate — but it *does* update the relative probability between $\{B,C\}$ and $\{A,B\}$ in exactly the right way to cancel $A$'s naive worry.

This is a cousin of the Monty Hall problem: the host/warder's *protocol* for choosing what to reveal is essential to the calculation.
