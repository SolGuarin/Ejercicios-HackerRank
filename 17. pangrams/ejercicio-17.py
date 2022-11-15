def pangrams(s):
    cont = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0
    for i in s:
        print(i)
        if i == 'a' or i == 'A':
            a = a + 1
            print(a)
        if i == 'b' or i == 'B':
            b += 1
        if i == 'c' or i == 'C':
            c += 1
        if i == 'd' or i == 'D':
            d += 1
        if i == 'e' or i == 'E':
            e += 1
        if i == 'f' or i == 'F':
            f += 1
        if i == 'g' or i == 'G':
            g += 1
        if i == 'h' or i == 'H':
            h += 1
        if i == 'i' or i == 'I':
            i += 1
        if i == 'j' or i == 'J':
            j += 1
        if i == 'K' or i == 'k':
            k += 1
        if i == 'l' or i == 'L':
            l += 1
        if i == 'm' or i == 'M':
            m += 1
        if i == 'n' or i == 'N':
            n += 1
        if i == 'o' or i == 'O':
            o += 1
        if i == 'p' or i == 'P':
            p += 1
        if i == 'q' or i == 'Q':
            q += 1
        if i == 'r' or i == 'R':
            r += 1
        if i == 's' or i == 'S':
            s += 1
        if i == 't' or i == 'T':
            t += 1
        if i == 'u' or i == 'U':
            u += 1
        if i == 'v' or i == 'V':
            v += 1
        if i == 'w' or i == 'W':
            w += 1
        if i == 'x' or i == 'X':
            x += 1
        if i == 'y' or i == 'Y':
            y += 1
        if i == 'z' or i == 'Z':
            z += 1
        cont = cont + 1

    if a >= 1 and b >= 1 and c >= 1 and d >=1 and e >= 1 and f >= 1 and g >= 1 and h >= 1 and i >= 1 and j >= 1 and k >= 1 and l >= 1 and m >= 1 and n >= 1 and o >= 1 and p >= 1 and q >= 1 and r >= 1 and s >= 1 and t >= 1 and u >= 1 and v >= 1 and w >= 1 and x >= 1 and y >= 1 and z >= 1:
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':
    s = 'Fabio me exige, sin tapujos, que añada cerveza al whisky'
    result = pangrams(s)
    print(result)
