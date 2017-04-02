# https://www.hackerrank.com/challenges/compare-the-triplets

import sys

a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

c1 = 0
c2 = 0

a = [a0, a1, a2]
b = [b0, b1, b2]

for i in range(3):
    if a[i] > b[i]:
        c1 += 1;
    elif b[i] > a[i]:
        c2 += 1
print(str(c1) + " " + str(c2))
