# https://www.hackerrank.com/challenges/word-order

from collections import OrderedDict

d = OrderedDict()
n = int(input())
for i in range(n):
    word = input()    
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(len(d))
print(*d.values())
