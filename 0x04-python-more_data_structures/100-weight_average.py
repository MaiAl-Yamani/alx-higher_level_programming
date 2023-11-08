#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    res = 0
    denom_add = 0
    for first, second in my_list:
        res += first * second
        denom_add += second
    avg_res = res / denom_add
    return avg_res
