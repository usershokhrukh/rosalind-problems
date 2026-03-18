# Introduction to Random Strings

### Problem Description
Introduction to Random Strings helps to identify probability of sequence, **with each given GC-content**, for example if we have **0.129** GC-content, in **ACGATACAA**, then probability of G/C would be **x / 2** => 0.129 / 2 = 0.0645, AT-content would be **(1 - x) / 2** => 1 - 0.129 = 0.871 / 2 = 0.4355

So, we have probabilities of each nucleotides, and with sequence order we can easily sum them up, but if sequence is too long, result will be with many zeros. Working with logarithm10, why 10? because it helps to know number of zeros

**Why we need this problem, and what it helps to?**:
Scientists want to know about gene, and they search it to understand is it a miracle or noise?, is gene actually helps in cell or it is just after mutations


### Algorithm steps

1. **Search about problem, and try to understand it**
2. **Read data, but with no just one line, read each line and sort them** 
3. **Use log10 and save like {:.3f} format, for Rosalind requirements** 
4. **Print each log10 result probabilities**
