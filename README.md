# Completing a Tree

> Given positive integer up to 1000, and a pair list, which gives the number of edges

---
>The tree often used for determine diseases for each other, it used to genetic relationships of something like Virus, or generation diseases


## Table of contents

- How to run?: python [filename].py
- Technologies: python, VS Code, Terminal,
- Author: Ashurov Shokhrukh

---

## About
The tree problem wants to identify minimum number of edges that can be added to produce a tree. Tree means, hierarchy of one life. If the number 'n' is given as 10, then total edges would be 9 'n-1', so with length of lists we can get the minimal missing edges, if pairs are 6, then answer would be **3**, so '9-6=3' 

## Algorithm Steps

1. **Read data as file.read().strip().split():**
2. **First number of list would be n, total edges are n-1**
3. **Get (len(list)-1) for each circle, and divide by 2 for pairs**
4. **Print total edges - pairs**

## Install

1. Clone repository:
   ```bash
   git clone [https://github.com/usershokhrukh/rosalind-problems](https://github.com/usershokhrukh/rosalind-problems)
   ```
