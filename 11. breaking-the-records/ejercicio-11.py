def breakingRecords(scores):
    # Write your code here
    cont1 = 0
    cont2 = 0
    puntaje_mayor = scores[0]
    puntaje_menor = scores[0]

    for i in range(len(scores)):
        if scores[i] > puntaje_mayor:
            puntaje_mayor = scores[i]
            cont1 = cont1 + 1
        if scores[i] < puntaje_menor:
            puntaje_menor = scores[i]
            cont2 = cont2 + 1
    return cont1, cont2


if __name__ == '__main__':
    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    result = breakingRecords(scores)
    print(result)
