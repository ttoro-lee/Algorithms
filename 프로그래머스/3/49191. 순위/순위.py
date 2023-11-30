from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    
    wins = defaultdict(list)
    defeats = defaultdict(list)
    
    for result in results:
        wins[result[0]].append(result[1])
        defeats[result[1]].append(result[0])
        
    for i in range(1, n+1):
        if bfs(i, wins) + bfs(i, defeats) + 1 == n:
            answer += 1
    
    return answer

def bfs(start, graph):
    
    stack = deque([start])
    visited = set([start])
    
    cnt = 0
    
    while(stack):
        
        node = stack.popleft()
        
        for n in graph[node]:
            if n not in visited:
                stack.append(n)
                visited.add(n)
                cnt += 1
    return cnt
    