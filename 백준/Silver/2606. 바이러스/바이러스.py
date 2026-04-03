# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 수 출력

# DFS 풀이

import sys

n = int(sys.stdin.readline()) # 컴퓨터 수
m = int(sys.stdin.readline()) # 연결 수 

from collections import defaultdict

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n + 1)

ans = 0

def dfs(graph, start, visited):
    
    global ans
    
    visited[start] = True
    
    for i in graph[start]:
        # 현재에서 방문할 수 있는 노드 탐색
        if not visited[i]:
            # 방문한 적이 없는 노드인 경우
            ans += 1
            dfs(graph, i, visited)
            
dfs(graph, 1, visited)
print(ans)
    
    
    