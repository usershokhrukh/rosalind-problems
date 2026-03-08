# Genome Assembly as Shortest Superstring

### Problem Description

Genome Assembly, given DNA strings, each has **supersting** in end or start of string. We should **compound** each string.
For example => we have:
```
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
```
**ATTAGACCTG** has **AGACCTG** at end, and **AGACCTGCCG** has at start, so we should compound them, result => **ATTAGACCTGCCG**, in second loop we should work with **ATTAGACCTGCCG** not with **ATTAGACCTG**, in second loop, **ATTAGACCTGCCG** compares with **CCTGCCGGAA** each has **CCTGCCG** at start and end


Rosalind gave us dataset, every string has it's superstring, so we can analyze without some bags

### Algorithm steps

1. **Read FASTA file**
2. **Find first matching string, which length of superstring longer than half of string** 
3. **Print shortest superstring** 
