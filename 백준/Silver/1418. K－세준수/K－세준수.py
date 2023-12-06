import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

ans = n

primes = [0,0] + [1] * (n-1)

for i in range(2, n+1):
    for j in range(i*2, n+1, i):
        if primes[j] == 1:
            primes[j] = 0

for i in range(1, n+1):
    answer = set()

    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            a = i // j
            b = j
            if primes[a]:
                answer.add(a)
            if primes[b]:
                answer.add(b)

    if len(answer) == 0:
        continue
    else:
        if max(answer) > k:
            ans -= 1

print(ans)
