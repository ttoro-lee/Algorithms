from collections import defaultdict, deque

def solution(plans):
    answer = []
    
    study = defaultdict(list)
    
    for plan in plans:
        name, time, left = plan
        time = list(map(int, time.split(':')))
        start = time[0] * 60 + time[1]
        
        study[name] = [start, int(left)]
        
    work = deque(sorted(study.items(), key=lambda x : x[1]))
    stack = []
    wait = []
        
    while(work):
        name, times = work.popleft()
        
        if not(stack):
            stack.append((name, times[0] + times[1])) # 일, 끝나는 시간
            cur = times[0] + times[1] # 현재 시간
        else:
            if cur >= times[0]: # 새로운 일 시간이 현재보다 빠르면
                check = stack.pop()
                left = check[1] - times[0] # 하고 있던 일 남은 시간
                if left == 0: # 만약 끝났다면
                    answer.append(check[0])
                else: # 시간이 남았다면
                    wait.append((check[0], left)) # 이름과 남은 시간 wait
                stack.append((name, times[0] + times[1])) # 일, 끝나는 시간 추가
                cur = times[0] + times[1] # 현재 시간
            else: # 빠르지 않다면
                work.appendleft((name, times)) # 다시 넣음
                
                check = stack.pop() # 일이 끝남
                answer.append(check[0])
                
                if wait:
                    name, left = wait.pop()
                    stack.append((name, cur+left)) # 일에 올림
                    cur = cur+left
    
    answer.append(stack[0][0])
    
    while(wait):
        name, _ = wait.pop()
        answer.append(name)
        
    return answer 