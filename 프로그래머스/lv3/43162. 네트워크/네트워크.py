def solution(n, computers):
    answer = 0
    visited = []
    
    def dfs(i, n, visited):
        for j in range(n):
            if computers[i][j] == 1 and j not in visited:
                visited.append(j)
                dfs(j, n, visited)
    
    for i in range(n):
        if i not in visited:
            visited.append(i)
            answer += 1
            dfs(i, n, visited)
            
    return answer
