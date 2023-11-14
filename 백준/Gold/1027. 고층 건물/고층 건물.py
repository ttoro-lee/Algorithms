
import sys

n = int(sys.stdin.readline())
buildings = list(map(int, sys.stdin.readline().split()))

def gradient(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def solution(n, buildings):

    # 왼쪽의 경우 다음 건물의 기울기가 이전 기울기보다 작아지면 보임
    # 오른쪽의 경우 다음 건물의 기울기가 이전 기울기보다 크다면 보임

    sights = [0] * n

    if n == 1:
        return 0

    for b in range(n):

        answer = 0

        left = buildings[:b]
        mid = buildings[b]
        right = buildings[b+1:]

        for idx, l in enumerate(left[::-1], start=1): # 왼쪽의 경우
            if idx == 1:
                tmp = gradient(0, l, idx, mid)
                answer += 1
            else:
                compare = gradient(0, l, idx, mid)
                if tmp > compare:
                    answer += 1
                    tmp = compare # 최소로 업데이트
        for idx, r in enumerate(right, start=1): # 오른쪽의 경우
            if idx == 1:
                tmp = gradient(0, mid, idx, r)
                answer += 1
            else:
                compare = gradient(0, mid, idx, r)
                if tmp < compare:
                    answer += 1
                    tmp = compare # 최대로 업데이트
        sights[b] = answer

    return max(sights)


print(solution(n, buildings))