# https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = int(input())
s = set(map(int, input().split())) 

for i in range(int(input())):
    comm = input()
    if comm[0] == 'p':
        s.pop()
    else:
        s.discard(int(comm.split()[1]))
print(sum(s))

