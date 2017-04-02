# https://www.hackerrank.com/challenges/py-introduction-to-sets

def average(array):
    nums = set()
    for num in array:
        nums.add(num)
    return sum(nums)/len(nums)
