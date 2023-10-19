from collections import deque

def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[0])
    
    print(routes)

    routes = deque(routes)
    
    cur = routes[0][1]
    
    while(routes):
        
        start, end = routes.popleft()
        
        if cur >= start and cur <= end:
            continue
        elif cur > start: #포함되지 않는데 현재가 크다면
            cur = end
        elif cur < start:
            cur = end
            answer += 1
            
    answer += 1
    return answer