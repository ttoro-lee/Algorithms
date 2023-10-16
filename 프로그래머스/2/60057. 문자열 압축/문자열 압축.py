def solution(s):
    answer = [''] * (len(s) + 1)
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)):
        cnt = 0
        t = 0
        tmp = s[:i]
        while(t < len(s)):
            # print(tmp, t)
            if t >= (len(s) - i):
                if tmp != s[t:t+i]: # 같지 않으면
                    if cnt != 1:
                        answer[i] += (str(cnt) + tmp)
                        answer[i] += s[t:t+i] # 같지 않은거 붙이기
                        answer[i] += s[t+i:]
                        break
                    else:
                        answer[i] += tmp
                        answer[i] += s[t:t+i] # 같지 않은거 붙이기
                        answer[i] += s[t+i:]
                        break
                else:
                    cnt += 1
                    if cnt != 1:
                        answer[i] += (str(cnt) + tmp)
                        answer[i] += s[t+i:]
                    break
            elif tmp == s[t:t+i]: # 같으면
                cnt += 1 # 횟수 올려
                t += i
            elif tmp != s[t:t+i]: # 같지 않으면
                if cnt != 1:
                    answer[i] += (str(cnt) + tmp)
                    cnt = 0
                else:
                    answer[i] += tmp
                    cnt = 0
                tmp = s[t:t+i] # 바꾸고

    return min([len(a) for a in answer if len(a) != 0])