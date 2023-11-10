# 0과 5사이 거리
# 0 1 2 3 4 5
# 1 2   1 1

# 0과 9사이 거리 -> 3 * 2 - 1
# 0 1 2 3 4 5 6 7 8 9
# 1 2   3     2   1

# 0과 10사이 거리 -> 3 * 2 - 1 (+ 1)
# 0 1 2 3 4 5 6 7 8 9 10
# 1 2   3     2   1 1

# 0과 11사이 거리
# 0 1 2 3 4 5 6 7 8 9 10 11
# 1 2   3     2   2   1

import math


n = int(input())

for _ in range(n):
    start, end = map(int, input().split())

    distance = end - start

    close = int(math.sqrt(distance))

    answer = close * 2 - 1

    remain = distance - close**2

    if remain != 0:
        if remain <= close: # 3인데 1 남은 경우
            answer += 1
        else:
            answer += 2 # 3인데 4 5가 남은 경우

    print(answer)

