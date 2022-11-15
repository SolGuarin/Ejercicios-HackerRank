"""
Dada una lista, encontrar la proporción de números positivos, números negativos y ceros
"""

def plusMinus(arr):
    # Write your code here
    count_pos = 0
    count_neg = 0
    count_zero = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            count_pos = count_pos + 1
        elif arr[i] < 0:
            count_neg = count_neg + 1
        else:
            count_zero = count_zero + 1

    proportion_positive = (round(count_pos / len(arr), 6))
    proportion_negative = (round(count_neg/len(arr), 6))
    proportion_zero = (round(count_zero/len(arr), 6))
    print(proportion_positive)
    print(proportion_negative)
    print(proportion_zero)

if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
