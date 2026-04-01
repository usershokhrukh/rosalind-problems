# Transitions and Transversions

>Given two DNA sequences in FASTA format, in this problem we have to analyze ratio of transitions and transverstions mutation
>First read FASTA file, and loop and check each letter of sequence and compare with each other, then if first letter of seq_1 is purins, then check seq_1 to purins and pyrimidines. Add +1 to transitions if letter in same index seq_1 and seq_2 are same type of mutation (purins <-> purins, pyrimidines <-> pyrimidines). But they differs of single mutation type, then we must add +1 to transversions variable
---

- **Transitions:** $A \leftrightarrow G$ or $C \leftrightarrow T$
- **Transversions:** $A/G \leftrightarrow C/T$

## Table of contents
* How to run?: python [filename].py
* Technologies: python, VS Code, Terminal, 
* Author: Ashurov Shokhrukh

---

## About
With this problem we can find is the mutation has came from nature or laboratory experiment, and compare two life for acquiring they divide times

## Algorithm Steps
1. **Read FASTA file:** Big(len(lines))
2. **Initializing variables**
3. **Check each letter in same index**
4. **Compare it's letter to transitions and transversions**

## Install
1. Clone repository:
   ```bash
   git clone [https://github.com/usershokhrukh/rosalind-problems](https://github.com/usershokhrukh/rosalind-problems)