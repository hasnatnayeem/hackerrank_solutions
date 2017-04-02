# https://www.hackerrank.com/challenges/grading


n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if grade > 37:
        if (grade + 1) % 5 == 0:
            grade += 1
        elif (grade + 2) % 5 == 0:
            grade += 2
    print(grade)

