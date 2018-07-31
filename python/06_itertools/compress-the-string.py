# https://www.hackerrank.com/challenges/compress-the-string

from itertools import groupby

print(' '.join(['(' + str(len(list(cs))) + ', ' + s + ')' for s, cs in groupby(input())]))

