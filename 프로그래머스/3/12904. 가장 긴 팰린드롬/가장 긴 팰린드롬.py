import sys

def solution(s):
    answer = -sys.maxsize
    
    n = len(s)
    
    for i in range(n):
        for j in range(i, n+1):
            if is_perlidurom(s[i:j]):
                if (j-i) > answer:
                    answer = j-i

    return answer


def is_perlidurom(string):
    
    if string == string[::-1]:
        return True
    return False