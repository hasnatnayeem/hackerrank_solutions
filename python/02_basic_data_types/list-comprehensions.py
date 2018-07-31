# https://www.hackerrank.com/challenges/list-comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())

list = [[p, q, r] for p in range(x + 1) for q in range(y + 1) for r in range(z + 1) if p + q + r != n]
print(list)
