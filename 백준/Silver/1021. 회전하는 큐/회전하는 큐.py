# N개의 원소를 포함하고 있는 양방향 순환 큐
# 몇 개 원소를 뽑아내려고 함
# 3가지 연산 수행 가능
# 1번째 원소 뽑아냄
# 왼쪽 한칸 이동 -> 1번이 맨 뒤로 이동
# 오른쪽 한칸 이동 -> 마지막이 1번으로 이동

from collections import deque

n, m = map(int, input().split())

nums = list(map(int, input().split()))

q1 = deque(list(range(1, n+1)))
q2 = deque(list(range(1, n+1)))

def dfs_left(q, target, cnt):

    if q[0] == target:
        q.popleft()
        return cnt
    
    else:
        cnt += 1
        tmp = q.popleft()

        q.append(tmp)

        return dfs_left(q, target, cnt)

def dfs_right(q, target, cnt):

    if q[0] == target:
        q.popleft()
        return cnt
    
    else:
        cnt += 1
        tmp = q.pop()

        q.appendleft(tmp)
        return dfs_right(q, target, cnt)

answer = []

for idx, num in enumerate(nums):
    cnt = 0
    
    left = dfs_left(q1, num, cnt)
    right = dfs_right(q2, num, cnt)

    if left < right:
        q2 = q1.copy()
        answer.append(left)
    else:
        q1 = q2.copy()
        answer.append(right)

print(sum(answer))