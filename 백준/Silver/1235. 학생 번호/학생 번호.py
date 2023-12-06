import sys

n = int(sys.stdin.readline().strip())

student = []
answer = []

for _ in range(n):
    student.append(sys.stdin.readline().strip())

for j in range(1, len(student[0])+1):
    check = set()
    for i in range(len(student)):
        string = student[i][-j:]

        if string not in check:
            check.add(string)
        else:
            break

    if len(check) == n:
        answer.append(j)

print(min(answer))