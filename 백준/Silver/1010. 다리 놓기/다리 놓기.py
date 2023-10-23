case = int(input())

legs = []

factori = [0] * 31

for i in range(31):
    if i < 2:
        factori[i] = 1
    else:
        factori[i] = factori[i-1] * i

for i in range(case):
    l, r = map(int, input().split())

    legs.append((l,r))

for leg in legs:
    r, n = leg

    print(factori[n] // (factori[r] * factori[n-r]))

    # 조합 계산 -> n! / (r! * (n-r)!)