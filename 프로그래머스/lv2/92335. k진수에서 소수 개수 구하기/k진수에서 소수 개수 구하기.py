def solution(n, k):
    answer = 0
    
    check = change_num(n, k)
    check = [num for num in check.split('0') if len(num)]
    
    for i in check:
        if check_sosu(int(i)):
            answer += 1
    
    
    return answer

def change_num(n, k):
    # k진수
    ans = ''
    
    if k == 10:
        return str(n)
    
    while(n):
        ans = str(n % k) + ans
        n = n // k
        
    return ans

def check_sosu(n):
    
    if n == 1:
        return False
    else:
        for i in range(2, int(n**(0.5) + 1)):
            if n % i == 0:
                return False 
    return True