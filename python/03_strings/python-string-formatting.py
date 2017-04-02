# https://www.hackerrank.com/challenges/python-string-formatting

def print_formatted(n):
    width = len(bin(n)) - 2
    for i in range(1, n + 1):
        print('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(i, oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:],width = width))
