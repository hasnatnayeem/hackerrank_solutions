# https://www.hackerrank.com/challenges/defaultdict-tutorial

from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n+1):
    d[input()].append(i)
for p in range(m):
    search = d[input()]
    if search == []:
        print(-1)
    else:
        print(*search)

