import sys

n, k = map(int, sys.stdin.readline().split())

visited = [False] * 1000001

def bfs(start):
    queue = [start]
    visited[start] = True

    while queue:
        x = queue.pop(0)

        if x == k:
            return visited[x] - 1

        for i in (x-1, x+1, x*2):
            if 0 <= i < 1000001 and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)
                
print(bfs(n))