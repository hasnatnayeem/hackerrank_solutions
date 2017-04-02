# https://www.hackerrank.com/challenges/mini-max-sum

import sys

ans = []
nums = list(map(int, input().strip().split(' ')))
nums.sort()
sum = sum(nums)
print("%d %d" % (sum - nums[-1], sum - nums[0]))

