#!/usr/bin/python3
def rom_val(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1


def roman_to_int(roman_string):
    roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0
    for i in range(len(roman_string)):
        if roman_string[i] not in roman_list:
            return 0
    num = 0
    i = 0
    while (i < len(roman_string)):
        s1 = rom_val(roman_string[i])
        if (i + 1 < len(roman_string)):
            s2 = rom_val(roman_string[i + 1])
            if (s1 > s2):
                num = num + s1
                i = i + 1
            else:
                if roman_string[i] == 'I' and roman_string[i + 1] in ['V', 'X']:
                    num = num + s2 - s1
                    i = i + 2
                elif roman_string[i] == 'X' and roman_string[i + 1] in ['L', 'C']:
                    num = num + s2 - s1
                    i = i + 2
                elif roman_string[i] == 'C' and roman_string[i + 1] in ['D', 'M']:
                    num = num + s2 - s1
                    i = i + 2
                else:
                    num = num + s1
                    i = i + 1
        else:
            num = num + s1
            i = i + 1
    return num
