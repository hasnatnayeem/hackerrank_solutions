# https://www.hackerrank.com/challenges/py-the-captains-room

k = int(input())
l = input().split()

c = set()
g = set()

for i in l:
    if i not in g:
        c.add(i)
        g.add(i)
    else:
        c.discard(i)
print(c.pop())

