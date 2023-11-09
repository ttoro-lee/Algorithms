from math import gcd
import sys

A,B = map(int, input().split())
# A,B = map(int, sys.stdin.readline().split())


print(''.join(['1'] * gcd(A,B)))
        
