import math

def analyzeLif(data):
   k = int(data[0]);
   N = int(data[1]);
   p = 0.25;
   n = 2**k;
   result = 0;
   for i in range(N):
      #$$P(i) = \binom{n}{i} \cdot p^i \cdot (1-p)^{n-i}$$
      c = math.comb(n, i);
      result += c * (p**i) * (0.75**(n-i));
      
   final = 1-result;
   print(round(final, 3))

with open("rosalind_lia.txt", "r") as file:
   data = file.read().strip().split(); 
   analyzeLif(data)