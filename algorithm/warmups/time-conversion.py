# https://www.hackerrank.com/challenges/time-conversion

import sys

time = input().strip()
h = int(time[0:2])
m = int(time[3:5])
s = int(time[6:8])

if time[8] == 'A' and h == 12:
    h = 0    
elif time[8] == 'P' and h < 12:
    h += 12  

print("%02d:%02d:%02d" % (h, m, s))

