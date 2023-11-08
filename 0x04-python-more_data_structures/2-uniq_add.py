#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
    unique_sum = reduce((lambda x, y: x + y), unique_list)
    return unique_sum
