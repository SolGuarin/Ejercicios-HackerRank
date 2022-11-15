"""
Dos niños, Lily y Ron, quieren compartir una barra de chocolate. Cada uno de los cuadrados tiene un
número entero.
Lily decide compartir un segmento contiguo de la barra seleccionada de manera que:
    * La longitud del segmento coincide con el mes de nacimiento de Ron
    * La suma de los números enteros en los cuadrados es igual a su día de nacimiento.
Determine how many ways she can divide the chocolate.
"""


def birthday(s, d, m):

    j = 0
    total = 0
    while j < len(s):
        if len(s) == 1:
            if s[0] == d and len(s) == m:
                return 1
            else:
                return 0

        suma = 0
        count = 0
        for i in s[j:]:
            suma = suma + i
            count = count + 1
            if suma == d and count == m:
                total = total + 1
        j = j + 1
    return total

    
if __name__ == '__main__':
    s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
    d = 18
    m = 7
    result = birthday(s, d, m)
    print(result)
