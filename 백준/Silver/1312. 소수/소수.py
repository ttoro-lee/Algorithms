import sys

a, b, n = map(int, sys.stdin.readline().split())

i = 0

answer = 0

for _ in range(n+1):
    answer = a // b
    a = (a % b) * 10

print(answer)