def balancedSums(arr):
    i = 0
    derecha = [0]
    izquierda = [0]
    i = 1
    while i < len(arr):
        suma = 0
        suma = sum(arr[-i:])
        derecha.append(suma)
        i += 1
    derecha2 = list(reversed(derecha))
    j = 0
    while j < len(arr)-1:
        suma = 0
        suma = sum(arr[0:j+1])
        izquierda.append(suma)
        j += 1

    print(derecha2)
    print(izquierda)
    i = 0
    se_cumple = 'NO'

    while i < len(arr):
        if derecha2[i] == izquierda[i]:
            se_cumple = 'YES'
            break
        i += 1

    return se_cumple

if __name__ == '__main__':

    arr = [1, 1, 4, 1, 1]
    result = balancedSums(arr)
    print(result)
