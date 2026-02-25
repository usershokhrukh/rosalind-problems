def analyze_revp(seq):
    matching = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reversedSeq = "".join(matching.get(i) for i in reversed(seq));
    return seq == reversedSeq;

def main_revp(data):
    for i in range(len(data)):
        for length in range(4, 13):
            if(i+length <= len(data)):
                seq = data[i:i+length];
                result = analyze_revp(seq);
                if(result):
                    print(f"{i+1} {len(seq)}")

with open("rosalind_revp.txt", "r") as file:
    data = file.readlines()
    seq = "".join(line.strip() for line in data[1:])
    main_revp(seq)