import heapq

def solution(n, works):
    answer = 0
    
    heap = []
    
    for w in works:
        heapq.heappush(heap, -w)
    
    while(n):
        k = -heapq.heappop(heap)
        if k == 0:
            break
        n -= 1
        
        heapq.heappush(heap, -(k-1))
        
    for h in heap:
        answer += h**2
    return answer