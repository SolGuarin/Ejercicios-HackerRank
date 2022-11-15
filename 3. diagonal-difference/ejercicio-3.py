#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonal_1 = 0
    diagonal_2 = 0
    num_columnas = len(arr[0])
    for i in range(len(arr)):
        for j in range(num_columnas):
            if i == j:
                diagonal_1 += arr[i][j]
            if i + j == num_columnas - 1:
                diagonal_2 += arr[i][j]
                print("it", arr[i][j])
    print(diagonal_1)
    print(diagonal_2)
    return abs(diagonal_1 - diagonal_2)


if __name__ == '__main__':

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)

    print(result)
