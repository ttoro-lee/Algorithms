n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
# 1 1 0 1 6
# 2 7 8 3 1

answer = 0

for a, b in zip(sorted(A), sorted(B, reverse=True)):
    answer += (a * b)

print(answer)