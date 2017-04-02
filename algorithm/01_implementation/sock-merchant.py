# https://www.hackerrank.com/challenges/sock-merchant

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
count = [0] * 102
num = 0
for x in c:
    count[x] += 1
    if count[x] % 2 == 0:
        num += 1
print(num)

