import bisect
# 9
# 3 7 12 16 1 2 3 4 5

def match_LGIS(n, subs):
  tails = []
  tails_indexes = []
  parent = [-1] * n
  for i, x in enumerate(subs):
    position = bisect.bisect_left(tails, x);
    if position < len(tails):
      tails[position] = x # 1 2 3 4 5
      tails_indexes[position] = i # 4 5 6 7 8
    else :
      tails.append(x)
      tails_indexes.append(i)
    if position > 0:
      parent[i] = tails_indexes[position - 1] # -1 4 5 6 7
  curr = tails_indexes[-1]
  result = []
  print(tails, tails_indexes, parent)
  while curr != -1:
    result.append(subs[curr])
    curr = parent[curr]
  return result[::-1]

      
with open("rosalind_lgis.txt", "r") as file:
  data = file.read().strip().split();
  subsequence = list(map(int, data))
  print(*match_LGIS(subsequence[0], subsequence[1:]))
  de_subsequence = [-x for x in subsequence]
  de_result = match_LGIS(subsequence[0], de_subsequence[1:])
  print(de_result)
  de_final = [-x for x in de_result];
  print(*de_final)
