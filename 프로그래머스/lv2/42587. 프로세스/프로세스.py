from collections import deque

def solution(priorities, location):
    answer = []
    q = deque([x for x in range(len(priorities))])
    prior = dict()
    
    for idx, p in enumerate(priorities):
        prior[idx] = p
             
    while(len(q) > 1):
        
        x = q.popleft()
        
        if prior[x] < max(list(prior.values())):
            q.append(x)
        else:
            answer.append(x)
            del prior[x]
            
        if len(q) == 1:
            answer.append(q.pop())
        
    return answer.index(location) + 1