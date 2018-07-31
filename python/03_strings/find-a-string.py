# https://www.hackerrank.com/challenges/find-a-string

def count_substring(string, sub_string):
    count = 0;
    index = -1;
    l = len(string)
    while True:
        index = string.find(sub_string, index + 1, l)
        if (index == -1):
            return count       
        count += 1
    return count
