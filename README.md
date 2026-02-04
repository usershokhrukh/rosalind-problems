# you can visit this problem on https://rosalind.info/problems/iev/ 
# let's try to understand this problem =>
# first we should know what means 1 0 0 1 0 1
# we have six different numbers up to 20,000
# and analyze to dominant table AA-AA AA-Aa AA-aa Aa-Aa Aa-aa aa-aa
# first number has given as 1, it means we have 1 pairs of AA-AA, second number has given as 0 we have 0 pairs of AA-Aa, and etc.
# we should give percent of dominant next generation, dominant must ber at least one A in genotype
# if we sprinkle AA-AA, it gives 100% at least A, but if we do with another one Aa-Aa it would be 50% percent of A
# with E = 2 * ((n1 * 1) + (n2 * 1) + (n3 * 1) + (n4 * 0.75) + (n5 * 0.5) + (n6 * 0)), after entering 1 0 0 1 0 1, we obtain 3.5 
# rosalind-problems
