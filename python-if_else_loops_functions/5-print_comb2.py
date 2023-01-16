#!/usr/bin/python3

for i in range(99):
    print("{}".format(str(i).zfill(2)), end=", ")
i += 1
print("{}".format(i))
