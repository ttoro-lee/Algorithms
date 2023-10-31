# 테스트 케이스 T
# 가로 m, 세로 n, 배추 위치 개수 k

from collections import deque

T = int(input())

def inbox(m,n,x,y):
    return x >= 0 and x < m and y >= 0 and y < n

for _ in range(T):  
    m, n, k = map(int, input().split())

    answer = 0
    maps = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 1

    visited = set()

    for i in range(m):
        for j in range(n):

            if maps[i][j] == 1 and (i,j) not in visited:

                stack = deque([(i,j)])
                visited.add((i,j))

                while(stack):

                    x, y = stack.popleft()

                    for idx, idy in [(1,0), (-1,0), (0,1), (0,-1)]:

                        nx = x + idx
                        ny = y + idy

                        if inbox(m,n,nx,ny) and maps[nx][ny] == 1 and (nx,ny) not in visited:
                            visited.add((nx,ny))
                            stack.append((nx,ny))
                answer += 1
    print(answer)
