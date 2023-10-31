#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for ch in range(len(str)):
        if ord(str[ch]) in range(97, 123):
            str_ascii = ord(str[ch]) - 32
            new_str += chr(str_ascii)
        else:
            new_str += str[ch]
            
    print("{}".format(new_str))
    return new_str
