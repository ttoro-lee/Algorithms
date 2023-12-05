# 공격 당하면 기술 취소, 순간엔 회복 X
# 공격 받으면 체력 회복
# 연속 성공 시간 0으로 초기화
# 현재 체력이 0 이하가 되면 캐릭터 사망, 체력회복 X


def solution(bandage, health, attacks):
    
    answer = health
    
    times, heal, bonus = bandage[0], bandage[1], bandage[2]
    
    monster = dict()
    
    for attack in attacks:
        time, damage = attack[0], attack[1]
        monster[time] = damage
        
    target = sorted(monster.keys())[-1]
    
    i = 0
    length = 0
    
    while(i != target):
        
        i += 1
        
        if monster.get(i, 0):
            answer -= monster[i]
            length = 0
            if answer <= 0:
                return -1
        else:
            answer += heal            
            length += 1
            
            if length == times:
                length = 0
                answer += bonus
                
            if answer > health:
                answer = health
            
    return answer