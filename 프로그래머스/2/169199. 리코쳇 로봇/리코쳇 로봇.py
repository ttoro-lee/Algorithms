from collections import deque

def solution(board):
    answer = 0
    count = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = (i,j)
                break
                
    stack = deque([(start[0], start[1], 0)])
    visited = set([start])
    
    while(stack):

        x, y, cur = stack.popleft()
        
        if board[x][y] == 'G':
            return cur
        
        for idx, idy in set([(1,0), (-1,0), (0,1), (0,-1)]):
            nx = x + idx
            ny = y + idy # 다음칸 이동
            while(inbox(board, nx, ny) and board[nx][ny] != 'D'): # 다음칸이 박스 안이면
                if not(inbox(board, nx+idx, ny+idy)) and (nx, ny) not in visited :
                    stack.append((nx,ny, cur + 1))
                    visited.add((nx, ny))
                    break
                elif inbox(board, nx+idx, ny+idy) and board[nx+idx][ny+idy] == 'D' and (nx, ny) not in visited : # 장애물까지
                    stack.append((nx,ny, cur + 1))
                    visited.add((nx, ny))
                    break
                nx = nx + idx
                ny = ny + idy
        count += 1
    
    return -1

def inbox(maps, i, j):
    return i >= 0 and i < len(maps) and j >= 0 and j < len(maps[0])