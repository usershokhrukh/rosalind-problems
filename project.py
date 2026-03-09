import math

def alg_perfect_match(seq):
  adenine = seq.count("A")
  guanine = seq.count("G")
  adenine_fact = math.factorial(adenine)
  guanine_fact = math.factorial(guanine)
  result = adenine_fact * guanine_fact
  return result

with open("rosalind_pmch.txt") as file:
  data = [part for part in file.read().strip().split() if not part.startswith(">")]
  seq = "".join(data[:])
  print(alg_perfect_match(seq))