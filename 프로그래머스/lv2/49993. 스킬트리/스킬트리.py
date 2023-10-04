def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        tmp = list(skill[::-1])
        for t in tree:
            if not len(tmp):
                break
            elif t == tmp[-1]:
                tmp.pop()
                
        if len(set(tree) & set(tmp)):
            continue
        else:
            print(tree)
            answer += 1
        
    return answer