# https://www.hackerrank.com/challenges/tutorial-intro

v = int(input())
n = int(input())
arr = list(map(int, input().strip().split(' ')))

for i in range(n):
    if arr[i] == v:
        print(i)
        break
