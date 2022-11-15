#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    # Write your code here
    puntos_a = 0
    puntos_b = 0
    i = 0
    j = 0

    while(i < len(a) and j < len(b)):

        if a[i] > b[j]:
            puntos_a += 1
        elif a[i] < b[j]:
            puntos_b += 1
        i += 1
        j += 1

    resultado = [puntos_a, puntos_b]
    print(resultado)







if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = list(map(int, input().rstrip().split()))

    #b = list(map(int, input().rstrip().split()))

    a = [1, 2, 3]
    b = [3, 2, 1]

    result = compareTriplets(a, b)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
