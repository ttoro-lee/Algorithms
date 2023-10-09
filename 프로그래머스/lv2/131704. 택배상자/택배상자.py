from collections import deque

def solution(order):
    answer = 0
    
    m_c = deque([i for i in range(1, len(order)+1)])
    s_c = []
    
    for o in order:
        check = answer
        if len(s_c) and s_c[-1] == o:
            answer += 1
            s_c.pop()
        else:
            while(m_c):
                tmp = m_c.popleft()

                if o != tmp:
                    s_c.append(tmp)
                else:
                    answer += 1
                    break
        # print(m_c, s_c, answer)
        if check == answer:
            break
    return answer