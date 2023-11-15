import sys

edges = []

v, e = map(int, sys.stdin.readline().split())
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a,b,c))

edges.sort(key=lambda x:x[2]) # Cost가 적은 것부터 정렬

parent = list(range(v+1))

def get_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent[x]) # 위로 parent를 찾아감
        return parent[x]

def union_parent(a,b): # 부모를 합침 # 즉 순환이 되는 구간

    a = get_parent(a)
    b = get_parent(b)

    if a < b: # 작은 쪽이 부모가 됨
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b): # 부모가 같은지 찾음
    return get_parent(a) == get_parent(b)

answer = 0

for a, b, cost in edges:
    # cost가 작은 edge부터 추가해가면서
    # 사이클(즉 같은 부모가 아닐때만 추가)
    if not same_parent(a,b):
        union_parent(a,b)
        answer += cost

print(answer)