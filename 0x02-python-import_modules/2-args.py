#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{:d} ".format(len(argv) - 1), end="")
    if (len(argv) == 1):
        print("arguments.")
    elif (len(argv) == 2):
        print("argument:")
    else:
        print("arguments:")

    if (len(argv) >= 2):
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
