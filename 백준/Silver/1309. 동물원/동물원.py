from collections import deque

N = int(input())

# n = 1 -> XX OX XO
# n = 2 -> XX OX XO
#          XX XX XX
#       -> XX XX XX
#       ->

# 맨 위 2칸이 공백인 경우 = i1
# 왼쪽 위가 있는 경우 = i2
# 오른쪽 위가 있는 경우 = i3

# 맨 위가 공백인 경우, 밑에는 아무거나 와도 상관 없음 (i1 + i2 + i3)
# 왼쪽 위가 있는 경우, 밑에는 공백인 경우 + 오른쪽 위가 채워진 경우 (i1 + i3)
# 오른쪽 위가 있는 경우, 밑에는 공백인 경우 + 왼쪽 위가 채워진 경우 (i1 + i2)

# 다음 N은 = (i1 + i2 + i3) + (i1 + i3) + (i1 + i2)
# N = 2(i1 + i2 + i3) + i1 -> N은 i + 1 (다음)
# 이때 i1 + i2 + i3는 N = i일때, i1은 N=i일때 맨 위가 공백인 경우, 즉 N = i - 1 경우와 같음
# N = i + 1 -> N = i로 바꾸면
# dp[i] = 2 * dp[i-1] + dp[i-2]

dp = deque([1])

for i in range(1, N+1):
    if i == 1:
        dp.append(3)
    else:
        tmp = 2 * dp[1] + dp[0]
        dp.append(tmp)

        if len(dp) > 2:
            dp.popleft()

print(dp[-1]%9901)
