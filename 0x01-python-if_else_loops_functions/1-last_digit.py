#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_str = str(number)[-1]
last_digit_int = int(last_digit_str)
print("Last digit of {} is {} ".format(number, last_digit_int), end='')
if last_digit_int > 5:
    print("and is greater than 5")
elif last_digit_int == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
