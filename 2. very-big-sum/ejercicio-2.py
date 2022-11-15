
#!/bin/python3

import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    # Write your code here

    suma = 0

    for i in ar:
        suma += i
    print(suma)


if __name__ == '__main__':

    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
