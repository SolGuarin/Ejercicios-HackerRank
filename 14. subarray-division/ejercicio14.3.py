def birthday(s, d, m):
    # Write your code here
    j = 0
    while j < len(s):
        if len(s) == 1:
            if s[0] == d and len(s) == m:
                return 1
            else:
                return 0
        suma = 0
        count = 0
        total = 0
        for i in s[j:]:
            suma += i
            count = count + 1
            if count == m and suma == d:
                total = total + 1
            return total
        j += 1



if __name__ == '__main__':

    s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
    d = 18
    m = 7
    result = birthday(s, d, m)
    print(result)
    """
    i = 0
    while i < len(s):
        print(s[i:], birthday(s[i:], d, m))
        i += 1
    """