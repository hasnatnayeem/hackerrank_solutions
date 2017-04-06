# https://www.hackerrank.com/challenges/py-collections-ordereddict

from collections import OrderedDict

d = OrderedDict()

n = int(input())
for i in range(n):
    line = input().split()
    item = ' '.join(line[:-1])
    price = int(line[-1])
    
    if item in d:
        d[item] += price
    else:
        d[item] = price

for x in d:
    print(x + ' ' + str(d[x]))
