# 팰린드롬, 소수

import sys

a, b = map(int, sys.stdin.readline().split())

def sosu(b):

    if b >= 10000000:
        max_num = 10000001
    else:
        max_num = b + 1

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

def solution(n):

    answer = ''

    # 중앙을 기준으로 앞을 자른 수 A, 뒤집은 수 A'
    # 뒤를 자른 수 B, 뒤집은 수 B'

    length = len(n)

    mid = length // 2

    if length == 1:
        C = int(n) + 1
        if C < 10:
            answer = str(C)
        else:
            answer = '11'

    elif length % 2 == 0:
        # 길이가 짝수인 경우
        # A' <= B 이면, A에 +1 값이 C일떄
        # CC' 가 정답
        r_A = n[:mid][::-1]
        A = n[:mid]
        B = n[mid:]

        if int(r_A) <= int(B):
            C = str(int(A) + 1)

            if len(A) != len(C):
                # 자리수가 변한다면
                answer = C + C[::-1][1:]
            else:
                answer = C + C[::-1]
        # A' > B
        else:
            answer = A + A[::-1]
    else:
        # 홀수인 경우
        m = n[mid]
        r_A = n[:mid][::-1]
        A = n[:mid]
        B = n[mid+1:]

        if int(r_A) <= int(B):

            C = str(int(m) + 1)

            if C == '10':
                n_A = str(int(A) + 1)
                if len(n_A) == len(A):
                    answer = n_A + '0' + n_A[::-1]
                else:
                    answer = n_A + n_A[::-1]
            else:
                answer = A + C + A[::-1]
        # A' > B
        else:
            answer = A + m + A[::-1]

    return answer

nums = sosu(b)

k = a - 1

while(k < (b + 1)):

    k = int(solution(str(k)))

    if k >= 10000000 or k > b:
        break

    if nums[k]:
        print(k)

print(-1)