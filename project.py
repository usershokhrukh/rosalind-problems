# def rev_complements(seq):
#     comps = {"A": "T", "T": "A", "G": "C", "C": "G"}
#     rev_seq = seq[::-1]
#     result = ""
#     for base in rev_seq:
#         result += comps[base]
#     return result


# def compare(seq_1, seq_2):
#     diffs = 0
#     for i, s in enumerate(seq_1):
#         if diffs > 1:
#             break
#         if s != seq_2[i]:
#             diffs += 1
#     return diffs <= 1


# def correction(data, rosalinds, seqs):
#     data_with_rev = []
#     amount_rev_all = {}
#     for ros in rosalinds:
#         curr_data = data[ros]
#         rev_seq = rev_complements(curr_data)
#         data_with_rev.append(curr_data)
#         data_with_rev.append(rev_seq)
#     # data_with_rev.sort()
#     for seq in data_with_rev:
#         if amount_rev_all.get(seq) is not None:
#             amount_rev_all[seq] = amount_rev_all.get(seq) + 1
#         else:
#             amount_rev_all[seq] = 1
#     corr_pre_res = []
#     for i in amount_rev_all.keys():
#         for i_2 in amount_rev_all.keys():
#             if i != i_2:
#                 if compare(i, i_2):
#                     curr_res = [i, i_2]
#                     curr_res.sort()
#                     corr_pre_res.append(curr_res)
#     set_corr_pre_res = list(set(map(tuple, corr_pre_res)))
#     corr_pre_final = []
#     # # print()
#     # # print(data_with_rev)
#     # print()
#     # print(amount_rev_all)
#     # # print()
#     # # print(corr_pre_res)
#     # print()
#     # print(set_corr_pre_res)
#     for s in set_corr_pre_res:
#         corr_pre_final.append(list(s))
#     for i in corr_pre_final:
#         n_seq_1 = amount_rev_all.get(i[0])
#         n_seq_2 = amount_rev_all.get(i[1])
#         if n_seq_1 >= n_seq_2:
#             if i[1] in seqs:
#                 print(f"{i[1]}->{i[0]}")
#         else:
#             if i[0] in seqs:
#                 print(f"{i[0]}->{i[1]}")
# with open("rosalind_corr.txt", "r") as file:
#     data = file.read().strip().split()
#     ros_file = {}
#     rosalinds = []
#     seqs = []
#     for index, ros in enumerate(data):
#         if ros.startswith(">"):
#             rosalinds.append(ros)
#             for ros_in in range(index + 1, len(data), 1):
#                 if not data[ros_in].startswith(">"):
#                     if ros_file.get(ros) is not None:
#                         ros_file[ros] = ros_file.get(ros) + data[ros_in]
#                     else:
#                         ros_file[ros] = data[ros_in]
#                 else:
#                     break
#     for ros in ros_file.keys():
#         seqs.append(ros_file.get(ros))
#     # print(ros_file)
#     # print()
#     # print(rosalinds)
#     # print()
#     # print(seqs)
#     correction(ros_file, rosalinds, seqs)



def rev_complements(seq):
    comps = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(comps[base] for base in reversed(seq))

def hamming_distance(seq_1, seq_2):
    diffs = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            diffs += 1
        if diffs > 1:
            return False
    return diffs == 1

def solve():
    seqs = []
    with open("rosalind_corr.txt", "r") as f:
        current_seq = ""
        for line in f:
            if line.startswith(">"):
                if current_seq:
                    seqs.append(current_seq)
                current_seq = ""
            else:
                current_seq += line.strip()
        if current_seq:
            seqs.append(current_seq)
    counts = {}
    for s in seqs:
        rev = rev_complements(s)
        canonical = min(s, rev)
        counts[canonical] = counts.get(canonical, 0) + 1
    correct_reads = set()
    incorrect_reads = []

    for s in seqs:
        rev = rev_complements(s)
        canonical = min(s, rev)
        if counts[canonical] >= 2:
            correct_reads.add(s)
            correct_reads.add(rev)
        else:
            incorrect_reads.append(s)
    for xato in incorrect_reads:
        for andoza in correct_reads:
            if hamming_distance(xato, andoza):
                print(f"{xato}->{andoza}")
                break

if __name__ == "__main__":
    solve()