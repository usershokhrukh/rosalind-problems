def long_super(data):
    match = data.pop(0)
    
    while len(data) > 0:
        found = False
        for i in range(len(match), 0, -1):
            overlap_seq = match[-i:]
            some = next(([idx, x] for idx, x in enumerate(data) if x.startswith(overlap_seq) and i > (len(x) // 2)), None)
            
            if some:

                match += some[1][i:]
                data.pop(some[0])
                found = True
                break
        
        if found: continue 

        for i in range(len(match), 0, -1):
            overlap_seq = match[:i]
            some = next(([idx, x] for idx, x in enumerate(data) if x.endswith(overlap_seq) and i > (len(x) // 2)), None)
            if some:
                match = some[1][:len(some[1])-i] + match
                data.pop(some[0])
                found = True
                break
        if not found and data:
            match += data.pop(0)

    print(match)

with open("rosalind_long.txt") as file:
    row_data = file.read().strip().split(">")
    data = []
    for entry in row_data:
        if entry:
            line = entry.strip().split("\n")
            data.append("".join(line[1:]))
    long_super(data)