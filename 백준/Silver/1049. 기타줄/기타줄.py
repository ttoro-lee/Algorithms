# N개의 줄이 끊어짐
# 새로 사거나 교체
# 돈을 적게
# 6줄 패키지 or 1개 이상 줄 구매
# 끊어진 줄 N, 브랜드 M개

n, m = map(int, input().split())

brands = dict()

for i in range(m):
    brands[i] = list(map(int, input().split()))

sets = n // 6
left = n % 6

# 세트와 낱개로 사는 방법
# 낱개로만 사는 방법
# 세트를 하나 더 사서 더 싼 경우

brand_set = sorted(brands.values(), key=lambda x: x[0])
brand_left = sorted(brands.values(), key=lambda x: x[1])

pk1 = sets * brand_set[0][0] + left * brand_left[0][1]
pk2 = n * brand_left[0][1]
pk3 = (sets + 1) * brand_set[0][0]

answer = min(pk1, pk2, pk3)

print(answer)
