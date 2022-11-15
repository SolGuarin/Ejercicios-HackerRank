def icecreamParlor(m, arr):
    """
    i = 0
    m = 4
    while i < len(arr)-1:
        sum = 0
        pos1 = i
        pos2 = i + 1
        for element in arr:
            sum = arr[i] + arr[i+1]
        if sum == m:
            break
        i = i + 1
    return pos1+1, pos2+1
    """


    i = 0
    while i < len(arr):
        sum = 0
        pos1 = 0
        pos2 = 0
        j = 1
        while j < len(arr):
            sum = arr[i] + arr[j]
            if sum == m:
                print(j)
                pos1 = i
                pos2 = j
                if i == j:
                    pos2 = j + 1
                return pos1+1, pos2+1
            j = j + 1
        i = i + 1


if __name__ == '__main__':
    m = 8
    arr = [1, 3, 4, 4, 6, 8]
    result = icecreamParlor(m, arr)
    print(result)
