# 1번 집은 2번 집의 색과 달라야함
# N번 집은 N-1번 집과 색이 달라야함
# i번 집은 i-1번, i+1번 집과 색이 달라야함
# 즉 다음 집과는 색이 무조건 달라야 함

N = int(input())

maps = []

answer = [[0] * 3 for _ in range(N)]

for _ in range(N):
    tmp = list(map(int, input().split()))
    maps.append(tmp)

for i in range(N):
    if i == 0:
        answer[0] = maps[0]
    else:
        answer[i][0] = min(maps[i][0] + answer[i-1][1], maps[i][0] + answer[i-1][2])
        answer[i][1] = min(maps[i][1] + answer[i-1][0], maps[i][1] + answer[i-1][2])
        answer[i][2] = min(maps[i][2] + answer[i-1][0], maps[i][2] + answer[i-1][1])

print(min(answer[-1]))
        
