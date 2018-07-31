# https://www.hackerrank.com/challenges/merge-the-tools

def merge_the_tools(string, k):
    n = len(string)
    s = set()
    for i in range(0, n, k):
        res = ""
        for x in range(i, i + k):
            if not string[x] in s:          
                res += string[x]          
                s.add(string[x])

        print(res)
        s.clear()
        
