import math
import os
import random
import re
import sys


def superReducedString(s):
    """
     s = list(s)
     position = 0
     i = 0
     while i < len(s):
         if s[i] == s[i+1]:
             position = s[i]
             s = s.pop(position)
         i = i + 1
     return s
     """

    new_string = ""

    i = 0
    while i < len(s) :
        if s[i] != s[i+1]:
            new_string = new_string + s[i]
        elif s[i] == s[i+1]:
            new_string = new_string
        i = i + 1

    return new_string




if __name__ == '__main__':
    s = 'aaabccddd'
    result = superReducedString(s)
    print(result)