import sys

n = int(input())

# 1 -> 1^2
# 2 -> 1^2 + 1^2
# 3 -> 1^2 + ... + 1^2
# 4 -> 2^2
# 5 -> 2^2
# 6
# 7
# 8

table = [1] * 100001

for i in range(1, 100001):
    if i ** 0.5 == int(i**0.5):
        table[i] = 1
    else:
        tmp = sys.maxsize
        for j in range(1, int(i**0.5)+1):
            pk = table[j**2] + table[i-j**2]
            if tmp > pk:
                tmp = pk
        table[i] = tmp
print(table[n])