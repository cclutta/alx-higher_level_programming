#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
m = number % 10
if m > 5:
    print(f"The last digit of {number} is {m} and is greater than 5")
elif number == 0:
    print(f"The last digit of {number} is {m} and is 0")
elif m < 6 and m != 0:
    print(f"The last digit of {number} is {m} and is less than 6 and not 0")
