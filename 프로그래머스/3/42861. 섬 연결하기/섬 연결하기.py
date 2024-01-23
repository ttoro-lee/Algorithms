def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    
    parent = list(range(n))
    
    for cost in costs:
        
        s, e, c = cost
        
        if find(parent, s) != find(parent, e):
            union(parent, s, e)
            answer += c
    
    return answer

def find(parent, x):
    
    if parent[x] == x: # 부모가 나 자신일 경우
        return x
    parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB