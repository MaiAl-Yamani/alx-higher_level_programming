#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    unique_sum = 0
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    for i in unique_list:
        unique_sum += i
    return unique_sum
