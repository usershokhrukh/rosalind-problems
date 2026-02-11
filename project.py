import requests
import re

def getResult(text, i):
   motif = r"(?=(N[^P][ST][^P]))";
   result = [];
   for match in re.finditer(motif, text):
      result.append(match.start() + 1);
   if(len(result) != 0):
      print(i)
      print(*result)

def analyze(data):
   for i in data:
      ID = i.split("_")[0];
      response = requests.get(f"https://www.uniprot.org/uniprotkb/{ID}.fasta");
      lines = response.text.strip().split('\n')
      text = "".join(lines[1:])
      getResult(text, i);
      

with open("rosalind_mprt.txt", "r") as file:
   data = file.read().strip().split();
   analyze(data)