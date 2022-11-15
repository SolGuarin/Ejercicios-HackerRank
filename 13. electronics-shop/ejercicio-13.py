"""
Determinar el teclado y USB más caros que se puedan comprar con un presupuesto dado.
-Si no es posible comprar ambos artículos se terna -1
"""
def getMoneySpent(keyboards, drives, b):

    if min(keyboards)+min(drives) > b:
        return -1
    if min(keyboards)+min(drives) == b:
        return b
    if max(keyboards)+max(drives) <= b:
        return max(keyboards)+max(drives)
    maximum = 0
    for i in keyboards:
        for j in drives:
            if i+j <= b and i + j > maximum:
                maximum = i+j
    return maximum



if __name__ == '__main__':

    keyboards = [40, 50, 60]
    drives = [5, 8, 12]
    b = 60

    result = getMoneySpent(keyboards, drives, b)

    print(result)

