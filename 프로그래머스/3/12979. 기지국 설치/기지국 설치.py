from collections import deque

def solution(n, stations, w):
    answer = 0

    visited = set(stations)
    
    for s in stations:
        if s-w > 0 and s-w < (n+1):
            visited.add(s-w)
        if s+w > 0 and s+w < (n+1):
            visited.add(s+w)
    
    stations = deque(stations)
    
    while(stations):
    
        cur = stations.popleft()
        
        for idx in [-2*w-1, -w-1, 2*w+1, w+1]:
            nx = cur + idx
            
            if inbox(n, nx) and nx not in visited:
                
                answer += 1
                visited.update(range(nx, nx+w+1))
                visited.update(range(nx-w, nx))
                stations.append(nx)

    return answer

def inbox(n, x):
    
    return x > 0 and x < n+1