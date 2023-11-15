
import sys
import math

n, m = map(int, sys.stdin.readline().split())

def solution(n, m):

    if n % m == 0:
        return 0
    else:
        k = math.gcd(n,m)
        return m - k

print(solution(n, m))