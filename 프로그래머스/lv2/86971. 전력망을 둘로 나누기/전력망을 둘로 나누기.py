from collections import defaultdict, deque
import sys

def solution(n, wires):
    answer = -1
    min_sum = sys.maxsize
    
    for i in range(len(wires)):
        new_w = wires[:i] + wires[i+1:]
    
        graphs = make_graph(new_w)
        visited = [0] * (n + 1)
        
        temp = []
        for i in range(1, n):
            if not visited[i]:
                visited[i] = 1
                temp.append(len(bfs(graphs, i, visited)))
        if len(temp) > 1:
            cond = abs(temp[0] - temp[1])
        else:
            cond = temp[0]
            
        if cond < min_sum:
            min_sum = cond


    return min_sum


def make_graph(wires):
    
    graphs = defaultdict(list)
    
    for i in range(len(wires)):
        v1, v2 = wires[i]
        graphs[v1].append(v2)
        graphs[v2].append(v1)
        
    return graphs

def bfs(graph, start, visited):
    
    q = deque([start])
    
    list = []
    
    while q:
        v = q.popleft()
        list.append(v)
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
            
    return list