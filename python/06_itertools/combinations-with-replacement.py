# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement

text, length = input().split()
length = int(length)
ans = [''.join(sorted(x)) for x in combinations_with_replacement(text, length)]
print('\n'.join(sorted(ans)))
