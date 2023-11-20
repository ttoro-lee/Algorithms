import sys

ax, ay, bx, by, cx, cy = map(int, sys.stdin.readline().split())

def gradient(ax, ay, bx, by):

    if ax == bx:
        return 'x'
    elif ay == by:
        return 'y'

    return (by-ay) / (bx-ax)

def length(ax, ay, bx, by):

    return ((ax - bx)**2 + (ay - by)**2)**0.5

def solution(ax, ay, bx, by, cx, cy):

    if gradient(ax, ay, bx, by) == gradient(ax, ay, cx, cy):
        # 한점에 대한 다른 기울기가 같은 경우
        # 평행 사변형을 구할 수 없음
        return -1.0

    ab_length = length(ax, ay, bx, by)
    bc_length = length(bx, by, cx, cy)
    ac_length = length(ax, ay, cx, cy)

    pk = [ab_length+bc_length, bc_length+ac_length, ab_length+ac_length]

    answer = max(pk) - min(pk)

    return answer*2

print(solution(ax,ay,bx,by,cx,cy))