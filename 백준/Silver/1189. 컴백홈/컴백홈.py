# 현재위치 왼쪽 아래 (i, 0)
# 집 오른쪽 위 (0, j)
# 거리가 k인 가짓수

r,c,k = map(int, input().split())

maps = []
visited = set([(r-1, 0)])

for _ in range(r):
    tmp = list(input())
    maps.append(tmp)

start = (r-1, 0)
end = (0, c-1)

answer = 0

def inbox(r,c,x,y):
    return x >= 0 and x < r and y >= 0 and y < c

def dfs(maps,x,y, cur, k):

    global answer

    if x == 0 and y == c - 1 and cur == k:
        answer += 1
        return
    
    elif cur > k:
        return
    
    else:

        for idx, idy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + idx
            ny = y + idy

            if inbox(r,c,nx,ny) and (nx,ny) not in visited and maps[nx][ny] != 'T':
                visited.add((nx,ny))
                dfs(maps,nx,ny,cur+1, k)
                visited.remove((nx,ny))

dfs(maps, start[0], start[1], 1, k)

print(answer)
        
