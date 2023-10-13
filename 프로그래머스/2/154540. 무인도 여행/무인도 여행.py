from collections import deque

def solution(maps):
    answer = []
    
    visited = set()
    
    def bfs(maps, visited, i, j):
        
        nums = 0
        
        q = deque([(i,j, int(maps[i][j]))])
        visited.add((i,j))
        
        while(q):
            
            i, j, cur = q.popleft()
            
            nums += cur
            
            for idx, idy in [(0,1), (0,-1), (1,0), (-1,0)]:
                tx = i + idx
                ty = j + idy
                
                if inbox(maps, tx, ty) and (tx,ty) not in visited and maps[tx][ty] != 'X':
                    visited.add((tx, ty))
                    q.append((tx, ty, int(maps[tx][ty])))
                
        return nums
        
    
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            
            if maps[x][y] != 'X' and (x,y) not in visited:
                answer.append(bfs(maps, visited, x, y))
    if len(answer):
        return sorted(answer)
    else:
        return [-1]

def inbox(maps, x, y):
    
    return x >= 0 and x < len(maps) and y >= 0 and y < len(maps[0])