import sys

A, B = sys.stdin.readline().strip().split()


def match(A, B):
    answer = 0

    for i in range(len(A)):
        if A[i] != B[i]:
            answer += 1

    return answer

def solution(A, B):

    tmp = sys.maxsize

    if len(A) == len(B):
        return match(A, B)

    for i in range(len(B) - len(A)+1):
        answer = 0
        for j in range(len(A)):
            if A[j] != B[i+j]:
                answer += 1
        if tmp > answer:
            tmp = answer

    return tmp

print(solution(A,B))