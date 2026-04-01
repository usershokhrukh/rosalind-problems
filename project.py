def rosalind_tran(seq_arr):
    transitions = 0
    transversions = 0
    purines = {'A': 'A', 'G': 'G'}
    pyrimidines = {'C': 'C', 'T': 'T'}
    seq_1 = seq_arr[0]
    seq_2 = seq_arr[1]
    for i in range(len(seq_1)):
        if(seq_1[i] == seq_2[i]): continue
        if purines.get(seq_1[i]) is not None:
            if purines.get(seq_2[i]) is not None: transitions += 1
            else: transversions += 1;
        else:
            if pyrimidines.get(seq_2[i]) is not None: transitions += 1
            else: transversions += 1;
    result = "No transversions found"
    if transversions and transitions:
        result = transitions / transversions
    return f"{result:.11f}"
with open("rosalind_tran.txt", "r") as file:
    data = {};
    seq_data = file.readlines()
    ros_values = []
    for index, item in enumerate(seq_data):
        if(item.strip().startswith(">")):
            for i in range(index+1, len(seq_data), 1):
                if(seq_data[i].strip().startswith(">")): break;
                curr_value = data.get(item.strip());
                if curr_value is not None:
                    data[item.strip()] = curr_value + seq_data[i].strip();
                else:
                    data[item.strip()] = seq_data[i].strip();
            ros_values.append(item.strip())
    sequences = []
    for ros in ros_values:
        sequences.append(data.get(ros));
    print(rosalind_tran(sequences))
                