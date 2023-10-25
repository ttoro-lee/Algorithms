# a의 크기
# A 원소 0부터 차례대로

# A의 크기 3
# A[0] = 2 -> B[P[0] -> 1]
# A[1] = 3 -> B[P[1] -> 2]
# A[2] = 1 -> B[P[2] -> 0]

n = int(input())
A = list(map(int, input().split()))

P = sorted(A)

answer = []

for a in A:
    # P에서 a의 인덱스를 찾고 싶음
    tmp = P.index(a)
    while(tmp in answer):
        tmp += 1
    answer.append(tmp)

print(*answer)