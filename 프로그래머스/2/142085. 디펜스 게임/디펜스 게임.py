import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for e in enemy:
        if n >= e:
            answer += 1
            n -= e
            heapq.heappush(heap, -e)
        elif k > 0 and n < e: # 무적권을 써야하는 경우
            k -= 1
            n -= e
            heapq.heappush(heap, -e)
            n += -heapq.heappop(heap)
            if n >= 0:
                answer += 1
            else:
                break
        else:
            break    
                
    return answer