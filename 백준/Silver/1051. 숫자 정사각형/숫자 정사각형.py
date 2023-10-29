n, m = map(int, input().split())

maps = []

temps = [[0] * m for _ in range(n)]

answer = 0

for _ in range(n):
    tmp = list(input())
    maps.append(tmp)

def inbox(n,m,x,y):
    return x >= 0 and x < n  and y >= 0 and y < m

def check_box(maps, x, y):

    n = len(maps)
    m = len(maps[0])

    k = 0

    while(1):
        if inbox(n,m,x+k, y) and inbox(n,m,x+k, y+k) and inbox(n,m,x,y+k):
            # 모두 상자 안에 있다면
            if (maps[x][y] == maps[x+k][y]) and (maps[x+k][y] == maps[x][y+k]) and (maps[x][y+k] == maps[x+k][y+k]):
                answer = k + 1
            k += 1
        else:
            break

    return answer

for i in range(n):
    for j in range(m):
        temps[i][j] = check_box(maps, i, j) ** 2
        if answer < temps[i][j]:
            answer = temps[i][j]

print(answer)