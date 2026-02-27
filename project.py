rna_codon_table = {
    # U bilan boshlanadiganlar
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "Stop",
    "UAG": "Stop",
    "UGU": "C",
    "UGC": "C",
    "UGA": "Stop",
    "UGG": "W",
    # C bilan boshlanadiganlar
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",# A bilan boshlanadiganlar
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    # G bilan boshlanadiganlar
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}


def splicing(DNA, introns):
    exons = DNA
    for miniIntrons in introns:
        exons = exons.replace(miniIntrons, "")
    exons = exons.replace("T", "U")
    protein = "".join(
        rna_codon_table.get(exons[codon : codon + 3])
        for codon in range(0, len(exons), 3)
        if rna_codon_table.get(exons[codon : codon + 3]) != "Stop"
    )
    return protein


def read_fasta(file_path):
    sequences = {}
    current_id = None

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                current_id = line[1:] 
                sequences[current_id] = ""
            else:
                sequences[current_id] += line

    return sequences


data = read_fasta("rosalind_splc.txt")

with open("rosalind_splc.txt", "r") as file:
    ros = [line[1:].strip() for line in file.readlines() if line.startswith(">")]
    DNA = data[ros[0]]
    introns = [data[line.strip()] for line in ros[1:]]
    result = splicing(DNA, introns)
    print(result)
