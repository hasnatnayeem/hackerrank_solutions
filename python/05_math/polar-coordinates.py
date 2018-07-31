# https://www.hackerrank.com/challenges/polar-coordinates

import cmath

s = input()

if s.find('+') != -1:
    x = s[:s.find('+', 1)]
    y = s[s.find('+', 1) + 1:-1]
elif s.find('-', 1) != -1 :
    x = s[:s.find('-', 1)]
    y = s[s.find('-', 1): -1]

print(abs(complex(int(x), int(y))))
print(cmath.phase(complex(int(x), int(y))))
