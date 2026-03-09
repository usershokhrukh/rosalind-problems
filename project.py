import math

def alg_perfect_match(seq):
  adenin = seq.count("A")
  guanine = seq.count("G")
  adening_fact = math.factorial(adenin)
  guanine_fact = math.factorial(guanine)
  result = adening_fact * guanine_fact
  return result

with open("rosalind_pmch.txt") as file:
  data = [part for part in file.read().strip().split() if not part.startswith(">")]
  seq = "".join(data[:])
  print(alg_perfect_match(seq))