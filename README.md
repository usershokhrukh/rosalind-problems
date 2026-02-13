# Inferring mRNA from Protein

### Problem Description

codon_counts = {
'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2,
'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4,
'A': 4, 'D': 2, 'E': 2, 'G': 4
}

Given the total number of different Protein strings from which the protein could have been translated, then with codon object below you can find how many codons current letter would be suggested, then if we don't module to 1,000,000 (number given in Rosalind), the super computers cant analyze it and print to console, so with module to million we can find last 6 numbers for simply get right answer 

And one important thing is, "MA" given in Rosalind shows 12 but why? M has 1 codon, A has 4 codons, in biology after translation (when mRNA translated to codons) to stop translation mRNA puts **THREE STOP CODONS (UAA, UAG, UGA)** and we must also analyze these combinations multiplying by 3

### Mathematical Logic

1. **Read given Protein string** given in Rosalind
2. **Put requires in Rosalind** codon data & module
3. **Multiply & Modulo**
4. **Print last 6 numbers**
