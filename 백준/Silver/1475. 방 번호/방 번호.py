import sys

strings = sys.stdin.readline().strip()

numbers = dict()
answer = 1

for i in range(10):
    if i == 9:
        numbers['6'] += 1
    else:
        numbers[str(i)] = 1

strings = strings.replace('9', '6')

for s in strings:
    if numbers[s] > 0:
        numbers[s] -= 1
    else: # 만약에 없다면
        numbers[s] -= 1
        answer += 1
        for i in range(10):
            if i == 9:
                numbers['6'] += 1
            else:
                numbers[str(i)] += 1

print(answer)