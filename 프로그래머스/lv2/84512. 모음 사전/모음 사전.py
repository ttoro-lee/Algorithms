def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']
    for i in range(5):
        w = []
        answer += 1
        w.append(words[i])
        if ''.join(w) == word:
            return answer
        for j in range(5):
            answer += 1
            w.append(words[j])
            if ''.join(w) == word:
                return answer
            for k in range(5):
                answer += 1
                w.append(words[k])
                if ''.join(w) == word:
                    return answer
                for n in range(5):
                    answer += 1
                    w.append(words[n])
                    if ''.join(w) == word:
                        return answer
                    for m in range(5):
                        answer += 1
                        w.append(words[m])
                        if ''.join(w) == word:
                            return answer
                        w.pop()
                    w.pop()
                w.pop()
            w.pop()
                        
    return answer