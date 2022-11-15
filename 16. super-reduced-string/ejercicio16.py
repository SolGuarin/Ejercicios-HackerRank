def superReducedStringIterative(s):

    if len(s) == 2:
        if s[0] == s[1]:
            return 'Empty String'
        elif s[0] != s[1]:
            return s

    i = 0
    new_string = ""
    ultima_position = s[-1]
    while i < len(s)-1:
        position1 = s[i]
        position2 = s[i+1]
        if position1 != position2:
            new_string = new_string + position1
            i = i + 1
        elif position1 == position2:
            new_string = new_string
            i = i + 2

    if len(new_string) == 0:
        return 'Empty String'

    if len(new_string) > 1 and s[-1]*3 == s[-3:]:
        new_string = new_string + ultima_position

    if s[-1] == s[-2]:
        return new_string

    elif s[-1] != s[-2]:
        new_string = new_string + ultima_position

    return new_string


def superReducedString(s):
    for i in range(len(s)):
        s = superReducedStringIterative(s)

        if s == 'Empty String':
            break
    return s


if __name__ == '__main__':
    s = 'aaabccddd'
    result = superReducedString(s)
    print(result)
