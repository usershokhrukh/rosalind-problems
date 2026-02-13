def analyze(data):
   n = 1000000
   startCount = 1;
   codon_counts = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2,
        'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4,
        'A': 4, 'D': 2, 'E': 2, 'G': 4
    }
   for aa in data:
      startCount = (startCount * codon_counts[aa]) % n;
   startCount = (startCount*3) % n
   return startCount

with open("rosalind_mrna.txt", "r") as file:
   data = file.read().strip();
   print(analyze(data))