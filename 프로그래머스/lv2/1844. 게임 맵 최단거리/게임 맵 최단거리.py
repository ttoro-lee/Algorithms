from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    
    q = deque([(0,0,1)])
    
    while q:
        x, y, num = q.popleft()
        
        if x == (n-1) and y == (m-1):
            return num
        
        for nx, ny in [(0,1), (1,0), (-1,0), (0,-1)]:
            xx = x + nx
            yy = y + ny
            
            if xx >= 0 and xx < n and yy >=0 and yy < m and maps[xx][yy] and not visited[xx][yy]:
                visited[xx][yy] = 1
                q.append((xx, yy, num + 1))
                
    return -1