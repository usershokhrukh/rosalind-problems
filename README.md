# Mendel's Second Law (Rosalind - LIA)

### Problem Description
This script calculates the probability that at least **N** organisms in the **k-th** generation will have the **Aa Bb** genotype.

### Mathematical Logic
1. **Total Population ($n$):** In the $k$-th generation, there are $2^k$ individuals.
2. **Success Probability ($p$):** The probability of any offspring being **Aa Bb** is always $0.25$ (due to mating with an Aa Bb partner).
3. **Optimization:** Instead of calculating $P(X \ge N)$ directly, which requires many loops, we use the complement:
   $$P(X \ge N) = 1 - \sum_{i=0}^{N-1} \binom{n}{i} \cdot p^i \cdot (1-p)^{n-i}$$
   This approach is faster because it only iterates through the "unwanted" cases ($0$ to $N-1$).