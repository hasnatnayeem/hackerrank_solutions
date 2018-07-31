# https://www.hackerrank.com/challenges/collections-counter

from collections import Counter

x = int(input())
sizes = Counter(map(int, input().split()))
earning = 0

for i in range(int(input())):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        earning += price
        sizes[size] -= 1
print(earning)
