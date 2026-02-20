import itertools;

def analyze(number):
    numbers = list(range(1, number +1));
    # print(numbers)
    permutations = list(itertools.permutations(numbers));
    print(len(permutations))
    for i in permutations:
        print(*i);


with open("rosalind_perm.txt", "r") as file:
   number = file.read().strip();
   analyze(int(number));