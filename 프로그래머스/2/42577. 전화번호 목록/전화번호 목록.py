def solution(phone_book):
    answer = True
    
    hash_map = dict()
    
    for phone in phone_book:
        hash_map[phone] = 1
    
    for phone in phone_book:
        tmp = ''
        for p in phone:
            tmp = tmp + p
            if tmp != phone and hash_map.get(tmp, 0):
                return False
            
    return answer