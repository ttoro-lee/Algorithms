# 합이 N이면서
# 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트

# N = x+1 + x+2 + ... + x+L
# N = Lx + (1 ~ L 합)
# N = Lx + (L(L+1)) / 2
# Lx = N - L(L+1) / 2
# 이때 L로 나누면 x는 정수
# x + 1은 0보다 크거나 같아야함

from collections import deque

n, l = map(int, input().split())

def solution(n, l):

    for i in range(l, 101): # l은 2보다크고 100보다 작거나 같음
        x = n - (i * (i+1) / 2)

        if x % i == 0: # x를 L로 나눈 값이 정수라면
            x = int(x / i) # x는 후보로 들어감

            if x >= -1: # x+1이 0보다 크거나 같다면
                for j in range(1, i+1): # l 길이만큼
                    print(x+j, end=' ')
                return
    return print(-1)

solution(n, l)
