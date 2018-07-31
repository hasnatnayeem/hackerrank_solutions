# https://www.hackerrank.com/challenges/no-idea

n,m = map(int,input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
count = 0

for x in arr:
    if x in A:
        count += 1
    if x in B:
        count -= 1

print(count)

