# https://www.hackerrank.com/challenges/symmetric-difference

n, a = int(input()), set(map(int,input().split()))
m, b = int(input()), set(map(int,input().split()))
for x in sorted(a.union(b) - a.intersection(b)):
    print(x)
