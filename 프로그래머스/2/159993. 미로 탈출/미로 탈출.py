from collections import deque

def solution(maps):
    answer = 0
    k = 0
    
    moved = [(-1,0), (1,0), (0, -1), (0, 1)]
    
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i,j)
            elif maps[i][j] == 'E':
                end = (i, j)
            elif maps[i][j] == 'L':
                lever = (i,j)
                
                
    l_visited = [(start[0], start[1])]
    l_stack = deque([(start[0], start[1], 0)])
    e_visited = [(lever[0], lever[1])]
    e_stack = deque([(lever[0], lever[1], 0)])
    
    l_ans = 0
    e_ans = 0
    
    while(l_stack):
        l_x, l_y, cur = l_stack.popleft()
        
        if l_x == lever[0] and l_y == lever[1]:
            l_ans = cur
            break
        
        for idx, idy in moved:
            m_x = l_x + idx
            m_y = l_y + idy

            
            if inbox(maps, m_x, m_y) and (m_x, m_y) not in l_visited and not(maps[m_x][m_y] == 'X'):
                l_visited.append((m_x, m_y))
                l_stack.append((m_x, m_y, cur + 1))
    
    while(e_stack):
        e_x, e_y, cur = e_stack.popleft()
        
        if e_x == end[0] and e_y == end[1]:
            e_ans = cur
            break
        
        for idx, idy in moved:
            m_x = e_x + idx
            m_y = e_y + idy
            
            if inbox(maps, m_x, m_y) and (m_x, m_y) not in e_visited and not(maps[m_x][m_y] == 'X'):
                e_visited.append((m_x, m_y))
                e_stack.append((m_x, m_y, cur + 1))
    if l_ans == 0 or e_ans == 0:
        return -1
    return l_ans + e_ans

def inbox(maps,x,y):
    return x >= 0 and x < len(maps) and y >= 0 and y < len(maps[0])