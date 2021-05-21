#!/usr/bin/env python

import sys

def fonction_cesar(key, str):
    key = 26 - key
    string = str.upper()
    res = ""
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):
            res += chr((ord(char) + key-65) % 26 + 65)
    res = res.lower();
    return(res)

lenSys = len(sys.argv)

if lenSys > 3 or lenSys < 2:
    print("Usage: ./Decode_cesar.py str key(key is optional)")
elif lenSys == 3:
    if sys.argv[2].isdigit():
        print fonction_cesar(int(sys.argv[2]) % 26, sys.argv[1])
    else:
        print("Error: key is not a digit.")
else:
    for i in range(26):
        print fonction_cesar(i, sys.argv[1]) + " for key: " + str(i) + "\n"
