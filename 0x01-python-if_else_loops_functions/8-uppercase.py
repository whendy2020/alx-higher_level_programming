#!/usr/bin/python3

def uppercase(str):
    newStr = ""
    for convert in str:
        if convert >= 'a' and convert <= 'z':
            newStr += chr(ord(convert) - 32)
        else:
            newStr += convert
    print("{}".format(newStr))
