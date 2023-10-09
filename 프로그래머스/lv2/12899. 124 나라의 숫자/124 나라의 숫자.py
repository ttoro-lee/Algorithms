def solution(n):
    answer = ''
    
    dict = {0:'4', 1:'1', 2:'2'}
    
    while(n):
        answer += dict[n % 3]
        if n % 3 == 0:
            n = n // 3 - 1
        else:
            n = n // 3
    return answer[::-1]