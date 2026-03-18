import math

def probability_main(seq, probs):
    log_results = []
    for x in probs:
        summa_log = 0;
        prob_gc = float(x) /2
        prob_at = (1-float(x))/2
        for nucleotide in seq:
            if nucleotide in "GC":
                summa_log += math.log10(prob_gc)
            else:
                summa_log += math.log10(prob_at)

        log_results.append("{:.3f}".format(summa_log))
    return log_results;
with open("rosalind_prob.txt") as file:
    sequence = ""
    probabilities = []
    for i in file.readlines():
        line = i.strip()
        hasA = line.find("A") != -1
        hasT = line.find("T") != -1
        hasC = line.find("C") != -1
        hasG = line.find("G") != -1
        if(hasA or hasT or hasG or hasC):
            sequence += (line)
        else:
            probabilities.extend(line.split())
    result = probability_main(sequence, probabilities)
    print(*result)