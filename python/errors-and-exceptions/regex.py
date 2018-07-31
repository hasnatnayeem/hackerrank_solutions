import re

# https://www.hackerrank.com/challenges/incorrect-regex/problem

for i in range(int(input())):
    pattern = input()
    try:
        re.compile(pattern)
        print(True)
    except:
        print(False)