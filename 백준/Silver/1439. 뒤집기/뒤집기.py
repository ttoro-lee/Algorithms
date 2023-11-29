import sys

n = sys.stdin.readline().strip()

def solution(n):

    zero = 0
    one = 0

    zero_check = n.count('0')
    one_check = n.count('1')


    if zero_check == 0 or one_check == 0:
        return 0
    elif zero_check == 1 or one_check == 1:
        return 1

    if n[0] == '0':
        switch = '0'
        zero += 1
    else:
        switch = '1'
        one += 1

    for i in range(len(n)):
        if switch == '1' and n[i] == '0':
            zero += 1
            switch = '0'
        elif switch == '0' and n[i] == '1':
            one += 1
            switch = '1'

    answer = min(zero, one)

    return answer

print(solution(n))