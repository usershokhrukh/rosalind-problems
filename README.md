# Finding a Protein Motif

### Problem Description
This problem wants to find motif **N{P}[ST]{P}** in http://www.uniprot.org/uniprot/uniprot_id.fasta response, then finds it

### Mathematical Logic
1. **Read UniProt Protein Database** given in Rosalind
2. **Works with Python requests** library and gets response
3. **Finds required** motif with **regexp finditer**
4. **Prints to console only found motifs** 