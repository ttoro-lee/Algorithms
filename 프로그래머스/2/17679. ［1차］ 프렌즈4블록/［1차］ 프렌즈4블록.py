def solution(m, n, board):
    answer = 0
    
    tmp = [[] for _ in range(n)]
    
    for j in range(n):
        for i in range(m-1, -1, -1):
            tmp[j].append(board[i][j])

    while(1):
        rows = [set() for _ in range(n)]
        temp = 0
        
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                if check(tmp, len(tmp), len(tmp[i]), i, j):
                    rows[i].add(j)
                    rows[i].add(j+1)
                    rows[i+1].add(j+1)
                    rows[i+1].add(j)
                    
        for idx,row in enumerate(rows):
            for r in row:
                tmp[idx][r] = '#'
            k = 0
            explo = 0
            while(k < len(tmp[idx])):
                if tmp[idx][k] == '#':
                    tmp[idx] = tmp[idx][:k] + tmp[idx][k+1:]
                    explo += 1
                    temp += 1
                else:
                    k += 1
            tmp[idx] = tmp[idx] + ['@'] * explo     
        
        if temp != 0:
            answer += temp
        else:
            break
    
    
    return answer

def inbox(m,n,i,j):
    return i >= 0 and i < m and j >= 0 and j < n

def check(maps, m, n, i, j):
    
    icon = maps[i][j]
    
    if icon.isupper() and inbox(m,n,i,j+1) and inbox(m,n,i+1,j) and inbox(m,n,i+1,j+1):
        return icon == maps[i][j+1] and icon == maps[i+1][j] and icon == maps[i+1][j+1]
    
    return 