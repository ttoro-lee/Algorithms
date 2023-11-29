import sys

n, score, p = map(int, sys.stdin.readline().split())

if n == 0:
    scores = []
else:
    scores = list(map(int, sys.stdin.readline().split()))

def solution(score, p, scores):

    if len(scores) >= p and min(scores) >= score: # 더 이상 올라갈 수 없는 경우
        return -1

    heap = []
    answer = 1

    for n in scores:
        if n <= score:
            return answer
        else:
            answer += 1
    return answer


print(solution(score, p, scores))