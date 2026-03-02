# Enumerating k-mers Lexicographically

### Problem Description

Given collection of symbols ordered in English alphabet, then we have number which tells us length of combinations

I have used **itertools** python library for combination them, I've learned these itertools methods work with analyzing:

1. **itertools.permutations** => it doesn't repeat used symbols, we can not use **"AA"** 

2. **itertools.combinations** => it makes combinations not **unique**, if it unique, then we may use "ACG" and "CGA", but we may not, for itself these are same

3. **itertools.product** => in this problem we worked with this one, it can be used to **all variants** (AA, AC, AG, GA, AT...) 

### Mathematical Logic

1. **Identify sequence and length of combination** 
2. **use itertools.product(seq, repeat=n) for get all k-mers** 
3. **Print result with no space**
