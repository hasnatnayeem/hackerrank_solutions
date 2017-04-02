# https://www.hackerrank.com/challenges/divisible-sum-pairs

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

count = 0
len = len(a)
for num in range(0, len):
    for x in range(0, len):
        if num < x and (a[x] + a[num]) % k == 0:
            count += 1
print(count)
