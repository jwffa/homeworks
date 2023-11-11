square_sum(numbers):
    my_sum = []
    for num in numbers:
        num = num ** 2
        my_sum.append(num)
    return sum(my_sum)
#version 2 == return sum([num ** 2 for num in numbers])
