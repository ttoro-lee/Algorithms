# 골드바흐 의 추측
# 2보다 큰 모든 짝수는 2개의 소수의 합으로 표현할 수 있다
# 8(짝수)의 경우 2 + 2 + 2 + 2
# 즉 (2 + 2) + A + B, A + B가 소수가 되는 값을 찾으면 됨

# N이 짝수인 경우
# N-4 -> A + B + (2 + 2)

# N이 홀수인 경우
# N-5 -> A + B + (2 + 3)

import sys

def makeprime(n):

    primes = [0,0] + [1] * n

    for i in range(2, n+1):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = 0

    return primes

n = int(sys.stdin.readline().strip())

answer = ''

if n < 8:
    print(-1)

elif n % 2 == 1:
    answer = "2 3 "
    n -= 5
else:
    answer = "2 2 "
    n -= 4

prime = makeprime(n)

for i in range(2, n+1):
    if prime[i] and prime[n-i]:
        answer += str(i) + ' ' + str(n-i)
        print(answer)
        break