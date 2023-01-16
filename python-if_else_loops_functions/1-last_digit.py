#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
modu = number % 10

print(f"Last digit of {number} is", end=" ")

if (number < 0):
        modu = number % -10
if (modu < 6 and modu != 0):
        print(f"{modu} and is less than 6 and not 0")
elif (modu > 5):
        print(f"{modu} and is greater than 5")
else:
        print(f"{modu} and is 0")
