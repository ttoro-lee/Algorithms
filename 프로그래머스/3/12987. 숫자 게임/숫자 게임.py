import heapq

def solution(A, B):
    answer = 0
    
    heapq.heapify(A)
    heapq.heapify(B)
    
    while(B):
        b = heapq.heappop(B)
        a = heapq.heappop(A)
    
        
        if a >= b:
            heapq.heappush(A, a)
        elif b > a:
            answer += 1
            
            
    return answer