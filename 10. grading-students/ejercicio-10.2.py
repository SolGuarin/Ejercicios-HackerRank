def gradingStudents(grades):
    nota = []

    if grades[0] < 38:
        nota.append(grades[0])
    elif grades[0] >= 38:
        i = grades[0]
        while i % 10 != 5 and i %10 != 0:
            i = i + 1
        if i - grades[0] < 3:
            nota.append(i)
        elif i - grades[0] >= 3:
            nota.append(grades[0])
    return nota


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # grades_count = int(input().strip())
    grades = [67]
    result = gradingStudents(grades)
    print(result)