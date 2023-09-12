from collections import deque

def solution(s):
    answer = checker(s)
    new_s = s
    
    for i in range(1, len(s)):
        new_s = new_s[1:] + new_s[0]
        answer += checker(new_s)
    
    return answer

def checker(s):
    
    stack = []
    
    for i in range(len(s)):
        k = len(stack)
        if s[i] in ['(','[','{']:
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif s[i] == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                return 0
        elif s[i] == '}':
            if len(stack) and stack[-1] == '{':
                stack.pop()
            else:
                return 0
    if len(stack):
        return 0
    return 1
        