# https://www.hackerrank.com/challenges/swap-case

def swap_case(s):
    str = ""
    for c in s:
        if c >= 'A' and c <= 'Z':
            str += chr(ord(c) + 32)
        elif c >= 'a' and c <= 'z':
            str += chr(ord(c) - 32)
        else:
            str += c
    return str
