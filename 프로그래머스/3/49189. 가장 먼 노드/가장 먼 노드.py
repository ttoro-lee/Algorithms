from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for vertex in edge:
        graph[vertex[0]].append(vertex[1])
        graph[vertex[1]].append(vertex[0])
        
    pk = bfs(1, graph)
    
    key = max(pk)
        
    for p in pk:
        if p == key:
            answer += 1
    return answer

def bfs(start, graph):
    
    answer = []
    
    stack = deque([(start, 0)])
    visited = set([start])
    
    while(stack):
        
        node, cnt= stack.popleft()
        
        answer.append(cnt)
        
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                stack.append((n, cnt+1))
                
    return answer