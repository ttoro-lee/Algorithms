import sys
import datetime

months = {'January':1, 'February':2, 'March':3,
          'April':4, 'May':5, 'June':6, 'July':7,
          'August':8, 'September':9, 'October':10,
          'November':11, 'December':12}

md, yt = sys.stdin.readline().strip().split(',')

month, day = md.split()
year, time = yt.split()

times = time.split(':')

start = datetime.datetime(int(year), 1,1)
end = datetime.datetime(int(year)+1, 1,1)
today = datetime.datetime(int(year), months[month], int(day), int(times[0]), int(times[1]))

nows = today - start
all_times = end - start

분자 = nows.days * 24 * 60 + nows.seconds // 60 # 분을 더해줌
분모 = all_times.days * 24 * 60

print(분자 / 분모 * 100)