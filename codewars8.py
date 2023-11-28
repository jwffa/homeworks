def move_zeros(list): #5kyu
    new_list = []
    zero_list = []
    for i in list:
        if i == 0:
            zero_list.append(i)
    for j in list:
        if j != 0:
            new_list.append(j)
    return new_list + zero_list
