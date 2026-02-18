# Open Reading Frames 

### Problem Description

CODON_TABLE = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': 'Stop', 'TAG': 'Stop', 'TGT': 'C', 'TGC': 'C', 'TGA': 'Stop', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

Given DNA string which gives us to search codons in CODON_TABLE, in problem said, return protein string in given unique string and **reversed** string.  We should reverse sequence to reverse complement like ATCGGATAG (unique) => GATAGGCTA (only reversed) => CTATCCGAT (reverse complement). About protein string, count every three codons and start adding **ORF** which returned from CODON_TABLE and print or save to list **ENDED protein strings**, means if we start counting from ATG and there is no STOP codons (in CODON_TABLE), we shouldn't print them it would wrong

### Mathematical Logic

1. **Read given DNA string** 
2. analyze **Reverse Complement** and **Unique string**
3. **make protein results to Unique** 
4. save or print **Protein string which exist STOP codons**
