from collections import deque
def solution(storey):
    answer = []
    
    def bfs(num):
        
        stack = deque([(num, 0)])
        
        while(stack):
            cur, k = stack.popleft()
            
            c = 1
            if cur == 0:
                answer.append(k)
                continue
            elif cur < 0:
                continue
            elif len(str(cur)) > len(str(num)) + 1:
                continue
            
            while(cur):
                if (cur % 10**(c)) > 0:
                    tmp = (cur % 10**(c))
                    break
                c += 1
            
            stack.append((cur + (10**(c) - tmp), k + (10**(c) - tmp) // 10**(c-1)))
            stack.append((cur - tmp, k + (tmp // 10**(c-1))))

    bfs(storey)

    return min(answer)