import sys

# 달걀 n개
# 고객 m명

n, m = map(int, input().split())

people = []

for _ in range(m):
    people.append(int(sys.stdin.readline().strip()))

def solution(n,m,people):

    answer = 0
    tmp = 0

    people.sort(reverse=True)

    if n == 0:
        return tmp, answer

    for i in range(0,m):
        k = i + 1

        if n < k:
            break
        elif (k * people[i]) > answer:
            answer = k * people[i]
            tmp = people[i]

    return tmp, answer


print(*solution(n,m,people))