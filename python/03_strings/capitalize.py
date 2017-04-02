# https://www.hackerrank.com/challenges/capitalize

def capitalize(string):
    string = string.split(' ')

    for i in range(len(string)):
        string[i] = string[i].capitalize()

    return ' '.join(string)
