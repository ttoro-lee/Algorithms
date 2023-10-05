from collections import deque

def solution(x, y, n):
    answer = []
    
    q = deque([(y, 0)])
    while(q):
        # print(q)
        c, k = q.popleft()
        
        if c == x:
            return k
        else:
            if (c - n) >= x:
                q.append((c - n, k+1))
            if (c % 2) == 0 and (c / 2) >= x:
                q.append((c / 2, k+1))
            if (c % 3) == 0 and (c / 3) >= x:
                q.append((c / 3, k+1))
    return -1        