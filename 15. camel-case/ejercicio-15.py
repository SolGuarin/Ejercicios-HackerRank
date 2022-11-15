import math
import os
import random
import re
import sys
"""
Determinar cuántas palabras tiene una cadena:
    Ejemplo: 
    saveChangesInTheEditor --- tiene 5
    save
    Changes
    In
    The
    Editor
"""


def camelcase(s):
    s2 = s.lower()
    total = 0

    if s[0] == s2[0]:
        total = total + 1
    i = 0
    while i < len(s):
        if s[i] == s[i].upper():
            total = total + 1
        i = i + 1
    return total


if __name__ == '__main__':
    s = 'saveChangesInTheEditor'
    result = camelcase(s)
    print(result)
