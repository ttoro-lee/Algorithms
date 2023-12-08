import sys

s = int(sys.stdin.readline().strip())

def solution(s):

    nums = 0
    answer = 0

    for i in range(1, s+1):
        answer += 1
        nums += i

        if nums > s:
            return answer - 1
        elif nums == s:
            return answer


print(solution(s))