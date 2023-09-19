def solution(n, t, m, p):
    # n진법
    # 미리 구할 숫자 갯수 t
    # 인원 m
    # 나의 순서 p
    
    answer = ''
    nums = ''
    
    
    for i in range(30000):
        nums += change(i, n)
        
    p = p - 1
    
    while(len(answer) != t):
        answer += nums[p]
        p += m
        
    return answer

def change(num, n):

    change = ''
    
    if num == 0:
        return '0'
    
    while(num):
        tmp = num % n
        if tmp > 9:
            change = chr(ord('A') + tmp - 10) + change
        else:
            change = str(tmp) + change
        num = num // n
        
    return change