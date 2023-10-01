from string import ascii_uppercase
from collections import deque

def solution(msg):
    lzw = dict()
    
    for idx, l in enumerate(list(ascii_uppercase), start=1):
        lzw[l] = idx
    
    k = len(lzw)
    answer = []
    
    msg = deque(msg)
    
    while(len(msg)):
        w = ''
        while(1):
            w += msg.popleft()
            if len(msg) and (w + msg[0]) not in lzw.keys():
                answer.append(lzw[w])
                k += 1
                if len(msg):
                    lzw[w + msg[0]] = k
                break
            elif not len(msg):
                if lzw.get(w, 0):
                    answer.append(lzw[w])
                    break
        
    return answer