# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
import email.utils
import re

pattern = '^[a-z]{1}[a-z0-9-,.,_]*@[a-z]+[.][a-z]{1,3}$'
for i in range(int(input())):
    string = input()
    text = email.utils.parseaddr(string)[1]
    if re.match(pattern, text):
        print(string)