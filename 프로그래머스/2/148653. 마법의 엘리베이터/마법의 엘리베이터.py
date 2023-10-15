from collections import deque
def solution(storey):
    
    answer = []
    
    def bfs(num):
        
        stack = deque([(num, 0)])
        visited = set([num])
        
        while(stack):
            cur, k = stack.popleft()
            
            c = 0

            if cur == 0:
                return k
            
            while(1):
                if (cur % 10**(c)) > 0:
                    tmp = (cur % 10**(c)) * 10**(c)
                    break
                c += 1
            
            if (cur + (10**c - tmp)) not in visited:
                stack.append((cur + (10**c - tmp), k + 1))
                visited.add(cur + (10**c - tmp))
            
            if (cur - tmp) not in visited:
                stack.append((cur - tmp, k + 1))
                visited.add(cur - tmp)
    answer = bfs(storey)
    return answer