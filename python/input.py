# https://www.hackerrank.com/challenges/input/problem

x, k = map(int,input().split())
polynomial = input()
result = eval(polynomial)
print(result == k)

