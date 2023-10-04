def solution(files):
    answer = []
    
    for file in files:
        answer.append(filter(file))
        
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
        
    return ["".join(a) for a in answer]


def filter(file):
    header = ''
    for idx, s in enumerate(file):
        if not(header) and s.isdigit():
            header = file[:idx]
            cp = idx
            if idx == len(file) - 1:
                number = file[cp:cp+5]
                tail = file[cp+5:]
        elif header and not(s.isdigit()):
            number = file[cp:idx]
            if len(number) > 5:
                number = file[cp:cp+5]
                tail = file[cp+5:]
            else:
                tail = file[idx:]
            break
        elif idx == len(file) - 1:
            number = file[cp:cp+5]
            tail = file[cp+5:]
    return header, number, tail