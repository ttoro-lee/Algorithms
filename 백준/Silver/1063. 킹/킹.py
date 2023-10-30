# 숫자는 행
# 알파벳 열

# 돌, 돌과 같은 곳으로 이동, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동
# 킹이나 돌이 체스판 밖으로 나갈 경우 그 이동을 건너 뛰고 다음 이동

# 킹의 위치, 돌의 위치, 움직이는 횟수 N

# A ~ H
# 8
# 1

def inbox(x,y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

king, stone, n = input().split()

moving = {'R': (0,1), 'L': (0,-1), 'B': (1,0), 'T':(-1,0),
          'RT': (-1,1), 'LT': (-1,-1), 'RB':(1,1), 'LB':(1,-1)}

col = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
t_col = {v:k for k,v in col.items()}

move = []

for _ in range(int(n)):
    move.append(input())

k = list(king)
s = list(stone)

k_pos = [8-int(k[1]), col[k[0]]]
s_pos = [8-int(s[1]), col[s[0]]]

for m in move:
    idx, idy = moving[m]
    
    nx = k_pos[0] + idx
    ny = k_pos[1] + idy

    if inbox(nx, ny): # 킹이 맵 안에 있다면
        if nx == s_pos[0] and ny == s_pos[1]:
            # 킹의 다음 위치가 돌이랑 같다면
            s_nx = s_pos[0] + idx
            s_ny = s_pos[1] + idy

            if inbox(s_nx, s_ny):
                s_pos[0] = s_nx
                s_pos[1] = s_ny
                k_pos[0] = nx
                k_pos[1] = ny
            else: # 돌이 밖으로 나가면 움직이지 않음
                continue
        else: # 돌이랑 같지 않다면
            k_pos[0] = nx
            k_pos[1] = ny
    else:
        continue

print(f"{t_col[k_pos[1]]}{(8-k_pos[0])}")
print(f"{t_col[s_pos[1]]}{str(8-s_pos[0])}")