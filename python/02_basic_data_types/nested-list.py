# https://www.hackerrank.com/challenges/nested-list

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students += [[name, score]]

s = sorted(set([student[1] for student in students]))

for name in sorted(row[0] for row in students if row[1] == s[1]):
    print(name)
