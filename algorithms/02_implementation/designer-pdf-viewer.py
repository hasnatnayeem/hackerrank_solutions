# https://www.hackerrank.com/challenges/designer-pdf-viewer

h = list(map(int, input().strip().split(' ')))
word = input().strip()

max = 0
len = len(word)

for ch in word:
    if h[ord(ch) - 97] > max:
        max = h[ord(ch) - 97]
        
print(str(len * max))

