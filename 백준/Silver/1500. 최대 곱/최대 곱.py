import sys

s, k = map(int, sys.stdin.readline().split())

# 합이 s인 k개의 양의 정수 찾기
# 곱이 가능한 최대

a, b = s // k, s % k

nums = [a] * k

for i in range(b):
    nums[i] += 1

answer = 1

for idx in range(k):
    answer *= nums[idx]

print(answer)