with open("rosalind_long.txt") as file:
    row_data = file.read().strip().split(">")
    data= [];
    for entry in row_data:
        if entry:
            line = entry.strip().split("\n")
            data.append("".join(line[1:]))
    long_super(data)