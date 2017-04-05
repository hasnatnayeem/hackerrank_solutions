from itertools import product

k, m = map(int, input().split())

mylist = []
for i in range(k):
    mylist += [list(map(int, input().split()))[1:]]

maximum = 0
for nums in product(*mylist):
    res = sum([num * num for num in nums]) % m
    if res > maximum:
        maximum = res

print(maximum)
