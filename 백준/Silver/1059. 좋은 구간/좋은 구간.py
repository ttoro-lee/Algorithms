# 집합 S
# 조건을 만족하는 [A, B]를 좋은 구간
# A와 B는 양수, A < B
# A 이상 B 이하를 만족하는 모든 정수 x가 집합 S에 없음
# n을 포함하는 좋은 구간 개수


l = int(input())
S = list(map(int, input().split()))
n = int(input())


def solution(S, n):

    answer = 0

    if n in S:
        return answer
    
    S.sort(reverse=True)

    better = 0
    less = S[-1]

    # n은 S의 가장 큰 수랑 같거나 작음

    for idx, num in enumerate(S):
        if num < n: # 처음으로 작아지는 부분
            better = num
            less = S[idx-1]
            break

    for i in range(better+1, n+1):
        for j in range(n, less):
            if i != j:
                answer += 1

    return answer

print(solution(S, n))

