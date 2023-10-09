from collections import Counter

def solution(topping):
    
    answer = 0
    
    me = dict()
    bro = Counter(topping)
    
    for t in topping:
        # print(bro, me)
        if bro[t] > 1:
            bro[t] -= 1
        else:
            del(bro[t])
        
        if not(me.get(t, 0)):
            me[t] = 1
        else:
            me[t] += 1
            
        if len(bro.keys()) == len(me.keys()):
            answer += 1
    
    return answer