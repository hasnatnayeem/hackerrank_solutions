# https://www.hackerrank.com/challenges/py-set-mutations

n = input()
s = set(input().split())

for i in range(int(input())):
    comm = input()
    T = set(input().split())
    if comm[0] == 'i':
        s.intersection_update(T)
    elif comm[0] == 'u':
        s.update(T)
    elif comm[0] == 's':
        s.symmetric_difference_update(T)
    elif comm[0] == 'd':
        s.difference_update(T)

print(sum(map(int, s)))

