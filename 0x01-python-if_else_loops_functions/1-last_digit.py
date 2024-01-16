#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
ld = abs(number) % 10
if number < 0:
    ld = -ld
if ld > 5:
     print("Last digit of " + str(number) + " is " + str(ld) + " and is greater than 5")
elif ld == 0:
    print("Last digit of " + str(number) + " is " + str(ld) + " and is 0")
elif ld < 6 and ld != 0:
        print("Last digit of " + str(number)+ " is " + str(ld) + " and is less than 6 and not 0")

