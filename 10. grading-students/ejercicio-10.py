
"""
dada una lista de notas:
reglas para redondear
-si es menor a 38, no se redondea
-si la diferencia entre la calificación y el siguiente múltiplo de 5 es menor que 3, la calificación
 se redondea al siguiente múltiplo de 5
-si la difrencia es mayor mayor o igual a 3 tampoco se redondea
"""
def gradingStudents(grades):
    # Write your code here
    notas = []
    for i in range(len(grades)):
        if grades[i] < 38:
            notas.append(grades[i])
        elif grades[i] >= 38:
            j = grades[i]
            while j % 10 != 0 and j % 10 != 5:
                j = j+1
            if j - grades[i] < 3:
                notas.append(j)
            elif j - grades[i] >= 3:
                notas.append(grades[i])
    return notas


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # grades_count = int(input().strip())
    grades = [73, 67, 38, 33]
    result = gradingStudents(grades)
    print(result)
