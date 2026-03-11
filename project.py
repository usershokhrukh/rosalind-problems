def func_pper(data):
    n = int(data[0])
    k = int(data[1])

    permutations = 1
    for i in range(k):
        permutations = (permutations * (n - i)) % 1_000_000
    return permutations


with open("rosalind_pper.txt", "r") as file:
    nums = file.read().strip().split()
    print(func_pper(nums))
