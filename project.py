def analyzeObject(sequences, objectData):
   for item in sequences:
      for valueS in sequences:
         if(item != valueS):
            end = item[-3:];
            start = valueS[0:3];
            if(start == end):
               print(f"{objectData[item]} {objectData[valueS]}")

def compoundSeq(data, indexesR):
    sequences = []
    objectData = {};
    for i in range(len(indexesR)):
        start = indexesR[i]
        end = indexesR[i+1] if i+1 < len(indexesR) else len(data)
        seq = "".join(data[start+1:end])
        sequences.append(seq)
    for i in range(len(indexesR)):
       objectData[sequences[i]] = data[indexesR[i]].replace(">", "");
    analyzeObject(sequences, objectData)

def analyzeR(data):
  indexes_rosalind = [];
  for i, indexR in enumerate(data):
    if(indexR.startswith(">")):
      indexes_rosalind.append(i)
  compoundSeq(data, indexes_rosalind)

with open("rosalind_grph.txt", "r") as file:
  data = [line.strip() for line in file.readlines()];
  analyzeR(data)
