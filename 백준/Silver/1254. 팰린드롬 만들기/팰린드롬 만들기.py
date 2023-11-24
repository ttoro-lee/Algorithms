import sys

strings = sys.stdin.readline().strip()

def pelinduorn(strings):

    mid = len(strings) // 2

    if len(strings) % 2 == 0:
        return strings[:mid] == strings[mid:][::-1]
    else:
        return strings[:mid] == strings[mid+1:][::-1]

tmp = strings
pk = 0
arr = []

while(pelinduorn(tmp) != True):

    arr = [strings[pk]] + arr
    tmp = strings + ''.join(arr)
    pk += 1


print(len(tmp))