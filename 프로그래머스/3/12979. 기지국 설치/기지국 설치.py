import math

def solution(n, stations, w):
    answer = 0
    
    gaps = []
    new_s = [1]
    
    for s in stations:
        new_s.append(max(s-w, 1))
        new_s.append(min(s+w, n))
    
    new_s += [n+1]
    
    for i in range(0,len(new_s),2):
        if i == 0:
            gaps.append(new_s[i+1] - new_s[i])
        elif i == len(new_s)-1:
            gaps.append(new_s[i+1] - new_s[i])
        else:
            gaps.append(new_s[i+1] - new_s[i] - 1)
        

    for g in gaps:
        if g % (2*w + 1) == 0:
            answer += g // (2*w + 1)
        else:
            answer += math.ceil(g / (2*w + 1))
        
    return answer