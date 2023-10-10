from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    b_sum = 0
    
    truck = deque(truck_weights)
    bridge = deque()
    destination = []
    
    while(len(destination) != len(truck_weights)):
        if len(bridge) == bridge_length:
            check = bridge.popleft()
            if check:
                destination.append(check)
                b_sum -= check
        answer += 1
        if truck and (not(bridge) or (b_sum + truck[0] <= weight)):
            cur = truck.popleft()
            bridge.append(cur)
            b_sum += cur
        else:
            bridge.append(0)
            
    return answer