def solution(number, k):

    stack = []
    for i in range(len(number)):
        while(stack and k):
            if number[i] > stack[-1]:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(number[i])
    if k:
        stack = stack[:-k]
        
    return "".join(stack)