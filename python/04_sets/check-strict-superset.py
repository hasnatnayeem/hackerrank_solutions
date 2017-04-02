# https://www.hackerrank.com/challenges/py-check-strict-superset

S = set(input().split())
flag = True
for i in range(int(input())):
    T = set(input().split())
    if not T.issubset(S) and T != S:
        flag = False
        break
print(flag)
