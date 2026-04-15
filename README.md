# Catalan Numbers and RNA Secondary Structures 

> Given RNA string < 300bp

---
>This problem has advantages for Biology and IT

>Biology:
>With Catalan numbers, we can identify amount of all combinations with mathematic way, and then we can produce the medicine for diseases. Structure = Function, the function of one protein depends on shape, there are many shapes we analyzed, and for cancer it would be another that shape.

>IT:
>Dynamic Programming: with dividing into pieces we acquired how to work with big data. Memorization, I used the memo object to do not analyze sequences which already analyzed, it keeps like cache. Parsing, pairs in RNA seems like compiling scopes () in dev. languages, compilations also translate and read scopes for syntax error with this algorithm.

---

## Table of contents

- How to run?: python [filename].py
- Technologies: python, VS Code, Terminal,
- Author: Ashurov Shokhrukh

---

## About
As I said the Catalan algorithm with DP, helps scientist to get all combinations of RNA shape

## Algorithm Steps

1. **Read sequence as "".join(seq for seq in file.read().strip().split()[1:])**
2. **Create memo object to avoid future calculations**
3. **Loop each 2nd number, because there can not be one letter without pair**
4. **For each recursion, it divides left side of sequence and right side, then checks each pair until empty string**

## Install

1. Clone repository:
   ```bash
   git clone [https://github.com/usershokhrukh/rosalind-problems](https://github.com/usershokhrukh/rosalind-problems)
   ```
