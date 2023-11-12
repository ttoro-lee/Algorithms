# 합집합 0 a b
# a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합침

# 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산
# 1 a b
# a와 b가 같은 집합에 포함되어 있는지 확인하는 연산

# {1} {3}
# {1, 3}

import sys

sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n + 1)] # 자기 자신을 부모로 갖는 n + 1개 집합

def find_parent(x):

    if parent[x] != x:
        parent[x] = find_parent(parent[x]) # root를 찾아서 올라감

    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b: # 값이 더 작은 쪽으로 부모로
        # a
        # |
        # b
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    oper, a, b = map(int, sys.stdin.readline().split())

    if oper == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')

