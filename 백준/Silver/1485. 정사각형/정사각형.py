import sys

case = int(sys.stdin.readline().strip())

def gradient(ax, ay, bx, by):

    if ax == bx:
        return 'x'
    elif ay == by:
        return 'y'
    else:
        return (by - ay) / (bx - ax)

def length(ax, ay, bx, by):

    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5

for _ in range(case):
    points = []
    for _ in range(4):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x,y))

    points.sort()

    if gradient(points[0][0], points[0][1], points[1][0], points[1][1]) == gradient(points[0][0], points[0][1], points[2][0], points[2][1]):
        # 두 기울기가 같다면
        print(0)
        continue
    elif length(points[0][0], points[0][1], points[1][0], points[1][1]) != length(points[0][0], points[0][1], points[2][0], points[2][1]):
        print(0)
        continue
    elif length(points[0][0], points[0][1], points[3][0], points[3][1]) != length(points[1][0], points[1][1], points[2][0], points[2][1]):
        print(0)
        continue
    else:
        print(1)