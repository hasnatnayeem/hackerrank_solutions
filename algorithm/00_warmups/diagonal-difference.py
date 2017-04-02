# https://www.hackerrank.com/challenges/diagonal-difference


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
d1 = d2 = i = 0
j = n - 1

for x in a:
    d1 += x[i]
    d2 += x[j]
    i += 1
    j -= 1

print(abs(d1-d2))
