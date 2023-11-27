# 팰린드롬, 소수

import sys

n = int(sys.stdin.readline().strip())

def sosu():

    max_num = 1100000

    numbers = [0] * max_num

    for i in range(2, max_num):
        numbers[i] = i
    # 만약 지워진 수라면
    # 넘어감
    # 자기 자신은 지우지 않음

    for i in range(2, max_num):
        if numbers[i] == 0:
            continue
        else:
            for j in range(i*2, max_num, i):
                numbers[j] = 0

    return numbers

def perlindnorm(n):

    mid = len(n) // 2

    if len(n) == 1:
        return True

    else:
        if len(n) % 2 == 0:
            return n[:mid] == n[mid:][::-1]
        else:
            return n[:mid] == n[mid+1:][::-1]

nums = sosu()

while(1):

    if nums[n] and perlindnorm(str(n)):
        print(n)
        break
    else:
        n += 1
        continue