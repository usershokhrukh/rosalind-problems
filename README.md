# Calculating Protein Mass

### Problem Description
```
mass_table = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333,
}
```

In this problem they want to **sum** each protein in given **protein string**, for example => SKADYEK would be **821.392**, and we should round three decimal places after dot

**Why we should calculate the mass?**:
  If scientists find unknown protein, they find the mass and compare to the proteins for acquiring which protein they found
**What if the mass doesn't equal?**:
  If found protein doesn't match to others, then we can understand that the nature itself added some molecules
**Molecular weight**:
  In Bioinformatics finding the mass provides how protein works in cell, and its functionalities

### Mathematical Logic

1. **Read protein string** 
2. **Calculate** with a protein table
3. **round** after three numbers and print
