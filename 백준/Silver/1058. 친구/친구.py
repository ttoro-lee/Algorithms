import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline().strip())

maps = []

friends = defaultdict(list)

for i in range(n):
    maps.append(list(sys.stdin.readline().strip()))

for l in range(n):
    for m in range(l, n):
        if maps[l][m] == 'Y':
            friends[l].append(m)
            friends[m].append(l)

def bfs(friends, start):

    answer = 0

    stack = deque([(start, 0)])
    visited = set([start])

    while(stack):

        cur, cnt = stack.popleft()

        if cnt >= 2:
            continue
        for friend in friends[cur]:
            if friend not in visited:
                answer += 1
                visited.add(friend)
                stack.append((friend, cnt + 1))

    return answer

pk = []

for t in range(n):
    pk.append(bfs(friends, t))

print(max(pk))