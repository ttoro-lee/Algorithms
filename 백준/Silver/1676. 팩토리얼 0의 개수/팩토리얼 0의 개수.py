import sys

n = int(sys.stdin.readline().strip())

def make_factori(n):

    factorial = [1] * (n+1)

    for i in range(n+1):
        if i <= 1:
            continue
        else:
            factorial[i] = factorial[i-1] * i

    return factorial

def solution(arr, n):
    answer = 0
    for k in str(arr[n])[::-1]:
        if k != '0':
            return answer
        else:
            answer += 1
    return answer

arr = make_factori(n)
print(solution(arr, n))