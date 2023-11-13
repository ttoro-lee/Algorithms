import sys

n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
ban = int(sys.stdin.readline())

tree = dict()

answer = 0

for idx in range(n):
    tree[idx] = []

for idx, parent in enumerate(parents):
    if parent == -1:
        root = idx
    elif idx == ban or parent == idx:
        continue
    else:
        tree[parent].append(idx)

del tree[ban]

def find_leaf(tree, root, ban):

    global answer

    if root == ban:
        return

    elif len(tree[root]) == 0:
        answer += 1
        return

    else:
        for node in tree[root]:
            if node == ban:
                continue
            else:
                find_leaf(tree, node, ban)

find_leaf(tree, root, ban)

print(answer)