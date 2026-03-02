import itertools

def lexicog(seq, n):
    combinations = itertools.product(seq, repeat=n);
    for i in combinations:
       print("".join(i))


with open("rosalind_lexf.txt", "r") as file:
  data = file.read().strip().split()
  data_len = len(data);
  sequence = data[:data_len-1]
  n = data[-1]
  lexicog(sequence, int(n))

