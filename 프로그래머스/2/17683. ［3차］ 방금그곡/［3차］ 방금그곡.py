def solution(m, musicinfos):
    answer = ''
    
    players = dict()
    
    for music in musicinfos:
        tmp = ""
        start, end, title, mell = music.split(',')
        start = list(map(int, start.split(":")))
        end = list(map(int, end.split(":")))
        time = (end[0] - start[0]) * 60 + (end[1] - start[1])
        mell = mell.replace("C#", "c").replace("D#", "d").replace("F#", "f")
        mell = mell.replace("G#", "g").replace("A#", "a")
        
        for i in range(time):
            tmp += mell[i % len(mell)]
        
        players[tmp] = title
        
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f")
    m = m.replace("G#", "g").replace("A#", "a")
    
    for music, title in sorted(players.items(), key=lambda x: -len(x[0])):
        if m in music:
            return title
        
    return '(None)'