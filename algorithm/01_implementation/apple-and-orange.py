# https://www.hackerrank.com/challenges/apple-and-orange

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
c1 = c2 = 0

for num in apple:
    if a + num >= s and a + num <= t:
        c1 += 1
for num in orange:
    if b + num >= s and b + num <= t:
        c2 += 1
        
print(str(c1) + "\n" + str(c2))  

