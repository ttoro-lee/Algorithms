from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        dict = {}
        
        for order in orders:
            for combi in combinations(order, c):
                part = ''.join(sorted(list(combi)))
                if dict.get(part, 0):
                    dict[part] += 1
                else:
                    dict[part] = 1
        tmp = []     
        for key, value in sorted(dict.items(), key=lambda x: -x[1]):
            if not(tmp) and value > 1:
                tmp.append(key)
                max_value = value
            elif value == max_value:
                tmp.append(key)
            else:
                break
        answer += tmp
    return sorted(answer)


