import sys

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉음
#
n, k = map(int, sys.stdin.readline().split())

nums = list(range(1,n+1))

answer = []

rm = 1

while(nums):

    rm = k % len(nums)

    if rm == 0:
        rm = len(nums) - 1
    else:
        rm -= 1

    answer.append(nums.pop(rm))

    nums = nums[rm:] + nums[:rm]

print('<', end='')

for a in range(len(answer)):
    if a == n-1:
        print(answer[a], end='>')
    else:
        print(answer[a], end=', ')