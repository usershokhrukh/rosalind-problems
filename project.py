import itertools

def perm_sign(n):
    signs = list(range(1, n+1))
    perms =  list(itertools.permutations(signs))
    pows = 2 ** n

    with open("result.txt", "a") as file:
        file.write(f"{len(perms) * pows}\n")
        for p in perms:
            for sign in itertools.product([-1, 1], repeat=n):
                test = [p[i] * sign[i] for i in range(n)]
                result = " ".join(map(str, test))
                file.write(f"{result}\n")
with open("rosalind_sign.txt", "r") as file:    
    n = int(file.read().strip())
    perm_sign(n)
