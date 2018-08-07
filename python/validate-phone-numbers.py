# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
pattern = '^[789]{1}\d{9}$'
for i in range(int(input())):
    if re.match(pattern, input()):
        print("YES")
    else:
        print("NO")
