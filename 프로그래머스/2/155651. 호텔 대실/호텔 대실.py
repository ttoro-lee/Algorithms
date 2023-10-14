import heapq

def solution(book_time):
    answer = 0
    mans = []

    
    for book in book_time:
        start, end = book
        start = start.split(':')
        end = end.split(':')
        
        mans.append([int(start[0]) * 60 + int(start[1]), int(end[0]) * 60 + int(end[1]) + 10])
        
    mans.sort(key=lambda x:x[0])
    
    rooms = []
    
    for man in mans:
        if rooms:
            if rooms[0] > man[0]: # 가장 먼저 나오는 사람보다 들어가는 사람이 빠르면
                heapq.heappush(rooms, man[1])
                answer += 1
            elif rooms[0] <= man[0]:
                heapq.heappop(rooms)
                heapq.heappush(rooms, man[1])
        else:
            heapq.heappush(rooms, man[1])
            answer += 1
        
    return answer