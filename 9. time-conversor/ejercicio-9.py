def timeConversion(s):
    if s[0:2] == '01' and s[-2:] == 'PM':
        return '13' + s[2:-2]
    elif s[0:2] == '02' and s[-2:] == 'PM':
        return '14' + s[2:-2]
    elif s[0:2] == '03' and s[-2:] == 'PM':
        return '15' + s[2:-2]
    elif s[0:2] == '04' and s[-2:] == 'PM':
        return '16' + s[2:-2]
    elif s[0:2] == '05' and s[-2:] == 'PM':
        return '17' + s[2:-2]
    elif s[0:2] == '06' and s[-2:] == 'PM':
        return '18' + s[2:-2]
    elif s[0:2] == '07' and s[-2:] == 'PM':
        return '19' + s[2:-2]
    elif s[0:2] == '08' and s[-2:] == 'PM':
        return '20' + s[2:-2]
    elif s[0:2] == '09' and s[-2:] == 'PM':
        return '21' + s[2:-2]
    elif s[0:2] == '10' and s[-2:] == 'PM':
        return '22' + s[2:-2]
    elif s[0:2] == '11' and s[-2:] == 'PM':
        return '23' + s[2:-2]
    elif s[0:2] == '12' and s[-2:] == 'AM':
        return '00' + s[2:-2]
    elif s[0:2] == '12' and s[-2:] == 'PM':
        return s[0:-2]
    elif s[-2:] == 'AM':
        return s[0:-2]
    else:
        return s


if __name__ == '__main__':
    s = '06:40:03AM'

    result = timeConversion(s)
    print(result)