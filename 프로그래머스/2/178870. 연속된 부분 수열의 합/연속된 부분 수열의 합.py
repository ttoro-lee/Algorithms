def solution(sequence, k):
    answer = []
    
    left = 0
    right = 0
    
    tmp = sequence[left]
    
    while(left < right+1):
        
        if tmp > k:
            tmp -= sequence[left]
            left += 1
        elif tmp < k:
            if right < len(sequence)-1:
                tmp += sequence[right+1]
                right += 1
            else:
                tmp -= sequence[left]
                left += 1
        elif tmp == k:
            answer.append((left, right, abs(left-right)))
            if right < len(sequence)-1:
                tmp += sequence[right+1]
                right += 1
            else:
                tmp -= sequence[left]
                left += 1
    answer.sort(key=lambda x: (x[2], x[0]))
    
        
    return answer[0][0], answer[0][1]