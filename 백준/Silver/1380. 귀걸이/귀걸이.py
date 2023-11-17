import sys

answer = []

while(1):

    n = int(sys.stdin.readline().strip())

    if n == 0:
        break

    student = dict()
    tmp = []

    for i in range(1, n+1):
        name = sys.stdin.readline().strip()
        student[str(i)] = name

    for _ in range(2*n-1):
        k, mark = sys.stdin.readline().split()

        if student[k] in tmp:
            tmp.remove(student[k])
        else:
            tmp.append(student[k])
            
    answer = answer + tmp

for i in range(len(answer)):
    print(i+1, answer[i])