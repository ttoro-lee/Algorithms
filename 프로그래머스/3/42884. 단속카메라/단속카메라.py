def solution(routes):
    
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001 # 끝나는 시점
    
    print(routes)

    answer = 0

    for route in routes:
        if last_camera < route[0]: # 이전 마지막 카메라가 지금을 포함할 수 있으면 넘어감
            answer += 1 # 없으면 카메라 업데이트
            last_camera = route[1]

    return answer