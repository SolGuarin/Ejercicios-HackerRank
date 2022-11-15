
def birthday(s, d, m):
    # Write your code here
    print(len(s))
    count = 0
    suma = 0
    for i in s:
        if s[i] + s[i+1] == d:
            count = count + 1
    return count


if __name__ == '__main__':

    s = [1, 2, 1, 3, 2]
    d = 3
    m = 2
    result = birthday(s, d, m)
    print(result)
