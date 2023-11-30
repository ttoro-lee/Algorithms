from collections import deque

def solution(board, h, w):
    
    answer = dfs(h,w,board)
    
    return answer

def inbox(x, y, board):
    
    return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])

def dfs(x,y,board):
    
    answer = 0
    target = board[x][y]

    for idx, idy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx = x + idx
        ny = y + idy
        
        if inbox(nx,ny,board) and board[nx][ny] == target:
            answer += 1
            
    return answer
        
        