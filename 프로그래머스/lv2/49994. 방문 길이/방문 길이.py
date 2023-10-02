def solution(dirs):
    answer = 0
    maps = [[0] * 11 for _ in range(11)]
    visited = set()
    
    start = [5,5]
    
    for d in dirs:
        print(start)
        
        x, y = start[0], start[1]
        
        if d == "L" and inbox(x, y-1):
            if ((x,y), (x, y-1)) not in visited:
                maps[x][y-1] = 1
                answer += 1
                visited.add(((x,y), (x, y-1)))
                visited.add(((x,y-1), (x,y)))
            start[0] = x
            start[1] = y-1
            
        elif d == "R" and inbox(x, y+1):
            if ((x,y), (x, y+1)) not in visited:
                maps[x][y+1] = 1
                answer += 1
                visited.add(((x,y), (x, y+1)))
                visited.add(((x,y+1), (x,y)))
            start[0] = x
            start[1] = y+1
            
        elif d == "U" and inbox(x-1, y):
            if ((x,y), (x-1, y)) not in visited:
                maps[x-1][y] = 1
                answer += 1
                visited.add(((x,y), (x-1, y)))
                visited.add(((x-1,y), (x,y)))
            start[0] = x-1
            start[1] = y
            
        elif d == "D" and inbox(x+1, y):
            if ((x,y), (x+1, y)) not in visited:
                maps[x+1][y] = 1
                answer += 1
                visited.add(((x,y), (x+1, y)))
                visited.add(((x+1,y), (x,y)))
            start[0] = x+1
            start[1] = y
    print(visited)

    
    return answer

def inbox(x,y):
    
    return x >= 0 and x < 11 and y >= 0 and y < 11