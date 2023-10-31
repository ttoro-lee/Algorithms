# 배열에 자연수 x를 넣는다
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다

# 연산 개수 n
# x가 자연수라면 배열 x에 값을 넣음
# x가 0이라면 가장 작은 값을 출력, 배열에서 제거

import heapq, sys

n = int(sys.stdin.readline().strip())

heap = []

for _ in range(n):

    x = int(sys.stdin.readline().strip())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, x)
