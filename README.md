# Finding a Spliced Motif

> Given two strings in FASTA format, DNA sequence and subsequence, we should find each letter of subsequence in DNA sequence.
> For example 
```
Dataset
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA
Output
3 8 10
```
> We should analyze each subsequence letter from last found index
> First letter of GTA is G, so in sequence it would be on 2 index, and second letter is T, so second index should be 4, but wait! Output shows that after 3 is 8, I searched it why, and found that, if subsequence in DNA sequence has same index as letter of subsequence, we may analyze that as one index, so after G index would be 3 and because of that ability, we may not find from that index and search other letter from it's last index.

>But what if got:
```
Dataset
>Rosalind_14
ACGTACGGCG
>Rosalind_18
GTA
Output
3 8 10
```
>There is ACGTACGGCG except ACGTACGTGACG, with our algorithm it gives us output 3 6 6, but it incorrect! I thought about this problem and added second analyzing under the first one. It finds without that whole subsequence finding
---

## Table of contents
* How to run?: python [filename].py
* Technologies: python, VS Code, Terminal, 
* Author: Ashurov Shokhrukh

---

## Loyiha Haqida
This problem helps to find mutations of **exons**, it is mRNA sequence, and translates to amino acids, then protein. Imagine you have many DNA sequence of organisms and translatable mRNA chain to protein. After some years maybe, the first DNA code could mutate to another, and we can find where it was mutated by this problem, also compare one mutate from another.

## Algorithm Steps
1. **Read FASTA file:** strip(), join(), split()
2. **Write first analyzing code**
3. **Check first result, and do another**

## Install
1. Clone repository:
   ```bash
   git clone [https://github.com/usershokhrukh/rosalind-problems](https://github.com/usershokhrukh/rosalind-problems)