# 가지고 있는 막대의 길이 모두 더함
# 합이 X보다 크면, 아래 과정 반복
    # 가장 짧은 것 절반
    # 자른 막대의 절반 중 하나를 버리고 남은 막대의 길이의 합이 X보다 크거나 같음
    # 위에서 자른 막대의 절반 중 하나를 버림
    # 남은 막대 모두 붙여 X 만듬
import heapq

x = int(input())

sticks = [64]
heapq.heapify(sticks)

k = 64

while(k != x):
    
    least = heapq.heappop(sticks)

    half_least = least // 2

    if (k - half_least) >= x: # 하나를 버리고 남은 막대의 길이 합이 X보다 큰 경우
        heapq.heappush(sticks, half_least)
    else:
        heapq.heappush(sticks, half_least)
        heapq.heappush(sticks, half_least) # 아닌 경우 둘 다 넣음

    k = sum(sticks)

print(len(sticks))
