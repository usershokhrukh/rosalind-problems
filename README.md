# Longest Increasing Subsequence

### Problem Description

Another hardest binary problem
if we work with list as [10, 20, 30, 1, 2,], after binary search the **tails** would be [1, 2, 30] the minimum increasing not [10, 20, 30], because **1 < 10** and **2 < 20**, and it gives us to have more chance of building sequence 

after bisect loop, we have **tails_indexes** and **parent** indexes, parent numerated of  pre index in tails_indexes, if tails have [10, 20, 30] then parent would be [-1, 0, 1]

After all outside of loop, if input 10 20 30 1 2 => with index [0, 1, 2, 3, 4], then tails [1, 2, 30] => indexes [3, 4 ,2] , tails_indexes [3, 4, 2] => values [1, 2, 30] , parent [-1, 0, 1, -1, 3] if we match in given input => None, 10, 20, but ```curr = tails_indexes[-1]``` in first curr has value of 2 (last value of tails_indexes) then in line ```result.append(subs[curr])``` result appends subs[2] which is 30, then we should change curr, so in line ```curr = parent[curr]``` first it gets **1** (2 index of parent), then appends subs[1] which is 20, then curr would be 0 (1 index of parent), finally subs[0] and result would be [30, 20, 10], but in problem we should print as increasing with **print[::-1]** it reverses and prints

this was increasing, we also should analyze decreasing:
You can simply get correct result if you change given numbers to negative like [-10, -20, -30, -1, -2], then after function we get [-30, -2]


### Algorithm steps

1. **Acknowledge meaning of the algorithm, then copy paste**
2. **analyze indexes, indexes of parents, then incorrect increasing values** 
3. **solve problem with parent indexes and print reversed values** 
4. **loop decreasing result and change negative to positive numbers**
