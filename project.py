def analyzeSequences(sequences):
   minSequence = min(sequences);
   for i in range(len(minSequence)-1, 0, -1):
      for start in range(len(minSequence) - i + 1):
         motif = minSequence[start: start + i]
         if all(motif in seq for seq in sequences):
            print(motif)
            return motif;
   return ""
def compoundSeq(data, indexesR):
   sequences = []
   for i in range(len(indexesR)):
        start = indexesR[i]
        end = indexesR[i+1] if i+1 < len(indexesR) else len(data)
        seq = "".join(data[start+1:end])
        sequences.append(seq)
   analyzeSequences(sequences)

def analyzeR(data):
  indexes_rosalind = [];
  for i, indexR in enumerate(data):
    if(indexR.startswith(">")):
      indexes_rosalind.append(i)
  compoundSeq(data, indexes_rosalind)

with open("rosalind_lcsm.txt", "r") as file:
  data = [line.strip() for line in file.readlines()];
  analyzeR(data)