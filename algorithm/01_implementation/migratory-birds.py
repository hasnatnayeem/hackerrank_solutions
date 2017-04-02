# https://www.hackerrank.com/challenges/migratory-birds

import sys

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
l = [0] * 5
for x in types:
    l[x - 1] += 1
maximum = 0
index = 0
for i in range(5):
    if l[i] > maximum:
        maximum = l[i]
        index = i
print(index + 1)
