# 연산 3가지

# x가 3으로 나뉘면 3으로 나눔
# x가 2로 나뉘면 2로 나눔
# -1

from collections import deque

n = int(input())


def bfs(n):

    stack = deque([(n, 0)])
    visited = set([n])

    while(stack):
        
        cur, cnt = stack.popleft()

        if cur == 1:
            return cnt
        
        if cur % 3 == 0 and cur // 3 not in visited:
            stack.append((cur // 3, cnt + 1))
            visited.add(cur // 3)
        if cur % 2 == 0 and cur // 2 not in visited:
            stack.append((cur // 2, cnt + 1))
            visited.add(cur // 2)
        if cur - 1 not in visited:
            stack.append((cur - 1, cnt + 1))
            visited.add(cur - 1)

print(bfs(n))