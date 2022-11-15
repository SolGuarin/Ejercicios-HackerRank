def staircase(n):

    simbolo = '#'
    espacio = " "
    for i in range(1, n+1):
        print(f"{espacio * (n - i)}{simbolo * i}")


if __name__ == '__main__':
    #n = int(input().strip())

    n = 6
    staircase(n)
