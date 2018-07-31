# https://www.hackerrank.com/challenges/string-validators

s = input()
str = list(s)

flag = [0, 0, 0, 0, 0]

for s in str:
    if s.isalnum():
        flag[0] = 1
    if s.isalpha():
        flag[1] = 1
    if s.isdigit():
        flag[2] = 1
    if s.islower():
        flag[3] = 1
    if s.isupper():
        flag[4] = 1

for f in flag:
    if f == 1:
        print("True")
    else:
        print("False")
