x, k = tuple(map(int,input().split()))
polynomial = input()
result = eval(polynomial.replace('x', str(x)))
print(result == k)

