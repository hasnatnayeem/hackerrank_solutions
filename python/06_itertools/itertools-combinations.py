from itertools import combinations

line, length = input().split()
for i in range(1, int(length) + 1):
    print('\n'.join(sorted(''.join(sorted(s)) for s in combinations(line,i))))
