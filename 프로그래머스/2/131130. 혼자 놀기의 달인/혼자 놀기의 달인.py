from collections import deque

def solution(cards):
    boxs = []
    visited = set([])
    
    for i in range(len(cards)):
        tmp = []
        if i not in visited:
            visited.add(i) # 0
            tmp.append(cards[i]) # 8
            while(1):
                i = cards[i] - 1 # 7
                if i not in visited:
                    visited.add(i) # 7
                    tmp.append(cards[i]) # 4
                else:
                    break
        boxs.append(tmp)
    boxs.sort(key=lambda x: -len(x))
    return len(boxs[0]) * len(boxs[1])