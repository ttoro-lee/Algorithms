x = int(input())

for i in range(10000000):
    k = i * (i+1) // 2
    if k >= x:
        break

if i == 1:
    분자 = 1
    분모 = 1

elif i % 2 == 1:
    # 홀수면
    분자 = 1
    분모 = i

    while(k != x):
        
        분자 += 1
        분모 -= 1

        k -= 1
else: # 짝수면
    분자 = i
    분모 = 1

    while(k != x):
        
        분자 -= 1
        분모 += 1

        k -= 1

print(f'{분자}/{분모}')
