from itertools import permutations

line, length = input().split()
print('\n'.join(sorted(''.join(p) for p in permutations(line, int(length)))))

