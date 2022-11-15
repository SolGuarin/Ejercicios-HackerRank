def missingNumbers(arr, brr):

    crr = [b for b in set(brr) if brr.count(b) > arr.count(b)]
    crr.sort()
    return crr

if __name__ == '__main__':
    arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
    brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

    result = missingNumbers(arr, brr)
    print(result)
