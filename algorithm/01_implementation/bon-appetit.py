# https://www.hackerrank.com/challenges/bon-appetit

n, k = map(int, input().split())
prices = [int(temp) for temp in input().split()]
taken = int(input())
if (sum(prices) - prices[k]) // 2 == taken:
    print("Bon Appetit")
else:
    print(taken - (sum(prices) - prices[k])// 2)

