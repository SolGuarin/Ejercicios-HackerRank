import math
import os
import random
import re
import sys


def superReducedString(s):


        new_string = ""

        letra = s[0]
        i = 0
        while i < len(s):
            print(letra)
            if s[i] == letra:
                letra = s[i]
            elif s[i] != letra:
                new_string = new_string + letra
                letra = s[i]
            i = i + 1
        return new_string
        """
        for i in range(len(s)):
            position1 = s[i]
            position2 = s[i + 1]
            if position1 != position2:
                new_string = new_string + position1
            i = i + 1
        return new_string
        """



if __name__ == '__main__':
    s = 'aaabccddd'
    result = superReducedString(s)
    print(result)