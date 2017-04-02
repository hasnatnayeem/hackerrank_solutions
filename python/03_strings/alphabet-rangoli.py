# https://www.hackerrank.com/challenges/alphabet-rangoli

def print_rangoli(n):
    s = ""
    width = 4 * n - 3
    result = []

    for x in range(n, 0, -1):
        for i in range(n , x - 1, - 1):
            s += chr(96 + i)
        s += s[-2::-1]
        s = '-'.join(s).center(width, '-')
        result.append(s)
        s = ""

    for i in list(range(0,n)) + list(range(n-2,-1,-1)):
        print(result[i])
