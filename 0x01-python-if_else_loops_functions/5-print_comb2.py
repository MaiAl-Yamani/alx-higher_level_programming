#!/usr/bin/python3
for i in range(0,100):
    if i in range(0, 10):
        i = "0" + str(i)
    if i == 99:
        print("{}".format(i))
    else:
        print("{}, ".format(i), end="")
