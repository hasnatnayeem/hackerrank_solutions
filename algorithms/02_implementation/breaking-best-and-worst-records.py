# https://www.hackerrank.com/challenges/breaking-best-and-worst-records


n = int(input().strip())
score = list(map(int, input().strip().split(' ')))

high = low = score[0]
c1 = c2 = 0

for x in score:
    if x > high:
        c1 += 1
        high = x
    if x < low:
        c2 += 1
        low = x
print(str(c1) + " " + str(c2))

