memo = {}


def sequence_cat(seq):
    if seq == "":
        return 1
    if seq in memo:
        return memo[seq]

    res = 0

    for k in range(1, len(seq), 2):
        pair = seq[0] + seq[k]

        if pair in ["AU", "UA", "GC", "CG"]:
            res += sequence_cat(seq[1:k]) * sequence_cat(seq[k + 1 :])
    memo[seq] = res
    return res


with open("rosalind_cat.txt", "r") as file:
    sequence = "".join(seq for seq in file.read().strip().split()[1:])
    print(sequence_cat(sequence) % 1_000_000)