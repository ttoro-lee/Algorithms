def solution(record):
    answer = []
    ans = []
    
    users = dict()
    
    for r in record:
        r = r.split()
        if r[0] == "Leave":
            answer.append((r[1], r[0]))
        elif r[0] == "Enter":
            if users.get(r[1], 0):
                users[r[1]] = r[2]
            else:
                users[r[1]] = r[2] # uid에 이름 추가
            answer.append((r[1], r[0]))
        elif r[0] == "Change":
            if users.get(r[1], 0):
                users[r[1]] = r[2]
                
    for a in answer:
        uid, op = a
        if op == "Enter":
            ans.append(f"{users[uid]}님이 들어왔습니다.")
        elif op == "Leave":
            ans.append(f"{users[uid]}님이 나갔습니다.")
    
    return ans