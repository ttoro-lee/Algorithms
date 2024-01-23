from collections import deque

def solution(prices):
    
    n = len(prices)
    answer = [0] * n
    stack = deque()

    for idx, price in enumerate(prices):
        
        if len(stack) == 0: # stack이 비어있다면
            stack.append((idx, price))
        else:
            while(stack and stack[-1][1] > price):
                i, target = stack.pop()
                answer[i] = idx - i
            stack.append((idx, price))
            
    if stack:
        for idx, k in stack:
            answer[idx] = n - 1 - idx
            
    return answer