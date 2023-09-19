from collections import defaultdict
import math

def solution(fees, records):
    
    # 기본시간 이하, 기본 요금
    # 기본시간 초과, 기본 요금 + 초과 시간 단위요금
    # 안떨어지면 올림
    answer = []
    
    cars = defaultdict(list)
    
    normal_time = fees[0]
    normal_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]
    
    for record in records:
        record = record.split()
        times = record[0].split(':')
        time = int(times[0]) * 60 + int(times[1])
        car_num = record[1]
        how = record[2]
        
        if how == 'in':
            cars[car_num].append(time)
        else:
            cars[car_num].append(time)
            
    for car in cars:
        if len(cars[car]) % 2 == 1:
            cars[car].append(23*60 + 59)
            
        time = 0
        
        for i in range(0, len(cars[car]) - 1, 2):
            time += (cars[car][i+1] - cars[car][i])
        if normal_time < time:
            fee = normal_fee + math.ceil((time - normal_time) / per_time) * per_fee
        else:
            fee = normal_fee
        answer.append((car, fee))
    return [a[1] for a in sorted(answer)]