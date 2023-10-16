def solution(k, d):
    answer = 0
    
    for a in range(0, d+1, k):
        
        b = d ** 2 - a ** 2
        answer += b**(0.5) // k + 1
    return answer