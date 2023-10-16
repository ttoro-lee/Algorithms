def solution(picks, minerals):
    answer = 0
    
    tools = {0:(1,1,1), 1:(5,1,1), 2:(25,5,1)}
    mine = {"diamond":0, "iron":0, "stone":0}
    
    array = []
    
    length = min(sum(picks)*5, len(minerals)) # 도구가 길이만큼 없다면
    
    for i in range(length):
        mine[minerals[i]] += 1 # 돌의 갯수를 셈
        
        if (i + 1) % 5 == 0 or (i == length - 1): # 5개마다, 또는 끝에 도달했을때
            array.append([mine['diamond'], mine['iron'], mine['stone']])
            mine['diamond'], mine['iron'], mine['stone'] = 0, 0, 0
            
    array.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True) # 다이아가 많은 것부터 순서대로
    
    for i in range(len(array)):
        for j in range(3):
            if picks[j]:
                picks[j] -= 1 # 도구 한개 사용
                answer += tools[j][0] * array[i][0] + tools[j][1] * array[i][1] + tools[j][2] * array[i][2]
                break
            
    return answer