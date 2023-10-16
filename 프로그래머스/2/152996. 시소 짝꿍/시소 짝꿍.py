from collections import Counter

def solution(weights):
    answer = 0
    
    # key를 갖는 사람은 몇 명인가?
    people = Counter(weights)
    
    for weight in set(weights):
        answer += people[weight] * (people[weight] - 1) // 2  # 같은 사람들 중 2명 뽑는 경우
        answer += people[weight] * (people[weight * 3 / 2]) # 나와 2 : 3인 비율
        answer += people[weight] * (people[weight * 4 / 2]) # 나와 2 : 4인 비율
        answer += people[weight] * (people[weight * 3 / 4]) # 나와 3 : 4인 비율
                
    return answer