def solution(data, ext, val_ext, sort_by):
    answer = []
    
    for tmp in data:
        code, date, maximum, remain = tmp[0],tmp[1],tmp[2],tmp[3]
        
        if ext == 'code':
            if code < val_ext:
                answer.append([code, date, maximum, remain])
        elif ext == 'date':
            if date < val_ext:
                answer.append([code, date, maximum, remain])
        elif ext == 'maximum':
            if maximum < val_ext:
                answer.append([code, date, maximum, remain])
        else:
            if remain < val_ext:
                answer.append([code, date, maximum, remain])
                
    pk = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    
    return sorted(answer, key = lambda x : x[pk[sort_by]])