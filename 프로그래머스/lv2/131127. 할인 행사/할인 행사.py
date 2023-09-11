from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    if set(want)- set(discount):
        return answer
    
    wants = []
    
    for w, n in zip(want, number):
        wants = wants + [w] * n

    for i in range(len(discount) - 9):
        if not(len(Counter(wants) - Counter(discount[i:i+10]))):
            answer += 1
        
    return answer