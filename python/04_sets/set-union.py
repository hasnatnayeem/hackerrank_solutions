# https://www.hackerrank.com/challenges/py-set-union

n1 = int(input())
a = set(map(int, input().split()))

n2 = int(input())
b = set(map(int, input().split()))
    
print(str(len(a.union(b))))
