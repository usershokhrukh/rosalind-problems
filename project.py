def unrooted_inod(n):
  return n - 2

with open("rosalind_inod.txt", "r") as file:
  n = int(file.read().strip().split()[0])
  res = unrooted_inod(n)
  print(res)