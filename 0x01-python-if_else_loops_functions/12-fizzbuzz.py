#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i == 100:
            print("{}".format(i))
        elif i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz ")
            print("Fizz ")
        elif i % 5 == 0:
            print("Buzz ")
        else:
            print("{} ".format(i))
