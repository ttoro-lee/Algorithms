import sys
from collections import Counter

strings = sys.stdin.readline().strip()

def solution(strings):

    counter = Counter(strings)
    counter = sorted(counter.items())

    answer = []

    if len(strings) % 2 == 0: # 길이가 짝수인 경우
        for s, c in counter:
            if c % 2 != 0:
                return "I'm Sorry Hansoo"
            else:
                answer = answer + [s] * (c // 2)
        answer = answer + answer[::-1]
    else:
        tmp = 0
        for s, c in counter:
            if c % 2 != 0:
                if tmp != 0:
                    return "I'm Sorry Hansoo"
                else:
                    tmp = s
                    answer = answer + [s] * ((c - 1) // 2)
            else:
                answer = answer + [s] * (c // 2)
        answer = answer + [tmp] + answer[::-1]

    return ''.join(answer)

print(solution(strings))