def solution(m, n, puddles):
    answer = 0
    
    maps = [[0] * m for _ in range(n)]
    visited = set([(0,0)])
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                maps[i][j] = 1
            else:
                if [j+1, i+1] not in puddles:
                    tmp = []
                    for idx, idy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        mx = i + idx
                        my = j + idy
                        if inbox(m,n, mx, my) and (mx, my) in visited and [my+1, mx+1] not in puddles:
                            tmp.append(maps[mx][my])
                    if tmp:
                        maps[i][j] = sum(tmp)
                    visited.add((i,j))
    return maps[n-1][m-1] % 1000000007

def inbox(m,n, x, y):
    return x >= 0 and x < n and y >= 0 and y < m