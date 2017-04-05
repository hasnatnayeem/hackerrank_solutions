from itertools import combinations
from math import factorial

string, length = input().split() 
length = int(length)
str_length = len(string)

ans = combinations(string, length)
c = 0
for item in ans:
    if 'a' in item:
        c += 1

ans = c / (factorial(str_length) / (factorial(length) * factorial(str_length - length)))
print("%.3f" % ans)



