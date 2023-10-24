# 윤년 year % 4 == 0
# 평년 year % 100 == 0
# 윤년 year % 400 == 0

import datetime

months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

start = list(map(int, input().split()))
end = list(map(int, input().split()))

def solution(start, end):
    if end[0] - start[0] > 1000:
        return "gg"
    elif end[2] >= start[2] and end[1] >= start[1] and end[0] - start[0] == 1000:
        return "gg"
    
    else:
        start = datetime.date(*start) # Date 클래스로 변환
        end = datetime.date(*end)

        d_days = end.toordinal() - start.toordinal() # 그레고리력 서수로 변환

        return f"D-{d_days}"

print(solution(start, end))

