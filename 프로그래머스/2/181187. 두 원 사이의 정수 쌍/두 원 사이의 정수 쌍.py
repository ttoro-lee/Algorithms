import math

def solution(r1, r2):
    
    answer = 0
    check = []
    
    for x in range(0, r2+1):
        y2 = math.sqrt(r2**2 - x**2)
        if x <= r1:
            y1 = math.sqrt(r1**2 - x**2)
        else:
            y1 = 0
        
        answer += (math.floor(y2) - math.ceil(y1) + 1)
                
    return answer * 4 - (r2 - r1 + 1) * 4