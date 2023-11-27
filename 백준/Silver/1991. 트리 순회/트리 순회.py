import sys

sys.setrecursionlimit(10000)

n = int(sys.stdin.readline().strip())

graphs = dict()

for _ in range(n):

    root, left, right = sys.stdin.readline().split()

    graphs[root] = [left, right]


def pre_search(start, graph):
    print(start, end='')

    for node in graph[start]:
        if node != '.':
            pre_search(node, graph)

    return

def mid_search(start, graph):

    visited  = set()

    for node in graph[start]:
        if node != '.':
            mid_search(node, graph)

        if start not in visited:
            print(start, end = '')
            visited.add(start)

    return

def post_search(start, graph):

    for node in graph[start]:
        if node != '.':
            post_search(node, graph)
    print(start, end='')
    return


pre_search('A',graphs)
print()
mid_search('A',graphs)
print()
post_search('A',graphs)