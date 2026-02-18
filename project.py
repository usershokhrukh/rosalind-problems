# 1. Codon Table - Biologik lug'at
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

def solve_orf(data):
    found = [];
    for i in range(len(data)):
        if(data[i:i+3] == "ATG"):
            codons = "";
            stop_codons = False;
            for i_2 in range(i, len(data)-2, 3):
                codon = CODON_TABLE.get(data[i_2:i_2+3]);
                if codon == "Stop":
                    stop_codons = True
                    break;
                elif codon == None:
                    break;
                else:
                    codons += codon;
            if stop_codons:
                found.append(codons)
    return found;
def rev_data(data):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'};
    returnData = "";
    for i in reversed(data):
        returnData += (complement.get(i))
    return returnData;
with open("rosalind_orf.txt", "r") as file:
    data = file.read().strip().split()
    input_data = "".join(data[1:])
    unique_proteins = solve_orf(input_data)
    rev_proteins = rev_data(input_data);
    rev_resultData = solve_orf(rev_proteins);
    result = set(unique_proteins + rev_resultData);
    for i in result:
        print(i)