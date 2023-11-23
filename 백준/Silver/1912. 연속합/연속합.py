import sys

n = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    nums[i] = max(nums[i], nums[i] + nums[i-1])
    # 지금과 이전까지 합의 최대값으로 업데이트

print(max(nums))
