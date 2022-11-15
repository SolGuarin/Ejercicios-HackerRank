def pangrams(s):
    s= s.lower()
    s = s.replace(" ","")
    s = sorted(s)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i in s :
        if i == alphabet[count]:
            count += 1
        if count == len(alphabet):
            return "pangram"
    return 'not pangram'
if __name__ == '__main__':
    s = 'Fabio me exige, sin tapujos, que añada cerveza al whisky'
    result = pangrams(s)
    print(result)