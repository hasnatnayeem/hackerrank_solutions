# https://www.hackerrank.com/challenges/itertools-product

from itertools import product

A = map(int, input().split())
B = map(int, input().split())
for x in list(product(A, B)):
    print(x, end = " ") 
