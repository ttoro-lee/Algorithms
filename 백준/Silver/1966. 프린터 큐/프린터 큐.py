# FIFO
# 가장 앞에 있는 문서의 중요도 확인

import sys
from collections import deque

case = int(sys.stdin.readline().strip())

for _ in range(case):

    n, target = map(int, sys.stdin.readline().split())

    nums = deque()

    tmp = -1

    ranks = list(map(int, sys.stdin.readline().split()))

    nums = deque([(rank, idx) for idx, rank in enumerate(ranks)])

    ranks.sort()

    answer = 1

    while(1):

        rank, i = nums.popleft()

        if ranks[tmp] <= rank and i == target:
            print(answer)
            break
        elif ranks[tmp] <= rank:# 우선 순위가 높은 경우
            tmp -= 1
            answer += 1
            continue
        else:
            nums.append((rank, i))