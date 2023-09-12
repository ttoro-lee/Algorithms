def solution(str1, str2):
    # 다중 집합 허용
    # 교집합은 min
    # 합집합은 max
    # 자카드 유사도 교집합 / 합집합
    top = 0
    bottom = 0
    
    set1 = []
    set2 = []
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set1.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            set2.append(str2[j:j+2])
            
    intersection = set(set1) & set(set2)
    union = set(set1) | set(set2)
    
    k = len(list(union))
    
    if k == 0:
        return 65536
    
    for inter in intersection:
        top = top + min(set1.count(inter), set2.count(inter)) - 1
        bottom = bottom + max(set1.count(inter), set2.count(inter)) - 1
        
    for diff in (union - intersection):
        if diff in set1:
            bottom += set1.count(diff)
        elif diff in set2:
            bottom += set2.count(diff)
    
    top += len(list(intersection))
    bottom += len(list(intersection))
    return int((top / bottom) * 65536)