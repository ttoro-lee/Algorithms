def solution(data, col, row_begin, row_end):
    answer = []
    
    # col번째 칼럼의 값을 기준으로 ASC
    # 값이 동일하면 첫번째 col기준 DESC
    # S_i = i번째 행의 튜플의 각 컬럼 값을 i로 나눈 나머지들의 합
    # rb -> re 모든 S_i 누적 -> XOR한 값 해시값
    
    data.sort(key = lambda x: (x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        s_i = 0
        for j in range(len(data[i])):
            s_i += (data[i][j] % (i+1))
        answer.append(s_i)
    
    k = answer[0]
    
    for i in range(1, len(answer)):
        k = k ^ answer[i]
        
    return k