# X 게임 횟수
# y 이긴 게임
# z 승률

import math

x, y = map(int, input().split())

z = math.floor((100 * y) / x)

def solution(x, y, z):

    if x == y or z == 99:
        return -1
    
    l1 = ((x * z) + x - (100 * y))
    l2 = 99 - z

    if l1 % l2 != 0:
        return math.floor(l1 / l2) + 1
    else:
        return (l1 // l2)


print(solution(x,y,z))