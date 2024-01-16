import sys

# x 정수
# b정수

x, b = map(int, sys.stdin.readline().split())


def solution(x,b):

    answer = ''
    pos = False

    if x == 0:
        return 0

    if x < 0 and b > 0:
        x = -x
        pos = True

    while(x):

        tmp = x % b
        if tmp < 0:
            x = x // b + 1
            tmp = tmp - b
        else:
            x = x // b

        answer = str(tmp) + answer

    if pos:
        return '-' + answer

    return answer


print(solution(x,b))