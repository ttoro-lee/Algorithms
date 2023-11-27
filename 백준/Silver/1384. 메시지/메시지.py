# 원형으로 앉은 아이들
# 종이 위에 자신의 이름
# 각자 종이를 자기 왼편으로 전달
# 종이를 받음, 맨 위에 쓰인 이름을 가진 아이에 대해 좋은 메세지를 써줌


import sys

k = 1

while(1):

    n = int(sys.stdin.readline().strip())

    if n == 0:
        break

    if k != 1:
        print()

    names = []
    cases = []

    for _ in range(n):
        strings = sys.stdin.readline().split()
        names.append(strings[0])
        cases.append(strings[1:])

    nasty = False

    print(f'Group {k}')

    for idx, case in enumerate(cases):

        for i, c in enumerate(case, start=1):
            if c == 'N':
                nasty=True
                who = idx - i # 자기 자신으로부터 왼쪽으로 몇 칸
                if who < 0:
                    who = n + who

                print(f'{names[who]} was nasty about {names[idx]}')

    k += 1
    if nasty:
        continue
    else:
        print('Nobody was nasty')


