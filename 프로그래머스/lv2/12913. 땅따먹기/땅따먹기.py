def solution(land):
    answer = 0
    temp = land.copy()
    
    for i in range(1, len(land)):
        for j in range(4):
            temp[i][j] += max(temp[i-1][:j]+temp[i-1][j+1:])

    return max(temp[-1])