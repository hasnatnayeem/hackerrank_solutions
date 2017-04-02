# https://www.hackerrank.com/challenges/the-minion-game

def minion_game(string):
    stuart = 0
    kevin = 0
    length = len(string)
    for i in range(length):
        if string[i] in "AEIOU":
            kevin += length - i
        else:
            stuart += length - i

    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif kevin > stuart:
        print("Kevin " + str(kevin))
    else:
        print("Draw")
