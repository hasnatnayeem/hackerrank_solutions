# https://www.hackerrank.com/challenges/write-a-function/submissions/code/37003554

def is_leap(year):
    leap = False
    
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap = True;
        
    return leap
