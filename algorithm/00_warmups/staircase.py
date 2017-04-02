# https://www.hackerrank.com/challenges/staircase


n = int(input().strip())
space = i = 1

while i <= n:
    for x in range(0, n - i):
        print(" ", end = "")
    for x in range(n - i, n):
        print("#", end = "")
    i += 1
    print()

