with open("rosalind_tree.txt", "r") as file:
  numbers = file.read().strip().split()
  n = int(numbers[0])-1
  pairs = int((len(numbers)-1)/2)
  print(n - pairs)