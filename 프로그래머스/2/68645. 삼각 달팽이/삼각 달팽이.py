def solution(n):
    answer = []
    triangle = []
    k = 1
    arrow = -1
    t = 0
    
    if n == 1:
        return [1]
    
    for i in range(1, n+1):
        t += i
        triangle.append([0] * i)
    
    triangle = [[0]*i for i in range(1,n+1)]
    i, j = 0, 0
    
    while(k != t):
        triangle[i][j] = k
        
        if arrow == -1:
            while(i+1 < len(triangle) and triangle[i+1][j] == 0):
                k += 1
                i += 1
                triangle[i][j] = k
            arrow = 0
        elif arrow == 0:
            while(j+1 < len(triangle[i]) and triangle[i][j+1] == 0):
                j += 1
                k += 1
                triangle[i][j] = k
            arrow = 1
        
        elif arrow == 1:
            while(i - 1 < len(triangle) and j - 1 < len(triangle[i]) and triangle[i-1][j-1] == 0):
                i -= 1
                j -= 1
                k += 1
                triangle[i][j] = k
            arrow = -1
    # 1
    # 2 9
    # 3 10 8
    # 4 5  6  7
    for t in triangle:
        answer += t
    return answer