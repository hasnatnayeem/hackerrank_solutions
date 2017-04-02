# https://www.hackerrank.com/challenges/python-lists

list = []
n = int(input())
i = 0
while i < n:
    cmd = input()
    p = cmd.split()
    cmd = p[0]

    if cmd == "insert":
        i = int(p[1])
        e = int(p[2])
        list.insert(i, e)
    elif cmd == "print":
        print(list)
    elif cmd == "remove":
        e = int(p[1])
        list.remove(e)
    elif cmd == "append":
        e = int(p[1])
        list.append(e)
    elif cmd == "sort":
        list.sort()
    elif cmd == "pop":
        list.pop()
    elif cmd == "reverse":
        list.reverse()

    i = i + 1

