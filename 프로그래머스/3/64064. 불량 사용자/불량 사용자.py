from collections import defaultdict
from itertools import product

def solution(user_id, banned_id):
    answer = []
    
    n = len(banned_id)
    
    hash = defaultdict(set)
    
    for ban_id in banned_id:
        for user in user_id:
            if len(user) != len(ban_id):
                continue
            else:
                check = True
                for i in range(len(user)):
                    # 가려진 지점이 아닌데, 다를 경우
                    if ban_id[i] != '*' and ban_id[i] != user[i]:
                        check = False
                        break
                if check:
                    hash[ban_id].add(user)
    pk = []
    
    for ban in banned_id:
        pk.append(list(hash[ban]))
        
    for p in product(*pk):
        if len(set(p)) == n and set(p) not in answer:
            answer.append(set(p))
            
    return len(answer)