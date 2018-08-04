# https://www.hackerrank.com/challenges/any-or-all/problem

n = input()
numbers = list(map(int, input().split()))
print(all([x >= 0 for x in numbers]) and any([str(x) == str(x)[::-1] for x in numbers]))