# 랜선 N개
# 오영식 K개 랜선 갖고 있음
# K는 길이 제각각
# 박성원 - N개의 같은 길이
# K를 잘라서 같게
# 300cm -> 140cm 2개, 20cm 버림


n, k = map(int, input().split())

lanes = []

for _ in range(n):
    l = int(input())
    lanes.append(l)

left = 1
right = max(lanes)

while(1):

    mid = (right + left) // 2
    
    if (mid == left) or (mid == right):
        answer = mid
        break

    pk1 = sum([l // left for l in lanes])
    pk2 = sum([l // mid for l in lanes])
    pk3 = sum([l // right for l in lanes])

    if pk3 >= k:
        answer = right
        break
    elif pk2 >= k:
        left = mid
    else:
        right = mid

print(answer)
