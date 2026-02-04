def mathAnalyze(data):
   resultReturn = 2 * ((int(data[0])*1) + (int(data[1]) * 1) + (int(data[2]) * 1) + (int(data[3]) * 0.75) + (int(data[4]) * 0.5) + (int(data[5]) * 0))
   return resultReturn;
with open("rosalind_iev.txt", "r") as file:
   data = file.read().strip().split();
   print(mathAnalyze(data))
