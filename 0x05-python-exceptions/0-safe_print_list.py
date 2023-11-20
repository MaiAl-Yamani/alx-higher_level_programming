#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    res = ""
    try:
        for i in range(0, x):
            res += str(my_list[i])
            ret_int = x
    except IndexError:
        ret_int = 0
        for j in my_list:
            ret_int += 1
    print("{}".format(res))
    return ret_int
