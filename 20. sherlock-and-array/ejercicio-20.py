def balancedSums(arr):
    contador = 0
    i = 0
    while i < len(arr):
        suma_right = sum(arr[i+1:])
        suma_left = sum(arr[:i])
        print(suma_right, suma_left)
        if suma_left == suma_right:
            contador += 1
        if suma_left < suma_right:
            return 'NO'
        if contador == 1:
            return 'YES'
        i = i + 1

    return 'NO'


if __name__ == '__main__':

    arr = []
    result = balancedSums(arr)
    print(result)
