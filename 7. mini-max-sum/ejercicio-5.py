#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    max_num = arr[0]
    position = 0
    new_list = arr.copy()
    min_sum = 0
    max_sum = 0

    # Encuentra el número mayor y lo elimina
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            position = i
    new_list.pop(position)

    # Encuentra el número menor y lo elimina
    min_num = arr[0]
    position2 = 0
    new_list2 = arr.copy()
    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            position2 = i
    new_list2.pop(position2)

    # suma mínima y máxima
    for i in new_list:
        min_sum += i
    for i in new_list2:
        max_sum += i
    return min_sum, max_sum





if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]
    result = miniMaxSum(arr)
    print(result)

