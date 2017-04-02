# https://www.hackerrank.com/challenges/plus-minus

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
len = len(arr)
positive = negative = zero = 0
for num in arr:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("%.6f\n%.6f\n%.6f" % (positive / len, negative / len ,zero / len))

