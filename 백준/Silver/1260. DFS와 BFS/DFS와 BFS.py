# 정점 개수 n
# 간선 개수 m
# 탐색 시작 v

from collections import defaultdict, deque

graph = defaultdict(list)

n, m, v = map(int, input().split())

for _ in range(m):
    s, e = map(int, input().split())
    
    graph[s].append(e)
    graph[e].append(s)

def bfs(graph, v):

    stack = deque([v])
    visited = set([v])

    while(stack):
        cur = stack.popleft()

        for num in sorted(graph[cur]):
            if num not in visited:
                visited.add(num)
                stack.append(num)
        
        print(cur, end=" ")

def dfs(graph, visited, v):

    print(v, end=" ")

    if v in visited:
        return
    else:
        visited.append(v)
        for num in sorted(graph[v]):
            if num not in visited:
                dfs(graph, visited, num)


dfs(graph, [], v)
print()
bfs(graph, v)