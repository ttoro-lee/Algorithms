n, m = map(int, input().split())

chest = []


for i in range(n):
    chest.append(list(input()))

pk = []

def switcher(color):
    if color:
        return False
    else:
        return True


for i in range(0,n-7):
    for j in range(0,m-7):
        tmp = 0
        if chest[i][j] == 'W':
            white = True
            for l in range(i, i+8):
                for k in range(j, j+8):
                    if chest[l][k] == 'W' and white == False: # 다음이 흰색이고, 흰색이 안된다면
                        tmp += 1
                    elif chest[l][k] == 'B' and white == True: # 다음이 검은색이고, 흰색이여야 한다면
                        tmp += 1
                
                    white = switcher(white)
                white = switcher(white)
            # 검사 끝
            pk.append(tmp)

            tmp = 0
            white = False

            for l in range(i, i+8):
                for k in range(j, j+8):
                    if chest[l][k] == 'W' and white == False: # 다음이 흰색이고, 흰색이 안된다면
                        tmp += 1
                    elif chest[l][k] == 'B' and white == True: # 다음이 검은색이고, 흰색이여야 한다면
                        tmp += 1
                
                    white = switcher(white)
                white = switcher(white)
            pk.append(tmp)

        elif chest[i][j] == 'B':
            white = False
            for l in range(i, i+8):
                for k in range(j, j+8):
                    if chest[l][k] == 'W' and white == False: # 다음이 흰색이고, 흰색이 안된다면
                        tmp += 1
                    elif chest[l][k] == 'B' and white == True: # 다음이 검은색이고, 흰색이여야 한다면
                        tmp += 1
                
                    white = switcher(white)
                white = switcher(white)
            pk.append(tmp)

            tmp = 0

            white = True
            for l in range(i, i+8):
                for k in range(j, j+8):
                    if chest[l][k] == 'W' and white == False: # 다음이 흰색이고, 흰색이 안된다면
                        tmp += 1
                    elif chest[l][k] == 'B' and white == True: # 다음이 검은색이고, 흰색이여야 한다면
                        tmp += 1
                
                    white = switcher(white)
                white = switcher(white)
            # 검사 끝
            pk.append(tmp)

print(min(pk))
                    
