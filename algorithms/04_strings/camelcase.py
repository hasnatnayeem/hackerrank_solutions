# https://www.hackerrank.com/challenges/camelcase

s = input().strip()

count = 1
for c in s:
    if c.isupper():
        count += 1
print(str(count))
