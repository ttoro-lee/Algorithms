def solution(numbers, target):
    
    def dfs(idx, n):
        nonlocal answer # local의 변수가 아님을 선언(global과 다름)
        
        if idx == len(numbers):
            if target == n:
                answer += 1
            return
        
        dfs(idx + 1, n + numbers[idx])
        dfs(idx + 1, n - numbers[idx])
        
    answer = 0
    dfs(0, 0)
    
    return answer
