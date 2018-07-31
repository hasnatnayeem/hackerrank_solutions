# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

n = int(input())
arr = map(int, input().split())
list = list(set(arr))
list.sort()
print(list[-2])
