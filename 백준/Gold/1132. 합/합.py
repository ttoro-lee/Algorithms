import sys

n = int(sys.stdin.readline().strip())

inputs = []
ans = 0

dicts = {'A':[0,False], 'B':[0,False],'C':[0,False],'D':[0,False],'E':[0,False],'F':[0,False],'G':[0,False],'H':[0,False],'I':[0,False],'J':[0,False]}
mapping = dict()

for _ in range(n):
    strings = sys.stdin.readline().strip()
    inputs.append(strings)

    for i in range(len(strings)):
        dicts[strings[i]][0] += 10**(len(strings)-i-1)
        if i == 0:
            dicts[strings[i]][1] = True

answer = sorted(dicts.items(), reverse=True, key= lambda x : x[1][0])

if answer[9][1][1]:
    for i in range(8, -1, -1):
        if answer[i][1][1] == False:
            back = answer.pop(i)
            answer.append(back)
            break

for i in range(9, -1,-1):
    mapping[answer[9-i][0]] = str(i)

for string in inputs:
    tmp = []
    for s in string:
        tmp.append(mapping[s])
    ans += int(''.join(tmp))

print(ans)