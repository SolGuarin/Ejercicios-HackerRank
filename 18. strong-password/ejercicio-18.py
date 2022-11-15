def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    contadores = {
        'count_num': 0,
        'count_lower': 0,
        'count_upper': 0,
        'count_special_char': 0
    }
    num = 0
    chars_missing = 0

    for i in password:
        for j in numbers:
            if i == j:
                contadores['count_num'] = contadores['count_num'] + 1

    for i in password:
        for j in lower_case:
            if i == j:
                contadores['count_lower'] = contadores['count_lower'] + 1

    for i in password:
        for j in upper_case:
            if i == j:
                contadores['count_upper'] = contadores['count_upper'] + 1

    for i in password:
        for j in special_characters:
            if i == j:
                contadores['count_special_char'] = contadores['count_special_char'] + 1

    if len(password) < 6:
        chars_missing = 6 - len(password)
        # return num

    for clave in contadores:
        if contadores.get(clave) == 0:
            num = num + 1

    if chars_missing > num:
        return chars_missing
    else:
        return num


if __name__ == '__main__':
    n = 11
    password = 'Ab1'
    result = minimumNumber(n, password)
    print(result)
