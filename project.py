with open("rosalind_sseq.txt", "r") as f:
    parts = f.read().split(">")
    s = "".join(line.strip() for line in parts[1].splitlines()[1:])
    t = "".join(line.strip() for line in parts[2].splitlines()[1:])
    pos = 0
    results = []
    n = len(t)
    for char in t:
        let = s[pos:].find(char) + pos +1
        exist = s[pos:].find(char)
        t_in_s = s[pos:].find(t) +1
        if let >= pos:
            pos = let
        if t_in_s == let:
            pos += n
        if(exist != -1):
            results.append(let)
    if(len(results) == n):
        print(*(results))
    else:
        results = []
        pos = 0
        for char in t:
            let = s[pos:].find(char) + pos +1
            if(let >= pos):
                pos = let
            results.append(let)
        print(*(results))